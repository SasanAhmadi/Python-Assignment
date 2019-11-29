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
import itertools
from glob import glob

ex_file = 'ex7.py'
full_points = 8
points = full_points
python = sys.executable

filenames = sorted(glob(os.path.join("ex7_testfiles", "*")))
if not len(filenames):
    raise FileNotFoundError("Could not find files in directory ex7_testfiles")

inputs = filenames

correct_outs = ['<TypeError> should be raised', '<ValueError> should be raised', '<ValueError> should be raised',
                '<ValueError> should be raised', '<ValueError> should be raised', '<ValueError> should be raised',
                '<ValueError> should be raised', ('0', 1, ['info', 'base', 'quality']),
                ('235gsa', 5, ['col0', 'col1', 'col2']), ('0', 1, ['info', 'base', 'quality']),
                ('0', 1, ['info', 'base', 'quality']), ('235gsa', 5, ['col0', 'col1', 'col2']),
                ('0', 1, ['info', 'base', 'quality'])]

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inputs, correct_outs)):
    filename, correct_out = test_params
    with open(filename, 'r') as fh:
        file_content = fh.read()

    try:
        from ex7 import parse_file_metadata
        proper_import = True
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inputs)
        proper_import = False
    
    if proper_import:
        try:
            outs = parse_file_metadata(data_as_string=file_content)
            errs = ''
            if len(outs) != 3:
                points -= full_points / len(inputs)
            else:
                if outs[0] != correct_out[0]:
                    points -= full_points / (len(inputs) / 3)
                if outs[1] != correct_out[1]:
                    points -= full_points / (len(inputs) / 3)
                if outs[2] != correct_out[2]:
                    points -= full_points / (len(inputs) / 3)
        except Exception as e:
            if correct_out == '<ValueError> should be raised':
                if isinstance(e, ValueError):
                    outs = f'<ValueError> was raised: {e}'
                    errs = ''
                else:
                    outs = ''
                    errs = e
                    points -= full_points / len(inputs)
            elif correct_out == '<TypeError> should be raised':
                if isinstance(e, TypeError):
                    outs = f'<TypeError> was raised: {e}'
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
    print(f"Input was:\n---\ndata_as_string = <content of file {filename}>\n---\n")
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"Output was:\n---\n{outs}\n---\n")
    print(f"Output should be:\n---\n{correct_outs}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")
