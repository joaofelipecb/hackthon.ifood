import React from "react";
import {
  Box,
  Typography,
  List,
  ListItem,
  ListItemText,
  Avatar,
  Paper,
  FormControl,
  RadioGroup,
  Radio,
  FormControlLabel,
  Grid,
} from "@mui/material";
import { img1 } from "../../assets/img";
import { styled } from "@mui/material/styles";

const Img = styled("img")({
  margin: "auto",
  display: "block",
  maxWidth: "100%",
  maxHeight: "100%",
});

const ingredientsList = [
  "Massa",
  "Molho",
  "Recheio",
  "Pimenta",
  "Cebola",
  "Tomate",
];

const Ingredients = () => {
  return (
    <Paper elevation={3} square sx={{ padding: 2, pl: 3 }}>
      <Typography variant="h6" component="div" sx={{ padding: 2 }}>
        Macarronada
      </Typography>
      <Grid item>
        <Avatar alt="R" src="/link" />
        <Typography component="div">Receita do Chef</Typography>
      </Grid>
      <Img alt="complex" src={img1} sx={{ mt: 3, mb: 3 }} />
      <Typography
        variant="h5"
        component="div"
        sx={{ padding: 2, color: "red" }}
      >
        Ingredientes
      </Typography>
      <List
        dense
        sx={{
          width: "100%",
          maxWidth: 360,
          bgcolor: "background.paper",
        }}
      >
        {ingredientsList.map((value) => (
          <ListItem key={value}>
            <ListItemText primary={value} />
          </ListItem>
        ))}
      </List>
      <Box sx={{ maxWidth: "500px", textAlign: "center" }}>
        <FormControl required sx={{ mb: 1, mt: 2 }}>
          <RadioGroup row aria-labelledby="row-radio-buttons-group-label">
            <FormControlLabel value="1" control={<Radio />} label="1 Pessoa" />
            <FormControlLabel value="2" control={<Radio />} label="2 Pessoas" />
            <FormControlLabel value="4" control={<Radio />} label="4 Pessoas" />
          </RadioGroup>
        </FormControl>
      </Box>
    </Paper>
  );
};

export default Ingredients;
