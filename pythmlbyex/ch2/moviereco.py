#!/usr/bin/env python

import numpy as np
from collections import defaultdict

data_path="ml-1m/ratings.dat"
n_users=6040
n_movies=3706

def load_rating_data() :
    data = np.zeros([n_users, n_movies], dtype=np.float32)
    movie_id_mapping = {}
    movie_n_rating = defaultdict(int)

    with open(data_path, 'r') as file :
        for line in file.readlines()[1:] :
            uid, mid, rating, _ = line.split("::")
            uid = int(uid) - 1
            if (mid not in movie_id_mapping) :
                movie_id_mapping[mid] = len(movie_id_mapping)
            rating = int(rating)
            data[uid, movie_id_mapping[mid]] = rating

            if (rating > 0) :
                movie_n_rating[mid] += 1
    return data, movie_n_rating, movie_id_mapping 

def display_distribution(data) :
    values, counts = np.unique(data, return_counts=True)
    for v, c in zip(values, counts) :
        print(f"Number in rating {v}: {c}")

a,b,c = load_rating_data()
display_distribution(a)
movie_id_most, n_rating_most = sorted(b.items(), key=lambda d: d[1], reverse=True)[0]
print (movie_id_most, n_rating_most)

X_raw = np.delete(a, c[movie_id_most], axis=1)
Y_raw = a[:,c[movie_id_most]]

X = X_raw[Y_raw > 0]
Y = Y_raw[Y_raw > 0]

display_distribution(Y)

## recommend = 3
## Convery Y into a Recommend/Not-Recommend array
Y[Y<=3] = 0
Y[Y>3] = 1

npos = (Y==1).sum()
nneg = (Y==0).sum()

print ("Positive/Negative", npos, nneg)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print("Train/Test sizes", len(Y_train), len(Y_test))

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=1.0, fit_prior=True)
clf.fit(X_train, Y_train)
predprob = clf.predict_proba(X_test)
print (predprob[0:10])

prediction = clf.predict(X_test)
print (prediction[:10])

accuracy = clf.score(X_test, Y_test)
print (accuracy)
