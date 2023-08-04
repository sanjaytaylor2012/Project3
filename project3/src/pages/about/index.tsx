import { Flex, Link, Stack, Text } from "@chakra-ui/react";
import React from "react";

type indexProps = {};

const index: React.FC<indexProps> = () => {
  return (
    <Stack justify={"center"} align="center" m={10}>
      <Text fontWeight={600} fontSize={50}>
        About Us
      </Text>
      <Text>
        This brand comparison tool compares the nutritional values for different
        brands and types of foods. To use, simply enter a food you would like to
        find different brands for and click “Search”. The tool will then do 2
        different types of searches, depth-first-search (DFS) and
        breadth-first-search (BFS). Simply put, DFS will generally find more
        diverse types of food, whereas BFS will generally find the same type of
        food sold by different brands. The displayed foods can be expanded to
        display more information such as macronutrient values and percent daily
        value. The tables can also be sorted by different macronutrients such as
        sodium and fat. This way, by using the BFS results, the user can find
        the healthiest brand for a certain food they want. By using DFS, the
        user can explore different types of foods that they may never have heard
        of.
      </Text>
      <Text fontWeight={600} fontSize={50}>
        Technical Details
      </Text>
      <Text>
        This website is built upon an Open Food Facts database found on{" "}
        <Link
          color={"blue.300"}
          href={
            "https://www.kaggle.com/datasets/openfoodfacts/world-food-facts?resource=download"
          }
        >
          kaggle
        </Link>
        . The csv data is parsed, stripping unnecessary information, and built
        into an adjacency list graph. In the graph, foods are adjacent to each
        other if their names’ are similar enough. This similarity is found by
        calculating the{" "}
        <Link
          color={"blue.300"}
          href={"https://en.wikipedia.org/wiki/Jaccard_index"}
        >
          Jaccard index
        </Link>{" "}
        for any two pairs of foods. When the user searches a food, their input
        is compared with every node in the graph. The top 10 most similar foods
        to the input are saved. Then BFS/DFS is called on the graph, with the
        starting node being the food that was most similar to the input. Each
        node traversed in the search is displayed on the website. If the
        traversal reaches a dead-end in the graph before displaying 10 values,
        BFS/DFS is then called again with the next most similar food that has
        not already been traversed being the starting node.
      </Text>
    </Stack>
  );
};
export default index;
