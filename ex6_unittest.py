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
import types
import hashlib

ex_file = 'ex6.py'
full_points = 4
points = full_points
python = sys.executable

directories = sorted(glob(os.path.join("ex6_testfiles", "*")))

inputs = directories

correct_outs = ['155a46db64601fb331ef9450f8da66ae', '0406008debab66f970be190019564085',
                'd41d8cd98f00b204e9800998ecf8427e', '155a46db64601fb331ef9450f8da66ae']


print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inputs, correct_outs)):
    directories, correct_out = test_params
    
    try:
        from ex6 import read_raw_files
        generator = read_raw_files(foldername=directories)
        
        errs = ''
        if not isinstance(generator, types.GeneratorType):
            points -= full_points / len(inputs)
            outs = f"not a generator object but {type(generator)} object"
        else:
            checksum = hashlib.md5()
            _ = [checksum.update(bytes(c, 'utf-8')) for c in generator]
            checksum = checksum.hexdigest()
            if checksum != correct_out:
                points -= full_points / len(inputs)
            outs = f"{checksum}"
            
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inputs)
    
    correct_outs = correct_out
    print("#" * 10)
    print(f"Test {test_i}")
    print("#" * 10)
    print(f"Input was:\n---\nfoldername = '{directories}'\n---\n")
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"MD5-hash of file contents was:\n---\n{outs}\n---\n")
    print(f"MD5-hash of file contents should be:\n---\n{correct_outs}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")
