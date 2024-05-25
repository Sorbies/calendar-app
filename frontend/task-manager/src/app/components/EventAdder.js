'use client'

import { useState } from 'react';

import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import { Form } from 'react-bootstrap';
import { addEvent } from '../lib/eventStuff';

import BigPlus from './BigPlus';

export default function EventAdder({ calendars }) {

    const [showEvent, setShowEvent] = useState(false);
    const [showTask, setShowTask] = useState(false);

    const handleCloseEvent = () => setShowEvent(false);
    const handleShowEvent = () => setShowEvent(true);

    const handleCloseTask = () => setShowTask(false);
    const handleShowTask = () => setShowTask(true);

    async function submitAddEvent(formData) {
        const result = await addEvent(formData);
        document.getElementById('addEventForm').reset();
        if (!('error' in result)) {alert('Event successfully added.');}
        else {alert('Error adding event.')}
    }

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
                    <Modal.Title>Add a new event</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form action={submitAddEvent} id='addEventForm'>
                        <Form.Group className="mb-3" controlId="calendarId">
                        <Form.Label>Calendar</Form.Label>
                            <Form.Select name="calendarId" aria-label='calendarSelect'>
                                <option>Select a calendar...</option>
                                {calendars.map((calendar) => {
                                    return (
                                        <option key={calendar['id']}
                                                value={calendar['id']}>
                                            {calendar['name']}
                                        </option>
                                    );
                                })}
                            </Form.Select>
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="eventTitle">
                            <Form.Label>Event Title</Form.Label>
                            <Form.Control type="text" placeholder="Enter title of your event" name="eventTitle" maxLength={100} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="eventDesc">
                            <Form.Label>Event Description</Form.Label>
                            <Form.Control as="textarea" rows={4} placeholder="Enter event description" name="eventDesc" maxLength={500} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="eventStartDate">
                            <Form.Label>Event Start Date</Form.Label>
                            <Form.Control type="datetime-local" name="eventStartDate" defaultValue={new Date().toISOString().substring(0, 16)} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="eventEndDate">
                            <Form.Label>Event End Date</Form.Label>
                            <Form.Control type="datetime-local" name="eventEndDate" defaultValue={new Date().toISOString().substring(0, 16)} />
                        </Form.Group>

                        <Form.Group>
                            <Button variant="primary" type='submit' name='submitAddEvent' onClick={handleCloseEvent}>
                                Add Task
                            </Button>
                        </Form.Group>
                    </Form>

                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleCloseEvent}>
                        Close
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