"""
XBMC DVD Manager
by asylumfunk, http://github.com/asylumfunk

For more information, fire up README.txt
To see what's been changing, check out changelog.xml
"""


import os
import config
from OfflineVideo import OfflineVideo

"""
Description:
	Processes a newline-deliminated list of videos
Args:
	batchFile - name of a newline-deliminated file of titles to be processed
	saveLocation - directory to which all output files are saved
TODO:	return a status flag (perhaps number of files succeeded (and failed), maybe even a message)
"""
def processBatch( batchFile, saveLocation ):
	input = open( batchFile, "r" )
	data = input.read()
	input.close()
	names = data.splitlines()

	for name in names:
		video = OfflineVideo( saveLocation, name )
		video.add()

#Now lets actually do something with it
batchFile = os.path.join( os.getcwd(), config.DefaultBatchFile )
processBatch( batchFile, config.DefaultLocation )
