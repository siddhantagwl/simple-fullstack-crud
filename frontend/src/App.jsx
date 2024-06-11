import { useState, useEffect } from "react";
import "./App.css";
import ContactList from "./components/ContactList";
import ContactForm from "./components/ContactForm";

function App() {
  const [contacts, setcontacts] = useState([]);

  // defining a modal, will be shown the form when creatign and updating a contact
  const [isModalOpen, setIsModalOpen] = useState(false);

  // as soon as this page loads, useEfect will be trigered and will be calling this function
  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const resp = await fetch("http://127.0.0.1:5000/contacts");
    const data = await resp.json();
    setcontacts(data[0].contacts);
    console.log("contacts are", data[0].contacts);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
  };

  return (
    <>
      <ContactList contacts={contacts} />
      <button onClick={openCreateModal}>Create new contact</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <ContactForm />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
