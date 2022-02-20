import * as React from "react";
import { Link } from "react-router-dom";
import { AppBar, Box, Typography, Toolbar, IconButton } from "@mui/material";
import { ChevronLeft } from "@mui/icons-material";
import { ThemeProvider, createTheme } from "@mui/material/styles";

import { Colors } from "../../styles";

const ifoodTheme = createTheme({
  palette: {
    primary: {
      main: `${Colors.ifood_white}`,
    },
  },
});

export default function MainAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <ThemeProvider theme={ifoodTheme}>
        <AppBar position="static">
          <Toolbar>
            <IconButton
              size="large"
              edge="start"
              color="error"
              aria-label="menu"
              component={Link}
              to={"/"}
            >
              <ChevronLeft />
            </IconButton>
            <Typography
              variant="h6"
              component="div"
              sx={{ mx: "auto", textAlign: "center" }}
            >
              iFood Receitas
            </Typography>
          </Toolbar>
        </AppBar>
      </ThemeProvider>
    </Box>
  );
}
