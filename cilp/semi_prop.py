import json
import re
import tempfile
import time
from os import path as osp
from .utils import get_features, load_json, pjoin, save_params, to_numpy

PREDICATE = 0
VARIABLES = 1

def check_decompositions(bc_list, decompositions_dict, count={}):
    variables_set = {}
    for bc in bc_list:
        for lit in bc:
            # Get variables
            var_l = lit.replace(')', '').split('(')[1].split(',')
            var = var_l[:]
            var.sort()
            var = ','.join(var)

            if var not in variables_set:
                # Save to dictionary with their corresponding predicate
                variables_set[var] = [(lit.split('(')[0], var_l)]
            else:
                variables_set[var].append((lit.split('(')[0], var_l))
    print(variables_set)
    
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


    
    decompositions, count = check_decompositions(examples_dict['neg'], decompositions, count)
    


