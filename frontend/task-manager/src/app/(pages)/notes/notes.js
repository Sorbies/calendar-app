"use client";

import React, { useState } from "react";
import { Button, Form } from 'react-bootstrap';
import styles from './notes.module.css';

export default function Notes() {
  const [note, setNote] = useState("");
  const [notes, setNotes] = useState([]);

  const handleNoteChange = (e) => {
    setNote(e.target.value);
  };

  const handleNoteSubmit = (e) => {
    e.preventDefault();
    if (note.trim() !== "") {
      const newNote = {
        text: note,
        date: new Date().toLocaleString(),
      };
      setNotes([...notes, newNote]);
      setNote("");
    }
  };

  return (
    <>
      <Form onSubmit={handleNoteSubmit} className="mt-4">
        <Form.Group controlId="noteTextArea">
          <Form.Label>Enter your note:</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            value={note}
            onChange={handleNoteChange}
          />
        </Form.Group>
        <Button variant="primary" type="submit" className="mt-3">
          Submit
        </Button>
      </Form>

      <div className="mt-5">
        <h2>Your Notes</h2>
        {notes.length > 0 ? (
          notes.map((note, index) => (
            <div key={index} className={styles.note}>
              <p>{note.text}</p>
              <small className="text-muted">{note.date}</small>
            </div>
          ))
        ) : (
          <p>No notes yet.</p>
        )}
      </div>
    </>
  );
}
