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
import subprocess
from glob import glob
import numpy as np
import pandas as pd

ex_file = 'ex8.py'
full_points = 8
points = full_points
python = sys.executable

filenames = sorted(glob(os.path.join("ex8_testfiles", "*/")))
if len(filenames) != 3:
    raise FileNotFoundError("Could not find 3 folders in directory ex8_testfiles")

inputs = filenames

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(inputs):
    foldername = test_params
    hamsterfilefolder = glob(os.path.join(foldername, "*/"))[0]
    unittestoutputfile = os.path.join(foldername, "unittestoutput.csv")
    correctoutputfile = os.path.join(foldername, "example_output.csv")
    
    function_call = "could not be called"
    outs = f'No issues found'
    try:
        function_call = [sys.executable, ex_file, hamsterfilefolder, unittestoutputfile, "attc"]
        with subprocess.Popen(function_call, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE) as proc:
            _, stderr = proc.communicate(timeout=30)
            with open(unittestoutputfile, 'r') as fh:
                created_content = pd.read_csv(fh, sep=';', dtype=np.float)
            with open(correctoutputfile, 'r') as fh:
                correct_content = pd.read_csv(fh, sep=';', dtype=np.float)
            
            if len(stderr):
                outs = 'Program call failed due to error'
                errs = stderr.decode('utf-8')
                points -= full_points / len(inputs)
            else:
                errs = ''
                if list(created_content.columns) != list(correct_content.columns):
                    outs = f'{list(created_content.columns)} != {list(correct_content.columns)}'
                    points -= (full_points / len(inputs)) / 4
                
                if not created_content.shape == correct_content.shape:
                    outs = f'Shapes of file columns/rows not equal: {created_content.shape} != {correct_content.shape}'
                    points -= (full_points / len(inputs)) * 3 / 4
                elif not np.all(np.isclose(created_content.values, correct_content.values, atol=0)):
                    inds = list(zip(*np.where(~np.isclose(created_content.values, correct_content.values, atol=0))))
                    outs = f'Values not equal at indices {inds}'
                    points -= (full_points / len(inputs)) * 3 / 4
                    
    except Exception as e:
        outs = f'Program call failed due to error {e}'
        errs = e
        points -= full_points / len(inputs)
    
    print("#" * 10)
    print(f"Test {test_i}")
    print("#" * 10)
    print(f"Program call was:\n---\n{' '.join(function_call)}\n---\n")
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"Notes:\n---\n{outs}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")
