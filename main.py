import pygame as p

def update():
    pass

def draw():
    if "main" in g.active_states:
        if g.current_level:
            pass

    i = 0
    while i < len(g.pipe_list):
        g.pipe_list[i].update()
        i += 1
        pass

def start_game():
    pass
def loadgame():
    pass

def go_to_menu():
    reset()
    g.active_states = set(("menu",))
    pass
def main():
    p.init()
    update()
    draw()
    p.display.set_mode((640, 480))
    p.display.set_caption('Hello World!')
    p.display.flip()
    p.time.delay(2000)
    p.quit()

if __name__ == '__main__':
    main()