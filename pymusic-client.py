import xmlrpclib
import sys

###############################################################################

def getInput(text = ""):
    userInput = raw_input(text)
    userInput = userInput.strip()
    
    if userInput == "":
        return getInput(text)
    else:
        return userInput

###############################################################################

def main():
    help()
    while(True):
        print ""
    	userInput = getInput("Do what? ")
	    
    	splitInput = userInput.split(None, 1)
	
    	action = splitInput[0]
	
    	try:
    	    splitInput[1]
    	except IndexError:
    	    if action == "ps" or action == "s":
    	        continue
    	    splitInput.append("")
	    
    	fnData = splitInput[1]
	
    	if(action.lower() == "c"):
    		currentTrack()
    	elif(action.lower() == "p"):
    		playPause()
    	elif(action.lower() == "s"):
    		search(fnData)
    	elif(action.lower() == "ps"):
    		playSong(fnData)
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
	
def playSong(songData):
	print "Now Playing: %s" %(iTunesServer.playSong(songData))
	
def search(songData):
	searchResults = iTunesServer.search(songData)
	for track in searchResults:
		print track
	
def mute():
	print "Muted" if iTunesServer.mute() else "Not muted"
	
def volumeUp():
	print "%d/100" %(iTunesServer.volumeUp())

def volumeDown():
	print "%d/100" %(iTunesServer.volumeDown())
	
def playPause():
	print "Playing" if iTunesServer.playPause() else "Paused"
	
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
	
###############################################################################

try:
	iTunesServer = xmlrpclib.ServerProxy("http://155.33.141.249:9000")
	iTunesServer.init()
	
	print "What would you like to do?"
	main()
		
except KeyboardInterrupt:
	sys.exit(0)