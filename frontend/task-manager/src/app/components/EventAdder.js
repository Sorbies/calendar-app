'use client'

import { useState } from 'react';

import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';

import BigPlus from './BigPlus';

export default function EventAdder() {

    const [showEvent, setShowEvent] = useState(false);
    const [showTask, setShowTask] = useState(false);

    const handleCloseEvent = () => setShowEvent(false);
    const handleShowEvent = () => setShowEvent(true);

    const handleCloseTask = () => setShowTask(false);
    const handleShowTask = () => setShowTask(true);

    return (
        <>
            {/* Add button with dropup */}
            <Dropdown drop="up-centered">
                <Dropdown.Toggle variant="success" id="dropdown-basic" as={BigPlus}>
                </Dropdown.Toggle>

                <Dropdown.Menu>
                    <Dropdown.Item onClick={handleShowEvent}>Add an event</Dropdown.Item>
                    <Dropdown.Item onClick={handleShowTask}>Add a task</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>

            {/* Event adder window */}
            <Modal show={showEvent} onHide={handleCloseEvent}>
                <Modal.Header closeButton>
                    <Modal.Title>Modal heading</Modal.Title>
                </Modal.Header>
                <Modal.Body>Adding an event</Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleCloseEvent}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={handleCloseEvent}>
                        Save Changes
                    </Button>
                </Modal.Footer>
            </Modal>

            {/* Task adder window */}
            <Modal show={showTask} onHide={handleCloseTask}>
                <Modal.Header closeButton>
                    <Modal.Title>Modal heading</Modal.Title>
                </Modal.Header>
                <Modal.Body>Adding a task</Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleCloseTask}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={handleCloseTask}>
                        Save Changes
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    )
}