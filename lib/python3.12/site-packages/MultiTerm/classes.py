from .modules import *
class canvas:
    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
        self.content = [[" "]*size[0] for _ in range(size[1])]

    def fill(self, char: str) -> None:
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                self.content[y][x] = char
        return

    def blit(self, text: str, pos: tuple[int, int], front_modifier: str = "", back_modifier: str = "") -> None:
        n = self.size[0]
        lines = text.split("\n")
        for y, line in enumerate(lines):
            # If y position is outside of the canvas height, scroll the canvas
            if y+pos[1] >= self.size[1]:
                self.content.pop(0)
                self.content.append([" "]*self.size[0])
                # Adjust y position to be at the bottom of the canvas
                pos = (pos[0], self.size[1]-1)
            for x, char in enumerate(line):
                if x+pos[0] < self.size[0] and y+pos[1] < self.size[1]:
                    self.content[y+pos[1]][x+pos[0]] = front_modifier+char+back_modifier


class Screen(canvas):
    def __init__(self, size: tuple, pos: tuple) -> None:
        super().__init__(size)
        self.pos = pos
        self.program_y = None
        self.program = None
        self.Program_Thread = None
        self.ExitFlag = Event()
        self.events = [Event() for _ in keys]
        self.cursor = [0, 0]

    def draw(self) -> None:
        for i,flag in enumerate(self.events):
            if flag.is_set():
                self.blit(list(keys.items())[i][1], (self.cursor[0], self.cursor[1]))
                flag.clear()
        for i, line in enumerate(self.content):
            if len(line)-1 > self.size[0]:
                self.clear()
                print_at(self.pos[0]+1, self.pos[1]+1,
                         f"line {i} too long!\n{len(line)}\ncropping line for next frame!")
                self.content[i] = self.content[i][:-(len(line)-self.size[0])]
                return
            # print(line)
            compiled = "".join(line)
            print_at(self.pos[0]+1, self.pos[1]+i+1, compiled)

    def clear(self) -> None:
        lines = []
        for i in range(self.size[1]):
            lines.append(" "*self.size[0])
        for i, line in enumerate(lines):
            print_at(self.pos[0]+1, self.pos[1]+i+1, line)
    def capture_program(self, program: str, args: list[str] = []) -> None:
        self.ExitFlag.set()
        self.program = Popen([program]+args, shell=True, stdout=PIPE)
        self.program_y = 0
        for line in self.program.stdout:
            self.blit(line.decode("utf-8").strip(), (0, self.program_y))
            self.draw()
            self.program_y += 1
            for i,flag in enumerate(self.events):
                if flag.is_set():
                    self.program.stdin.write(list(keys.items())[i][1].encode("utf-8")+b"\n")
                    flag.clear()
            if not self.ExitFlag.is_set():
                break
        self.program.terminate()
        self.ExitFlag.clear()
    def program_thread(self,program:str,args:list[str]=[]):
        self.Program_Thread = Thread(target=self.capture_program,args=(program,args))
        self.Program_Thread.start()
    def stop_program(self):
        self.ExitFlag.clear()
        self.Program_Thread.join()
        self.Program_Thread = None
        self.program.terminate()
        self.program = None
        self.program_y = None
        self.clear()
        self.draw()
        return


class cluster:
    def __init__(self):
        self.screens = []
        self.focus = 0
        self.cursors = []

    def draw(self, index: int):
        if not index > len(self.screens):
            self.screens[index].draw()

    def draw_all(self):
        for screen in self.screens:
            screen.draw()

    def remove_screen(self, index: int):
        if not index > len(self.screens):
            self.screens[index].clear()
            self.screens.remove(self.screens[index])
    def add_screen(self,screen:Screen):
        self.screens.append(screen)
        self.cursors.append([0,0])
    def loop(self,callback=empty):
        while True:
            event = window.get_event()       
            for screen in self.screens:
                screen.draw()
                if type(event) == asciimaticsEvent.MouseEvent:
                    if screen.pos[0] <= event.x <= screen.pos[0]+screen.size[0] and screen.pos[1] <= event.y <= screen.pos[1]+screen.size[1]:
                        self.focus = self.screens.index(screen)
            if type(event) == asciimaticsEvent.KeyboardEvent:
                if event.key_code == 10 or self.cursors[self.focus][0] >= self.screens[self.screens.index(screen)].size[0]:
                    self.cursors[self.focus][1] += 1
                    self.cursors[self.focus][0] = 0
                    self.screens[self.focus].cursor[1] += 1
                    self.screens[self.focus].cursor[0] = 0
                if event.key_code in keys:

                    self.screens[self.screens.index(screen)].events[list(keys.keys()).index(event.key_code)].set()
                    self.screens[self.focus].cursor[0] += 1
                    self.cursors[self.focus][0] += 1
                callback(screen,event,self.focus,self.screens)
            sleep(0.1)