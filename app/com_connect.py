from serial.tools import list_ports
import serial
import time



def _com_connect(self):
	if (self._connection == None):
		self.log_add_message("Connecting..." + "\n")
		self.log_add_message("Detected devices: " + "\n")
		ports = list_ports.comports()
		pi    = None
		for port in ports:
			self.log_add_message(str(list(port)) + "\n")
			if "VID:PID" in list(port)[-1]:
				if (list(port)[-1].split()[1] == "VID:PID=2E8A:0005"):
					pi = list(port)
		if not(pi == None):
			self._connection = serial.Serial(pi[0], 1152000, timeout=1)
			self.log_add_message("Connected to: " + str(pi) + "\n")
		else:
			self.log_add_message("No Raspberry PI PICO detected!" "\n")
