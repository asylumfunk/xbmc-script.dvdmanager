"""
XBMC DVD Manager
by asylumfunk, http://github.com/asylumfunk

For more information, fire up README.txt
To see what's been changing, check out changelog.xml
"""

#Standard modules
import os
import traceback
#Third-party modules
import xbmcgui
#Project modules
import act
import config
import lang
from Logger import log

"""
Description:
	Processes a newline-deliminated list of videos
Args:
	batchFile: name of a newline-deliminated file of titles to be processed
	saveLocation: directory to which all output files are saved
Returns:
	[0]: number of successes
	[1]: number of skips
	[2]: number of failures
"""

#Now lets actually do something with it
lang = lang.lang()

#menu = xbmcgui.Dialog()
#choice = menu.select( config.ApplicationName, [ 'one', 'two', 'three' ] )
#print choice

batchFile = os.path.join( os.getcwd(), config.DefaultBatchFile )
result = act.processBatch( batchFile, config.DefaultLocation )

if result[ 0 ] >= 0 and result[ 1 ] >= 0 and result[ 2 ] >= 0:
	dlg = xbmcgui.Dialog()
	ok = dlg.ok( lang.get( "Add_Batch_Results_Header" )
		, lang.get( "Add_Batch_Results_Copied" ).replace( "{0}", str( result[ 0 ] ) )
		, lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 1 ] ) )
		, lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 2 ] ) ) )
#TODO: log a stat