# -*- coding: iso-8859-1 -*-

"""
Cropping functionality for krop.

Copyright (C) 2010-2017 Armin Straub, http://arminstraub.com
"""

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

import copy
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter

class AbstractPdfFile:
    """Abstract class for loading a PDF document used in a corresponding
    PdfCropper class"""
    def loadFromStream(self, stream):
        pass
    def loadFromFile(self, filename):
        self.loadFromStream(open(filename, "rb"))

class AbstractPdfCropper:
    """Abstract class for writing a PDF documents composed of cropped pages
    from PdfFile instances"""
    def writeToStream(self, stream):
        pass
    def writeToFile(self, filename):
        stream = open(filename, "wb")
        self.writeToStream(stream)
        stream.close()
    def addPageCropped(self, pdffile, pagenumber, croplist, rotate=0):
        pass


class PyPdfFile(AbstractPdfFile):
    """Implementation of PdfFile using pyPdf"""
    def __init__(self):
        self.reader = None
    def loadFromStream(self, stream):
        self.reader = PdfFileReader(stream, strict=False)
    def getPage(self, nr):
        page = self.reader.getPage(nr-1)

class PyPdfCropper(AbstractPdfCropper):
    """Implementation of PdfCropper using pyPdf"""
    def __init__(self):
        self.output = PdfFileWriter()
    def writeToStream(self, stream):
        # For certain large pdf files, PdfFileWriter.write() causes the error:
        #  maximum recursion depth exceeded while calling a Python object
        # This issue is present in pyPdf as well as PyPDF2 1.23
        # We therefore temporarily increase the recursion limit.
        old_reclimit = sys.getrecursionlimit()
        sys.setrecursionlimit(10000)
        self.output.write(stream)
        sys.setrecursionlimit(old_reclimit)
    def addPageCropped(self, pdffile, pagenumber, croplist, rotate=0):
        if not croplist:
            return
        page = pdffile.reader.getPage(pagenumber)
        for c in croplist:
            newpage = copy.copy(page)
            self.cropPage(newpage, c, rotate)
            self.output.addPage(newpage)
    def cropPage(self, page, crop, rotate):
        # Note that the coordinate system is up-side down compared with Qt.
        x0, y0 = page.cropBox.lowerLeft
        x1, y1 = page.cropBox.upperRight
        x0, y0, x1, y1 = float(x0), float(y0), float(x1), float(y1)
        x0, x1 = x0+crop[0]*(x1-x0), x1-crop[2]*(x1-x0)
        y0, y1 = y0+crop[3]*(y1-y0), y1-crop[1]*(y1-y0)
        # Update the various PDF boxes
        for box in (page.artBox, page.bleedBox, page.cropBox, page.mediaBox, page.trimBox):
            box.lowerLeft = (x0, y0)
            box.upperRight = (x1, y1)
        if rotate != 0:
            page.rotateClockwise(rotate)

PdfFile = PyPdfFile
PdfCropper = PyPdfCropper
