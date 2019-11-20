import os
from glob import glob

def read_raw_files(foldername):
    fileNames = sorted(glob(os.path.join(foldername, "*.seq.raw")))
    

    for singleFile in fileNames:
        with open(singleFile, 'r') as fh:
            file_content = fh.read()
            yield file_content;