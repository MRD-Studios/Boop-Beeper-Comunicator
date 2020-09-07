import I2C_LCD_driver, time, pynput

mylcd = I2C_LCD_driver.lcd()

def splahScreen():
    mylcd.lcd_display_string("Beep Boop by MRDTech", 1)
    mylcd.lcd_display_string(" A Short Range Comm ", 2)
    mylcd.lcd_display_string(" Built Using Python ", 3)
    mylcd.lcd_display_string("433Mhz Radio Pi Zero", 4)
    time.sleep(5)
    mylcd.lcd_clear()

def mainMenu(ID, messages):
    mylcd.lcd_clear()
    page = 1
    while True:
        if page == 1:
            mylcd.lcd_display_string("------- Menu -------", 1)
            mylcd.lcd_display_string("(1): Messages (x) UP", 2)
            mylcd.lcd_display_string("(2): Contacts (-) DN", 3)
            mylcd.lcd_display_string("Enter your Choice: " , 4)
            with pynput.keyboard.Events() as events:
                event = events.get(1e6)
                if event.key == pynput.keyboard.KeyCode.from_char('-'):
                    page = 2
                    mylcd.lcd_clear()
                elif event.key == pynput.keyboard.KeyCode.from_char('1'):
                    return "msg"
                if event.key == pynput.keyboard.KeyCode.from_char('2'):
                    return "cont"
        if page == 2:
            mylcd.lcd_display_string("------- Menu -------", 1)
            mylcd.lcd_display_string("(1): My ID    (+) UP", 2)
            mylcd.lcd_display_string("(2): Settings (x) DN", 3)
            mylcd.lcd_display_string("Enter your Choice: " , 4)
            with pynput.keyboard.Events() as events:
                event = events.get(1e6)
                if event.key == pynput.keyboard.KeyCode.from_char('+'):
                    page = 1
                    mylcd.lcd_clear()
                elif event.key == pynput.keyboard.KeyCode.from_char('1'):
                    return "ID"
                if event.key == pynput.keyboard.KeyCode.from_char('2'):
                    return "Setup"

def ID(ID, Uptime):
    mylcd.lcd_clear()
    mylcd.lcd_display_string("----- Your  ID -----", 1)
    mylcd.lcd_display_string("Your ID in Ascii: " , 2)
    mylcd.lcd_display_string(ID)
    mylcd.lcd_display_string(Uptime)