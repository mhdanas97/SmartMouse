from Graph import *
import random


def initialize(g):
    stairway = Node('stairway', True)
    m1 = Node('M1', False)
    m2 = Node('M2', False)
    m3 = Node('M3', False)
    m4 = Node('M4', False)
    c1 = Node('C1', False)
    c2 = Node('C2', False)
    c3 = Node('C3', False)
    c4 = Node('C4', False)
    c5 = Node('C5', False)
    c6 = Node('C6', False)
    c1.add_children([stairway], -1)
    c2.add_children([c1, c3], -1)
    c3.add_children([stairway], -1)
    c4.add_children([stairway], -1)
    c5.add_children([c4, c6], -1)
    c6.add_children([stairway], -1)
    m1.add_children([m2, m4, stairway], -1)
    m2.add_children([stairway], -1)
    m3.add_children([m2, m4, stairway], -1)
    m4.add_children([stairway], -1)
    g.add_nodes([stairway, m1, m2, m3, m4, c1, c2, c3, c4, c5, c6])
    # g.traverse_all_nodes_dfs(random.choice(list(g.nodes.values())))
    # g.clear()
    # g.traverse_all_nodes_bfs(random.choice(list(g.nodes.values())))
    # g.clear()
    # g.find_cheese_bfs(random.choice(list(g.nodes.values())))
    # g.clear()
    # g.find_cheese_dfs(random.choice(list(g.nodes.values())))
    g.clear()
    g.find_cheese_ucs(random.choice(list(g.nodes.values())))


if __name__ == '__main__':
    g = Graph()
    initialize(g)
