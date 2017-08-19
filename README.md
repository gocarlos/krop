<h1 align="center">
  <img
  src="https://raw.githubusercontent.com/gocarlos/krop/master/snap/gui/icon.png" style="max-width:200px;">
  <br />

Krop</h1>

<p align="center"><b>This is the snap for Krop app</b>, It works on Ubuntu, Fedora, Debian, and other major Linux
distributions.</p>

<br>
<p align="center">Published for  <img src="http://anything.codes/slack-emoji-for-techies/emoji/tux.png" align="top" width="24" /></p>


# Krop
krop is a simple graphical tool to crop the pages of PDF files. It is written in Python and relies on PyQT, python-poppler-qt4 and pyPDF for its functionality. A unique feature of krop is its ability to automatically split pages into subpages to fit the limited screen size of devices such as eReaders. This is particularly useful, if your eReader does not support convenient scrolling.

## Build status
[![Snap Status](https://build.snapcraft.io/badge/gocarlos/krop.svg)](https://build.snapcraft.io/user/gocarlos/krop)


## Installation:
The installation can be done using the terminal or using the software center.

* <img src="snap/gui/Gnome-terminal.png" align="top" width="50" /> Terminal -> type:
    ```bash
    sudo snap install krop
    ```
* <img src="snap/gui/Gnome-software.jpg" align="top" width="50" /> Software center -> search for **krop**.

* Direct [download](https://uappexplorer.com/snap/ubuntu/krop)


## Usage
* ##### To start GUI type:

    ```bash
    # Due to the nature of the snap apps:
    # instead of krop, on has to type krop.krop-app to use the app
    krop.krop-app
    ```



* ##### To start the GUI app without terminal:

    search for krop in gnome, KDE menu etc.
* ##### To use the app without GUI:
    For more cli commands type
    ```bash
    krop.krop-app --help
    ```
    Or consult [Armins webpage](http://arminstraub.com/software/krop#afewtricks)


## Disclaimer:
This software was written by Armin Straub and packaged as Linux snap app by Carlos Gomes. This software is sand-boxed with the confinement strict, meaning can only access your home directory & removable media to read/write the pdf files.

Armin has also debian and gentoo packages available on this [website](http://arminstraub.com/software/krop).
