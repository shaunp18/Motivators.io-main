import Home from "./pages/home/Home";
import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import Users from "./pages/users/Users";
import Products from "./pages/products/Products";
import Navbar from "./components/navbar/Navbar";
import Footer from "./components/footer/Footer";
import Menu from "./components/menu/Menu";
import Login from "./pages/login/Login";
import "./styles/global.scss";
import User from "./pages/user/User";
import Product from "./pages/product/Product";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import Assessments from "./pages/assessments/assessments";
import SettingsPage from "./pages/settings/settings";
import { useAuth0 } from "@auth0/auth0-react";
import { useState } from "react";
import LogoutButton from "./components/logout/LogoutButton";
import { AirTable } from "./pages/airTable/airTable";
import { Chatbot } from "./pages/chatbot/chatbot";
import LoginButton from "./components/login/LoginButton";

const queryClient = new QueryClient();

function App() {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const Layout = () => {
    const { isAuthenticated } = useAuth0();
    return (
      <div className={`main ${darkMode ? 'dark-mode' : 'light-mode'}`}>
        <Navbar darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>
        <div className="top-right">
          {!isAuthenticated ? <LoginButton /> : <LogoutButton />}
        </div>
        <div className="container">
          <div className="menuContainer">
            <Menu darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>
          </div>
          <div className="contentContainer">
            <QueryClientProvider client={queryClient}>
              <Outlet />
            </QueryClientProvider>
          </div>
        </div>
        <Footer />
      </div>
    );
  };

  const router = createBrowserRouter([
    {
      path: "/",
      element: <Layout />,
      children: [
        {
          path: "/",
          element: <Home darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>,
        },
        {
          path: "/users",
          element: <Users />,
        },
        {
          path: "/Assessments",
          element: <Assessments />,
        },
        {
          path: "/Chatbot",
          element: <Chatbot />,
        },
        {
          path: "/products",
          element: <Products />,
        },
        {
          path: "/settings",
          element: <SettingsPage />,
        },
        {
          path: "/AirTable",
          element: <AirTable />,
        },
      ],
    },
    {
      path: "/login",
      element: (
        <>
          <Login />
          <LoginButton />
        </>
      ),
    },
    {
      path: "/logout",
      element: (
        <>
          <LogoutButton />
        </>
      ),
    },
  ]);

  return <RouterProvider router={router} />;
}

export default App;
