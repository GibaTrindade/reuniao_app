import React, { useEffect, useState } from "react";

const ReuniaoModal = ({ active, handleModal, token, id, setErrorMessage }) => {
  const [nome, setNome] = useState("");


  useEffect(() => {
    const getReuniao = async () => {
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
      };
      const response = await fetch(`http://127.0.0.1:8000/reuniao/${id}`, requestOptions);

      if (!response.ok) {
        setErrorMessage("Não conseguimos buscar a Reunião");
      } else {
        const data = await response.json();
        setNome(data.nome);

      }
    };

    if (id) {
     getReuniao();
    }
  }, [id, token]);

  const cleanFormData = () => {
    setNome("");
  };

  const handleCreateReuniao = async (e) => {
    e.preventDefault();
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
      body: JSON.stringify({
        nome: nome,
      }),
    };
    const response = await fetch("http://127.0.0.1:8000/reuniao", requestOptions);
    if (!response.ok) {
      setErrorMessage("Algo deu errado na criaç~çao da reunião!");
    } else {
      cleanFormData();
      handleModal();
    }
  };

  const handleUpdateReuniao = async (e) => {
    e.preventDefault();
    const requestOptions = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
      body: JSON.stringify({
        nome: nome,
      }),
    };
    const response = await fetch(`http://127.0.0.1:8000/reuniao/${id}`, requestOptions);
    if (!response.ok) {
      setErrorMessage("Something went wrong when updating lead");
    } else {
      cleanFormData();
      handleModal();
    }
  };

  return (
    <div className={`modal ${active && "is-active"}`}>
      <div className="modal-background" onClick={handleModal}></div>
      <div className="modal-card">
        <header className="modal-card-head has-background-primary-light">
          <h1 className="modal-card-title">
            {id ? "Editar Reunião" : "Criar Reunião"}
          </h1>
        </header>
        <section className="modal-card-body">
          <form>
            <div className="field">
              <label className="label">Título</label>
              <div className="control">
                <input
                  type="text"
                  placeholder="Digite o título da reunião"
                  value={nome}
                  onChange={(e) => setNome(e.target.value)}
                  className="input"
                  required
                />
              </div>
            </div>
            
            
          </form>
        </section>
        <footer className="modal-card-foot has-background-primary-light">
          {id ? (
            <button className="button is-info" onClick={handleUpdateReuniao}>
              Editar
            </button>
          ) : (
            <button className="button is-primary" onClick={handleCreateReuniao}>
              Criar
            </button>
          )}
          <button className="button" onClick={handleModal}>
            Cancelar
          </button>
        </footer>
      </div>
    </div>
  );
};

export default ReuniaoModal;
