#Ran once to create final CSV that is read in app.py
import csv
from temp_graph import temp_graph
import time

CONST_NUM_ITEMS = 110000
CONST_SIMILARITY_THRESHOLD = 0.75
CONST_MAX_ADJACENT = 10
CONST_INTIAL_ADJACENT = 5
food_graph = temp_graph()

# Calculates the Jaccard similarity between 2 strings, returns a number 0-1, 1 being very similar, 0 being very unsimilar
def jsim(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    similarity = len(intersection) / len(union)
    return similarity

# Parses through raw data, removing many extra foods and nutritional data
def raw_data_parser():
    with open("raw_data.csv", mode="r", encoding="utf8") as file:
        csvFile = csv.reader(file)
        twoD_array = list(csvFile)

        new_2D = []
        set_of_nameplusbrand = set()  # set of "name+brand" keys

        arr = [12, 1, 40, 63, 65, 102, 111, 112, 117]  #Represents columns of importance in CSV 
        #Loops through every food in CSV
        for row in range(1, len(twoD_array)):
            new_row = []
            name = twoD_array[row][7]
            brand = twoD_array[row][12]
            
            # Checks to make sure the food is from the US, its name is not too long, and that it actually has a name and brand
            if (
                twoD_array[row][33] == "United States"
                and name != ""
                and len(name) < 32
                and brand != ""
            ):
                if name[:7] == "Organic": # Strips away the word organic since it messes with Jaccard algorithm
                    name = name[8:]
                nameplusbrand = name + brand
                if nameplusbrand not in set_of_nameplusbrand: # Ensures there are no duplicate foods
                    # Adds food data to temporary array
                    new_row.append(nameplusbrand)
                    new_row.append(name)
                    for col in range(0, len(arr)):
                        if twoD_array[row][arr[col]] == "":
                            new_row.append("N/A") # Replaces nutritional data with no value with "N/A"
                        else:
                            new_row.append(twoD_array[row][arr[col]]) 
                    new_2D.append(new_row) # Adds row to a 2D array that will become the new CSV
                    set_of_nameplusbrand.add(nameplusbrand)

    # Writes contents of 2D array into new CSV
    with open(
        "nutritional_data.csv",
        "w",
        encoding="utf8",
        newline="",
    ) as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "name+brand",
                "name",
                "brand",
                "url",
                "serving_size",
                "energy_100g",
                "fat_100g",
                "sugar_100g",
                "protein_100g",
                "fiber_100g",
                "sodium_100g",
                "Adjacent nodes:",
            ]
        )
        print("writing to csv")
        for row in new_2D:
            writer.writerow(row)


def create_name_brand_neighbors():
    
    nutrition2D = []

    with open('nutritional_data.csv', mode='r', encoding="utf8") as file:
        csvFile = csv.reader(file)

        # start the graph creation here:
        first_line = True
        count = 0
        
        for row in csvFile:
            count += 1
            if count > CONST_NUM_ITEMS:
                break
            if first_line:
                first_line = False
            else:
                nutrition2D.append(row)
                nameplusbrand = row[0]
                name = row[1]
                
                # Adds food to graph
                food_graph.addVertex(nameplusbrand, name)
                count_of_neighbors = 0

                # Finds and adds adjacent foods based on the similarity of names, if jaccard similarity is >.75 and the food has <10 neighbors adds neighbor
                for key, val in food_graph.graph.items():
                    if len(food_graph.graph[key][1]) < CONST_MAX_ADJACENT:
                        if (key != nameplusbrand and jsim(name, val[0]) > CONST_SIMILARITY_THRESHOLD):
                            food_graph.addEdge(key, nameplusbrand)
                            count_of_neighbors += 1
                    if (count_of_neighbors >= CONST_INTIAL_ADJACENT):
                        break  
            if count % 2000 == 0:
                print(count)
    
    # Writes final csv
    with open('data.csv' ,'w', encoding="utf8", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["name+brand", "name", "brand", "url", "serving_size", "energy_100g", "fat_100g", "sugar_100g", "protein_100g", "fiber_100g", "sodium_100g", "Adjacent nodes:"])

        for each in nutrition2D:
            row = each
            for item in food_graph.graph[each[0]][1]:
                row.append(item)
            writer.writerow(row)


def main():
    start_time = time.time()
    raw_data_parser()
    create_name_brand_neighbors()
    print("created graph with ", len(food_graph.graph), " nodes.")
    end_time = time.time()

    print(end_time - start_time)


# entry point:
if __name__ == "__main__":
    main()
