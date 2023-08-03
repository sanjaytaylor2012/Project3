import { Flex, Text } from "@chakra-ui/react";
import { useRouter } from "next/router";
import React from "react";

type NavbarProps = {};

const Navbar: React.FC<NavbarProps> = () => {
  const router = useRouter();
  return (
    <Flex bg="black" height="55px" padding="10px 20px" align="center" gap={5}>
      <Text>Brand Balance</Text>
      <Text cursor="pointer" onClick={() => router.push("/")}>
        Home
      </Text>
      <Text cursor="pointer" onClick={() => router.push("/about")}>
        About
      </Text>
    </Flex>
  );
};
export default Navbar;
