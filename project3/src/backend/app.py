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
    for key, val in food_graph.graph.items():
        food_name = val[0].name
        currCosine = max(
            jsim(word, food_name), maxCosine if maxCosine else jsim(word, food_name)
        )
        if currCosine != maxCosine and food_name != word:
            maxCosine = currCosine
            heapq.heappush(heap, [maxCosine, key])
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
            queue.append(heapq.heappop(heap))
        else:
            heap = search(res_list[-1])
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


@app.route("/index", methods=["POST"])
def index():
    req = request.get_json()

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
