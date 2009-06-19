"""
Set up some basic configuration values
TODO: make configurable via UI, once we have one
"""
#Standard modules
import os

DefaultLocation = "DVDs/"
DefaultVideo = "insertDisc.mpg"
DefaultVideoExtension = os.path.splitext( DefaultVideo )[ 1 ][ 1: ]

#Sanitize the default location
if DefaultLocation == "":
	DefaultLocation = os.getcwd()
elif not os.path.isabs( DefaultLocation ):
	DefaultLocation = os.path.join( os.getcwd(), DefaultLocation )

ApplicationName = "XBMC DVD Manager"

BatchFileTypeMask = ".txt"