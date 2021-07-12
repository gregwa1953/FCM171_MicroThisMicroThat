import time
from ws2812b import ws2812b

num_leds = 24  #24
pixels = ws2812b(num_leds, 0,16, delay=0)
pixels.brightness(30)
pixels.fill(10,10,10)
pixels.show()

doloop = True
while doloop:
    for i in range(num_leds):
        for j in range(num_leds):
            pixels.set_pixel(j,abs(i+j)%10,abs(i-(j+3))%10,abs(i-(j+6))%10)
            # print(j, abs(i+j)%10, abs(i-(j+3))%10, abs(i-(j+6))%10)
            # time.sleep(2)
        pixels.show()
        try:
            time.sleep(0.05)
        except KeyboardInterrupt:
            pixels.fill(0,0,0)
            pixels.show()
            doloop = False

