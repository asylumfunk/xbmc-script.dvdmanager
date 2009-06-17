"""
XBMC DVD Manager
by asylumfunk, http://github.com/asylumfunk

For more information, fire up README.txt
To see what's been changing, check out changelog.xml
"""


import os

"""
Set up some basic configuration values
TODO: split this out into its own module(?)
TODO: pull from XML
TODO: make configurable via UI, once we have one
TODO: should this really be a dictionary?
"""
config = {
	"DefaultBatchFile" : "dvds.txt",
	"DefaultLocation" : "DVDs/",
	"DefaultVideo" : "insertDisc.mpg"
}
#TODO: do we care if this could blow up???
config[ "DefaultExtension" ] = os.path.splitext( config.get( "DefaultVideo" ) )[ 1 ][ 1: ]

#Sanitize the default location
if config.get( "DefaultLocation" ) == "":
	config[ "DefaultLocation" ] = os.getcwd()
elif not os.path.isabs( config.get( "DefaultLocation" ) ):
	config[ "DefaultLocation" ] = os.path.join( os.getcwd(), config.get( "DefaultLocation" ) )


"""
Description:	an OfflineVideo object which represents a video entry in the system
TODO:		split this out into its own module(?)
TODO:		can we make the instance variables private?
"""
class OfflineVideo:
	"""
	Desc:	basic constructor
		assigns values to instance variables
	Args:	location - where the file will be saved
		name - the name of video, sans file extension
	Return:	a new OfflineVideo instance
	TODO:	do I really want to be assigning to self.extension when this value never changes, for now ;-)
	"""
	def __init__( self, location, name ):
		self.location = os.path.abspath( location )
		self.name = name
		self.extension = config.get( "DefaultExtension" )

	"""
	Desc:	copies the default video and saves it to the path specified by the object
	Args:	n/a
	Return:	n/a
	TODO:	error handling, what if I/O fails?
	TODO:	return a status flag of some sort (success/failure)
	TODO:	see if we can use (and if there's a benefit to using) a native file copy
	"""
	def add( self ):
		#We need to make sure the location actually exists before we try writing there.
		if not os.path.isdir( self.location ):
			os.makedirs( self.location )

		input = open( os.path.join( os.getcwd(), config.get( "DefaultVideo" ) ), "rb" )
		output = open( self.path(), "wb" )
		output.write( input.read() )
		input.close()
		output.close()

	"""
	Desc:	returns the full pathname of the file
	Args:	n/a
	Return:	the full pathname of the file (including extension)
	"""
	def path( self ):
		return os.path.join( self.location, self.name ) + os.path.extsep + self.extension

"""
Desc:	Processes a newline-deliminated list of videos
Args:	batchFile - name of a newline-deliminated file of titles to be processed
	saveLocation - directory to which all output files should be saved
Return:	n/a
TODO:	can we always assume that the CWD will be constant?
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
batchFile = os.path.join( os.getcwd(), config.get( "DefaultBatchFile" ) )
processBatch( batchFile, config.get( "DefaultLocation" ) )
