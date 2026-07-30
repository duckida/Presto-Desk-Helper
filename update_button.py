from presto import Presto
from touch import Button
import time

presto = Presto()
display = presto.display

TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)
BLACK = display.create_pen(0, 0, 0)

touch = presto.touch

button_1 = Button(5, 5, 40, 20)

def leds_off():
    presto.set_led_rgb(4, 0, 0, 0)
    presto.set_led_rgb(5, 0, 0, 0)
    presto.set_led_rgb(6, 0, 0, 0)
    presto.set_led_rgb(1, 0, 0, 0)
    presto.set_led_rgb(2, 0, 0, 0)
    presto.set_led_rgb(3, 0, 0, 0)
    presto.set_led_rgb(0, 0, 0, 0)

def leds_on():
    
    presto.set_led_rgb(4, 255, 255, 255)
    presto.set_led_rgb(5, 255, 255, 255)
    presto.set_led_rgb(6, 255, 255, 255)
    presto.set_led_rgb(1, 255, 255, 255)
    presto.set_led_rgb(2, 255, 255, 255)
    presto.set_led_rgb(3, 255, 255, 255)
    presto.set_led_rgb(0, 255, 255, 255)

touch_ticks = time.ticks_ms() # the current tick
# a tick is the time of the clock of the system since boot
# starts at 0 when you plug it in, counts up in milliseconds

while True:
    touch.poll()

    if button_1.is_pressed():
        display.set_pen(BLACK)
        display.rectangle(5, 5, 40, 20)
        
        display.set_thickness(1)
        display.set_pen(TEXT_BLUE)
        display.set_font("sans")
        display.text("UPDATE", 8, 15, scale=0.3)
        presto.update()
    else:
        display.set_pen(LIGHT_BLUE)
        display.rectangle(5, 5, 40, 20)
        
        display.set_thickness(1)
        display.set_pen(TEXT_BLUE)
        display.set_font("sans")
        display.text("UPDATE", 8, 15, scale=0.3)
        presto.update()
    
    if touch.state:
        touch_ticks = time.ticks_ms()
        leds_on()
        
    if time.ticks_ms() >= touch_ticks + (10*1000):
        leds_off()
    