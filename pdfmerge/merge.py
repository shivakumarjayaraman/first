#!/usr/bin/env python

import glob
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

for f in glob.iglob("*.pdf") :
    merger.append(f)

combined = open("combined.pdf", "wb")
merger.write(combined)


