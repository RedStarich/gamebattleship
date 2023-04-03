from tkinter import *               # module of workspace
from tkinter import messagebox      # module of closing the window
import time


#create the workspace
tk = Tk()
#check if the game is on
APP_RUNNING = True


#define the size of the workspace (800x800 pixels)
size_canvas_x = 800
size_canvas_y = 800


def on_closing():
    '''function for closing the application'''
    global APP_RUNNING
    if messagebox.askokcancel("Leave the game", "Do you want to leave the game?"):
        APP_RUNNING = False




tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Battleship Game")
tk.resizable(0, 0)  # the window size cannot be changable
tk.wm_attributes("-topmost", 1) #the window is not covered by other applications



canvas = Canvas(tk, width = size_canvas_x, height = size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill = "white")
canvas.pack()
tk.update()

while APP_RUNNING:
    if APP_RUNNING:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
