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

ex_file = 'ex9.py'
full_points = 5
points = full_points
python = sys.executable

inputs = ["testfolder1", "testfolder2"]

for inputfolder in inputs:
    if os.path.exists(inputfolder):
        raise FileExistsError(f"Please remove folders {inputs} to start the unit test script.")

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(inputs):
    foldername = test_params
    
    function_call = "could not be called"
    outs = f'No issues found'
    try:
        function_call = [sys.executable, ex_file, foldername]
        with subprocess.Popen(function_call, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE) as proc:
            _, stderr = proc.communicate(timeout=60*5)
            
            if len(stderr):
                outs = 'Program call failed due to error'
                errs = stderr.decode('utf-8')
                points -= full_points / len(inputs)
            else:
                errs = ''
                outs = ''
                for folder in [f"{i:02}" for i in range(10)]:
                    if not os.path.exists(os.path.join(foldername, folder)):
                        points -= full_points / len(inputs) / 3
                        outs += f"Folder {os.path.join(foldername, folder)} not found\n"
                        break
                else:
                    outs += f"Creation of folders seems correct\n"
                for folder in [f"{i:02}" for i in range(10)]:
                    if not os.path.exists(os.path.join(foldername, folder, 'sequence_analysis.csv')):
                        points -= full_points / len(inputs) / 3
                        outs += f"File {os.path.join(foldername, folder, 'sequence_analysis.csv')} not found\n"
                        break
                else:
                    outs += f"Creation of {os.path.join(foldername, folder, 'sequence_analysis.csv')} seems correct\n"
                for folder in [f"{i:02}" for i in range(10)]:
                    if not os.path.exists(os.path.join(foldername, folder, 'sequence_analysis.png')):
                        points -= full_points / len(inputs) / 3
                        outs += f"File {os.path.join(foldername, folder, 'sequence_analysis.png')} not found\n"
                        break
                else:
                    outs += f"Creation of {os.path.join(foldername, folder, 'sequence_analysis.png')} seems correct\n"
                
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
