import React, { useContext, useState } from "react";

import { UserContext } from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmationPassword, setConfirmationPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [, setToken] = useContext(UserContext);

    const submitRegistration = async () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({email: email, password: password}),
          };
          console.log("entrou")
          const response = await fetch("http://127.0.0.1:8000/users", requestOptions);
          const data = await response.json();
          if(!response.ok){
            setErrorMessage(data.detail)
          }else{
            setToken(data.access_token)
          }
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        if(password === confirmationPassword && password.length > 5){
            submitRegistration()
        }else{
            setErrorMessage("Verifique se os passwords estão iguais e são maiores que 5 caracteres ")
        }
    }

    return(
        <div className="column">
            <form className="box" onSubmit={handleSubmit}>
                <h1 className="title has-text-centered">Registrar</h1>
                <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                        <input 
                            type="email" 
                            placeholder="Digite seu email" 
                            value={email} 
                            onChange={(e) => setEmail(e.target.value)}
                            className="input"
                            required
                        />

                    </div>
                </div>

                <div className="field">
                    <label className="label">Password</label>
                    <div className="control">
                        <input 
                            type="password" 
                            placeholder="Digite seu password" 
                            value={password} 
                            onChange={(e) => setPassword(e.target.value)}
                            className="input"
                            required
                        />

                    </div>
                </div>

                <div className="field">
                    <label className="label">Confirmação do Password</label>
                    <div className="control">
                        <input 
                            type="password" 
                            placeholder="Digite seu password novamente" 
                            value={confirmationPassword} 
                            onChange={(e) => setConfirmationPassword(e.target.value)}
                            className="input"
                            required
                        />

                    </div>
                </div>
                <ErrorMessage message={errorMessage} />
                <br/>
                <button className="button is-primary" type="submit">
                    Registrar
                </button>
            </form>
        </div>
    )
}

export default Register;