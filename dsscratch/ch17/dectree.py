#!/usr/bin/env python

from collections import *
import math
from pprint import pprint
from functools import partial

def entropy(class_probabilities) :
    return sum(-1 * p * math.log(p, 2) for p in class_probabilities if p)

def class_probabilities(labels) :
    return [v/len(labels) for v in Counter(labels).values()]

def data_entropy(labeled_data) :
    return entropy(class_probabilities([l[-1] for l in labeled_data]))

def partition_entropy(subsets) :
    total = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset)*len(subset)/total for subset in subsets)

def partition_by(inputs, attribute) :
    ## inputs is a list of pairs (dict, label)
    groups = defaultdict(list)
    for i in inputs :
        key = i[0][attribute]
        groups[key].append(i)
    return groups

def partition_entropy_by(inputs, attribute) :
    groups = partition_by(inputs, attribute)
    return partition_entropy(groups.values())

def classify(tree, input) :
    if tree in [True, False] : return tree

    attr, subtree = tree
    subtree_key = input.get(attr)
    if subtree_key not in subtree : subtree_key = None

    return classify(subtree[subtree_key], input)

def build_tree_id3(inputs, split_candidates=None) :
    if split_candidates == None :
        split_candidates = inputs[0][0].keys()

    num_inputs = len(inputs)
    num_trues  = len([l for i, l in inputs if l])
    num_falses = num_inputs - num_trues
    
    if num_trues == 0 : return False
    if num_falses == 0 : return True

    if not split_candidates :
        return num_trues >= num_falses

    best_attr = min(split_candidates, key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attr)
    new_candidates = [a for a in split_candidates if a != best_attr]

    subtrees = {attrval : build_tree_id3(subset, new_candidates)
                    for attrval, subset in partitions.items() }

    subtrees[None] = num_trues > num_falses

    return (best_attr, subtrees)


Candidate = namedtuple('Candidate', ['level', 'lang', 'tweets', 'phd', 'didwell'])

def totuple(c: Candidate) :
    d = dict()
    d['level'] = c.level
    d['lang'] = c.lang
    d['tweets'] = c.tweets
    d['phd'] = c.phd
    didwell = True if c.didwell=="yes" else False 
    return (d, didwell)

if __name__ == "__main__" :
    inputs = [Candidate('Senior', 'Java',   "no", "no", "no"),
          Candidate('Senior', 'Java',   "no", "yes",  "no"),
          Candidate('Mid',    'Python', "no", "no", "yes"),
          Candidate('Junior', 'Python', "no", "no", "yes"),
          Candidate('Junior', 'R',      "yes",  "no", "yes"),
          Candidate('Junior', 'R',      "yes",  "yes",  "no"),
          Candidate('Mid',    'R',      "yes",  "yes",  "yes"),
          Candidate('Senior', 'Python', "no", "no", "no"),
          Candidate('Senior', 'R',      "yes",  "no", "yes"),
          Candidate('Junior', 'Python', "yes",  "no", "yes"),
          Candidate('Senior', 'Python', "yes",  "yes",  "yes"),
          Candidate('Mid',    'Python', "no", "yes",  "yes"),
          Candidate('Mid',    'Java',   "yes",  "no", "yes"),
          Candidate('Junior', 'Python', "no", "yes",  "no")
         ]

    intups = [totuple(c) for c in inputs]
    #for key in ['level', 'lang', 'tweets', 'phd'] :
    #    print (key, partition_entropy_by(intups, key))
    #
    #print ("-------------")

    #senior_inputs = [c for c in intups if c[0]['level'] == 'Senior']
    #for key in ['lang', 'tweets', 'phd'] :
    #    print (key, partition_entropy_by(senior_inputs, key))
    
    tree = build_tree_id3(intups)

    pprint (tree)

    print (classify(tree, {
        "level" : "Junior", "lang" : "Java", "tweets" : "yes", "phd" : "no"
        }))
    print (classify(tree, {
        "level" : "Junior", "lang" : "Java", "tweets" : "yes", "phd" : "yes"
        }))
    print (classify(tree, {
        "level" : "Intern"
        }))
    print (classify(tree, {
        "level" : "Senior"
        }))
