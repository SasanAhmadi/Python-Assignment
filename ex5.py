def generate_subsuence_record(row):
    result = ''
    if len(row) > 0:
        if len(row.split(';')) > 1:
            if row.split(';')[1].lower() in ('a', 'c', 'g', 't'):
                if float(row.split(';')[2]) >= 0.05:
                    result = row.split(';')[1].lower()
              
    if result == '':
        result = '#'
    return result;

def count_bases_and_subsequence (data_as_string, subsequence):
    data = data_as_string.split("\n")
    endOfData = data.index("# Data end")
    basesList = [x.split(';')[1].lower() for x in data[:endOfData] if not x.startswith('#') and \
        not len(x) == 0 and \
        x.split(';')[1].lower() in ('a', 'c', 'g', 't') and \
        float(x.split(';')[2]) >= 0.05]

    subsequenceList = [generate_subsuence_record(x) for x in data[:endOfData] ]
    
    number_of_bases = {}
    number_of_bases['a'] = basesList.count('a')
    number_of_bases['g'] = basesList.count('g')
    number_of_bases['c'] = basesList.count('c')
    number_of_bases['t'] = basesList.count('t')

    count_of_the_subsequence = (''.join(subsequenceList)).count(subsequence.lower())

    return number_of_bases,count_of_the_subsequence