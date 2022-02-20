import * as React from "react";
import {
  AppBar,
  Box,
  Typography,
  MenuList,
  MenuItem,
  IconButton,
} from "@mui/material";
import { ShoppingBag } from "@mui/icons-material";
import { ThemeProvider, createTheme } from "@mui/material/styles";

import { Colors } from "../../styles";

const handleClick = () => {
  console.log("Ver Sacola");
};

const ifoodTheme = createTheme({
  palette: {
    primary: {
      main: `${Colors.ifood_red}`,
    },
  },
});

export default function MainAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <ThemeProvider theme={ifoodTheme}>
        <AppBar position="static">
          <MenuList>
            <MenuItem onClick={handleClick}>
              <IconButton
                size="large"
                edge="start"
                color="inherit"
                aria-label="menu"
                sx={{ mr: 6, ml: 1 }}
              >
                <ShoppingBag />
              </IconButton>
              <Typography
                variant="h6"
                component="div"
                sx={{ mx: "auto", textAlign: "center" }}
              >
                Ver Sacola
              </Typography>
              <Typography variant="h6" component="div" sx={{ mr: 1 }}>
                R$ 34,00
              </Typography>
            </MenuItem>
          </MenuList>
        </AppBar>
      </ThemeProvider>
    </Box>
  );
}
