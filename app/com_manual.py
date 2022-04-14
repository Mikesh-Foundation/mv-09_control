from tkinter import *



def _com_manual(self):
	manual_window = Toplevel(self)
	manual_window.title("Manual Control")
	manual_window.geometry("{:d}x{:d}".format(500,500))

	edit_steps = Entry(
		manual_window,
		width            = 10
	)
	edit_steps.insert(0,"1")
	edit_steps.place(relx=0.5, rely=0.5)

	button_up = Button(
		manual_window,
		anchor  = "center",
		text    ="↑",
		command = lambda: self._move_up(int(edit_steps.get()))
	)
	button_up.place(relx=0.5, rely=0.25)

	button_down = Button(
		manual_window,
		anchor  = "center",
		text    ="↓",
		command = lambda: self._move_down(1)
	)
	button_down.place(relx=0.5, rely=0.75)

	button_left = Button(
		manual_window,
		anchor  = "center",
		text    ="←",
		command = lambda: self._move_left(1)
	)
	button_left.place(relx=0.25, rely=0.50)

	button_right = Button(
		manual_window,
		anchor  = "center",
		text    ="→",
		command = lambda: self._move_right(1)
	)
	button_right.place(relx=0.75, rely=0.50)
