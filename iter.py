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
		
		super().__init__( sys.argv )

		self.setApplicationName( "Skunk-Browser" )
		self.setApplicationDisplayName( "Skunk" )

class Browser( QMainWindow ):
	"""
	
	"""

	def __init__( self ):
		super().__init__()

		self.setWindowTitle( "Skunk Browser" )
		self.resize( 1366, 768 )
		self.setMinimumSize( 1366, 768 )
		self.setMaximumSize( 1366, 768 )

		self.webView = QWebEngineView()

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
	print ( "Hello from Skunk Browser" ) # Console test

	App = SkunkApp()

	Browser = Browser()

	Browser.show()

	exit( App.exec() ) # Terminate the program when the app exits