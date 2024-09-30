
from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
characteridle = load_image('idle.png')


def key_event():

    pass



for x in range(0,800,5):
    clear_canvas()
    ground.draw(640,512)
    characteridle.draw(x,90)

    key_event()

    

    update_canvas()
    delay(10.0)

close_canvas()