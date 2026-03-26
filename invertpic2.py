#!/usr/bin/env python

import numpy as np
from PIL import Image
import sys

Image.fromarray(np.array(Image.open(sys.argv[1]))[:,::-1,:]).save(f"{sys.argv[1]}_changed.jpeg")

