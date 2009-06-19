#Standard modules
import inspect
import os
import time
#Third-party modules
import xbmcgui
#Project modules
import config

class log:
	def __init__( self ):
		pass

	def debug( self, message ):
		print self._log( "debug", message )

	def error( self, message ):
		print self._log( "error", message )

	def stat( self, message ):
		print self._log( "stat", message )

	def _log( self, level, message ):
		caller = inspect.stack()[ 3 ][ 3 ]
		line = time.strftime( "%Y.%m.%d %H:%M:%S" ) + " (" + level + ") : " + caller + " : " + message
		print line

log = log( )