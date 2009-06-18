import os
import shutil
import config

class OfflineVideo:
	"""Represents an entry in the system"""
	#TODO: error logging

	"""
	Description:
		basic constructor
		assigns values to instance variables
	Args:
		location: where the file will be saved
		name: the name of video, without file extension
	Returns:
		a new OfflineVideo instance
	"""
	def __init__( self, location, name ):
		self.location = os.path.abspath( location )
		self.name = name

	"""
	Description:
		copies the default video and saves it to the specified path
	Returns:
		Success: True
		Failure: False
	"""
	def add( self ):
		#We need to make sure the location actually exists before we try writing there.
		if not os.path.isdir( self.location ):
			try:
				os.makedirs( self.location )
			except OSError:	#failed to create the directory
				return False

		src = os.path.join( os.getcwd(), config.DefaultVideo )
		dst = self.path()

		#We don't want to risk overwriting any existing files, until we have a prompt.
		if not os.path.isfile( src ):
			try:
				shutil.copyfile( src, dst )
			except shutil.Error:	#source and destination are the same file
				return False
			except IOError:	#destination is not writable
				return False
			else:
				return True
		else:
			return False

	"""
	Desciption:
		calculates the full pathname of the file
	Returns:
		the full pathname of the file (including extension)
	"""
	def path( self ):
		return os.path.join( self.location, self.name ) + os.path.extsep + config.DefaultVideoExtension