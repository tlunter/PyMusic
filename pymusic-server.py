import win32com.client, pythoncom
import SocketServer
import sys
import xmlrpclib
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

###############################################################################

class ThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer): pass

###############################################################################

def clear(f):
	def send_init(*args):
		args[0].init()
		return f(*args)
	return send_init
	
class iTunesSearcher:
	def init(self):
		pythoncom.CoInitialize()
		self.iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
		self.library = self.iTunes.LibraryPlaylist
		return "Success"
	
	@clear
	def playSong(self, text):
		searchTracks = self.library.Search(text,0);
		if searchTracks:
			searchTracks[0].Play()
			
		return self.currentTrack
		
	@clear
	def search(self, text):
		searchTracks = self.library.Search(text,0)
		if searchTracks:
			results = [self.trackListing(item) for item in searchTracks]
		else:
			results = []
		return results
		
	@clear
	def mute(self):
		self.iTunes.Mute = not(self.iTunes.Mute)
		return self.iTunes.Mute
		
	@clear
	def volumeUp(self):
		if self.iTunes.SoundVolume >= 90:
			self.iTunes.SoundVolume = 100
		else:
			self.iTunes.SoundVolume += 10
		return self.iTunes.SoundVolume
			
	@clear
	def volumeDown(self):
		if self.iTunes.SoundVolume <= 10:
			self.iTunes.SoundVolume = 0
		else:
			self.iTunes.SoundVolume -= 10
		return self.iTunes.SoundVolume
		
	@clear
	def playPause(self):
		self.iTunes.PlayPause()
		return (self.iTunes.PlayerState == True)
		
	@clear
	def currentTrack(self):
		data = self.iTunes.CurrentTrack
		return (self.trackListing(data) if data else "None")
		
	@clear
	def nextTrack(self):
		self.iTunes.NextTrack()
		return self.currentTrack()
		
	@clear
	def prevTrack(self):
		self.iTunes.PreviousTrack()
		return self.currentTrack()
	
	def trackListing(self,item):
		return "%s - %s - %s" %(item.Artist,item.Name,item.Album)

		 
###############################################################################
		
###############################################################################

server = ThreadedXMLRPCServer(("0.0.0.0", 9000), SimpleXMLRPCRequestHandler)
server.register_instance(iTunesSearcher())

try:
	server.serve_forever()
except KeyboardInterrupt:
	sys.exit(0)