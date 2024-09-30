from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
characteridle = load_image('idle.png')


idleanimation = 9

idlenmm_x = [3,39,73,111,149,193,240,286,332]
idlenmm_y = [50,50,50,50,50,50,50,52,53]
idlenmm_w = [29,31,36,36,35,38,41,42,41]
idlenmm_h = [41,40,38,37,36,40,38,37,36]


runanimation = 5

runnmm_x = [13,51,88,124,156]
runnmm_y = [49,53,58,58,51]
runnmm_w = [34,31,25,26,36]
runnmm_h = [43,47,52,52,45]


x = 800//2

dirRL = 0
dirUD = 0

def key_event():
    global running
    global dirRL
    global dirUD
    global x
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:

            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDLK_RIGHT:
                pass
            elif event.type == SDLK_LEFT:
                pass
            elif event.type == SDLK_UP:
                pass
            elif event.type == SDLK_DOWN:
                pass

        if event.type == SDL_KEYUP:
            if event.type == SDLK_RIGHT:
                pass
            elif event.type == SDLK_LEFT:
                pass
            elif event.type == SDLK_UP:
                pass
            elif event.type == SDLK_DOWN:
                pass


    pass

def CharaterDraw():

    pass


running = True


for x in range(0,800,5):
    clear_canvas()
    ground.draw(640,512)
    CharaterDraw()

    key_event()



    update_canvas()
    delay(10.0)

close_canvas()