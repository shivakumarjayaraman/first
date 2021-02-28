#!/usr/bin/env python

import numpy as np
from collections import defaultdict

X_train = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0],
    [1, 1, 0]])

Y_train = ['Y', 'N', 'Y', 'Y']
X_test = np.array([[1, 1, 0]])

def get_label_indices(labels) :
    lb = defaultdict(list)
    for i, l in enumerate(labels) :
        lb[l].append(i)
    return lb

## prob of labels
def get_prior(li) :
    tot = sum(len(l) for l in li.values())
    return {l : len(v)/tot for l, v in li.items()}

## prob of each feature given its label
def get_likelihood(features, li, smoothing=0) :
    likelihood = {}
    for l, i in li.items() :
        likelihood[l] = (features[i,:].sum(axis=0) + smoothing)/(len(i)+ 2*smoothing)
    return likelihood

def get_posterior(X, prior, li) :
    uli = {l : (1-x) for l, x in li.items()}
    probs = {}
    for l in li :
        probs[l] = prior[l]
        for i, x in enumerate(X) :
            if x : 
                probs[l] *= li[l][i]
            else : 
                probs[l] *= uli[l][i]
    tot = sum(probs.values())
    print (tot)
    probs = {l : p/tot for l, p in probs.items() }
    return probs


li = get_label_indices(Y_train)
prior = get_prior(li)
likelihood = get_likelihood(X_train, li, 1)
res = get_posterior(X_test[0], prior, likelihood)
print (res)
