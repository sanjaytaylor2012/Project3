import { Flex, Stack, Text } from "@chakra-ui/react";
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
    </Stack>
  );
};
export default index;
