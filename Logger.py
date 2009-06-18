import inspect
import os
import time
import xbmcgui

import config

class Logger:
	def __init__( self, fileName ):
		self.fileName = fileName

	def debug( self, message ):
		print self._log( "debug", message )

	def error( self, message ):
		print self._log( "error", message )
		dlg = xbmcgui.Dialog()
		ok = dlg.ok( "Error", message )

	def stat( self, message ):
		print self._log( "stat", message )

	def _log( self, level, message ):
		caller = inspect.stack()[ 3 ][ 3 ]
		line = time.strftime( "%Y.%m.%d %H:%M:%S" ) + " (" + level + ") : " + caller + " : " + message
		print line

log = Logger( config.Logfile )