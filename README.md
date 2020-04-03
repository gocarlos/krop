<h1 align="center">
  <img src="https://raw.githubusercontent.com/gocarlos/krop/master/snap/gui/icon.png" style="max-width:100px;">

  <br />

Krop</h1>

<p align="center"><b>This is the snap for Krop app</b>, It works on Ubuntu, Fedora, Debian, and other major Linux
distributions.</p>

<br>

<p align="center">Published for 🐧</p>

# Krop ✄

krop is a simple graphical tool to crop the pages of PDF files. It is written in Python and relies on PyQT, python-poppler-qt4 and pyPDF for its functionality. A unique feature of krop is its ability to automatically split pages into subpages to fit the limited screen size of devices such as eReaders. This is particularly useful, if your eReader does not support convenient scrolling.

[![Snap Status](https://build.snapcraft.io/badge/gocarlos/krop.svg)](https://build.snapcraft.io/user/gocarlos/krop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/962d353f2fab4ea2bb594185dd506f0a)](https://www.codacy.com/manual/edumco/krop?utm_source=github.com&utm_medium=referral&utm_content=edumco/krop&utm_campaign=Badge_Grade)

## Installation

The installation can be done using the terminal or using the software center.

💻 Terminal: `sudo snap install krop`

🛍 [Software center](https://snapcraft.io/krop/): search for **krop** in the Software center.

## Usage

1. To start GUI type `krop`

2. To start the GUI app without terminal search for krop in Dvisual menu of your distro.

3. To use the app without GUI: `krop.krop-app --help`

Or consult [Armins webpage](http://arminstraub.com/software/krop#afewtricks)

## Disclaimer

This software was written by Armin Straub and packaged as Linux snap app by Carlos Gomes. This software is sand-boxed with the confinement strict, meaning can only access your home directory & removable media to read/write the pdf files.

Armin has also debian and gentoo packages available on this [website](http://arminstraub.com/software/krop).
