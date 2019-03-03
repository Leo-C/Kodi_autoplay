## **Autoplay for Kodi**


### Introduction

**Autoplay for Kodi** is a script to play automatically media file at startup of Kodi (using it in Kiosk mode).  
It starts a media file or a playlist from external storage (USB or HD disk) or locally, if no playlist is found on external storage.  


### Installation

*`autoexec.py`* must be copied in userdata directory (generally `/storage/.kodi/userdata/`)


### Configuration

The script can be customized changing some variables (if different than default):

* `LOCAL_VIDEO_PATH` store path for local playlist (default `/storage/.kodi/userdata`)
* `EXT_MEDIA_PATH` store path for external storage (default `/media`)
* `AUTO_PLAYLIST` store name of playlist (or file) to play (default `auto.m3u`)

Using a playlist is preferred, because if file to play change, only `.m3u` playlist must be modified without change  python script


### Debug

From a command window or SSH session (for stand-alone media-player) start `autoexec.py` with command:  
`kodi-send --action='RunScript("special://profile/autoexec.py")'`
  
This permit debug without restarting Kodi; logs are in `/storage/.kodi/temp/kodi.log`


### References:
* [Autoexec for Kodi](https://kodi.wiki/view/Autoexec.py)
* [Python libraries for Kodi](https://codedocs.xyz/xbmc/xbmc/group__python.html)
* [Built-in functions for Kodi](https://kodi.wiki/view/List_of_built-in_functions)
