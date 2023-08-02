import { Link } from "@chakra-ui/next-js";
import {
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
  Box,
  Button,
  Stack,
  Text,
} from "@chakra-ui/react";
import React from "react";

type FoodItemProps = { food: FoodObj };

const FoodItem: React.FC<FoodItemProps> = ({ food }) => {
  return (
    <AccordionItem>
      <h2>
        <AccordionButton>
          <Box as="span" flex="1" textAlign="left">
            {food["name"]}
          </Box>
          <AccordionIcon />
        </AccordionButton>
      </h2>
      <AccordionPanel pb={4}>
        <Stack>
          <Text>Brand: {food["brand"]}</Text>
          <Text>Energy: {food["energy"]} kilajoules</Text>
          <Text>fat: {food["fat"]} g</Text>
          <Text>fiber: {food["fiber"]} g</Text>
          <Text>protein: {food["protein"]} g</Text>
          <Text>serving size: {food["serving_size"]}</Text>
          <Text>sodium: {food["sodium"]} g</Text>
          <Text>sugar: {food["sugar"]} g</Text>
          <Button>
            <Link target="_blank" href={food["url"]}>
              Click Here for More Info
            </Link>
          </Button>
        </Stack>
      </AccordionPanel>
    </AccordionItem>
  );
};
export default FoodItem;
