from tkinter import *
import tkinter.messagebox
import tcp_port_scan as tps

# Grundaufbau:
COLOR_THEME_1 = "cyan"
TEXT_COLOR = "black"
gui_ps = Tk()
gui_ps.title("Port-Scanner")
gui_ps.configure(bg="black")
ps_frame = Frame(relief=RAISED, bd=8, bg=COLOR_THEME_1)

# Labels:
label_title = Label(ps_frame, bg=COLOR_THEME_1, fg=TEXT_COLOR, text="PORT-SCANNER", font=30, height=4)

# Baue Umgebnung:
ps_frame.grid()
label_title.grid(column=0, row=0, columnspan=4)

# Starte GUI:
gui_ps.mainloop()