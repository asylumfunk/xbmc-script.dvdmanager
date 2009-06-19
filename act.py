#Project modules
from log import log
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