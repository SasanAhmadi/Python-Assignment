"""
Author -- Atieh yazdani
Matr.Nr -- K11932911
Exercise -- 9

"""
import os
import sys, getopt
import subprocess

def main(argv):
    output_folder = argv[0]

    os.mkdir(output_folder)

    from plot_csv import plot_csv
    
    for x in range(10):
        folder = output_folder + '\\0' + str(x)
        os.mkdir(folder)

        function_call = [sys.executable, "hamstergenegen.py", folder]
        with subprocess.Popen(function_call, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE) as proc:
           _, stderr = proc.communicate(timeout=60)

        function_call = [sys.executable, "ex8.py", folder, folder + "\\sequence_analysis.csv", "actc"]
        with subprocess.Popen(function_call, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE) as proc:
            _, stderr = proc.communicate(timeout=60)

        plot_csv(folder + "\\sequence_analysis.csv", folder + "\\sequence_analysis.png")
        

if __name__ == "__main__":
    main(sys.argv[1:])