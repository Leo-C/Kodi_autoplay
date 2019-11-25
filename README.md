## **Autoplay for Kodi**


### Introduction

**Autoplay for Kodi** is a script to play automatically media file and/or show photos at startup of Kodi (using it in Kiosk mode).  
It play a media file or a playlist and show photos from external storage (USB drive), or locally if no playlist is found on external storage.  


### Installation

*`autoexec.py`* must be copied in userdata directory (generally `/storage/.kodi/userdata/`)


### Configuration

The script can be customized changing some variables (if different than default).  
It's possible also to show some photos listening music, defining:  

* a playlist only with music
* a slideshow config file


Common variables:

* `LOCAL_VIDEO_PATH` store path for local playlist and/or photo cfg file (default `/storage/.kodi/userdata`)
* `EXT_MEDIA_PATH` store path for external storage (default `/media`)

For media files:

* `PLAYLIST` store name of playlist (or file) to play (default `auto.m3u`)

Using a playlist is preferred, because if file to play change, only `.m3u` playlist must be modified without change  python script

For photos:

* `SLIDE_CFG` is config file for slideshow (default `photos.cfg`)

this config file is a text file with key-value structure:

`#Comment`  
`dir=<slideshow path>` #mandatory  
`subdirs=[1|0]` #optional (default = no)  
`random=[1|0]` #optional (default = yes); if not random photos show in alphabetic order  


### Debug

From a command window or SSH session (for stand-alone media-player) start `autoexec.py` with command:  
`kodi-send --action='RunScript("special://profile/autoexec.py")'`
  
This permit debug without restarting Kodi; logs are in `/storage/.kodi/temp/kodi.log`


### References:
* [Autoexec for Kodi](https://kodi.wiki/view/Autoexec.py)
* [Python libraries for Kodi](https://codedocs.xyz/xbmc/xbmc/group__python.html)
* [Built-in functions for Kodi](https://kodi.wiki/view/List_of_built-in_functions)
* [List of booleans conditions](https://kodi.wiki/view/List_of_boolean_conditions)
