import json
import re
import tempfile
import time
from os import path as osp
from .utils import get_features, load_json, pjoin, save_params, to_numpy

def check_decompositions(bc_list, decompositions_dict, count={}):
    for e in bc_list:
        body = ','.join(e)
        
        if body not in decompositions_dict:
            decompositions_dict[body] = f'L{len(decompositions_dict)+1}'
            count[decompositions_dict[body]] = 1
        else:
            count[decompositions_dict[body]] += 1
    return decompositions_dict, count

def generate_bcp(decompositions, h_arity):
    letter_A = ord('A')
    decompositions_clauses = decompositions.values()
    h_args = ','.join([chr(letter_A+i) for i in range(0,h_arity)])

    return [d + '(' + h_args + ')' for d in decompositions_clauses]

def run_semi_prop(data_dir, h_arity, cached=True, print_output=False):
    print('Running Semi-Propositionalization')
    bc_file = pjoin(data_dir, 'bc_filtered.json')
    if osp.exists(bc_file) and cached:
        print('Loading from cache')
        return
    
    examples_dict = load_json(pjoin(data_dir, 'bc.json'))

    n_positives_examples, n_negative_examples = len(examples_dict['pos']), len(examples_dict['neg'])
    print(f"Loaded {len(examples_dict['pos'])} pos examples")
    print(f"Loaded {len(examples_dict['neg'])} neg examples")

    # Create variables to store decompositions
    decompositions = {}
    count = {}

    # Filter positive examples
    decompositions, count = check_decompositions(examples_dict['pos'], decompositions, count)
    rules = generate_bcp(decompositions, h_arity)
    # Generate new bottom clauses using decompositions

    print(decompositions)
    print(rules)
    KSOAPKSOPAKSOPAKSOPAKS
    
    decompositions, count = check_decompositions(examples_dict['neg'], decompositions, count)
    


