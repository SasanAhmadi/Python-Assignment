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

ex_file = 'ex5.py'
full_points = 10
points = full_points
python = sys.executable

filenames = sorted(glob(os.path.join("ex5_testfiles", "*")))
subsequences = ["ATtC", "aT"]

inputs = list(itertools.product(filenames, subsequences))

correct_outs = [({'a': 1, 'c': 2, 'g': 2, 't': 2}, 0), ({'a': 1, 'c': 2, 'g': 2, 't': 2}, 0),
                ({'a': 4, 'c': 2, 'g': 0, 't': 2}, 0), ({'a': 4, 'c': 2, 'g': 0, 't': 2}, 1),
                ({'a': 2, 'c': 2, 'g': 1, 't': 2}, 0), ({'a': 2, 'c': 2, 'g': 1, 't': 2}, 1),
                ({'a': 3, 'c': 3, 'g': 2, 't': 4}, 1), ({'a': 3, 'c': 3, 'g': 2, 't': 4}, 1),
                ({'a': 6, 'c': 5, 'g': 1, 't': 12}, 3), ({'a': 6, 'c': 5, 'g': 1, 't': 12}, 6),
                ({'a': 11, 'c': 7, 'g': 1, 't': 19}, 3), ({'a': 11, 'c': 7, 'g': 1, 't': 19}, 11),
                ({'a': 0, 'c': 0, 'g': 0, 't': 0}, 0), ({'a': 0, 'c': 0, 'g': 0, 't': 0}, 0),
                ({'a': 86, 'c': 71, 'g': 69, 't': 108}, 2), ({'a': 86, 'c': 71, 'g': 69, 't': 108}, 25)]


print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inputs, correct_outs)):
    (filename, subsequence), correct_out = test_params
    with open(filename, 'r') as fh:
        file_content = fh.read()
    
    try:
        from ex5 import count_bases_and_subsequence
        outs = count_bases_and_subsequence(data_as_string=file_content, subsequence=subsequence)
        errs = ''
        if len(outs) != 2:
            points -= full_points / len(inputs)
        else:
            if outs[0] != correct_out[0]:
                points -= full_points / len(inputs) / 2
            if outs[1] != correct_out[1]:
                points -= full_points / len(inputs) / 2
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inputs)
    
    correct_outs = correct_out
    print("#" * 10)
    print(f"Test {test_i}")
    print("#" * 10)
    print(f"Input was:\n---\ndata_as_string = <content of file {filename}>, subsequence = '{subsequence}'\n---\n")
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"Output was:\n---\n{outs}\n---\n")
    print(f"Output should be:\n---\n{correct_outs}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")
