from tkinter import *               # module of workspace
from tkinter import messagebox      # module of closing the window
import time


#create the workspace
tk = Tk()
#check if the game is on
APP_RUNNING = True



#default size of the workspace (800x800 pixels)
size_canvas_x = 800
size_canvas_y = 800
s_x = s_y = 8 # size of game field
step_x = size_canvas_x // s_x # step of horizontal drawing
step_y = size_canvas_y // s_y # step of vertical drawing
#adapt for the field size
size_canvas_x = step_x * s_x 
size_canvas_y = step_y * s_y

menu_x = 250 # debug space


def on_closing():
    '''function for closing the application'''
    global APP_RUNNING
    if messagebox.askokcancel("Leave the game", "Do you want to leave the game?"):
        APP_RUNNING = False



tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Battleship Game")
tk.resizable(0, 0)  # window cannot change
tk.wm_attributes("-topmost", 1) # covers other applications
canvas = Canvas(tk, width = size_canvas_x + menu_x, height = size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill = "white")
canvas.pack()
tk.update()



def draw_table():
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)
            


def button_show_enemy():
    pass


def button_restart():
    pass



b0 = Button(tk, text = "Enemy: visible", command = button_show_enemy)
b0.place(x=size_canvas_x + 20, y=30)
b1 = Button(tk, text = "Restart", command = button_restart)
b1.place(x=size_canvas_x + 20, y=70)


draw_table()
while APP_RUNNING:
    if APP_RUNNING:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
