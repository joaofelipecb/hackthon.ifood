import React from "react";
import Box from "@mui/material/Box";
import { AppBar, Items, ShopBagBar, AppBarBotton } from "../../components";

const Page1 = () => {
  return (
    <Box sx={{ maxWidth: "500px" }}>
      <AppBar />
      <Items />
      <ShopBagBar />
      <AppBarBotton />
    </Box>
  );
};

export default Page1;
