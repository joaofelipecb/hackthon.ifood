import React from "react";
import { Paper, Divider, Typography, Button } from "@mui/material";
import { img1, img2, img3, img4, img5 } from "../../assets/img";

import { styled } from "@mui/material/styles";

const imageList = [img1, img2, img3, img4, img5];

const Img = styled("img")({
  margin: "auto",
  display: "block",
  maxWidth: "100%",
  maxHeight: "100%",
});

const Items = () => {
  return (
    <Paper elevation={3} square sx={{ padding: 3 }}>
      <Typography variant="h6" component="div">
        Massas
      </Typography>
      {imageList.map((value) => (
        <Button key={value} sx={{ width: 128, height: 128 }}>
          <Img alt="complex" src={value} />
          {/* <ListItemText primary={value} /> */}
        </Button>
      ))}
      <Divider />
      <Typography variant="h6" component="div">
        Molhos
      </Typography>
      {imageList.map((value) => (
        <Button key={value} sx={{ width: 128, height: 128 }}>
          <Img alt="complex" src={value} />
          {/* <ListItemText primary={value} /> */}
        </Button>
      ))}
      <Divider />
      <Typography variant="h6" component="div">
        Recheio
      </Typography>
      {imageList.map((value) => (
        <Button key={value} sx={{ width: 128, height: 128 }}>
          <Img alt="complex" src={value} />
          {/* <ListItemText primary={value} /> */}
        </Button>
      ))}
    </Paper>
  );
};

export default Items;
