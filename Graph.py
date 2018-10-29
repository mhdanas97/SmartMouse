import random
import queue
import heapq


class Node:
    def __init__(self, label, is_stairway):
        self.is_stairway = is_stairway
        self.visited = False
        self.label = label
        self.children = set()
        self.has_cheese = False
        self.prev = None
        self.weights = {}

    def add_children(self, children, weight):
        for child in children:
            if child not in self.children:
                self.children.add(child)
                if weight < 0:
                    w = random.randint(1, 10)
                else:
                    w = weight
                self.weights[str(child)] = w
                child.add_children([self], w)

    def __repr__(self):
        return self.label


class Graph:
    def __init__(self):
        self.nodes = dict()

    def add_nodes(self, nodes):
        for node in nodes:
            self.nodes[node.label] = node

    def add_cheese(self):
        cheese_node = random.choice(list(self.nodes.values()))
        cheese_node.has_cheese = True
        # print("Cheese at: " + str(cheese_node))

    def traverse_all_nodes_bfs(self, start_node):
        q = queue.Queue()
        q.put(start_node)
        while not q.empty():
            node = q.get()
            if not node.visited:
                node.visited = True
                print(node)
                for child in node.children:
                    q.put(child)

    def traverse_all_nodes_dfs(self, start_node):
        start_node.visited = True
        print(start_node)
        for child in start_node.children:
            if not child.visited:
                self.traverse_all_nodes_dfs(child)

    def find_cheese_dfs(self, start_node):
        print(str(start_node) + ': ' + str(start_node.weights))
        if start_node.has_cheese and not start_node.visited:
            print("Found cheese at: " + str(start_node) + ' Path:')
            for node in self.nodes:
                self.nodes[node].visited = True
            temp = start_node
            while temp:
                print(str(temp) + '<-', end='')
                temp = temp.prev
            return

        start_node.visited = True
        for child in start_node.children:
            if not child.visited:
                child.prev = start_node
                self.find_cheese_dfs(child)

    def find_cheese_bfs(self, start_node):
        q = queue.Queue()
        q.put(start_node.weights)
        while not q.empty():
            node = q.get()
            if node.has_cheese and not node.visited:
                print("Found cheese at: " + str(node) + ', Path:')
                temp = node
                while temp:
                    print(str(temp) + '<-', end='')
                    temp = temp.prev
                return
            node.visited = True
            print(node)
            for child in node.children:
                if not child.visited:
                    child.prev = node
                    q.put(child)

    def clear(self):

        for node in self.nodes:
            self.nodes[node].visited = False
            self.nodes[node].has_cheese = False
        self.add_cheese()
        print('\nCLEARED\n')

    def find_cheese_ucs(self, start_node):
        distance = dict()
        q = list(self.nodes.values())
        for child in q:
            distance[str(child)] = 100
        distance[str(start_node)] = 0
        while True:
            chosen_node = self.choose_min_distance(distance, q)
            q.remove(chosen_node)
            if chosen_node.has_cheese:
                print('Found cheese at ' + str(chosen_node))
                return True
            print(str(chosen_node))
            for child in chosen_node.children:
                alt = distance[str(chosen_node)] + chosen_node.weights[str(child)]
                if alt < distance[str(child)]:
                    distance[str(child)] = alt

    def choose_min_distance(self, distance, q):
        chosen_node = q[0]
        for i in range(1, len(q)):
            if distance[str(q[i])] < distance[str(chosen_node)]:
                chosen_node = q[i]
        return chosen_node
