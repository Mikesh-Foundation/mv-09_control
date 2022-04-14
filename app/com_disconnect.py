def _com_disconnect(self):
	if not(self._connection == None):
		self._connection.close()
		self._connection = None
		self.log_add_message("Connection closed!" + "\n")
	else:
		self.log_add_message("No device connected!" + "\n")
