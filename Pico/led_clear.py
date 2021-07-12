# LED Clear
from ws2812b import ws2812b

num_leds = 24
pixels = ws2812b(num_leds, 0, 16, delay=0)
pixels.brightness(100)
pixels.fill(0,0,0)
pixels.show()
