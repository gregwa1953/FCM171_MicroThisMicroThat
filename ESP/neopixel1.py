# ESP32 Neopixel Demo
# https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/
# Modified by G.D. Walters
import machine, neopixel
import time
n = 24  # 8
p = 16  # 12

np = neopixel.NeoPixel(machine.Pin(p), n)

# np[0] = (255, 0, 0)
# np[2] = (125, 204, 223)
# np[5] = (120, 153, 23)
# np[8] = (255, 0, 153)
# np.write()

def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
    
def bounce(r, g, b, brightness, wait):
  for i in range(4 * n):
      for j in range(n):
          np[j] = (int(r*brightness), int(g*brightness), int(b*brightness))
      if (i // n) % 2 == 0:
          np[i % n] = (0, 0, 0)
      else:
          # pass
          which = n-1-(i%n)
          np[which] = (0, 0, 0)
      np.write()
      time.sleep_ms(wait)

def set_color(r, g, b, brightness):
  for i in range(n):
    np[i] = (int(r*brightness), int(g*brightness), int(b*brightness))
  np.write()
  
def cycle(r, g, b, brightness, wait):
  for i in range(4 * n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (int(r*brightness), int(g*brightness), int(b*brightness))
    np.write()
    time.sleep_ms(wait)

def wheel(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(brightness, wait):
  for j in range(int(brightness*255)):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    time.sleep_ms(wait)
    
print('Clear')
clear()
print('Set Colour')
set_color(0,102,.5,230)
time.sleep(2)
clear()
print('Cycle')
cycle(0,102,230,.5,200)
print('Bounce')
bounce(0,255,250,.5,200)    
clear()
time.sleep(2)
print('Rainbow Cycle')
rainbow_cycle(.5,5)
clear()
print('Program Ends')