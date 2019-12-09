"""
Author -- Atieh yazdani
Matr.Nr -- K11932911
Exercise -- 8

"""
import sys, getopt
import numpy as np

def main(argv):
    
    inputfolder = argv[0] #"C:/Users/Sasan/source/repos/Python-Assignment - a8/ex8_testfiles/test0/00"
    outputfile = argv[1] #"C:/Users/Sasan/source/repos/Python-Assignment - a8/ex8_testfiles/test0/00/unittestoutput.csv"#
    subsequence = argv[2] #"attc"

    from ex5 import count_bases_and_subsequence
    from ex6 import read_raw_files 
    from ex7 import parse_file_metadata

    allvalues = np.zeros(shape=(10, 5, 200))

    generator = read_raw_files(foldername=inputfolder)
    for c in generator:
        hamster_id, date_entry, column_names = parse_file_metadata(c)
        counts, subsequence_count = count_bases_and_subsequence(c,subsequence)
        allvalues[int(hamster_id),0:4,date_entry] = list(counts.values())
        
        allvalues[int(hamster_id),4,date_entry] = subsequence_count

    finaldata = np.mean(allvalues, axis=0)
    
    result = open(outputfile,'w')
    result.write("a;c;g;t;subsequence"+"\n")
    for item in finaldata.transpose():
        result.write(str(item[0])+';'+str(item[1])+';'+str(item[2])+';'+str(item[3])+';'+str(item[4])+"\n")
    
    result.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])