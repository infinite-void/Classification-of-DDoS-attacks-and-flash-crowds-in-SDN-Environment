import pandas as pd
from scipy.stats import entropy
import sys

print('opening file')
filename = sys.argv[1]
data = pd.read_csv(filename)

print('finding incoming packets')
incomingpkts = data[data['Destination'] == '45.24.1.10']
src = incomingpkts['Source']

print('calculating Entropy')
ent = entropy(src.value_counts())

print('SourceIP entropy : ', ent, '\n', 
        'Incoming Packet Info : \n', src.value_counts(), '\n')