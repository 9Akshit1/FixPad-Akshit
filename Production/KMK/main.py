import board
import time
import supervisor
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.mouse_keys import MouseKeys
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
layers = Layers()
keyboard.modules = [layers, encoder_handler]

keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(MouseKeys())

keyboard.direct_pins = [
    board.GPIO2,  
    board.GPIO3,  
    board.GPIO4   
]

encoder_handler.pins = ((board.GPIO2, board.GPIO3, board.GPIO1, False),)

tab_open = False
site_url = 'https://www.google.com'

keyboard.keymap = [
    [
        KC.NO,  
        KC.NO,  
        KC.NO
    ]
]

encoder_handler.map = [
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.NO),)
]

@keyboard.key_pressed
def on_key_pressed(key):
    global tab_open

    if key == keyboard.keys[0]: 
        keyboard.send(KC.LCTRL(KC.C))  
        time.sleep(0.1)
        keyboard.send(KC.LCTRL(KC.LSHIFT(KC.Y)))  
    elif key == keyboard.keys[1]:  
        if not tab_open:
            keyboard.send(KC.LGUI(KC.R)) 
            time.sleep(0.2)
            keyboard.send(send_string(site_url + "\n"))
            tab_open = True
        else:
            keyboard.send(KC.LCTRL(KC.W))  
            tab_open = False
    elif key == keyboard.keys[2]:  
        print("Starting anti-sleep mouse movement")
        start_time = time.monotonic()
        while True:
            if not supervisor.runtime.serial_connected:  
                break
            current = time.monotonic()
            if current - start_time >= 5:
                keyboard.mouse.move(x=10, y=0)
                time.sleep(0.2)
                keyboard.mouse.move(x=-10, y=0)
                start_time = current

if __name__ == '__main__':
    keyboard.go()