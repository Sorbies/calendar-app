'use client';

import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Collapse } from 'react-bootstrap';
import styles from './todo.module.css';

export default function Page() {
    const [tasks, setTasks] = useState([
        { id: 1, text: "Task 1", completed: false },
        { id: 2, text: "Task 2", completed: false },
        { id: 3, text: "Task 3", completed: false }
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
            <div style={{ textAlign: "left" }}>
                <h5>This is where our inspirational quote goes</h5>
            </div>

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
                    <div key={task.id} className="form-check">
                        <input
                            type="checkbox"
                            className="form-check-input"
                            id={`task-${task.id}`}
                            checked={task.completed}
                            onChange={() => toggleTaskCompletion(task.id)}
                        />
                        <label className={"form-check-label " + (task.completed ? styles.completed : "")} htmlFor={`task-${task.id}`} style={{ fontSize: "1.5rem" }}>
                            {task.text}
                        </label>
                    </div>
                ))}

                <Collapse in={showCompleted}>
                    <div className="mt-4">
                        <h2>Completed Tasks</h2>
                        <ul>
                            {completedTasks.map(task => (
                                <li key={task.id}>{task.text}</li>
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
