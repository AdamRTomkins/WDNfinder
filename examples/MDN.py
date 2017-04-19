#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: weightedNetworkAnalysis.py
#          Desc:
#        Author: Chu Yanshuo
#         Email: chu@yanshuo.name
#      HomePage: http://yanshuo.name
#       Version: 0.0.1
#    LastChange: 2015-12-23 19:28:32
#       History:
# =============================================================================
'''
from WDNfinder.model.utils import *
from WDNfinder.model.gcsp import *
from WDNfinder.model.structuralcontrol import *

import pickle

import argparse

import networkx as nx

G = nx.DiGraph()
G.add_node('x1')
G.add_node('x2')
G.add_node('x3')
G.add_node('x4')

G.add_edge('x1','x2',weight=1)
G.add_edge('x2','x3',weight=1)
G.add_edge('x3','x4',weight=1)

input_nodes= ['x1','x2','x3']



directedGraph = G
bipartiteGraph =toBipartite(directedGraph)

structuralcontrol = StructuralControl(directedGraph, bipartiteGraph)
MDN = structuralcontrol.Enum_Maximum_Matching()
print MDN
