import React from "react";
import { Link } from "react-router-dom";
import { Box, Button } from "@mui/material";

const SelectItems = () => {
  return (
    <Box sx={{ maxWidth: "500px", textAlign: "center", mb: 4 }}>
      <Button
        color="error"
        sx={{ fontSize: "10", mt: 2 }}
        variant="contained"
        component={Link}
        to={"/4"}
      >
        Selecionar itens
      </Button>
    </Box>
  );
};

export default SelectItems;
