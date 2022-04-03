from tkinter import font as tkFont
from PIL     import Image, ImageTk
from control import *
from config  import *
import tkinter as tk

window = tk.Tk()
window.state("zoomed")
window.title("MV-09 Control")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("{}x{}".format(int(0.95*screen_width), int(0.95*screen_height)))

#Frames___________________________________________________________________
tray    = tk.Frame(
		window,
		width  = 0.500*screen_width,
		height = 0.750*screen_height,
		background="white"
	)
status  = tk.Frame(
		window,
		width  = 0.195*screen_width,
		height = 0.750*screen_height,
		background="white"
	)
log     = tk.Frame(
		window,
		width  = 0.700*screen_width,
		height = 0.180*screen_height,
		background="white"
	)
control = tk.Frame(
		window,
		width  = 0.200*screen_width,
		height = 0.945*screen_height - 10,
		background="white"
	)
tray.place(x=10, y=10)
status.place(x=0.505*screen_width + 10, y=10)
log.place(x=10, y=0.765*screen_height)
control.place(x=0.725*screen_width, y=10)

window.update_idletasks()

canvas = tk.Canvas(
		tray,
		width      = tray.winfo_width(),
		height     = tray.winfo_height(),
		background = "white"
	)
canvas.place(x=0, y=0)

#Text_____________________________________________________________________
text = tk.Text(
		log,
		state  = 'disabled'
	)
text.place(x=0, y=0, relwidth=1, relheight=1)

window.update_idletasks()

#Buttons__________________________________________________________________
button_start                 = tk.Button(control)
button_start["bd"]           = 3
button_start["font"]         = tkFont.Font(size=BUTTON_FONT_SIZE)
button_start["text"]         = BUTTON_START_LABEL
button_start["state"]        = 'disabled'
button_start.place(relx=0, rely=0, relwidth=1, relheight=0.1)

button_stop = tk.Button(control)
button_stop["bd"]            = 3
button_stop["font"]          = tkFont.Font(size=BUTTON_FONT_SIZE)
button_stop["text"]          = BUTTON_STOP_LABEL
button_stop["state"]         = 'disabled'
button_stop.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)

button_queue                 = tk.Button(control)
button_queue["bd"]           = 3
button_queue["font"]         = tkFont.Font(size=BUTTON_FONT_SIZE)
button_queue["text"]         = BUTTON_QUEUE_LABEL
button_queue.place(relx=0, rely=0.2, relwidth=1, relheight=0.1)

button_calibration           = tk.Button(control)
button_calibration["bd"]     = 3
button_calibration["font"]   = tkFont.Font(size=BUTTON_FONT_SIZE)
button_calibration["text"]   = BUTTON_CALIBRATION_LABEL
button_calibration.place(relx=0, rely=0.3, relwidth=1, relheight=0.1)

button_manual                = tk.Button(control)
button_manual["bd"]          = 3
button_manual["font"]        = tkFont.Font(size=BUTTON_FONT_SIZE)
button_manual["text"]        = BUTTON_MANUAL_LABEL
button_manual.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)

button_wiki                  = tk.Button(control)
button_wiki["bd"]            = 3
button_wiki["font"]          = tkFont.Font(size=BUTTON_FONT_SIZE)
button_wiki["text"]          = BUTTON_WIKI_LABEL
button_wiki.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

button_07                    = tk.Button(control)
button_07["bd"]              = 3
button_07["font"]            = tkFont.Font(size=BUTTON_FONT_SIZE)
button_07["state"]           = 'disabled'
button_07.place(relx=0, rely=0.6, relwidth=1, relheight=0.1)

button_connect               = tk.Button(control)
button_connect["bd"]         = 3
button_connect["font"]       = tkFont.Font(size=BUTTON_FONT_SIZE)
button_connect["text"]       = BUTTON_CONNECT_LABEL
button_connect.place(relx=0, rely=0.7, relwidth=1, relheight=0.1)

button_disconnect            = tk.Button(control)
button_disconnect["bd"]      = 3
button_disconnect["font"]    = tkFont.Font(size=BUTTON_FONT_SIZE)
button_disconnect["text"]    = BUTTON_DISCONNECT_LABEL
button_disconnect["state"]   = 'disabled'
button_disconnect.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)

button_exit                  = tk.Button(control)
button_exit["bd"]            = 3
button_exit["font"]          = tkFont.Font(size=BUTTON_FONT_SIZE)
button_exit["text"]          = BUTTON_EXIT_LABEL
button_exit.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


window.mainloop()
