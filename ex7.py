"""
Author -- Atieh yazdani
Matr.Nr -- K11932911
Exercise -- 7

"""


def parse_file_metadata(data_as_string):
    data = data_as_string.split("\n")

    outs = return_header_data(data)

    idRow = outs[0]
    dateRow = outs[1]
    columnsRow = outs[2]
    
    dateValue = 0

    try:
        dateValue = int(dateRow.replace("# Date:", ""))
    except Exception as e:
        raise TypeError("Date is not a valid integer value")

    idValue = idRow.replace("# ID:", "").strip()
    columnsValue = columnsRow.replace("# Columns:", "").strip().split(';')
    
    return idValue, dateValue, columnsValue

def return_header_data(data):

    headerStartrRow = next((item for item in data if item.startswith("# SeqHeadStart")), None)
    headerEndRow = next((item for item in data if item.startswith("# SeqHeadEnd")), None)
    dataEndRow = next((item for item in data if item.startswith("# Data end")), None)
    
    idRow = next((item for item in data if item.startswith("# ID:")), None)
    dateRow = next((item for item in data if item.startswith("# Date:")), None)
    columnsRow = next((item for item in data if item.startswith("# Columns:")), None)

    if headerStartrRow == None or headerEndRow == None or dataEndRow == None:
        raise ValueError

    headerStartIndex = data.index(headerStartrRow)
    headerEndIndex = data.index(headerEndRow)
    dataEndIndex = data.index(dataEndRow) 

    idRowIndex = -1 if idRow == None else data.index(idRow)
    dateRowIndex = -1 if dateRow == None else data.index(dateRow)
    columnsRowIndex = -1 if columnsRow == None else data.index(columnsRow)

    if dataEndIndex < headerStartIndex or dataEndIndex < headerEndIndex or headerEndIndex < headerStartIndex:
        raise ValueError

    for index in range(headerStartIndex): 
        if data[index] != "":
            raise ValueError

    if not (dateRowIndex == idRowIndex + 1 \
        and columnsRowIndex > headerStartIndex \
        and columnsRowIndex < headerEndIndex \
        and idRowIndex > headerStartIndex \
        and idRowIndex < headerEndIndex \
        and dateRowIndex > headerStartIndex \
        and dateRowIndex < headerEndIndex):
        raise ValueError

    for index in range(headerEndIndex - 2):
        if not data[index + headerStartIndex + 1].startswith("#") and data[index + headerStartIndex + 1] != "":
            raise ValueError

    return idRow, dateRow, columnsRow
