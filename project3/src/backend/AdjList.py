import Food


class AdjList:
    def __init__(self):
        # key: food + brand
        # value: food obj, adj nodes
        self.graph = {}

    # Adds vertex to graph which contains the key, food object, and adjacent foods
    def addVertex(self, nameplusbrand, foodObj, adj_nodes):
        self.graph[nameplusbrand] = [] 
        self.graph[nameplusbrand].append(foodObj) 
        self.graph[nameplusbrand].append(adj_nodes) 
