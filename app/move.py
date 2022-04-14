def _move_up(self, steps=1):
	if not(self._connection == None):
		self.log_add_message("Taking {:d} steps up...".format(steps) + "\n")
		self._connection.write(
			"driver_v.move(steps={:d},direction=True,speed=10)\r\f".format(steps).encode("UTF8")
		)
	else:
		self.log_add_message("Raspberry PI PICO is not connected!" + "\n")

def _move_down(self, steps=1):
	if not(self._connection == None):
		self.log_add_message("Taking {:d} steps down...".format(steps) + "\n")
		self._connection.write(
			"driver_v.move(steps={:d},direction=False,speed=10)\r\f".format(steps).encode("UTF8")
		)
	else:
		self.log_add_message("Raspberry PI PICO is not connected!" + "\n")

def _move_left(self, steps=1):
	if not(self._connection == None):
		self.log_add_message("Taking {:d} steps left...".format(steps) + "\n")
		self._connection.write(
			"driver_h.move(steps={:d},direction=True,speed=10)\r\f".format(steps).encode("UTF8")
		)
	else:
		self.log_add_message("Raspberry PI PICO is not connected!" + "\n")

def _move_right(self, steps=1):
	if not(self._connection == None):
		self.log_add_message("Taking {:d} steps right...".format(steps) + "\n")
		self._connection.write(
			"driver_h.move(steps={:d},direction=False,speed=10)\r\f".format(steps).encode("UTF8")
		)
	else:
		self.log_add_message("Raspberry PI PICO is not connected!" + "\n")
