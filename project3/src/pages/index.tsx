import { Inter } from "next/font/google";
import { Button, Flex, Input, Select, Stack, Text } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { Accordion } from "@chakra-ui/react";
import FoodItem from "@/FoodItem";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  const [formInput, setFormInput] = useState("");
  const [response, setResponse] = useState();
  const [bfsNodes, setBfsNodes] = useState<FoodObj[]>();
  const [dfsNodes, setdfsNodes] = useState<FoodObj[]>();
  const [sortParameter, setSortParameter] = useState("");

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
        setBfsNodes(data["res"]["bfs"]["bfs nodes"]);
        setdfsNodes(data["res"]["dfs"]["dfs nodes"]);
        console.log(data["res"]);
      });
  };

  const sortNodes = (sortParameter: string) => {
    if (sortParameter == "") {
      return;
    } else if (sortParameter == "fat") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.fat);
        const b_num = parseFloat(b.fat);
        return b_num - a_num;
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.fat);
        const b_num = parseFloat(b.fat);
        return b_num - a_num;
      });
    } else if (sortParameter == "fiber") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.fiber);
        const b_num = parseFloat(b.fiber);
        return b_num - a_num;
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.fiber);
        const b_num = parseFloat(b.fiber);
        return b_num - a_num;
      });
    } else if (sortParameter == "protein") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.protein);
        const b_num = parseFloat(b.protein);
        return b_num - a_num;
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.protein);
        const b_num = parseFloat(b.protein);
        return b_num - a_num;
      });
    } else if (sortParameter == "sodium") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.sodium);
        const b_num = parseFloat(b.sodium);
        return b_num - a_num;
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.sodium);
        const b_num = parseFloat(b.sodium);
        return b_num - a_num;
      });
    } else if (sortParameter == "sugar") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.sugar);
        const b_num = parseFloat(b.sugar);
        return b_num - a_num;
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.sugar);
        const b_num = parseFloat(b.sugar);
        return b_num - a_num;
      });
    }
    // } else {
    //   bfsNodes?.sort((a, b) => {
    //     const a_num = parseFloat(a.sortParameter);
    //     const b_num = parseFloat(b.sortParameter);
    //     return b_num - a_num;
    //   });
    // }
  };

  const onSubmit = (event: React.FormEvent<HTMLButtonElement>) => {
    event.preventDefault();
    sendForm();
  };

  const handleSelectChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSortParameter(event.target.value);
    sortNodes(event.target.value);
  };

  return (
    <>
      <Stack align="center" justifyContent="center" mt={8} mb={8}>
        <Text fontSize={50}>Brand Recommender</Text>
        <Input
          placeholder="Enter food here"
          onChange={onChange}
          width={{ base: "90%", md: "70%" }}
        />
        <Flex gap={4}>
          <Button type="submit" onClick={onSubmit}>
            Enter
          </Button>
          {response && (
            <Select
              value={sortParameter}
              onChange={handleSelectChange}
              placeholder="Sort By"
            >
              <option value="fat">Fat</option>
              <option value="fiber">Fiber</option>
              <option value="protein">Protein</option>
              <option value="sodium">Sodium</option>
              <option value="sugar">Sugar</option>
            </Select>
          )}
        </Flex>

        {response && (
          <>
            <Flex width={"100%"} justifyContent={"space-around"}>
              <Stack align="center" justifyContent="center">
                <Text>DFS</Text>
                <Text>
                  DFS Time: {Number(response["dfs"]["dfs time"].toFixed(5))}
                </Text>
                <Accordion width="40vw">
                  {dfsNodes &&
                    dfsNodes.map((food: FoodObj) => {
                      return <FoodItem key={food["url"]} food={food} />;
                    })}
                </Accordion>
              </Stack>
              <Stack align="center" justifyContent="center">
                <Text>BFS</Text>
                <Text>
                  BFS Time: {Number(response["bfs"]["bfs time"].toFixed(5))}
                </Text>
                <Accordion width="40vw">
                  {bfsNodes &&
                    bfsNodes.map((food: FoodObj) => {
                      return <FoodItem key={food["url"]} food={food} />;
                    })}
                </Accordion>
              </Stack>
            </Flex>
          </>
        )}
      </Stack>
    </>
  );
}
