'''
small utility for parsing network-traffic-data from XML-files as provided e.g. for networks with dynamic traffic data in the SNDlib (www.sndlib.zib.de)
for importing the function, the folder containing this file has to be in $PYTHONPATH
the functions xmlparser.xmlMeanParser() and xmlparser.xmlDemandsParser() are designed for use outside of this script and can be called afer importing.
the script uses the xmltodict python-library
the path of the files to parse has to be given in an index file (default on path ./index.txt) 
other index-file-paths can be passed through the index_file="..." argument of the functions 
if you find any bugs, feel free to contact or post an issue!
'''

import xmltodict
import pandas as pd
import numpy as np
import sys

#returns DataFrame with demand-ids and demand-values of the xml-file
#this function is internally used for unpacking the XML-file, should not be used outside this script (probably throws an error anyway...)!
def xmlDemandParser(filepath=None):
    doc = xmltodict.parse(open(filepath,"rb"))
    demands = doc['network']['demands']['demand']
    demandSourceArray = []
    demandTargetArray = []
    demandValueArray = []
    Time = pd.to_datetime(doc['network']['meta']['time'])

    for demand in demands:
        demandSourceArray.append(demand['source'])
        demandTargetArray.append(demand['target'])
        demandValueArray.append(demand['demandValue'])

    demandFrame = pd.DataFrame({'Time': Time, 'source':demandSourceArray, 'target':demandTargetArray, 'demandValue':demandValueArray})
    demandFrame["demandValue"] = pd.to_numeric(demandFrame["demandValue"])
    return demandFrame

#return the DataFrame holding mean traffic over all nodes per timestep (per XML-file):
def xmlMeanParser(index_file="index.txt"):
    matricies = pd.read_csv(index_file,header=None)
    print("Parsing files: ")
    print(matricies)
    frame = pd.DataFrame()
    for matrix in matricies[0]:
        try:
            temp = xmlDemandParser(matrix)
            temp.set_index("Time",inplace=True)
            frame = frame.append(temp)
            sys.stdout.write(".")
            sys.stdout.flush()
        except Exception as e:
            print(e)
            continue

    frame = frame.mean(level="Time")
    sys.stdout.write('\n')
    return frame

#returns DataFrame holding an entry for each demand in each timestep with the columns: source, target and demand value, index is timestamp:
def xmlDemandsParser(index_file="index.txt"):
    matricies = pd.read_csv(index_file,header=None)
    print("Parsing files: ")
    print(matricies)
    frame = pd.DataFrame()
    for matrix in matricies[0]:
        try:
            temp = xmlDemandParser(matrix)
            temp.set_index("Time",inplace=True)
            frame = frame.append(temp)
            sys.stdout.write(".")
            sys.stdout.flush()
        except Exception as e:
            print(e)
            continue
    sys.stdout.write('\n')
    return frame
