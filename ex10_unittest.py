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

ex_file = 'ex10.py'
full_points = 11
points = full_points
python = sys.executable

filenames = sorted(glob(os.path.join("ex10_testfiles", "*")))
if not len(filenames):
    raise FileNotFoundError("Could not find files in directory ex10_testfiles")

inputs = filenames

with open('ex10_correct_outputs.pkl', 'rb') as pfh:
    correct_outs = pickle.load(pfh)

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inputs, correct_outs)):
    filename, correct_out = test_params
    
    try:
        from ex10 import read_config_file
        proper_import = True
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inputs)
        proper_import = False
    
    if proper_import:
        try:
            outs = read_config_file(configpath=filename)
            errs = ''
            if correct_out == '<ValueError> should be raised':
                    outs = outs
                    points -= full_points / len(inputs)
            elif correct_out == '<AttributeError> should be raised':
                    outs = outs
                    points -= full_points / len(inputs)
            else:
                n_expected_returns = 4
                if len(outs) != n_expected_returns:
                    points -= full_points / len(inputs)
                else:
                    if not isinstance(outs[0], int) or outs[0] != correct_out[0]:
                        points -= full_points / len(inputs) / n_expected_returns
                    if outs[1] != correct_out[1]:
                        points -= full_points / len(inputs) / n_expected_returns
                    if outs[2] != correct_out[2]:
                        points -= full_points / len(inputs) / n_expected_returns
                    try:
                        if not np.all(outs[3] == correct_out[3]) or not outs[3].dtype == np.bool:
                            points -= full_points / len(inputs) / n_expected_returns
                    except Exception as e:
                        points -= full_points / len(inputs) / n_expected_returns
        except Exception as e:
            if correct_out == '<ValueError> should be raised':
                if isinstance(e, ValueError):
                    outs = f'<ValueError> was raised: {e}'
                    errs = ''
                else:
                    outs = ''
                    errs = e
                    points -= full_points / len(inputs) * 3
            elif correct_out == '<AttributeError> should be raised':
                if isinstance(e, AttributeError):
                    outs = f'<AttributeError> was raised: {e}'
                    errs = ''
                else:
                    outs = ''
                    errs = e
                    points -= full_points / len(inputs)
            else:
                outs = ''
                errs = e
                points -= full_points / len(inputs)
    
    correct_outs = correct_out
    print("#" * 10)
    print(f"Test {test_i}")
    print("#" * 10)
    print(f"Functioncall was:\n---\nread_config_file(configpath={filename})>\n---\n")
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"Output was:\n---\n{outs}\n---\n")
    print(f"Output should be:\n---\n{correct_outs}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")

