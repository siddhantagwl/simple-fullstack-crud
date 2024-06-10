import { useState } from "react";

const ContactForm = ({}) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const onSubmit = async (e) => {
    // not refreshing the page which is the default behaviour
    e.preventDefault();

    // send a post request
    const data = {
      firstName,
      lastName,
      email,
    };
    const url = "http://127.0.0.1:5000/create_contact";
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };

    const resp = await fetch(url, options);
    if (resp.status !== 201 && resp.status != 200) {
      const data = await resp.json();
      alert(data.message);
    } else {
      // success
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        ></input>
      </div>

      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        ></input>
      </div>

      <div>
        <label htmlFor="email">email:</label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        ></input>
      </div>
      <button type="submit">Create Contact</button>
    </form>
  );
};

export default ContactForm;
