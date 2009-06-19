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
import config
import lang
from Logger import log
from OfflineVideo import OfflineVideo

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
def processBatch( batchFile, saveLocation ):
	try:
		input = open( batchFile, "r" )
	except IOError:
		log.error( "Zero files saved, unable to open the input file: " + batchFile )
		return -1, -1, -1

	data = input.read()
	input.close()

	names = data.splitlines()
	successes = 0
	failures = 0
	skips = 0

	for name in names:
		video = OfflineVideo( saveLocation, name )
		result = video.add()
		if result > 0:
			successes = successes + 1
		elif result < 0:
			failures = failures +1
		else:
			skips = skips + 1

	return successes, skips, failures

#Now lets actually do something with it
lang = lang.lang()
batchFile = os.path.join( os.getcwd(), config.DefaultBatchFile )
result = processBatch( batchFile, config.DefaultLocation )

if result[ 0 ] >= 0 and result[ 1 ] >= 0 and result[ 2 ] >= 0:
	dlg = xbmcgui.Dialog()
	ok = dlg.ok( lang.get( "Add_Batch_Results_Header" )
		, lang.get( "Add_Batch_Results_Copied" ).replace( "{0}", str( result[ 0 ] ) )
		, lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 1 ] ) )
		, lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 2 ] ) ) )
#TODO: log a stat