from datetime import datetime
from config   import *



def log_add_message(self, text):
	current_time = datetime.now().strftime("%H:%M:%S")
	text         = "[" + current_time + "] " + text
	self._text["state"] = "normal"
	self._text.insert(
		self._text.index(self._text_index),
		text
	)
	self._text.tag_add(
		"time",
		self._text.index(self._text_index),
		self._text.index(self._text_index + 0.1) + "0"
	)
	self._text.tag_config(
		"time",
		foreground="black",
		font=('Helvetica', LOG_FONT_SIZE, 'bold')
	)
	
	self._text.see("end")
	self._text["state"] = "disabled"
	self._text_index += 1.0
