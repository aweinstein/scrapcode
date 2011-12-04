#import string
#import random
## from itertools import product
## from operator import itemgetter

import networkx as nx

## get_next_state = lambda G,v,a: sorted(G.edges(v), key=itemgetter(1))[a][1]
## get_actions = lambda G, v: range(len(G.edges(v)))

## def Gsa_graph(G):
##     Gsa = nx.DiGraph()
##     #Gsa = nx.Graph()
##     for s in G:
##         Gsa.add_nodes_from(product((s, ), get_actions(G, s)))

##     for s, a in Gsa:
##         next_state = get_next_state(G, s, a)
##         next_state_actions = get_actions(G, next_state)
##         destinations = product((next_state, ), next_state_actions)
##         Gsa.add_edges_from(product(((s, a),), destinations))
        
##     return Gsa

#Gsa = Gsa_graph(G)

G = nx.Graph()
G.add_edges_from([(u'a',u'b'), (u'b',u'c'), (u'c', u'd'), (u'a', u'c')])
G = G.subgraph(['a', 'b', 'c'])

H = nx.DiGraph()
H.add_node((G.nodes()[0],0))
H.add_node((G.nodes()[2],0))

H.add_edge((G.edges()[0][1],0), (G.edges()[2][1],0))
nx.write_gexf(H, 'H.gexf')

## dol = {('a', 0): [('b', 0), ('b', 1)],
##        ('a', 1): [('c', 0), ('c', 1)],
##        ('b', 0): [(u'a', 1), (u'a', 0)],
##        ('b', 1): [('c', 0), ('c', 1)],
##        ('c', 0): [(u'a', 1), (u'a', 0)],
##        ('c', 1): [(u'b', 0), (u'b', 1)]}

## H = nx.from_dict_of_lists(dol)
## nx.write_gexf(H, 'H.gexf')
