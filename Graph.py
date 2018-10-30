import random
import queue


class Node:
    def __init__(self, label: str, is_stairway: bool, x: int, y: int, z: int):
        self.is_stairway: bool = is_stairway
        self.visited: bool = False
        self.label: str = label
        self.children = set()
        self.has_cheese = False
        self.prev: Node = None
        self.weights = {}
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def add_children(self, children, weight: int):
        for child in children:
            if child not in self.children:
                self.children.add(child)
                # if weight < 0:
                #     w = random.randint(1, 10)
                # else:
                #     w = weight
                w = random.randint(1, 10) if weight < 0 else weight
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

    def add_cheese(self) -> Node:
        cheese_node: Node = random.choice(list(self.nodes.values()))
        cheese_node.has_cheese: bool = True
        return cheese_node
        # print("Cheese at: " + str(cheese_node))

    def traverse_all_nodes_bfs(self, start_node):
        q = queue.Queue()
        q.put(start_node)
        while not q.empty():
            node: Node = q.get()
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
        print('\nCLEARED\n')
        return self.add_cheese()

    def find_cheese_a_star(self, start_node: Node, goal: Node):
        distance = dict()
        q = list(self.nodes.values())
        for child in q:
            distance[str(child)] = 100
        distance[str(start_node)] = 0
        for _ in range(400):
            chosen_node = self.choose_min_distance(distance, q)
            q.remove(chosen_node)
            if chosen_node.has_cheese:
                print('Found cheese at ' + str(chosen_node))
                print('Total cost: ' + str(distance[str(chosen_node)]))
                return True
            print(str(chosen_node))
            for child in chosen_node.children:
                alt = distance[str(chosen_node)] + chosen_node.weights[str(child)] + \
                      manhattan_distance(chosen_node,
                                         goal)
                if alt < distance[str(child)]:
                    distance[str(child)] = alt

    def choose_min_distance(self, distance, q) -> Node:
        chosen_node: Node = q[0]
        for i in range(1, len(q)):
            if distance[str(q[i])] < distance[str(chosen_node)]:
                chosen_node = q[i]
        return chosen_node


def manhattan_distance(node1: Node, node2: Node) -> int:
    return abs(node1.x - node2.x) + abs(node1.y - node2.y) + abs(node1.z - node2.z)
