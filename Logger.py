import os
import time

import config

class Logger:
	def __init__( self, fileName ):
		self.fileName = fileName

	def debug( self, message ):
		print time.strftime("%Y.%m.%d %H:%M:%S -"), message

log = Logger( config.Logfile )