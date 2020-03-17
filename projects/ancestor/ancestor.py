from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    return g.dfs(starting_node, ancestors)
