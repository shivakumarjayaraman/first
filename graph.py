#!/usr/bin/env python

import networkx as nx
import networkx.algorithms.community as nxcom
from matplotlib import pyplot as plt
import csv

def get_color(i, r_off=1, g_off=1, b_off=1):
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)


def community_net(G_in):
    G_out = nx.Graph()
    node_color = []
    node_community = {}
    communities = nxcom.greedy_modularity_communities(G_in)
    for i, com in enumerate(communities):
        for v in com:
            G_out.add_node(v)
            node_color.append(get_color(i))
            node_community[v] = i
    G_out.add_edges_from(G_in.edges())
    return node_color, node_community, G_out


g = nx.Graph()

with open('token_of_thanks.csv') as csvf :
    reader = csv.reader(csvf, delimiter=',')
    count = 0
    for row in reader :
        count += 1
        if (count > 3) :
            g.add_edge(row[0].split()[0], row[1].split()[0])

#plt.figure(figsize=(10,10))
nc, ncom, gg = community_net(g)

##nx.draw_networkx(gg, pos=nx.circular_layout(g), node_color=nc)

degrees = dict(g.degree())
labels = sorted(degrees.keys(), key=lambda x: degrees[x], reverse=True)
nlist = []
i, k = 0, 6
while i < len(labels):
    shell_labels = labels[i:i+k]
    ordered_labels = sorted(shell_labels, key=lambda x: ncom[x])
    nlist.append(ordered_labels)
    i += k
    k += 12
pos = nx.shell_layout(g, nlist=nlist)
cm = plt.get_cmap('cool')
nx.draw_networkx(
    g, pos, alpha=1, node_color=nc, with_labels=True)

plt.show()
