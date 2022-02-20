import * as React from "react";
import Box from "@mui/material/Box";
import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";

import { Search, ListAlt, Home, Person } from "@mui/icons-material";

export default function AppBarBotton() {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ maxWidth: 500 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <BottomNavigationAction label="Início" icon={<Home />} />
        <BottomNavigationAction label="Busca" icon={<Search />} />
        <BottomNavigationAction label="Pedidos" icon={<ListAlt />} />
        <BottomNavigationAction label="Perfil" icon={<Person />} />
      </BottomNavigation>
    </Box>
  );
}
