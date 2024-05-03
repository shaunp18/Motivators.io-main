// Menu.tsx
import React from 'react';
import { Link } from "react-router-dom";
import "./Menu.scss";
import { menu } from "../../data";
import Switch from '@mui/material/Switch';

interface MenuProps {
  darkMode: boolean;
  toggleDarkMode: () => void;
}

const Menu: React.FC<MenuProps> = ({ darkMode, toggleDarkMode }) => {
  return (
    <>
      <br />
      <div className={`menu ${darkMode ? 'dark-mode' : 'light-mode'}`}>
        {menu.map((item) => (
          <div className="item" key={item.id}>
            <span className="title">{item.title}</span>
            {item.listItems.map((listItem) => (
              <Link to={listItem.url} className="listItem" key={listItem.id}>
                <img src={listItem.icon} alt="" />
                <span className="listItemTitle">{listItem.title}</span>
              </Link>
            ))}
          </div>
        ))}
      </div>
      {/* Light/Dark mode switch */}
      
    </>
  );
};

export default Menu;