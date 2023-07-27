import { Inter } from "next/font/google";
import { Button, Flex, Input, Stack, Text } from "@chakra-ui/react";
import { FormEventHandler, useState } from "react";

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
        setResponse(data["message"]);
      });
  };

  const onSubmit = (event: React.FormEvent<HTMLButtonElement>) => {
    event.preventDefault();
    sendForm();
  };

  return (
    <>
      <Stack align="center" justifyContent="center" mt={8}>
        <Text fontSize={50}>Food Ideas</Text>
        <Input
          placeholder="Enter food here"
          onChange={onChange}
          width={{ base: "90%", md: "70%" }}
        />
        <Button type="submit" onClick={onSubmit}>
          Enter
        </Button>
        {response && <Text fontSize={50}>{response}</Text>}
      </Stack>
    </>
  );
}
