from presto import Presto
from touch import Button
from time import sleep

presto = Presto()
display = presto.display

TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)

touch = presto.touch

button_1 = Button(5, 5, 40, 20)

def LEDS_OFF():
    presto.set_led_rgb(4, 0, 0, 0)
    presto.set_led_rgb(5, 0, 0, 0)
    presto.set_led_rgb(6, 0, 0, 0)
    presto.set_led_rgb(1, 0, 0, 0)
    presto.set_led_rgb(2, 0, 0, 0)
    presto.set_led_rgb(0, 0, 0, 0)


def LEDS_ON():
    
    presto.set_led_rgb(4, 255, 255, 255)
    presto.set_led_rgb(5, 255, 255, 255)
    presto.set_led_rgb(6, 255, 255, 255)
    presto.set_led_rgb(1, 255, 255, 255)
    presto.set_led_rgb(2, 255, 255, 255)
    presto.set_led_rgb(0, 255, 255, 255)

        
while True:
    touch.poll()

    if button_1.is_pressed():
        display.set_pen(LIGHT_BLUE)
        display.rectangle(5, 5, 40, 20)
    
        LEDS_ON()
        sleep(10)
        LEDS_OFF()
        
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