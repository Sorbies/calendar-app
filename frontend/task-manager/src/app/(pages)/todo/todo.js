'use client';

import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Collapse, Form } from 'react-bootstrap';
import styles from './todo.module.css';

export default function Todo() {
    const [tasks, setTasks] = useState([
        { id: 1, title: "Task 1", description: "Description for Task 1", dueDate: "2023-05-20", completed: false },
        { id: 2, title: "Task 2", description: "Description for Task 2", dueDate: "2023-05-21", completed: false },
        { id: 3, title: "Task 3", description: "Description for Task 3", dueDate: "2023-05-22", completed: false }
    ]);

    const [showCompleted, setShowCompleted] = useState(false);

    const toggleTaskCompletion = (taskId) => {
        setTasks(tasks.map(task => {
            if (task.id === taskId) {
                return { ...task, completed: !task.completed };
            }
            return task;
        }));
    };

    const completedTasks = tasks.filter(task => task.completed);

    return (
        <>
            <div style={{ textAlign: "left" }} className="todo-main-buttons">
                <div>
                    <Button variant="dark" className="me-2">
                        <i className="bi bi-plus-circle"></i>
                    </Button>
                    <Button variant="dark" className="me-2">
                        <i className="bi bi-pencil-square"></i>
                    </Button>
                    <Button variant="dark">
                        <i className="bi bi-arrow-counterclockwise"></i>
                    </Button>
                </div>
            </div>

            <div className="mt-4 d-flex justify-content-center align-items-center flex-column">
                {tasks.map(task => (
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
    );
}
