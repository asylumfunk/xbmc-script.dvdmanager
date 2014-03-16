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

"""
XBMC DVD Manager
by asylumfunk, http://github.com/asylumfunk

For more information, fire up README.txt
To see what's been changing, check out changelog.xml
"""

import os
import sys
import xbmcaddon

__addon__ = xbmcaddon.Addon('script.dvdmanager')
__scriptname = __addon__.getAddonInfo('name')
__path__ = __addon__.getAddonInfo('path')
__resources__ = os.path.join(__path__, 'resources')
__lib__ = os.path.join(__resources__, 'lib')

sys.path.append(__lib__)

#Project modules
import ui

if __name__ == '__main__':
	if ui.lang.isSupported():
		ui.displayMainMenu()
	else:
		ui.ok( "Error", "We were unable to ititialize the script.", "The script will now close.", "If the problem persists, please reinstall the script." )
