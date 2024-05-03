import { blue, green, purple } from "@mui/material/colors";
import "./navbar.scss";
import { ThemeProvider, createTheme } from "@mui/material";
import { useState } from "react";

interface NavbarProps {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

const Navbar = ({ darkMode, toggleDarkMode }: NavbarProps) => {
  // Define theme based on the current mode
  const theme = createTheme({
    palette: {
      mode: darkMode ? 'dark' : 'light',
      primary: {
        main: darkMode ? blue[500] : blue[700], // Change blue[500] to the shade of blue you prefer
      },
      secondary: {
        main: darkMode ? green[500] : purple[500],
      },
      text: {
        primary: darkMode ? '#fff' : '#000', // Adjust text color based on mode
      },
      background: {
        default: darkMode ? '#000' : '#fff', // Adjust background color based on mode
      },
    },
  });

  return (
    <ThemeProvider theme={theme}>
      <div className={`navbar ${darkMode ? 'dark-mode' : 'light-mode'}`}>
        <div className="logo">
          <img src="logo.png" alt="" />
        </div>
        {/* Add other navbar content here */}
      </div>
    </ThemeProvider>
  );
};

export default Navbar;

