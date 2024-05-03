import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import "./login.scss";

const LoginButton: React.FC = () => {
  const { loginWithRedirect, isAuthenticated } = useAuth0();

  return (
    !isAuthenticated && (
      <button className="login-button" onClick={() => loginWithRedirect()}>
        Sign In
      </button>
    )
  );
};

export default LoginButton;
