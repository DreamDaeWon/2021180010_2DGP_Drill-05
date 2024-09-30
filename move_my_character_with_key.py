
from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
#character = load_image('character.png')

for x in range(0,800,5):
    clear_canvas()
    ground.draw(640,512)
    #character.draw(x,90)
    update_canvas()
    delay(10.0)

close_canvas()