from presto import Presto
import picographics
from touch import Button
import jpegdec
import time
from update_view import *
from getinfo import *

presto = Presto()
display = presto.display
touch = presto.touch
button_1 = Button(5, 5, 40, 20)
width = display.measure_text("2,400km", 1, 3)


TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)
BLACK = display.create_pen(0, 0, 0)

# welcome
display.set_pen(LIGHT_BLUE)
display.text("Welcome to Presto!", 10, 10, scale=2)
presto.update()

# fetch the time
time_data = fetch_time() # fetch the datetime string

time_string = time_data[11:16] # extract the time part of it and set this as time string
date_string = timedata_to_date(time_data) # call the function `timedata_to_date` to convert it into a date (basically the get_date without the fetching part)
seconds = int(timedata_to_seconds(time_data))

time.sleep(60 - seconds)

time_data = fetch_time() # fetch the datetime string
time_string = time_data[11:16] # extract the time part of it and set this as time string


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

def clock():
    # Create a new JPEG decoder for our PicoGraphics
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file("moon.jpeg")

    # Decode the JPEG
    j.decode(0, 0, jpegdec.JPEG_SCALE_FULL, dither=False)

    # Display the result

    display.set_pen(TEXT_BLUE)
    display.set_thickness(3)
    display.set_font("sans")
    display.text("2,400km", 65, 80, scale=0.8) # how many km I have done
    display.set_thickness(2)
    display.text("20d 9h 30m", 68, 60, scale=0.5) # how much time I have taken
    display.text("Out of 10,921", 63, 100, scale=0.5) # out of total distance needed to be covered
    display.set_thickness(1)
    display.text("24%", 95, 120, scale=0.7) #percentage

    display.set_pen(LIGHT_BLUE)
    display.set_thickness(3)
    display.text(f"{date_string}", 40, 220, scale=0.9) # date text

    display.set_pen(LIGHT_BLUE)
    display.set_thickness(8)
    display.text(f"{time_string}", 30, 180, scale=2)
    display.set_pen(LIGHT_BLUE)
    display.rectangle(5, 5, 40, 20)
    
    display.set_thickness(1)
    display.set_pen(TEXT_BLUE)
    display.set_font("sans")
    display.text("UPDATE", 8, 15, scale=0.3)
    presto.update()

touch_ticks = time.ticks_ms() # the current tick
last_fetch = time.ticks_ms()
presto.set_backlight(0.1)

while True:
    touch.poll()

    if button_1.is_pressed():
        buttons_screen()
        update_screen()
        presto.update()

    else:
        clock()
        presto.update()
        
    if time.ticks_ms() >= last_fetch + (60*1000):
        print("time update")
        time_data = fetch_time() # fetch the datetime string
        time_string = time_data[11:16] # extract the time part of it and set this as time string
        
        date_string = timedata_to_date(time_data) # call the function `timedata_to_date` to convert it into a date (basically the get_date without the fetching part)
        
        last_fetch = time.ticks_ms()
    
    if touch.state:
        touch_ticks = time.ticks_ms()
        print("leds on")
        leds_on()
        presto.set_backlight(1)
        
    if time.ticks_ms() >= touch_ticks + (10*1000):
        print("leds off")
        leds_off()
        presto.set_backlight(0.1)