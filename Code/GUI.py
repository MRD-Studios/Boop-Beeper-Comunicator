import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()
I2C_LCD_driver.

def splahScreen():
    mylcd.lcd_display_string("Beep Boop by MRDTech", 1)
    mylcd.lcd_display_string(" A Short Range Comm ", 2)
    mylcd.lcd_display_string(" Built Using Python ", 3)
    mylcd.lcd_display_string("433Mhz Radio Pi Zero", 4)
    sleep(5)
    mylcd.lcd_clear()

def mainMenu(ID, messages):
    mylcd.lcd_display_string("------- Menu -------", 1)
    mylcd.lcd_display_string("(1): Messages (+) UP", 2)
    mylcd.lcd_display_string("(2): Contacts (-) DN", 3)
    choice = mylcd.lcd_display_string(input(), 4)
    if choice == "+" or choice == "-":
        mylcd.lcd_display_string("------- Menu -------", 1)
        mylcd.lcd_display_string("(1): My ID    (+) UP", 2)
        mylcd.lcd_display_string("(2): Settings (-) DN", 3)
        choice = mylcd.lcd_display_string(input(), 4)
