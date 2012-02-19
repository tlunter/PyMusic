import xmlrpclib
import sys

###############################################################################

def main():
	action = raw_input("Do what? ")
	print ""
	if(action.lower() == "c"):
		currentTrack()
	elif(action.lower() == "p"):
		playPause()
	elif(action.lower() == "s"):
		search()
	elif(action.lower() == "ps"):
		playSong()
	elif(action.lower() == "m"):
		mute()
	elif(action.lower() == "vu"):
		volumeUp()
	elif(action.lower() == "vd"):
		volumeDown()
	elif(action.lower() == "h"):
		help()
	elif(action.lower() == "x"):
		sys.exit(0)
	else:
		main()
		
def currentTrack():
	print iTunesServer.currentTrack()
	main()
	
def playSong():
	playInput = raw_input("Search Track: ")
	print 'Now Playing: %s'%(iTunesServer.playSong(playInput))
	main()
	
def search():
	searchInput = raw_input("Search: ")
	searchResults = iTunesServer.search(searchInput)
	for track in searchResults:
		print track
	main()
	
def mute():
	print ("Muted" if iTunesServer.mute() else "Not muted")
	main()
	
def volumeUp():
	print "%d/100" %(iTunesServer.volumeUp())
	main()

def volumeDown():
	print "%d/100" %(iTunesServer.volumeDown())
	main()
	
def playPause():
	print "Playing" if iTunesServer.playPause() else "Paused"
	main()
	
def help():
	print "c  = current track"
	print "p  = play/pause"
	print "s  = search"
	print "ps = play song"
	print "m  = mute"
	print "vu = volume up"
	print "vd = volume down"
	print "h  = show these commands"
	print "x  = exit"
	main()
	
###############################################################################

try:
	iTunesServer = xmlrpclib.ServerProxy("http://155.33.141.249:9000")
	iTunesServer.init()
	
	print "What would you like to do?"
	help()
		
except KeyboardInterrupt:
	sys.exit(0)