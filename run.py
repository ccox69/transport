
# python3 run.py <graph_type> <parameter> <num_trials> <id>

import sys
import graphs
import steps

graph_type = int(sys.argv[1])
graph_param = int(sys.argv[2])
M = graphs.matrix(graph_type, graph_param)

num_trials = int(sys.argv[3])

fid = sys.argv[4]

fname = f'data/graph_{graph_type}_{graph_param}_{fid}.txt'

steps.expected_transport_distance(M, num_trials, fname)

