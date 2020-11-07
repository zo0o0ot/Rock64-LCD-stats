from subprocess import check_output
from time import sleep
from datetime import datetime
from RPLCD.i2c import CharLCD
import os

lcd = CharLCD('PCF8574', 0x3f, auto_linebreaks=False, cols=16, rows=2)
lcd.clear()

def get_ip():
        cmd = "hostname -I | cut -d\' \' -f1"
        return check_output(cmd, shell=True).decode("utf-8").strip()
while True:
        lcd.clear()
        uptime = os.popen('uptime -p').read()[:-1]
        lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S')
        lcd_line_2 = "IP " + get_ip()
        lcd_line_3 = uptime
        output = lcd_line_2 + '\r\n' + lcd_line_3

        lcd.home()
        lcd.write_string(output)
        sleep(10)
