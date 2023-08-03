import { Link } from "@chakra-ui/next-js";
import {
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
  Box,
  Button,
  Flex,
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
            {food["name"]}, {food["brand"]}
          </Box>
          <AccordionIcon />
        </AccordionButton>
      </h2>
      <AccordionPanel pb={4}>
        <Flex width="100%" justify="space-around">
          <Stack>
            <Text>
              Protein: {food["protein"]} g, {food["dailyproteinpercent"]}% DV
            </Text>
            <Text>
              Fat: {food["fat"]}g, {food["dailyfatpercent"]}% DV
            </Text>
            <Text>
              Fiber: {food["fiber"]}g, {food["dailyfiberpercent"]}% DV
            </Text>
            <Text>
              Sodium: {food["sodium"]}g, {food["dailysodiumpercent"]}% DV
            </Text>
          </Stack>
          <Stack>
            <Text>Energy: {food["energy"]} calories</Text>

            <Text>Serving size: {food["serving_size"]}</Text>
            <Text>Sugar: {food["sugar"]} g</Text>
            <Link target="_blank" href={food["url"]}>
              Click Here for More Info
            </Link>
          </Stack>
        </Flex>
      </AccordionPanel>
    </AccordionItem>
  );
};
export default FoodItem;
