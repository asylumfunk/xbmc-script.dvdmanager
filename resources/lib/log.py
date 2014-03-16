"""
Copyright 2009 asylumfunk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#Standard modules
import inspect
import time

"""Basic error logging functionality for the project"""

"""
Description:
	Used to display non-critical messages
Args:
	message::string : text to be displayed
"""
def debug( message ):
	_log( "debug", message )

"""
Description:
	Used to display non-critical messages
Args:
	message::string : text to be displayed
"""
def error( message ):
	_log( "error", message )

"""
Description:
	Used internally to display all messages
Args:
	level::string : severity of the issue
	message::string : text to be displayed
"""
def _log( level, message ):
	caller = inspect.stack()[ 3 ][ 3 ]
	line = time.strftime( "%Y.%m.%d %H:%M:%S" ) + " (" + level + ") : " + caller + " : " + message
	print line