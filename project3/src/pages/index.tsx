import { Inter } from "next/font/google";
import { Button, Flex, Input, Stack, Text } from "@chakra-ui/react";
import { useState } from "react";
import { Accordion } from "@chakra-ui/react";
import FoodItem from "@/FoodItem";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  const [formInput, setFormInput] = useState("");
  const [response, setResponse] = useState();

  const onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormInput(event.target.value);
  };

  const sendForm = async () => {
    await fetch("http://127.0.0.1:5000/index", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formInput),
    })
      .then((response) => response.json())
      .then((data) => {
        setResponse(data["res"]);
        console.log(data["res"]);
      });
  };

  const onSubmit = (event: React.FormEvent<HTMLButtonElement>) => {
    event.preventDefault();
    sendForm();
  };

  return (
    <>
      <Stack align="center" justifyContent="center" mt={8}>
        <Text fontSize={50}>Food Recommender</Text>
        <Input
          placeholder="Enter food here"
          onChange={onChange}
          width={{ base: "90%", md: "70%" }}
        />
        <Button type="submit" onClick={onSubmit}>
          Enter
        </Button>
        {response && (
          <>
            <Flex width={"100%"} justifyContent={"space-around"}>
              <Stack align="center" justifyContent="center">
                <Text>DFS</Text>
                <Text>DFS Time: {response["dfs"]["dfs time"]}</Text>
                <Accordion width="40vw">
                  {response["dfs"]["dfs nodes"].map((food: FoodObj) => {
                    return <FoodItem key={food["url"]} food={food} />;
                  })}
                </Accordion>
              </Stack>
              <Stack align="center" justifyContent="center">
                <Text>BFS</Text>
                <Text>BFS Time: {response["bfs"]["bfs time"]}</Text>
                <Accordion width="40vw">
                  {response["bfs"]["bfs nodes"].map((food: FoodObj) => {
                    return <FoodItem key={food["url"]} food={food} />;
                  })}
                </Accordion>
              </Stack>
            </Flex>
          </>
        )}
        {/* {response && <Text fontSize={50}>{response}</Text>} */}
      </Stack>
    </>
  );
}
