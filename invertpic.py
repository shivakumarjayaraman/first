#!/usr/bin/env python

import numpy as np
from PIL import Image
import sys

filename = sys.argv[1]

pil_image = Image.open(filename)
print(f"Original image type: {type(pil_image)}")

# 2. Convert the PIL image to a NumPy array
# np.array() or np.asarray() can be used
numpy_array = np.array(pil_image)
print(f"Converted array type: {type(numpy_array)}")
print(f"Array shape: {numpy_array.shape}") 
new_numpy_array = numpy_array[:,::-1,:]


new_pil_image = Image.fromarray(new_numpy_array)
new_pil_image.save(f"{filename}_changed.jpeg")
