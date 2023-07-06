import React, { createContext, useEffect, useState } from "react";

export const UserContext = createContext();

export const UserProvider = (props) => {
    const [token, setToken] = useState(localStorage.getItem("meuToken"))
    const [user, setUser] = useState(null)

    useEffect(() => {
        const fetchUser = async () => {
            const requestOptions = {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: "Bearer " + token,
                },
            };
            const response = await fetch("http://127.0.0.1:8000/current_user/me", requestOptions);
            
            if(!response.ok){
                setToken(null);
            }else{
                const data = await response.json()
                setUser(data)
            }
            localStorage.setItem("meuToken", token);
            
        }
        fetchUser();
    }, [token])

    return (
        <UserContext.Provider value={[token, setToken, user]}>
            {props.children}
        </UserContext.Provider>
    )
}