'use client';

import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Collapse, Form, Modal } from 'react-bootstrap';
import styles from './todo.module.css';
import { addTask, getTasksOfTodo, toggleTaskComplete } from '@/app/lib/taskStuff';
import { useSearchParams } from 'next/navigation';

export default function Todo() {
    const searchParams = useSearchParams();
    const currentTodoId = searchParams.get('id');

    const [tasks, setTasks] = useState([]);

    const [showCompleted, setShowCompleted] = useState(false);
    const [showAddTask, setShowAddTask] = useState(false);
    const [refreshTasks, setRefreshTasks] = useState(false);

    const completedTasks = tasks.filter(task => task.completed);

    //refreshes the task data without requiring reload whenever selected todoid changes
    useEffect(() => {
        async function updateTasks() {
            if (currentTodoId != null) {
                const newTaskData = await getTasksOfTodo(currentTodoId);

                //modifying the data due to differencies in back/frontend implementations
                newTaskData.forEach((task) => {
                    //renaming the content key to description
                    task['description'] = task['content'];
                    delete task['content'];
                    //renaming the end_date_time to dueDate
                    task['dueDate'] = task['end_date_time'];
                    delete task['end_date_time'];
                    //modifying the format slightly
                    task['dueDate'] = task['dueDate'].replace('T', ' ');
                });

                setTasks(newTaskData);
            }
        }
        updateTasks();
    }, [refreshTasks, searchParams])


    const toggleTaskCompletion = async (taskId) => {
        await toggleTaskComplete(taskId);
        forceTaskRefresh();
    };

    function forceTaskRefresh() { setRefreshTasks(prev => !prev); }
    const handleCloseAddTask = () => setShowAddTask(false);
    const handleShowAddTask = () => setShowAddTask(true);

    async function submitAddTask(formData) {
        const result = await addTask(formData);
        document.getElementById('addTaskForm').reset();
        if (!('error' in result)) { alert('Task successfully added.'); }
        else { alert('Something went wrong while adding the task.'); }
        forceTaskRefresh();
    }


    return (
        <>
            {currentTodoId == null ? 'Select a todo list from the sidebar.' : (
                <>
                    {/* Top three buttons */}
                    <div style={{ textAlign: "left" }} className="todo-main-buttons">
                        <div>
                            <Button variant="dark" className="me-2" data-toggle="tooltip" title="Add a task" onClick={handleShowAddTask}>
                                <i className="bi bi-plus-circle"></i>
                            </Button>
                            <Button variant="dark" className="me-2" data-toggle="tooltip" title="Edit tasks">
                                <i className="bi bi-pencil-square"></i>
                            </Button>
                            <Button variant="dark" data-toggle="tooltip" title="Reset task completion status">
                                <i className="bi bi-arrow-counterclockwise"></i>
                            </Button>
                        </div>
                    </div>

                    {/* Adding task modal */}
                    <Modal show={showAddTask} onHide={handleCloseAddTask}>
                        <Modal.Header closeButton>
                            <Modal.Title>Add a new task</Modal.Title>
                        </Modal.Header>

                        {/* Add task form */}
                        <Modal.Body>
                            <Form action={submitAddTask} id='addTaskForm'>
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
                                    <Form.Control type="hidden" name="todoId" value={currentTodoId} />
                                </Form.Group>

                                <Form.Group>
                                    <Button variant="primary" type='submit' name='submitAddTask' onClick={handleCloseAddTask}>
                                        Add Task
                                    </Button>
                                </Form.Group>
                            </Form>
                        </Modal.Body>

                        <Modal.Footer>
                            <Button variant="secondary" onClick={handleCloseAddTask}>
                                Close
                            </Button>
                        </Modal.Footer>
                    </Modal>


                    {/* Todo body */}
                    <div className="mt-4 d-flex justify-content-center align-items-center flex-column">
                        {/* Todo tasks */}
                        {tasks.length == 0 ? 'There are currently no tasks to do.' : tasks.map(task => (
                            <div key={task.id} className={`form-check ${styles.taskContainer}`}>
                                <input
                                    type="checkbox"
                                    className="form-check-input"
                                    id={`task-${task.id}`}
                                    checked={task.completed}
                                    onChange={() => toggleTaskCompletion(task.id)}
                                />
                                <div className={styles.taskContent}>
                                    <label className={`form-check-label ${task.completed ? styles.completed : ""}`} htmlFor={`task-${task.id}`} style={{ fontSize: "1.5rem" }}>
                                        {task.title}
                                    </label>
                                    <p className={styles.taskDescription}>{task.description}</p>
                                    <p className={styles.taskDueDate}>Due: {task.dueDate}</p>
                                </div>
                            </div>
                        ))}

                        {/* Completed section */}
                        <Collapse in={showCompleted}>
                            <div className="mt-4">
                                <h2>Completed Tasks</h2>
                                <ul>
                                    {completedTasks.map(task => (
                                        <li key={task.id}>
                                            <strong>{task.title}</strong><br />
                                            {task.description}<br />
                                            Due: {task.dueDate}
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        </Collapse>

                        {/* Button to show/hide completed */}
                        <Button
                            onClick={() => setShowCompleted(!showCompleted)}
                            aria-controls="completed-tasks"
                            aria-expanded={showCompleted}
                            variant="secondary"
                            className="mt-3"
                        >
                            {showCompleted ? 'Hide Completed' : 'Show Completed'}
                        </Button>
                    </div>


                </>
            )}
        </>
    );
}
