import xmlrpclib
import sys

inputRequired = ["ps","s"]
pyMusicServer = "http://155.33.141.249:9000"

###############################################################################

def getInput(text = ""):
	userInput = raw_input(text)
	userInput = userInput.strip()
	
	if userInput:
		return userInput
	return getInput(text)

###############################################################################

def main():
	help()
	print ""
	while(True):
		try:
			userInput = getInput("Do what? ")
			
			splitInput = userInput.split(None, 1)
			
			action = splitInput[0]
			
			try:
				splitInput[1]
			except IndexError:
				if action in inputRequired:
					continue
				splitInput.append("")
			
			fnData = splitInput[1]
			
			if action.lower() == "c":
				currentTrack()
			elif action.lower() == "p":
				playPause()
			elif action.lower() == "s":
				search(fnData)
			elif action.lower() == "ps":
				playSong(fnData)
			elif action.lower() == "pr":
				prevSong()
			elif action.lower() == "n":
				nextSong()
			elif action.lower() == "m":
				mute() 
			elif action.lower() == "vu":
				volumeUp()
			elif action.lower() == "vd":
				volumeDown()
			elif action.lower() == "h":
				help()
			elif action.lower() == "x":
				break
			else:
				continue
			print ""
			
		except KeyboardInterrupt:
			print ""
			break

def currentTrack():
	print iTunesServer.currentTrack()

def playSong(songData):
	print "Now Playing: {0}".format(iTunesServer.playSong(songData))

def search(songData):
	searchResults = iTunesServer.search(songData)
	for track in searchResults:
		print track

def mute():
	print "Muted" if iTunesServer.mute() else "Not muted"

def volumeUp():
	print "{0}/100".format(iTunesServer.volumeUp())

def volumeDown():
	print "{0}/100".format(iTunesServer.volumeDown())

def playPause():
	print "Playing" if iTunesServer.playPause() else "Paused"
	
def nextSong():
	print iTunesServer.nextTrack()
	
def prevSong():
	print iTunesServer.prevTrack()

def help():
	print "c  = current track"
	print "p  = play/pause"
	print "s  = search"
	print "ps = play song"
	print "pr = previous song"
	print "n  = next song"
	print "m  = mute"
	print "vu = volume up"
	print "vd = volume down"
	print "h  = show these commands"
	print "x  = exit"

###############################################################################

iTunesServer = xmlrpclib.ServerProxy(pyMusicServer)
iTunesServer.init()

print "What would you like to do?"
main()