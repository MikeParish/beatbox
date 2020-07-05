# beatbox
![beatbox image](https://github.com/MikeParish/beatbox/blob/master/IMG_0717.jpg)

# about
beatbox is an MPC style finger drum machine using Raspberry Pi and Python. It was inspired by the gpio music box Raspberry Pi project but uses an MCP3008 chip to handle analog to digital conversion for the buttons and solves the playback lag issues in the original project.

# other notes
I tried using pyglet for this project but ran into a "nasty circular dependency" with the music player object in that library (https://pyglet.readthedocs.io/en/latest/modules/media.html). Apparently, there's no way to garbage collect the music player objects, so pyglet will continue making more and more objects every time you play a sound using the buttons until the program crashes and runs out of memory (usually about 1-2 minutes in depending on how fast you push the buttons). I burned a few days trying to solve this problem and implement this project with pyglet but wound up scrapping it. Using pygame mixer seems to be the best way to create something like this (as long as you pre-initialize the mixer and adjust the buffer size).
