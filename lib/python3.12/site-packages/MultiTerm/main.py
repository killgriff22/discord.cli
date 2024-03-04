from classes import *
width,height = os.get_terminal_size()
screen1 = Screen((width//2,height),(0,0))
screen2 = Screen(((width)//2,height),((width+1)//2,0))
screens = cluster()
screens.add_screen(screen1)
screens.add_screen(screen2)
cursors = [[0,0],[0,0]]
def main(screen:Screen,event,focus:int,screens:cluster):
    if focus == screens.index(screen):
        if type(event) == asciimaticsEvent.MouseEvent:
            screen.fill(f"{Fore.BLUE}{Back.BLUE}█{RESET}")
    else:
        screen.fill(f"{Back.BLACK} {RESET}")

screens.loop(main)