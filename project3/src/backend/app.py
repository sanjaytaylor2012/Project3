# to start the venv: $ source project3_env/Scripts/activate
# to start flask server: flask run
# to start next.js: npm run dev
# project3/src/backend/
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from AdjList import AdjList
from Food import Food
import heapq
import collections
import time


food_graph = AdjList()

# Calculates the Jaccard similarity between 2 strings, returns a number 0-1, 1 being very similar, 0 being very unsimilar
def jsim(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    similarity = len(intersection) / len(union)
    return similarity

# Reads the serialized csv, constructs graph datastructure
def parse_csv():
    with open("data.csv", mode="r", encoding="utf8") as file:
        csvFile = csv.reader(file)

        first_line = True

        for row in csvFile:
            if first_line:
                first_line = False
                continue
            # Creates food object with all necessary values such as nutrition values
            food_node = Food(
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
            )
            adj_nodes = []
            # Creates adjacent foods list for the current food
            for i in range(11, len(row)):
                adj_nodes.append(row[i])
            nameplusbrand = row[0]
            food_graph.addVertex(nameplusbrand, food_node, adj_nodes)

# Returns min heap of the input string's 10 most similar foods in the graph
def search(word):
    heap = []
    maxSim = None
    for key, val in food_graph.graph.items():
        food_name = val[0].name
        heapq.heappush(heap, [jsim(word, food_name), key]) #Calculates similarity between food in graph and entered food and adds to minheap
        if len(heap) > 10:
            heapq.heappop(heap) #If heap is at max capacity, pop least similar food
    return heap

# Converts the heap to a "max heap" by multiplying all similarities by -1
def reverseHeap(heap):
    for pair in heap:
        pair[0] = pair[0] * -1
    heapq.heapify(heap)
    return heap

# Conducts a Depth First Search of the graph with the starting node being the first value in the heap
def dfs(heap):
    heap = reverseHeap(heap)

    stack = [heapq.heappop(heap)]
    res = set()
    res_list = []

    while len(res) < 10:
        while stack:
            for i in range(len(stack)):
                node = stack.pop()
                res.add(node[1])
                res_list.append(node[1])
                if len(res) > 10:
                    return res
                for adj_node in food_graph.graph[node[1]][1]:
                    if adj_node not in res:
                        stack.append([1, adj_node])
        if heap:
            stack.append(heapq.heappop(heap)) #If traversal ends before 10 nodes are found, next highest value in heap added to stack
        else:
            heap = search(res_list[-1]) #Recreates the heap if it is empty and 10 nodes are still not found
            stack.append(heap[-1])
    return res

# Conducts a Breadth First Search of the graph with the starting node being the first value in the heap
def bfs(heap):
    heap = reverseHeap(heap)
    queue = collections.deque([heapq.heappop(heap)])
    res = set()
    res_list = []

    while len(res) < 10:
        while queue and len(res) < 10:
            for i in range(len(queue)):
                node = queue.popleft()
                res.add(node[1])
                res_list.append(node[1])
                if len(res) > 10:
                    return res
                for adj_node in food_graph.graph[node[1]][1]:
                    if adj_node not in res:
                        queue.append([1, adj_node])
        if heap:
            queue.append(heapq.heappop(heap)) #If traversal ends before 10 nodes are found, next highest value in heap added to stack
        else:
            heap = search(res_list[-1]) #Recreates the heap if it is empty and 10 nodes are still not found
            heap = reverseHeap(heap)
            queue.append(heapq.heappop(heap))
    return res


print("parsing csv")
parse_csv()
print("done parsing csv")
app = Flask(__name__)
CORS(app)


CONST_Per100gtoPer28g = 0.28
CONST_DAILYPROTEIN = 50
CONST_DAILYFAT = 78
CONST_DAILYFIBER = 28
CONST_DAILYSODIUM = 2.3

# Calculate Daily Value %'s for a given food based on its nutritional values and constants
def getDailyValues(node):
    if node.energy != "N/A":
        node.energy = round(
            float(node.energy) * 0.239006, 2
        )  # Converts from KJ to Kcal
    if node.fat != "N/A":
        node.dailyfatpercent = round(
            float(node.fat) * CONST_Per100gtoPer28g / CONST_DAILYFAT * 100, 2
        )
    if node.protein != "N/A":
        node.dailyproteinpercent = round(
            float(node.protein) * CONST_Per100gtoPer28g / CONST_DAILYPROTEIN * 100, 2
        )
    if node.fiber != "N/A":
        node.dailyfiberpercent = round(
            float(node.fiber) * CONST_Per100gtoPer28g / CONST_DAILYFIBER * 100, 2
        )
    if node.sodium != "N/A":
        node.dailysodiumpercent = round(
            float(node.sodium) * CONST_Per100gtoPer28g / CONST_DAILYSODIUM * 100, 2
        )
    return node

# Runs when the user hits "Enter" on website
@app.route("/index", methods=["POST"])
def index():
    req = request.get_json()

    #Finds DFS results and tracks time taken
    start_time = time.time()
    node = search(req)
    dfs_result = dfs(node)
    end_time = time.time()
    dfs_time = end_time - start_time
    dfs_time = round(dfs_time, 5)

    dfs_result = list(dfs_result)[0:10]
    dfs_nodes = []
    for name in dfs_result:
        node = food_graph.graph[name][0]
        node = getDailyValues(node)
        node = node.to_dict()
        dfs_nodes.append(node)

    print("dfs: ", dfs_nodes)
    print("dfs time: ", dfs_time)

    #Finds BFS results and tracks time taken
    start_time = time.time()
    node = search(req)
    bfs_result = bfs(node)
    end_time = time.time()
    bfs_time = end_time - start_time
    bfs_time = round(bfs_time, 5)

    bfs_result = list(bfs_result)[0:10]
    bfs_nodes = []
    for name in bfs_result:
        node = food_graph.graph[name][0]
        node = getDailyValues(node)
        node = node.to_dict()
        bfs_nodes.append(node)

    print("bfs: ", bfs_nodes)
    print("bfs time: ", bfs_time)

    response = {
        "res": {
            "dfs": {"dfs nodes": dfs_nodes, "dfs time": dfs_time},
            "bfs": {"bfs nodes": bfs_nodes, "bfs time": bfs_time},
        }
    }
    return jsonify(response), 200
