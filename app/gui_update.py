def _gui_update(self):
	if not(self._connection == None) and self._button_connect["state"] == "normal":
		self._button_connect["state"]     = "disabled"
		self._button_connect.update()
		self._button_disconnect["state"]  = "normal"
		self._button_disconnect.update()
		self._button_calibration["state"] = "normal"
		self._button_calibration.update()
		self._button_manual["state"]      = "normal"
		self._button_manual.update()

	if self._connection == None and self._button_connect["state"] == "disabled":
		self._button_connect["state"]     = "normal"
		self._button_connect.update()
		self._button_disconnect["state"]  = "disabled"
		self._button_disconnect.update()
		self._button_calibration["state"] = "disabled"
		self._button_calibration.update()
		self._button_manual["state"]      = "disabled"
		self._button_manual.update()

	#Queue variable change_____________________________________________________
	if self._queue == None and not(self._connection == None):
		self._button_start["state"]       = "disabled"
		self._button_start.update()
		self._button_stop["state"]        = "disabled"
		self._button_stop.update()

	if not(self._queue == None) and not(self._connection == None):
		self._button_start["state"]       = "normal"
		self._button_start.update()
		self._button_stop["state"]        = "disabled"
		self._button_stop.update()

	#Started variable change___________________________________________________
	if self._started:
		self._button_connect["state"]     = "disabled"
		self._button_connect.update()
		self._button_disconnect["state"]  = "disabled"
		self._button_disconnect.update()
		self._button_calibration["state"] = "normal"
		self._button_calibration.update()
		self._button_start["state"]       = "disabled"
		self._button_start.update()
		self._button_stop["state"]        = "normal"
		self._button_stop.update()

	self.after(100, self._gui_update)
