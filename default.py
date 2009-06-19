"""
XBMC DVD Manager
by asylumfunk, http://github.com/asylumfunk

For more information, fire up README.txt
To see what's been changing, check out changelog.xml
"""


#Project modules
import ui

ui = ui.ui()

if ui.lang.isSupported():
	ui.batchAdd()
else:
	ui.ok( "Error", "We were unable to ititialize the script.", "The script will now close.", "If the problem persists, please reinstall the script." )