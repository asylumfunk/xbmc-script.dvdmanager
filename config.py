"""
Set up some basic configuration values
TODO: make configurable via UI, once we have one
"""

import os


DefaultBatchFile = "dvds.txt"
DefaultLocation = "DVDs/"
DefaultVideo = "insertDisc.mpg"
DefaultExtension = os.path.splitext( DefaultVideo )[ 1 ][ 1: ]

#Sanitize the default location
if DefaultLocation == "":
	DefaultLocation = os.getcwd()
elif not os.path.isabs( DefaultLocation ):
	DefaultLocation = os.path.join( os.getcwd(), DefaultLocation )
