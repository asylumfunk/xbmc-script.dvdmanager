#Standard modules
import os
import traceback
#Third-party modules
import xbmcgui
#Project modules
import act
import config
from lang import lang
from log import log


class ui:

	browseTypes = {
		'ShowAndGetDirectory' : 0,
		'ShowAndGetFile' : 1,
		'ShowAndGetImage' : 2,
		'ShowAndGetWriteableDirectory' : 3
	}

	def batchAdd( self ):
		browser = xbmcgui.Dialog()
		file = browser.browse(
			ui.browseTypes[ 'ShowAndGetFile' ] #type
			, lang.get( "Add_Batch_Browse_File_Header" ) #heading
			, "files" #shares
			, config.BatchFileTypeMask #mask
			, False #useThumbs
			, False #treatAsFolder
			, os.getcwd() + os.sep #default
		)
		if not os.path.isfile( file ): #the user cancelled the dialog
			return
		browser = xbmcgui.Dialog()
		location = browser.browse(
			ui.browseTypes[ 'ShowAndGetDirectory' ] #type
			, lang.get( "Add_Batch_Browse_Location_Header" ) #heading
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
			ok = dlg.ok( lang.get( "Add_Batch_Results_Header" )
				, lang.get( "Add_Batch_Results_Copied" ).replace( "{0}", str( result[ 0 ] ) )
				, lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 1 ] ) )
				, lang.get( "Add_Batch_Results_Skipped" ).replace( "{0}", str( result[ 2 ] ) ) )
		#TODO: log a stat