import { useState, useEffect } from "react";
import "./App.css";
import ContactList from "./components/ContactList";

function App() {
  const [contacts, setcontacts] = useState([]);

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

  return <ContactList contacts={contacts}></ContactList>;
  // return "Hi";
}

export default App;
