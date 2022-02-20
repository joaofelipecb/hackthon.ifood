import React from "react";
import { Routes, Route } from "react-router-dom";

import Page3 from "../pages/page3";
import Page4 from "../pages/page4";

const appRoutes = () => {
  return (
    <Routes>
      <Route path="/*" element={<Page3 />} />
      <Route path="/4" element={<Page4 />} />
    </Routes>
  );
};

export default appRoutes;
