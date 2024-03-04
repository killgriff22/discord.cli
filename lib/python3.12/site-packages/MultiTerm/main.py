from classes import *
width,height = os.get_terminal_size()
screen1 = Screen((width//2,height),(0,0))
screen2 = Screen(((width)//2,height),((width+1)//2,0))
screens = cluster()
screens.add_screen(screen1)
screens.add_screen(screen2)
cursors = [[0,0],[0,0]]
def main(screen,event,focus,screens):
    if focus == screens.index(screen):
        if type(event) == asciimaticsEvent.MouseEvent:
            screen.blit("█", (event.x-screen.pos[0], event.y-screen.pos[1]))
    else:
        screen.fill(f"{RESET} {RESET}")

screens.loop(main)