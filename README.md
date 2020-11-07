# Rock64-LCD-stats

This is the code I used to display the IP and Uptime on the front LCD of the Iconikal Rockchip RK3328, also known as the "Recon Sentinel" or a Rock64 v2 with an IPC.

I installed Raspbian Buster and OpenMediaVault before starting.

The command to install OpenMediaVault is `sudo wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | sudo bash`

Shoutout to [Dan On Coding](https://medium.com/dan-on-coding/raspberrypi-ip-address-lcd-display-d31b496325fb), since his Medium article got me most of the way to where I was trying to go.

Setup:

I did all of this while logged in as root, which may not be how other people would want to do this.

This uses [RPLCD](https://github.com/dbrgn/RPLCD/tree/18f1d793399ba197b8ad2f4226e72e000b067df6).

You need to install python and i2c, as well as some other stuff.

Here's what I installed:

```
apt install i2c-tools
sudo apt install python3-wheel python3-setuptools python3-dev build-essential
sudo apt install python3-smbus
apt install python-pip
pip install rplcd
```

Here are the commands that I used to test the LCD:

```
i2cdetect -y 1
rplcd-tests i2c testsuite expander=PCF8574 addr=0X18 cols=16 rows=2
rplcd-tests i2c show_charmap expander=PCF8574 addr=0X3f cols=16 rows=2
```

I created and tested `/root/lcd_ip.py`, and then after that was working, I created `/etc/systemd/system/lcd.service`.

Once that seemed to look right, I did the command `systemctl enable lcd.service` followed by `reboot`.

lcd_ip.py also has a string that represents the current time, but I decided that information wasn't as important, and I only had a 16x2 display to work with.



