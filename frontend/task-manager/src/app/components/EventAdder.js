'use client'

import { useState } from 'react';

import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import { Form } from 'react-bootstrap';

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
                    <Modal.Title>Add a new event</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form action={''} id='addTaskForm'>
                        <Form.Group className="mb-3" controlId="taskTitle">
                            <Form.Label>Task Title</Form.Label>
                            <Form.Control type="text" placeholder="Enter title of a task" name="taskTitle" maxLength={100} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="taskDesc">
                            <Form.Label>Task Description</Form.Label>
                            <Form.Control as="textarea" rows={4} placeholder="Enter task description" name="taskDesc" maxLength={500} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="taskDueDate">
                            <Form.Label>Due Date</Form.Label>
                            <Form.Control type="datetime-local" name="taskDueDate" defaultValue={new Date().toISOString().substring(0, 16)} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="todoId">
                            <Form.Control type="hidden" name="todoId" value={''} />
                        </Form.Group>

                        <Form.Group>
                            <Button variant="primary" type='submit' name='submitAddTask' onClick={''}>
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