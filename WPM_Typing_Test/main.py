import curses
from curses import wrapper
import time
import random

def start_test(stdSCR):
    stdSCR.clear()
    stdSCR.addstr(0, 0, "Welcome to Speed Test Game \nWhile in Game Press 'esc' to Exit!\nPress Any Key To Begin: ", curses.color_pair(4))
    stdSCR.refresh()
    stdSCR.getkey()

def disply_text(stdSCR, target, current, wpm=0):
    stdSCR.addstr(0, 0, target, curses.color_pair(3))
    stdSCR.addstr(1,0, f"WPM: {wpm}", curses.color_pair(4))

    
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdSCR.addstr(0, i, char,color) 

def load_file():
    with open("text.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()
def wpm_test(stdSCR):
    target_Text = load_file()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdSCR.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed/60)) / 5)
        stdSCR.clear()
        disply_text(stdSCR, target_Text, current_text, wpm)
        stdSCR.refresh()

        if "".join(current_text) == target_Text: 
            stdSCR.nodelay(False)
            break

        try:
            key = stdSCR.getkey()
        except:
            continue  
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_Text):
            current_text.append(key)


        
def main(stdSCR):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    start_test(stdSCR)
    while True:
        wpm_test(stdSCR)
        stdSCR.addstr(2,0, "You Completed The Test! press Any key to Continue('esc' to exit): ")
        key = stdSCR.getkey()
        if ord(key) == 27:
            break
wrapper(main)