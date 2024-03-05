from functions import *

while True:
    event = MultiTerm.window.get_event()
    if event == None:
        continue
    elif type(event) == MultiTerm.asciimaticsEvent.KeyboardEvent:
        print(process_arrows(event))