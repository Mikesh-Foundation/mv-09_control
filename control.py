from PIL import Image, ImageTk
import tkinter as tk



window = tk.Tk()
window.state("zoomed")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("{}x{}".format(int(0.95*screen_width), int(0.95*screen_height)))

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

text = tk.Text(
		log,
		width=log.winfo_width(),
		height=log.winfo_height(),
		state='disabled'
	)
text.place(x=0, y=0)

window.update_idletasks()

window.mainloop()
