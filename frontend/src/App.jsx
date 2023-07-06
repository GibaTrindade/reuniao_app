import React, { useContext, useEffect, useState } from "react";

import Register from "./components/Register";
import Header from "./components/Header";
import Login from "./components/Login";
import TabelaReuniao from "./components/TabelaReunioes";
import { UserContext } from "./context/UserContext";



const App = () => {
  const [message, setMessage] = useState("")
  const [token, , user] = useContext(UserContext);
  const [login, setLogin] = useState(true)
  const [register, setRegister] = useState(false)

  const showLogin = () => {
    setLogin(true)
    setRegister(false)
  }
  const showRegister = () => {
    setLogin(false)
    setRegister(true)
  }

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
      <Header title={"Sala de Reunião"} showLogin={showLogin} showRegister={showRegister}/>
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
          {
            !token && login && (
              <div className="columns">
                 <Login />
              </div>
            )
          } 
          {
            !token && register && (
              <div className="columns">
                <Register /> 
              </div>
            )
          } 
          {token && (
              <TabelaReuniao />
            )
          }
        </div>
        <div className="column"></div>
      </div>
    </>
  );
}

export default App;
