#Standard modules
import os
import traceback
#Third-party modules
import xbmcgui
#Project modules
import act
import config
import lang
from log import log

class ui:
	"""Handles the user interface layer"""

	def __init__( self ):
		self.lang = lang.lang()

	browseTypes = {
		'ShowAndGetDirectory' : 0,
		'ShowAndGetFile' : 1,
		'ShowAndGetImage' : 2,
		'ShowAndGetWriteableDirectory' : 3
	}

	def batchAdd( self ):
		fileBrowser = xbmcgui.Dialog()
		file = fileBrowser.browse(
			ui.browseTypes[ 'ShowAndGetFile' ] #type
			, self.lang.get( "Add_Batch_Browse_File_Header" ) #heading
			, "files" #shares
			, config.BatchFileTypeMask #mask
			, False #useThumbs
			, False #treatAsFolder
			, os.getcwd() + os.sep #default
		)
		if not os.path.isfile( file ): #the user cancelled the dialog
			return
		locationBrowser = xbmcgui.Dialog()
		location = locationBrowser.browse(
			ui.browseTypes[ 'ShowAndGetDirectory' ] #type
			, self.lang.get( "Add_Batch_Browse_Location_Header" ) #heading
			, "video" #shares
			, "" #mask
			, True #useThumbs
			, False #treatAsFolder
			, "" #default
		)
		location = os.path.normpath( location )
		if not os.path.isdir( location ): #the user cancelled the dialog
			return
		result = act.processBatch( file, location )
		if result[ 0 ] >= 0 and result[ 1 ] >= 0 and result[ 2 ] >= 0:
			dlg = xbmcgui.Dialog()
			ok = self.ok( self.lang.get( "Add_Batch_Results_Header" )
				, self.lang.get( "Add_Batch_Results_Copied" ).replace( "{0}", str( result[ 0 ] ) )
				, self.lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 1 ] ) )
				, self.lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 2 ] ) ) )
		#TODO: log a stat

	def ok( self, header, line1 = "", line2 = "", line3 = "" ):
		dialog = xbmcgui.Dialog()
		return dialog.ok( header, line1, line2, line3 )