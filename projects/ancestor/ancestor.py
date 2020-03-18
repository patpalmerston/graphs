from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # create ancestor graph
    g = Graph()
    # loop through and add all acestors as vectors
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    # add the edges
    for i in ancestors:
        g.add_edge(i[1], i[0])

    # implement a DFS while storing the path
    max_path = 1
    # if the input has no parents return -1
    earliest_a = -1
    # DFS uses stacks
    stack = Stack()
    # Start the stack with the first node/vector
    stack.push([starting_node])
    while stack.size() > 0:
        # create the path
        path = stack.pop()
        # grab the last vector in the path
        v = path[-1]
        # if the path is longer or equal and value is smaller or if path is longer
        if(len(path) >= max_path and v < earliest_a) or (len(path) > max_path):
            earliest_a = v
            max_path = len(path)
        for neighbor in g.vertices[v]:
            new_path = list(path)
            new_path.append(neighbor)
            stack.push(new_path)
    return earliest_a
