'use client'

import { useState } from 'react';
import { useRouter } from 'next/navigation';

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Alert, ButtonGroup, ButtonToolbar } from 'react-bootstrap';

import { sendRegisterData, sendLoginData, setTokenCookie } from '../lib/authenticationStuff';

import styles from "./SignUp.module.css";

export default function SignUp({ initShow = false, initMsg = "", initStyle = "", }) {
    //states
    const [registerMode, setRegisterMode] = useState(true);
    const [showAlertMsg, setShowAlertMsg] = useState(initShow);
    const [alertMsg, setAlertMsg] = useState(initMsg);
    const [alertStyle, setAlertStyle] = useState(initStyle);

    const containerStyle = styles.signUpContainer;

    //router used for redirecting
    const router = useRouter();

    //state dependent vals
    let title = registerMode ? "Register" : "Log in";
    let switcher = registerMode ? "Already have an account? Log in" : "Don't have an account? Sign up";
    let submitFn = registerMode ? submitRegister : submitLogin;

    //state setter fns
    function toggleRegisterMode() {
        setRegisterMode((prev) => !prev);
    }

    //submission handling fns
    async function submitRegister(formData) {
        const result = await sendRegisterData(formData); //submit the data
        document.getElementById("registerForm").reset(); //clear the form

        if (result != null) { // if registration succeeds

            //show the alert message
            setShowAlertMsg(false); //hide any existing alert message
            setAlertMsg("Successfully registered! Redirecting soon...");
            setAlertStyle("success");
            setShowAlertMsg(true);

            //proceed to login with the same data
            const token = await sendLoginData(formData);
            await setTokenCookie(token);

            //redirect after a lil while
            setTimeout(() => router.push("/home"), 2000);

        }
        else { //if registration fails

            //show the alert message
            setShowAlertMsg(false); //hide any existing alert message
            setAlertMsg("Failed to register.");
            setAlertStyle("danger");
            setShowAlertMsg(true);

        }
    }

    async function submitLogin(formData) {
        const result = await sendLoginData(formData); //submit the data
        document.getElementById("registerForm").reset(); //clear the form
        if (result != null) { // if logging in succeeds

            //show the alert message
            setShowAlertMsg(false); //hide any existing alert message
            setAlertMsg("Successfully logged in! Redirecting soon...");
            setAlertStyle("success");
            setShowAlertMsg(true);

            //set the token cookie
            setTokenCookie(result);

            //redirect after a lil while
            setTimeout(() => router.push("/home"), 3000);

        } else { //if login fails

            //show the alert message
            setShowAlertMsg(false); //hide any existing alert message
            setAlertMsg("Failed to log in.");
            setAlertStyle("danger");
            setShowAlertMsg(true);
        }
    }

    return (
        <>
            <div className={containerStyle}>
                {/* Alert */}
                <div id="alertContainer">
                    {showAlertMsg ? <Alert variant={alertStyle} onClick={() => setShowAlertMsg(false)} dismissible>
                        {alertMsg}
                    </Alert> : ""}
                </div>

                {/* Login/Register form */}
                <Form action={submitFn} id='registerForm'>
                    <Form.Group className='mb-0' controlId='Form Title'>
                        <Form.Label><h3>{title}</h3></Form.Label>
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="usernameField">
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Enter username" name="username" />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="passwordField">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" name="password" />
                    </Form.Group>

                    <ButtonToolbar>
                        <ButtonGroup>
                            <Button className="me-2" variant="primary" type="submit">
                                Submit
                            </Button>
                        </ButtonGroup>
                        <ButtonGroup>
                            <Button className="me-2" variant="primary" onClick={toggleRegisterMode}>
                                {switcher}
                            </Button>
                        </ButtonGroup>
                    </ButtonToolbar>

                </Form>
            </div>
        </>
    );

}