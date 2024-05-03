import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import { Auth0Provider } from "@auth0/auth0-react";

const domain = import.meta.env.VITE_REACT_APP_AUTH0_DOMAIN;
const clientId = import.meta.env.VITE_REACT_APP_AUTH0_CLIENT_ID;

const Main = () => {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };
  return(
  <React.StrictMode>
    <Auth0Provider
      domain={domain}
      clientId={clientId}
      authorizationParams={{
        redirect_uri: window.location.origin,
      }}
    >
      <App darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>
    </Auth0Provider>
  </React.StrictMode>
  )
    };

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <Main />
)
