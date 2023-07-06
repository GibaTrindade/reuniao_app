import React, { useContext, useEffect, useState } from "react";
//import moment from "moment";

import ErrorMessage from "./ErrorMessage";
import ReuniaoModal from "./ReuniaoModal";
import { UserContext } from "../context/UserContext";

const TabelaReuniao = () => {
  const [token] = useContext(UserContext);
  const [reunioes, setReunioes] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [loaded, setLoaded] = useState(false);
  const [activeModal, setActiveModal] = useState(false);
  const [id, setId] = useState(null);

  const handleUpdate = async (id) => {
    setId(id);
    setActiveModal(true);
  };

  const handleDelete = async (id) => {
    const requestOptions = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
    };
    const response = await fetch(`/api/reunioes/${id}`, requestOptions);
    if (!response.ok) {
      setErrorMessage("Failed to delete reuniao");
    }

    getReunioes();
  };

  const getReunioes = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
    };
    const response = await fetch("http://127.0.0.1:8000/reunioes", requestOptions);
    if (!response.ok) {
      setErrorMessage("Algo deu errado, não coseguimos baixar as reuniões");
    } else {
      const data = await response.json();
      console.log(data)
      setReunioes(data);
      setLoaded(true);
    }
  };

  useEffect(() => {
    getReunioes();
  }, []);

  const handleModal = () => {
    setActiveModal(!activeModal);
    getReunioes();
    setId(null);
  };

  return (
    <>
      <ReuniaoModal
        active={activeModal}
        handleModal={handleModal}
        token={token}
        id={id}
        setErrorMessage={setErrorMessage}
      />
      <button
        className="button is-fullwidth mb-5 is-primary"
        onClick={() => setActiveModal(true)}
      >
        Criar Reunião
      </button>
      <ErrorMessage message={errorMessage} />
      {loaded && reunioes ? (
        <table className="table is-fullwidth">
          <thead>
            <tr>
              <th>Título</th>
              <th># Participantes</th>
              <th># Encaminhamentos</th>
              <th></th>
             
            </tr>
          </thead>
          <tbody>
            {reunioes.map((reuniao) => (
              <tr key={reuniao.id}>
                <td>{reuniao.nome}</td>
                <td>{reuniao.participantes.length}</td>
                <td>{reuniao.encaminhamentos.length}</td>
                <td>
                  <button
                    className="button mr-2 is-info is-light"
                    onClick={() => handleUpdate(reuniao.id)}
                  >
                    Update
                  </button>
                  <button
                    className="button mr-2 is-danger is-light"
                    onClick={() => handleDelete(reuniao.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Loading</p>
      )}
    </>
  );
};

export default TabelaReuniao;
