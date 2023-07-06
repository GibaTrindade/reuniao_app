import React, { useContext, useEffect, useState } from "react";

import Register from "./components/Register";
import Header from "./components/Header";
import Login from "./components/Login";
import { UserContext } from "./context/UserContext";



const App = () => {
  const [message, setMessage] = useState("")
  const [token, , user] = useContext(UserContext);


  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("http://127.0.0.1:8000/api", requestOptions)
    const data = await response.json()

    if(!response.ok){
      console.log("Deu merda!")
    } else{
      setMessage(data.message)
    }
  };

  useEffect(() => {
    getWelcomeMessage()
  }, [])

  return (
    <>
      <Header title={"Sala de Reunião"} />
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
          {
            !token ? (
              <div className="columns">
                <Register /> <Login />
              </div>
            ) : (
              <p>User é admin: {JSON.stringify(user ? user.is_admin : "")}</p>
            )
          }
        </div>
        <div className="column"></div>
      </div>
    </>
  );
}

export default App;
