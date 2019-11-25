#by Leonardo Cocco - 20191125
from os import listdir
from os.path import isfile, isdir, join
import xbmc


LOCAL_VIDEO_PATH = "/storage/.kodi/userdata"
EXT_MEDIA_PATH = "/media"

#for media files
PLAYLIST = "auto.m3u"

# config file with following entry:
#  dir=<slideshow path> #mandatory
#  subdirs=[1|0] #optional (default = no)
#  random=[1|0] #optional (default = yes); if not random photos are show in alphabetic order
SLIDE_CFG = "photos.cfg"


def play(): # ... audio/video files!
	filepath = ''
	
	# look first on external media (USB drive) ...
	for fn in listdir(EXT_MEDIA_PATH):
		if isdir(join(EXT_MEDIA_PATH, fn)) and isfile(join(EXT_MEDIA_PATH, fn, PLAYLIST)):
			filepath = join(EXT_MEDIA_PATH, fn, PLAYLIST)
			xbmc.executebuiltin('PlayMedia("%s")' % filepath)
	
	# ... then look in internal filesystem
	if filepath == '' and isfile(join(LOCAL_VIDEO_PATH, PLAYLIST)):
		filepath = join(LOCAL_VIDEO_PATH, PLAYLIST)
		xbmc.executebuiltin('PlayMedia("%s")' % filepath)
	
	if filepath != '':
		xbmc.executebuiltin("PlayerControl(RepeatAll)") #loop media player
		return True
	else:
		return False


def read_cfg(filename):
	props = {}
	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip() #removes trailing whitespace and '\n' chars
			
			if "=" not in line: continue #skips blanks and comments w/o '='
			if line.startswith("#"): continue #skips comments that starts with '#'
			
			k, v = line.split("=", 1)
			props[k] = v
	
	return props

def show(): # ... photos!
	path = ''
	
	# look first on external media (USB drive) ...
	for fn in listdir(EXT_MEDIA_PATH):
		if isdir(join(EXT_MEDIA_PATH, fn)) and isfile(join(EXT_MEDIA_PATH, fn, SLIDE_CFG)):
			path = join(EXT_MEDIA_PATH, fn)
	
	# ... then look in internal filesystem
	if path == '' and isfile(join(LOCAL_VIDEO_PATH, SLIDE_CFG)):
		path = LOCAL_VIDEO_PATH
	
	if path != '':
		cfg = read_cfg(join(path, SLIDE_CFG))
		if 'dir' in cfg.keys():
			dir = cfg['dir']
			options = ''
			
			subdirs = False #default
			if 'subdirs' in cfg.keys():
				value = cfg['subdirs']
				subdirs = (value.strip() == '1')
			if subdirs:
				options += ", recursive"
			
			random = True #default
			if 'random' in cfg.keys():
				value = cfg['random']
				random = (value.strip() == '1')
			if random:
				options += ", random"
			else:
				options += ", notrandom"
			
			xbmc.executebuiltin('SlideShow("%s"%s)' % (join(path, dir), options))
			return True
		else:
			return False
	else:
		return False


def main():
	if play():
		xbmc.sleep(1000)
	show()


main()
