'use client'

import { useState } from 'react';

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import styles from "./SignUp.module.css";

export default function SignUp() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const containerStyle = styles.signUpContainer;

    function updateUsername(e) {
        setUsername(e.target.value);
    }

    function updatePassword(e) {
        setPassword(e.target.value);
    }

    return (
        <>
            <div className={containerStyle}>
                <Form>
                    <Form.Group className="mb-3" controlId="usernameField">
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Enter username" value={username} onChange={updateUsername}/>
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="passwordField">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" value={password} onChange={updatePassword}/>
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>
            </div>
        </>
    );

}