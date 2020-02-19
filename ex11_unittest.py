"""
Author -- Michael Widrich
Contact -- widrich@ml.jku.at
Date -- 01.10.2019

###############################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This  material,  no  matter  whether  in  printed  or  electronic  form,
may  be  used  for personal  and non-commercial educational use only.
Any reproduction of this manuscript, no matter whether as a whole or in parts,
no matter whether in printed or in electronic form, requires explicit prior
acceptance of the authors.

###############################################################################

"""

import os
import sys
from glob import glob
import pickle
import numpy as np

ex_file = 'ex11.py'
full_points = 11
points = full_points
python = sys.executable

inputs = sorted(glob(os.path.join("ex11_testfiles", "input*.pkl")))
correct_outs = sorted(glob(os.path.join("ex11_testfiles", "output*.pkl")))
if not len(inputs) or not len(correct_outs):
    raise FileNotFoundError("Could not find files in directory ex11_testfiles")

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inputs, correct_outs)):
    filename, correct_out = test_params
    
    with open(filename, 'rb') as pfh:
        input_state = pickle.load(pfh)
    with open(correct_out, 'rb') as pfh:
        correct_state = pickle.load(pfh)
    
    try:
        from ex11 import __compute_next_state__
        proper_import = True
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inputs)
        proper_import = False
    
    if proper_import:
        try:
            outs = __compute_next_state__(state=input_state)
            errs = ''
            if not isinstance(outs, np.ndarray):
                points -= full_points / len(inputs)
            else:
                if (outs.dtype != np.bool) or np.any(outs != correct_state):
                    points -= full_points / len(inputs)
        except Exception as e:
            outs = ''
            errs = e
            points -= full_points / len(inputs)
    
    correct_outs = correct_out
    print("#" * 10)
    print(f"Test {test_i}")
    print("#" * 10)
    print(f"Functioncall was:\n---\n__compute_next_state__(state=\n{input_state})\n---\n")
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"Output was:\n---\n{outs}\n---\n")
    print(f"Output should be:\n---\n{correct_state}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")
