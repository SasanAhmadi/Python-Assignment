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
import shutil
import sys
from glob import glob
import pickle
import numpy as np

ex_file = 'ex13.py'
full_points = 5
points = full_points
python = sys.executable
output_dir = 'ex13_unittest_tmp'
os.makedirs(output_dir, exist_ok=True)

inp_filenames = sorted(glob(os.path.join("ex13_testfiles", "input*.pkl")))
out_filenames = sorted(glob(os.path.join("ex13_testfiles", "output*.txt")))
if not len(inp_filenames) and not len(out_filenames):
    raise FileNotFoundError("Could not find files in directory ex13_testfiles")

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inp_filenames, out_filenames)):
    inp_filename, out_filename = test_params
    outs = ''
    errs = ''
    
    with open(inp_filename, 'rb') as pfh:
        input_state = pickle.load(pfh)
    
    try:
        from ex13 import GameOfLife
        proper_import = True
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inp_filenames)
        proper_import = False
    
    if proper_import:
        try:
            outfilename = os.path.join(output_dir, os.path.basename(inp_filename).replace('input', 'output') + '.txt')
            def unitinit(self, configpath, outputfile):
                self.state = input_state["state"]
                self.symbol_dead = input_state["symbol_dead"].replace(' ', '-')
                self.symbol_live = input_state["symbol_live"]
                self.outputfile = outputfile
            GameOfLife.__init__ = unitinit
            instance = GameOfLife(configpath=None, outputfile=outfilename)
            
            if not hasattr(instance, '__state_to_file__'):
                outs += f'  no method __state_to_file__() found!\n'
                points -= full_points / len(inp_filenames)
            else:
                instance.__state_to_file__()
                instance.state = ~input_state["state"]
                instance.__state_to_file__()
                
                # Check if output file was created
                if not os.path.exists(outfilename):
                    outs += f'  did not create output file {outfilename}!\n'
                    points -= full_points / len(inp_filenames)
                else:
                    with open(outfilename, 'r') as fh:
                        outcontent = fh.read()
                    with open(out_filename, 'r') as fh:
                        correct_content = fh.read()
                    if outcontent != correct_content:
                        outs += f'  content of output file not correct;\n' \
                                f'  your output:\n"{outcontent}"\n' \
                                f'  correct output:\n"{correct_content}"\n\n'
                        points -= full_points / len(inp_filenames)
            
            errs = ''
        except Exception as e:
            outs = ''
            errs = e
            points -= full_points / len(inp_filenames)
    
    print("#" * 10)
    print(f"Test {test_i}")
    print("#" * 10)
    print(f"Error messages:\n---\n{errs}\n---\n")
    print(f"Notes:\n---\n{outs}\n---\n")
    print(f"Current points:{points:.2f}")

points = points if points > 0 else 0
print("#" * 10)
print(f"Estimated points upon submission: {points:.2f}")
shutil.rmtree(output_dir)
