from tkinter            import font as tkFont
from PIL                import Image, ImageTk
from svglib.svglib      import svg2rlg
from reportlab.graphics import renderPM
from config   import *
import tkinter as tk
import math



class App(tk.Tk):
	#Non-GUI related vaiables
	_connection         = None
	_queue              = None
	_started            = False

	#Frame variables
	_tray               = None
	_log                = None
	_tray_background    = None
	_text               = None
	_text_index         = 1.0

	#Button variables
	_button_start       = None
	_button_stop        = None
	_button_queue       = None
	_button_calibration = None
	_button_manual      = None
	_button_wiki        = None
	_button_07          = None
	_button_connect     = None
	_button_disconnect  = None
	_button_exit        = None

	from app.move           import _move_up
	from app.move           import _move_down
	from app.move           import _move_left
	from app.move           import _move_right
	from app.com_connect    import _com_connect
	from app.com_disconnect import _com_disconnect
	from app.com_manual     import _com_manual
	from app.com_wiki       import _com_wiki
	from app.com_exit       import _com_exit
	from app.gui_update     import _gui_update
	from app.log            import log_add_message

	def __init__(self):
		super().__init__()
		self.state("zoomed")
		self.title("MV-09 Control")
		self.iconbitmap(default='assets/mikesh_logo.ico')

		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		self.geometry(
			"{}x{}".format(
				int(0.95*screen_width),
				int(0.95*screen_height)
			)
		)

		#Frames_________________________________________________________________
		self._tray = tk.Frame(
			self,
			width  = 0.500*screen_width,
			height = 0.750*screen_height,
			background="white"
		)
		status  = tk.Frame(
			self,
			width  = 0.195*screen_width,
			height = 0.750*screen_height,
			background="white"
		)
		self._log     = tk.Frame(
			self,
			width  = 0.700*screen_width,
			height = 0.180*screen_height,
			background="white"
		)
		control = tk.Frame(
			self,
			width  = 0.200*screen_width,
			height = 0.945*screen_height - 10,
			background="white"
		)
		self._tray.place(x=10, y=10)
		status.place(x=0.505*screen_width + 10, y=10)
		self._log.place(x=10, y=0.765*screen_height)
		control.place(x=0.725*screen_width, y=10)

		self.update_idletasks()
		#Tray___________________________________________________________________
		canvas = tk.Canvas(
			self._tray,
			width      = self._tray.winfo_width(),
			height     = self._tray.winfo_height(),
			background = "white"
		)
		canvas.place(x=0, y=0)

		drawing        = svg2rlg("assets/tray.svg")
		xL, yL, xH, yH = drawing.getBounds()
		sx             = 0.95*self._tray.winfo_width()  / (xH - xL)
		sy             = 0.95*self._tray.winfo_height() / (yH - yL)
		sf             = min(sx,sy)
		min_dimension  = min(self._tray.winfo_width(), self._tray.winfo_height())
		drawing.width  = 0.95*(min_dimension + 2*sf*xL)
		drawing.height = 0.95*(min_dimension + 2*sf*yL)
		drawing.scale(sf, sf)
		renderPM.drawToFile(drawing, "assets/tray.png", fmt="PNG")

		self._tray_background = ImageTk.PhotoImage(Image.open("assets/tray.png"))
		cx  = self._tray.winfo_width()/2
		cy  = self._tray.winfo_height()/2
		canvas.create_image(
			cx - 1, # -1 is correction for the offset of the sample tray picture
			cy + 1, # +1 is correction for the offset of the sample tray picture
			image  = self._tray_background,
			anchor = "center"
		)

		r = sf*75
		circles = []
		for x in range(1,10,1):
			a = math.sin(x*math.pi/5) * cy/1.49
			b = math.cos(x*math.pi/5) * cy/1.49

			canvas.create_oval(
				cx-a-r*0.95,
				cy-b-r*0.95,
				cx-a+r*0.95,
				cy-b+r*0.95,
				width   = 3,
				outline = "blue",
				fill    = "white"
			)
			canvas.create_oval(
				cx-a-r*0.9,
				cy-b-r*0.9,
				cx-a+r*0.9,
				cy-b+r*0.9,
				width   = 3,
				outline = "cyan"
			)

			circles.append(tk.Label(
				self._tray,
				text   = str(x),
				bg     = "white",
				anchor = "center",
				font   = tkFont.Font(size=22)
			))
			circles[-1].place(
				x      = cx - a - circles[-1].winfo_width()/2,
				y      = cy - b + circles[-1].winfo_height()/2,
				anchor = "center"
			)

			#Text_______________________________________________________________
			self._text = tk.Text(
					self._log,
					state  = 'disabled'
				)
			self._text.place(x=0, y=0, relwidth=1.0, relheight=1.0)

			self.update_idletasks()

			#Buttons____________________________________________________________
			self._button_start                 = tk.Button(control)
			self._button_start["bd"]           = 3
			self._button_start["font"]         = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_start["text"]         = BUTTON_START_LABEL
			self._button_start["state"]        = 'disabled'
			self._button_start.place(relx=0, rely=0, relwidth=1, relheight=0.1)

			self._button_stop = tk.Button(control)
			self._button_stop["bd"]            = 3
			self._button_stop["font"]          = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_stop["text"]          = BUTTON_STOP_LABEL
			self._button_stop["state"]         = 'disabled'
			self._button_stop.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)

			self._button_queue                 = tk.Button(control)
			self._button_queue["bd"]           = 3
			self._button_queue["font"]         = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_queue["text"]         = BUTTON_QUEUE_LABEL
			self._button_queue.place(relx=0, rely=0.2, relwidth=1, relheight=0.1)

			self._button_calibration           = tk.Button(control)
			self._button_calibration["bd"]     = 3
			self._button_calibration["font"]   = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_calibration["text"]   = BUTTON_CALIBRATION_LABEL
			self._button_calibration["state"]  = 'disabled'
			self._button_calibration.place(relx=0, rely=0.3, relwidth=1, relheight=0.1)

			self._button_manual                = tk.Button(control)
			self._button_manual["bd"]          = 3
			self._button_manual["font"]        = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_manual["text"]        = BUTTON_MANUAL_LABEL
			self._button_manual["state"]       = 'normal'
			self._button_manual.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)

			self._button_wiki                  = tk.Button(control)
			self._button_wiki["bd"]            = 3
			self._button_wiki["font"]          = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_wiki["text"]          = BUTTON_WIKI_LABEL
			self._button_wiki.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

			self._button_07                    = tk.Button(control)
			self._button_07["bd"]              = 3
			self._button_07["font"]            = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_07["state"]           = 'disabled'
			self._button_07.place(relx=0, rely=0.6, relwidth=1, relheight=0.1)

			self._button_connect               = tk.Button(control)
			self._button_connect["bd"]         = 3
			self._button_connect["font"]       = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_connect["text"]       = BUTTON_CONNECT_LABEL
			self._button_connect.place(relx=0, rely=0.7, relwidth=1, relheight=0.1)

			self._button_disconnect            = tk.Button(control)
			self._button_disconnect["bd"]      = 3
			self._button_disconnect["font"]    = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_disconnect["text"]    = BUTTON_DISCONNECT_LABEL
			self._button_disconnect["state"]   = 'disabled'
			self._button_disconnect.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)

			self._button_exit                  = tk.Button(control)
			self._button_exit["bd"]            = 3
			self._button_exit["font"]          = tkFont.Font(size=BUTTON_FONT_SIZE)
			self._button_exit["text"]          = BUTTON_EXIT_LABEL
			self._button_exit.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

			#Button command functions
			self._button_connect["command"]    = lambda: self._com_connect()
			self._button_disconnect["command"] = lambda: self._com_disconnect()
			self._button_manual["command"]     = lambda: self._com_manual()
			self._button_wiki["command"]       = lambda: self._com_wiki()
			self._button_connect["command"]    = lambda: self._com_connect()
			self._button_exit["command"]       = lambda: self._com_exit(self)

			self.after(100, self._gui_update)
