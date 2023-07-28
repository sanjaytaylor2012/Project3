# to start the venv: $ source project3_env/Scripts/activate
# to start flask server: flask run
# to start next.js: npm run dev
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)


@app.route("/index", methods=["POST"])
def index():
    req = request.get_json()
    print(req)
    response = {"message": "Data received successfully", "data": req}
    return jsonify(response), 200

# function to return the cosine similarity of two strings
def cosine_similarity(str1, str2):
    # Create a vectorizer
    vectorizer = TfidfVectorizer()

    # Create vectors based of the strings
    vectors = vectorizer.fit_transform([str1, str2])

    # Compute the cosine similarity between the vectors
    cosine_sim = cosine_similarity(vectors[0], vectors[1])[0][0]

    return cosine_sim

CONST_SIMILARITY_THRESHOLD = 0.55

food_graph = AdjList()

def parse_csv():
    with open('backend/formatted_data.csv', mode='r', encoding="utf8") as file:
        csvFile = csv.reader(file)

        first_line = True

        for row in csvFile:
            if first_line:
                first_line = False
            else:
                food_node = Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                
                food_graph.addVertex(food_node)

                for key, value in food_graph.graph.items():
                    if (cosine_similarity(key, food_node.name) > CONST_SIMILARITY_THRESHOLD):
                        food_graph.addEdge(value[0], food_node)
                        food_graph.addEdge(food_node, value[0])








            

        
