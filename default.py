"""
XBMC DVD Manager
by asylumfunk, http://github.com/asylumfunk

For more information, fire up README.txt
To see what's been changing, check out changelog.xml
"""

import os
import config
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
	[1]: number of attempts, -1 if unable to process
"""
def processBatch( batchFile, saveLocation ):

	try:
		input = open( batchFile, "r" )
	except IOError:
		return 0, -1	#zero files saved, unable to open input file

	data = input.read()
	input.close()

	names = data.splitlines()
	successes = 0

	for name in names:
		video = OfflineVideo( saveLocation, name )
		if video.add():
			successes = successes + 1

	return successes, len(names)

#Now lets actually do something with it
batchFile = os.path.join( os.getcwd(), config.DefaultBatchFile )
print processBatch( batchFile, config.DefaultLocation )
