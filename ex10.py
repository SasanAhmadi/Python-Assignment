"""
Author -- Atieh yazdani
Matr.Nr -- K11932911
Exercise -- 10

"""

import re
import numpy as np

def read_config_file(configpath: str):
    with open(configpath, 'r') as file:
        data = file.read()

    n_iteration = None #AttributeError      (space)digit(space)
    symbol_dead = None #AttributeError      (space)"c"(space)
    symbol_live = None #AttributeError      (space)"c"(space)
    start_seed = None #AttributeError , ValueError        (space)\n"string\n"(space) 

    p = re.finditer(pattern= r'(n_iterations:\s*(?P<NumberOfIter>[-+]?([0-9]*\.[0-9]+|[0-9]+))\s*)?(symbol_live:\s+\"(?P<LiveSymbol>.)\")?(symbol_dead:\s+\"(?P<DeadSymbol>.)\")?', string=data, flags=re.M)

    for l in p:
        if 'DeadSymbol' in l.groupdict().keys() and l.groupdict()['DeadSymbol'] != None:
            symbol_dead = l.groupdict()['DeadSymbol']
        elif 'LiveSymbol' in l.groupdict().keys() and l.groupdict()['LiveSymbol'] != None:
            symbol_live = l.groupdict()['LiveSymbol']
        elif 'NumberOfIter' in l.groupdict().keys() and l.groupdict()['NumberOfIter'] != None:
            if not l.groupdict()['NumberOfIter'].isdigit():
                raise AttributeError()
            n_iteration = int(l.groupdict()['NumberOfIter'])
        

    p = re.finditer(pattern= r'(gamefield:\s*\n\"\n(?P<Seed>(.*\n)*)\"\s*)?', string=data, flags=re.M)

    for l in p:
        if 'Seed' in l.groupdict().keys() and l.groupdict()['Seed'] != None:
            start_seed = l.groupdict()['Seed']

    if symbol_dead == None or symbol_live == None or n_iteration == None or start_seed == None:
        raise AttributeError()        
    
    #print ('Iterations:\n', n_iteration, '\nsymbol_dead\n', symbol_dead, '\nsymbol_live\n', symbol_live, '\nstart_seed\n', start_seed)

    seed2d = []
    line_length = None

    for i,v in enumerate(start_seed.splitlines()):
        row = []

        if line_length != None and line_length != len(v):
            raise ValueError()
        else:
            line_length = len(v)

        for c in v:
            if c != symbol_dead and c != symbol_live:
                raise ValueError()

            row.append(c==symbol_live)

        seed2d.append(row)
    
    seed2d = np.array(seed2d)

    return (n_iteration, symbol_dead, symbol_live, seed2d)


