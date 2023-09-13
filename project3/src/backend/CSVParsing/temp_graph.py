class temp_graph:
    def __init__(self):
        # structure: key: name+brand val:[[name],[adj nodes (name+brand)]]
        self.graph = {}

    # Adds edge between two foods, making them neighbors
    # _from and _to are keys (name_brand)
    def addEdge(self, _from, _to):
        self.graph[_from][1].append(_to)
        self.graph[_to][1].append(_from)

    
    # Adds food vertex to graph, adjacent nodes are added through addEdge
    # Peanut ButterTrader Joe's: [Peanut Butter, [PeanutButterWalmart, ...]]
    def addVertex(self, name_brand, food_name):
        self.graph[name_brand] = []
        self.graph[name_brand].append(food_name)
        self.graph[name_brand].append([])
