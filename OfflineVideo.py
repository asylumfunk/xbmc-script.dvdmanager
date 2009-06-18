import os
import config

class OfflineVideo:
	"""Represents an entry in the system"""

	"""
	Description:
		basic constructor
		assigns values to instance variables
	Args:
		location : where the file will be saved
		name : the name of video, without file extension
	Returns:
		a new OfflineVideo instance
	TODO:	do I really want to be assigning to self.extension when this value never changes, for now ;-)
	"""
	def __init__( self, location, name ):
		self.location = os.path.abspath( location )
		self.name = name
		self.extension = config.DefaultVideoExtension

	"""
	Description:
		copies the default video and saves it to the specified path
	TODO: error handling, what if I/O fails?
	TODO: return a status flag of some sort (success/failure)
	TODO: see if we can use (and if there's a benefit to using) a native file copy
	"""
	def add( self ):
		#We need to make sure the location actually exists before we try writing there.
		if not os.path.isdir( self.location ):
			os.makedirs( self.location )

		input = open( os.path.join( os.getcwd(), config.DefaultVideo ), "rb" )
		output = open( self.path(), "wb" )
		output.write( input.read() )
		input.close()
		output.close()

	"""
	Desciption:
		calculates the full pathname of the file
	Returns:
		the full pathname of the file (including extension)
	"""
	def path( self ):
		return os.path.join( self.location, self.name ) + os.path.extsep + self.extension