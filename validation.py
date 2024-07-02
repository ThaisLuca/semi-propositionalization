import os
import math
import numpy as np
from os.path import isfile, join


experiments = [
            {'id': '1', 'source':'imdb', 'target':'uwcse', 'predicate':'workedunder', 'to_predicate':'advisedby', 'arity': 2},
            ##{'id': '2', 'source':'uwcse', 'target':'imdb', 'predicate':'advisedby', 'to_predicate':'workedunder', 'arity': 2},
            {'id': '3', 'source':'imdb', 'target':'cora', 'predicate':'workedunder', 'to_predicate':'samevenue', 'arity': 2},
            {'id': '4', 'source':'cora', 'target':'imdb', 'predicate':'samevenue', 'to_predicate':'workedunder', 'arity': 2},
            ##{'id': '5', 'source':'uwcse', 'target':'cora', 'predicate':'advisedby', 'to_predicate':'samevenue', 'arity': 2},
            ##{'id': '6', 'source':'cora', 'target':'uwcse', 'predicate':'samevenue', 'to_predicate':'advisedby', 'arity': 2},
            {'id': '7', 'source':'yeast', 'target':'twitter', 'predicate':'proteinclass', 'to_predicate':'accounttype', 'arity': 2},
            {'id': '8', 'source':'twitter', 'target':'yeast', 'predicate':'accounttype', 'to_predicate':'proteinclass', 'arity': 2},
            {'id': '9', 'source':'nell_sports', 'target':'nell_finances', 'predicate':'teamplayssport', 'to_predicate':'companyeconomicsector', 'arity': 2},
            {'id': '10', 'source':'nell_finances', 'target':'nell_sports', 'predicate':'companyeconomicsector', 'to_predicate':'teamplayssport', 'arity': 2},
]


def get_CLL(posProb, negProb):
    #print(f'''Pos= {len(posProb)}''')
    #print(f'''Neg= {len(negProb)}''')
    llSum = 0
    for prob in posProb:
        if prob == 0:
            a_prob = 1e-6
            llSum += math.log(a_prob)
        else:
            llSum += math.log(prob)

    #print("LL:" + str(llSum))
    for prob in negProb:
        if prob == 1:
            a_prob = 1 - 1e-6
            llSum += math.log(1 - a_prob)
        else:
            llSum += math.log(1 - prob)
    return llSum/(len(posProb) + len(negProb))

for exp in experiments:
    
    experiment_title = exp['id'] + '_' + exp['source'] + '_' + exp['target']
    target = exp['target']
    path = f'''CLLs/{target}'''
    files = [f for f in os.listdir(path) if isfile(join(path, f))]
    
    print(f'''Experiment name: {experiment_title}''')

    probPos, probNeg, clls = [], [], []
    for file in files:
        with open(f'''CLLs/{target}/{file}''', "r") as f:
            for line in f:
                aux = line.split(' ')
                value, classification = aux[0],aux[1].strip()

                if classification == '1':
                    probPos.append(float(value))
                else:
                    probNeg.append(float(value))
        clls.append(get_CLL(probPos,probNeg))
        #print(clls)
        #print(f'''Size of array {len(my_clls)}''')
    
    print(f'''CLL {np.mean(clls)}''')