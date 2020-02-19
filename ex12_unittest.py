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

ex_file = 'ex12.py'
full_points = 8
points = full_points
python = sys.executable
output_dir = 'ex12_unittest_tmp'
os.makedirs(output_dir, exist_ok=True)

inputs = sorted(glob(os.path.join("ex12_testfiles", "input*.pkl")))
if not len(inputs):
    raise FileNotFoundError("Could not find files in directory ex11_testfiles")
outputfilenames = [os.path.join(output_dir, 'out00'), os.path.join(output_dir, 'out01')]

print(f"Unittest for: {ex_file}")

for test_i, test_params in enumerate(zip(inputs, outputfilenames)):
    filename, outputname = test_params
    outs = ''
    errs = ''
    
    with open(filename, 'rb') as pfh:
        input_dict = pickle.load(pfh)
    
    try:
        from ex12 import GameOfLife
        proper_import = True
    except Exception as e:
        outs = ''
        errs = e
        points -= full_points / len(inputs)
        proper_import = False
    
    if proper_import:
        try:
            outfilename = os.path.join(outputname, os.path.basename(filename))
            def unittest_read_config_file(_, configpath):
                with open(configpath, 'rb') as pfh:
                    content_dict = pickle.load(pfh)
                return tuple([content_dict[k] for k in ('n_iterations', 'symbol_dead', 'symbol_live', 'state')])
            GameOfLife.read_config_file = unittest_read_config_file
            instance = GameOfLife(configpath=filename, outputfile=outfilename)
            
            # Check if output file was created
            if not os.path.exists(outfilename):
                outs += f'  did not create output file {outfilename}!\n'
                points -= full_points / len(inputs) / 6
            plot_folder = os.path.join(outputname, 'plots')
            if not os.path.exists(plot_folder):
                outs += f'  did not create folder {plot_folder}!\n'
                points -= full_points / len(inputs) / 6
            
            attribute = 'outputfile'
            if not hasattr(instance, 'outputfile'):
                outs += f'  missing attribute {attribute}!\n'
                points -= full_points / len(inputs) / 6
            else:
                out = getattr(instance, attribute)
                if outfilename != out:
                    outs += f'  attribute {attribute} has incorrect value (should be {outfilename} but is {out})!\n'
                    points -= full_points / len(inputs) / 6
                
            for attribute in input_dict.keys():
                if not hasattr(instance, attribute):
                    outs += f'  missing attribute {attribute}!\n'
                    points -= full_points / len(inputs) / 6
                else:
                    out = getattr(instance, attribute)
                    cout = input_dict[attribute]
                    if isinstance(cout, np.ndarray) and np.any(cout != out):
                        outs += f'  attribute {attribute} has incorrect value (should be {cout} but is {out})!\n'
                        points -= full_points / len(inputs) / 6
                    if not isinstance(cout, np.ndarray) and cout != out:
                        outs += f'  attribute {attribute} has incorrect value (should be {cout} but is {out})!\n'
                        points -= full_points / len(inputs) / 6
            
            errs = ''
        except Exception as e:
            outs = ''
            errs = e
            points -= full_points / len(inputs)
    
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
