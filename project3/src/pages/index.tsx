import { Inter } from "next/font/google";
import {
  Button,
  Flex,
  Input,
  Radio,
  RadioGroup,
  Select,
  Stack,
  Text,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { Accordion } from "@chakra-ui/react";
import FoodItem from "@/Components/FoodItem";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  const [formInput, setFormInput] = useState("");
  const [response, setResponse] = useState();
  const [bfsNodes, setBfsNodes] = useState<FoodObj[]>();
  const [dfsNodes, setdfsNodes] = useState<FoodObj[]>();
  const [sortParameter, setSortParameter] = useState("");
  const [loading, setLoading] = useState(false);
  const [sortDirection, setSortDirection] = useState("");

  const onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormInput(event.target.value);
  };

  const sendForm = async () => {
    setLoading(true);
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
        setLoading(false);
      });
  };

  // const sortNodes = (sortParameter: string) => {
  //   if (sortParameter == "") {
  //     return;
  //   } else if (sortParameter == "fat") {
  //     bfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.fat);
  //       const b_num = parseFloat(b.fat);
  //       return b_num - a_num;
  //     });
  //     dfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.fat);
  //       const b_num = parseFloat(b.fat);
  //       return b_num - a_num;
  //     });
  //   } else if (sortParameter == "fiber") {
  //     bfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.fiber);
  //       const b_num = parseFloat(b.fiber);
  //       return b_num - a_num;
  //     });
  //     dfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.fiber);
  //       const b_num = parseFloat(b.fiber);
  //       return b_num - a_num;
  //     });
  //   } else if (sortParameter == "protein") {
  //     bfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.protein);
  //       const b_num = parseFloat(b.protein);
  //       return b_num - a_num;
  //     });
  //     dfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.protein);
  //       const b_num = parseFloat(b.protein);
  //       return b_num - a_num;
  //     });
  //   } else if (sortParameter == "sodium") {
  //     bfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.sodium);
  //       const b_num = parseFloat(b.sodium);
  //       return b_num - a_num;
  //     });
  //     dfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.sodium);
  //       const b_num = parseFloat(b.sodium);
  //       return b_num - a_num;
  //     });
  //   } else if (sortParameter == "sugar") {
  //     bfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.sugar);
  //       const b_num = parseFloat(b.sugar);
  //       return b_num - a_num;
  //     });
  //     dfsNodes?.sort((a, b) => {
  //       const a_num = parseFloat(a.sugar);
  //       const b_num = parseFloat(b.sugar);
  //       return b_num - a_num;
  //     });
  //   }
  //   // } else {
  //   //   bfsNodes?.sort((a, b) => {
  //   //     const a_num = parseFloat(a.sortParameter);
  //   //     const b_num = parseFloat(b.sortParameter);
  //   //     return b_num - a_num;
  //   //   });
  //   // }
  // };

  const sortNodes = (sortParameter: string, sortDirection: string) => {
    if (sortParameter == "") {
      return;
    }
    if (sortDirection == "") {
      sortDirection = "ascending";
      setSortDirection("ascending");
    }
    if (sortParameter == "fat") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailyfatpercent);
        const b_num = parseFloat(b.dailyfatpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailyfatpercent);
        const b_num = parseFloat(b.dailyfatpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
    } else if (sortParameter == "protein") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailyproteinpercent);
        const b_num = parseFloat(b.dailyproteinpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailyproteinpercent);
        const b_num = parseFloat(b.dailyproteinpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
    } else if (sortParameter == "fiber") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailyfiberpercent);
        const b_num = parseFloat(b.dailyfiberpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailyfiberpercent);
        const b_num = parseFloat(b.dailyfiberpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
    } else if (sortParameter == "sodium") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailysodiumpercent);
        const b_num = parseFloat(b.dailysodiumpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.dailysodiumpercent);
        const b_num = parseFloat(b.dailysodiumpercent);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
    } else if (sortParameter == "sugar") {
      bfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.sugar);
        const b_num = parseFloat(b.sugar);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
      dfsNodes?.sort((a, b) => {
        const a_num = parseFloat(a.sugar);
        const b_num = parseFloat(b.sugar);
        if (sortDirection == "ascending") {
          return b_num - a_num;
        } else {
          return a_num - b_num;
        }
      });
    }
  };

  const onSubmit = (event: React.FormEvent<HTMLButtonElement>) => {
    event.preventDefault();
    sendForm();
  };

  const handleSelectChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSortParameter(event.target.value);
    sortNodes(event.target.value, sortDirection);
  };

  const handleSortChange = (nextValue: string) => {
    setSortDirection(nextValue);
    sortNodes(sortParameter, nextValue);
  };

  return (
    <>
      <Stack align="center" justifyContent="center" mt={8} mb={8}>
        <Text fontSize={50}>Brand Balance</Text>
        <Input
          placeholder="Enter any food here"
          onChange={onChange}
          width={{ base: "90%", md: "70%" }}
        />
        <Flex gap={4} align="center" mb={8}>
          <Button isLoading={loading} type="submit" onClick={onSubmit}>
            Enter
          </Button>
          {response && (
            <>
              <Select
                value={sortParameter}
                onChange={handleSelectChange}
                placeholder="Sort By"
              >
                <option value="fat">Fat</option>
                <option value="fiber">Fiber</option>
                <option value="protein">Protein</option>
                <option value="sodium">Sodium</option>
                {/* <option value="sugar">Sugar</option> */}
              </Select>
              <RadioGroup onChange={handleSortChange} value={sortDirection}>
                <Stack direction="row">
                  <Radio value="descending">Ascending</Radio>
                  <Radio value="ascending">Descending</Radio>
                </Stack>
              </RadioGroup>
            </>
          )}
        </Flex>

        {response && (
          <>
            <Flex
              direction={{ base: "column", md: "row" }}
              width={"100%"}
              justifyContent={"space-around"}
            >
              <Stack align="center" justifyContent="center" mb={5}>
                <Text fontWeight={700} fontSize={20}>
                  DFS (Depth First Search) for different foods
                </Text>
                <Text fontWeight={700} fontSize={20}>
                  DFS Time: {response["dfs"]["dfs time"]} seconds
                </Text>
                <Accordion width={{ base: "90%", md: "45vw" }}>
                  {dfsNodes &&
                    dfsNodes.map((food: FoodObj) => {
                      return <FoodItem key={food["url"]} food={food} />;
                    })}
                </Accordion>
              </Stack>
              <Stack align="center" justifyContent="center" mb={5}>
                <Text fontWeight={700} fontSize={20}>
                  BFS (Breadth First Search) for similar foods
                </Text>
                <Text fontWeight={700} fontSize={20}>
                  BFS Time: {response["bfs"]["bfs time"]} seconds
                </Text>
                <Accordion width={{ base: "90%", md: "45vw" }}>
                  {bfsNodes &&
                    bfsNodes.map((food: FoodObj) => {
                      return <FoodItem key={food["url"]} food={food} />;
                    })}
                </Accordion>
              </Stack>
            </Flex>
          </>
        )}
        {response && <Text>*% Daily Value (Per 28 grams)</Text>}
      </Stack>
    </>
  );
}
