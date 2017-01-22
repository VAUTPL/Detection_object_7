Detection_object_7
===========
This project is a prototipe to game using Python and Open CV. The code is free to be used and modified by anyone wishing to do it. It was designed with the purpose of play a game and move your arms.

##UTPL
###Professor:
- Rodrigo Barba [lrbarba@utpl.edu.ec](lrbarba@utpl.edu.ec)

###Student:
- Jonathan Torres [jptorres6@utpl.edu.ec](mailto:jptorres6@utpl.edu.ec)

System Requirements
-------------------
* An i3 or better processor. The faster the better, especially at high video resolutions.
* 2 GB or more RAM.
* At least 100 MB Free Disk space
* Windows 7 or later (has only been tested on 10), OS X 10.8 or later, Linux 3.0+

Installation
------------
1. First, one should install the following libraries:
  - [OpenCV](http://opencv.org/) version 2.4.10+
  - [Python](https://www.python.org/) 2.7.9 (or any later Python 2.x) ([See **_Installation on OS X_** if using a Mac](#installation-on-os-x))
  - [Numpy](http://www.numpy.org/) 1.9.2+
  - [Pygame](http://www.pygame.org/) 1.9.1+
- Now download and extract this repository with one of several options:
  - Clone the repository with `$ git clone https://github.com/VAUTPL/Detection_object_7.git`
  - Download the repository as a `.zip` or `.tar.gz` and then extract it.

Running
-------
From a command line in the folder of the repository:

`$ python juego_detection.py

Videos resolution should be 480x150

###On UNIX...
You may add a shebang (`#!`) line to the top of [juego_detection.py](juego_detection.py) with the path to the appropriate Python. Example:

`#! /bin/python` (`#! /bin/hbpython` in the case of Mac) at the top of [juego_detection.py](juego_detection.py)

####Make the script executable
`$ chmod +x juego_detection.py`

####To Run:
`$ ./juego_detection.py

If no video is specified, OpenCV attempts to open the Webcam, see line number 276:
`captura = cv2.VideoCapture(1)`
in [juego_detection.py](juego_detection.py)

###Examples:
**Windows:** `C:\path\to\repository> python juego_detection.py`

**UNIX and UNIX-Like:** `$ python juego_detection.py` or `$ ./juego_detection.py`

**Mac OSX:** `$ hbpython juego_detection.py` or `$ ./juego_detection.py`
