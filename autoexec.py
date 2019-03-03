#by Leonardo Cocco - 20170423
from os import listdir
from os.path import isfile, isdir, join
import xbmc


LOCAL_VIDEO_PATH = "/storage/.kodi/userdata"
EXT_MEDIA_PATH = "/media"
AUTO_PLAYLIST = "auto.m3u"

found = False
for fn in listdir(EXT_MEDIA_PATH):
    if isdir(join(EXT_MEDIA_PATH, fn)) and isfile(join(EXT_MEDIA_PATH, fn, AUTO_PLAYLIST)):
        path = join(EXT_MEDIA_PATH, fn, AUTO_PLAYLIST)
        found = True
        xbmc.executebuiltin("PlayMedia(%s)" % path)

if not found and isfile(join(LOCAL_VIDEO_PATH, AUTO_PLAYLIST)):
    path = join(LOCAL_VIDEO_PATH, AUTO_PLAYLIST)
    found = True
    xbmc.executebuiltin("PlayMedia(%s)" % path)

if found:
    xbmc.executebuiltin("PlayerControl(RepeatAll)")
