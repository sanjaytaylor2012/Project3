# to start the venv: $ source project3_env/Scripts/activate
# to start flask server: flask run
# to start next.js: npm run dev
# project3/src/backend/
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from AdjList import AdjList
from Food import Food

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)


# function to return the cosine similarity of two strings
def cosine_sim(str1, str2):
    # Create a vectorizer
    vectorizer = TfidfVectorizer()

    # Create vectors based of the strings
    vectors = vectorizer.fit_transform([str1, str2])

    # Compute the cosine similarity between the vectors
    cosine_sim = cosine_similarity(vectors[0], vectors[1])[0][0]

    return cosine_sim


def parse_csv():
    with open("formatted_data.csv", mode="r", encoding="utf8") as file:
        csvFile = csv.reader(file)

        first_line = True
        count = 0

        for row in csvFile:
            count += 1
            if count > 10000:
                break
            if first_line:
                first_line = False
            else:
                food_node = Food(
                    row[0],
                    row[1],
                    # row[2],
                    # row[3],
                    # row[4],
                    # row[5],
                    # row[6],
                    # row[7],
                    # row[8],
                )
                print(food_node.name)

                food_graph.addVertex(food_node)
                count_nodes = 0
                for key in food_graph.graph:
                    if (
                        key != food_node.name
                        and cosine_sim(key, food_node.name) > CONST_SIMILARITY_THRESHOLD
                    ):
                        print("adding edge: from: ", food_node.name, " to: ", key)
                        food_graph.addEdge(key, food_node.name)
                        food_graph.addEdge(food_node.name, key)
                        count_nodes += 1
                    if count_nodes > 10:
                        break

    count = 0
    for key in food_graph.graph:
        count += 1
        print("Food: ", key, "adj nodes: ", print(food_graph.graph[key][1]))
        if count > 10000:
            break


CONST_SIMILARITY_THRESHOLD = 0.2
food_graph = AdjList()
parse_csv()


@app.route("/index", methods=["POST"])
def index():
    req = request.get_json()
    print(req)
    response = {"message": "Data received successfully", "data": req}
    return jsonify(response), 200
