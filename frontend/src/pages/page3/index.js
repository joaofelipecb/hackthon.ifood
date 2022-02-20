import React from "react";
import Box from "@mui/material/Box";
import { AppBar, Ingredients, SelectItems } from "../../components";

const Page1 = () => {
  return (
    <Box sx={{ maxWidth: "500px" }}>
      <AppBar />
      <Ingredients />
      <SelectItems />
    </Box>
  );
};

export default Page1;
