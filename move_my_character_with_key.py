from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
characteridle = load_image('idle.png')
characterrun = load_image('run_ani.png')


idleanimation = 9

idlenmm_x = [3,39,73,111,149,193,240,286,332]
idlenmm_y = [4,4,4,4,4,4,4,2,1]
idlenmm_w = [29,31,36,36,35,38,41,42,41]
idlenmm_h = [41,40,38,37,36,40,38,37,36]


runanimation = 5

runnmm_x = [13,51,88,124,156]
runnmm_y = [49,53,58,58,51]
runnmm_w = [34,31,25,26,36]
runnmm_h = [43,47,52,52,45]






def key_event():
    global running
    global dirRL
    global dirUD
    global x
    global y
    global idle
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirRL += 1
            elif event.key == SDLK_LEFT:
                dirRL -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_DOWN:
                dirUD -= 1
            elif event.key == SDLK_UP:
                dirUD += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirRL -= 1
            elif event.key == SDLK_LEFT:
                dirRL += 1
            elif event.key == SDLK_DOWN:
                dirUD += 1
            elif event.key == SDLK_UP:
                dirUD -= 1

    if dirRL == 0 and dirUD == 0:
        idle = True
    else:
        idle = False


    pass




def CharaterDraw():
    global idle
    global x
    global y

    global frame

    if idle:
        frame = (frame + 1) % 9
        characteridle.clip_draw(idlenmm_x[frame],idlenmm_y[frame],idlenmm_w[frame],idlenmm_h[frame],x,y,idlenmm_w[frame]*3,idlenmm_h[frame]*3)
        #characteridle.clip_draw(50,50,50,50,x,y)
        #characteridle.draw(400,300)
    else:
        frame = (frame + 1) % 5
        if dirRL > 0:
            characterrun.clip_draw(runnmm_x[frame], 62-runnmm_y[frame], runnmm_w[frame], runnmm_h[frame], x, y,runnmm_w[frame]*3,runnmm_h[frame]*3)
        else:
            characterrun.clip_composite_draw(runnmm_x[frame], 62-runnmm_y[frame], runnmm_w[frame], runnmm_h[frame],0,'h', x, y,runnmm_w[frame]*3,runnmm_h[frame]*3)
        pass

def PlayerControl():
    global x
    global y
    if x <= 750 and x >= 50:
        x += dirRL * 10
    elif x>750:
        x = 750
    elif x<50:
        x = 50


    if y <= 550 and y >= 50:
        y += dirUD * 10
    elif y<50:
        y = 50
    elif y>550:
        y = 550

    pass


running = True
frame = 0
x = 800//2
y = 600//2

dirRL = 0
dirUD = 0

idle = True

while running:
    clear_canvas()
    ground.draw(400, 300)
    CharaterDraw()
    update_canvas()
    key_event()
    PlayerControl()

    delay(0.05)

close_canvas()