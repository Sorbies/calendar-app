'use server'
import { cookies } from "next/headers";

export async function getTasksOfTodo(todoId) {
    const response = await fetch(`http://127.0.0.1:5000/todo_lists/${todoId}/tasks`, {
        method: 'GET',
        headers: {
            'Authorization': cookies().get('token')['value'],
        },
    })

    const data = await response.json();
    //console.log(data);
    return data;
}

export async function addTask(formData) {
    const today = new Date();

    const rawFormData = {
        title: formData.get('taskTitle'),
        content: formData.get('taskDesc'),
        todo_list_id: formData.get('todoId'),
        start_date_time: today.toISOString(),
        end_date_time: formData.get('taskDueDate'),
    }

    const response = await fetch('http://127.0.0.1:5000/tasks', {
        method: 'POST',
        headers: {
            'Authorization': cookies().get('token')['value'],
            "Content-Type": "application/json",
        },
        body: JSON.stringify(rawFormData),
    })

    const data = await response.json();
    //console.log(data);
    return data;
}

export async function toggleTaskComplete(taskId) {
    //get the task info
    let response = await fetch(`http://127.0.0.1:5000/tasks/${taskId}`, {
        method: 'GET',
        headers: {
            'Authorization': cookies().get('token')['value'],
        },
    })

    const taskData = await response.json();
    taskData['completed'] = !taskData['completed']

    //update the completed value
    response = await fetch(`http://127.0.0.1:5000/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
            'Authorization': cookies().get('token')['value'],
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData),
    });

    const data = await response.json();
    //console.log(data);
    return data;
}