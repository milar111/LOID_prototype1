import board
import time
import digitalio
import microcontroller
import random
import usb_cdc
import busio
import displayio
import adafruit_displayio_ssd1306
import adafruit_imageload

email = "testacc201235@gmail.com"
password = "testacc123456"

email1 = f"({email})"
password1 = f"({password})"

button_login = digitalio.DigitalInOut(board.GP1)
button_login.switch_to_input(pull = digitalio.Pull.UP)

button_logout = digitalio.DigitalInOut(board.GP0)
button_logout.switch_to_input(pull = digitalio.Pull.UP)

IMAGE_FILE1 = "bee.bmp"
IMAGE_FILE2 = "loading1.bmp"
SPRITE_SIZE = (64, 64)
FRAMES1 = 28
FRAMES2 = 20

def invert_colors(palette):
    palette[0], palette[1] = palette[1], palette[0]

displayio.release_displays()

i2c = busio.I2C(board.GP9, board.GP8)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

group = displayio.Group()

icon_bit1, icon_pal1 = adafruit_imageload.load(IMAGE_FILE1, bitmap=displayio.Bitmap, palette=displayio.Palette)
icon_bit2, icon_pal2 = adafruit_imageload.load(IMAGE_FILE2, bitmap=displayio.Bitmap, palette=displayio.Palette)
invert_colors(icon_pal1)
invert_colors(icon_pal2)

icon_grid1 = displayio.TileGrid(icon_bit1, pixel_shader=icon_pal1, width=1, height=1, tile_height=SPRITE_SIZE[1], tile_width=SPRITE_SIZE[0], default_tile=0, x=32, y=0)
icon_grid2 = displayio.TileGrid(icon_bit2, pixel_shader=icon_pal2, width=1, height=1, tile_height=SPRITE_SIZE[1], tile_width=SPRITE_SIZE[0], default_tile=0, x=32, y=0)
group.append(icon_grid1)

display.show(group)

timer = 0
pointer1 = 0
pointer2 = 0

while True:
    if button_login.value == False:
        print(email1)
        print(password1)
        if icon_grid1 in group:
            group.remove(icon_grid1)
        if icon_grid2 not in group:
            group.append(icon_grid2)
        for i in range(FRAMES2):
            icon_grid2[0] = i
            time.sleep(0.70)
        time.sleep(1)
        if icon_grid2 in group:
            group.remove(icon_grid2)
        if icon_grid1 not in group:
            group.append(icon_grid1)
    elif button_logout.value == False:
        print("Logout")
        if icon_grid1 in group:
            group.remove(icon_grid1)
        if icon_grid2 not in group:
            group.append(icon_grid2)
        for i in range(FRAMES2):
            icon_grid2[0] = i
            time.sleep(0.25)
        time.sleep(1)
        if icon_grid2 in group:
            group.remove(icon_grid2)
        if icon_grid1 not in group:
            group.append(icon_grid1)
    else:
        if icon_grid2 in group:
            group.remove(icon_grid2)
        if icon_grid1 not in group:
            group.append(icon_grid1)
        icon_grid1[0] = (icon_grid1[0] + 1) % FRAMES1
        time.sleep(0.1)
