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

app = Flask(__name__)
CORS(app)


food_graph = AdjList()


def jsim(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    similarity = len(intersection) / len(union)
    return similarity

def parse_csv():
    with open("data.csv", mode="r", encoding="utf8") as file:
        csvFile = csv.reader(file)

        first_line = True

        for row in csvFile:
            if first_line:
                first_line = False
                continue
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
            for i in range(11, len(row)):
                adj_nodes.append(row[i])
            nameplusbrand = row[0]
            food_graph.addVertex(nameplusbrand, food_node, adj_nodes)

def search(word):
    # [0.234234, peanut butter]
    heap = []
    maxCosine = None
    for food in food_graph.graph:
        currCosine = max(jsim(word, food), maxCosine if maxCosine else jsim(word, food))
        if currCosine != maxCosine and food != word:
            maxCosine = currCosine
            heapq.heappush(heap, [maxCosine, food])
            if len(heap) > 10:
                heapq.heappop(heap)
    heapq.heappop(heap)
    return heap

def reverseHeap(heap):
    for pair in heap:
        pair[0] = pair[0] * -1
    heapq.heapify(heap)
    return heap


def dfs(heap):
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
            stack.append(heapq.heappop(heap))
        else:
            heap = search(res_list[-1])
            stack.append(heap[-1])
    return res


def bfs(heap):
    heap = reverseHeap(heap)
    queue = collections.deque([heapq.heappop(heap)])
    res = set()
    res_list = []

    while len(res) < 10:
        while queue:
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
            queue.append(heapq.heappop(heap))
        else:
            heap = search(res_list[-1])
            heap = reverseHeap(heap)
            queue.append(heapq.heappop(heap))
    return res

print("parsing csv")
parse_csv()
print("donw parsing csv")

@app.route("/index", methods=["POST"])
def index():
    req = request.get_json()
    print(req)
    start_time = time.time()
    node = search(req)
    dfs_result = dfs(node)
    end_time = time.time()
    dfs_time = end_time - start_time
    # dfs_time = round(dfs_time, 3)

    dfs_result = list(dfs_result)
    dfs_result = dfs_result[0:10]

    dfs_nodes = []

    for name in dfs_result:
        dfs_nodes.append(food_graph.graph[name][0].to_dict())
    
    print("dfs: ", dfs_result)
    print("dfs time: ", dfs_time)

    start_time = time.time()
    node = search(req)
    bfs_result = bfs(node)    
    end_time = time.time()
    bfs_time = end_time - start_time
    # bfs_time = round(bfs_time, 3)

    bfs_result = list(bfs_result)
    bfs_result = bfs_result[0:10]
    bfs_nodes = []

    for name in bfs_result:
        bfs_nodes.append(food_graph.graph[name][0].to_dict())
    
    print("bfs: ", bfs_result)    
    print("bfs time: ", bfs_time)

    response = {"res": {"dfs": {"dfs nodes": dfs_nodes, "dfs time" : dfs_time}, 
                        "bfs": {"bfs nodes" : bfs_nodes, "bfs time" : bfs_time}}}
    return jsonify(response), 200

