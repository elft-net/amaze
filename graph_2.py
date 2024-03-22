class Graph:
    def adjacent_nodes(self, node):
        nb_list = []
        if node[0] in self.graph:
            nblist.append(self.graph[node[1]])

        if node[1] in self.graph:
            nblist.append(self.graph[node[0]])

        return nb_list

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}


# my_silly_code:
class Graph:
    def adjacent_nodes(self, node):
        nb_list = []

        if node in self.graph:
            for i in self.graph[node]:
                nb_list.append(i)

        return nb_list

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

# their_solution:
class Graph:
    def adjacent_nodes(self, node):
        return list(self.graph[node])

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

