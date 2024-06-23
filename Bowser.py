#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class SkunkApp( QApplication ):
	"""
	
	"""

	def __init__( self ):
		self.setAttribute( Qt.AA_UseOpenGLES ) # Enable hardware abstraction using OpenGL
		self.setAttribute( Qt.AA_EnableHighDpiScaling )
		self.setAttribute( Qt.AA_DontUseNativeDialogs )

		super().__init__( sys.srgv )

		self.setApplicationName( "Skunk Browser" )
		self.setApplicationDisplayName( "Skunk" )

class Browser( QMainWindow ):
	"""
	
	"""

	def __init__( self ):
		super().__init__()

		self.setWindowTitle( "Skunk Browser" )
		self.resize( 1366, 768 )
		self.setMinimumSize( 1366, 768 )
		# self.setMaximumSize(  )

		settings = QWebEngineSettings.globalSettings()
		settings.setAttribute( QWebEngineSettings.Accelerated2dCanvasEnabled, True )
		settings.setAttribute( QWebEngineSettings.WebGLEnabled, True )
		settings.setAttribute( QWebEngineSettings.FullScreenSupportEnabled, True )
		settings.setAttribute( QWebEngineSettings.PluginsEnabled, True )
		settings.setAttribute( QWebEngineSettings.JavascriptEnabled, True )
		settings.setAttribute( QWebEngineSettings.DnsPrefetchEnabled, True )
		
		URL = "https://www.google.com/"
		self.webView.load( QUrl( URL ) )

if __name__ == "__main__":
	print ( "Hello world from Skunk Browser!" ) # Console test

	App = SkunkApp()

	Browser = Browser()

	Browser.show()

	sys.exit( App.exec() ) # Terminate the app when the program exits