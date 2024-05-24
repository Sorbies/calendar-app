'use server'
import { cookies } from "next/headers";

export async function getTodos() {
    const response = await fetch('http://127.0.0.1:5000/todo_lists', {
        method: 'GET',
        headers: {
            'Authorization': cookies().get('token')['value'],
        },
    })

    const data = await response.json();
    return data;
}

export async function addTodo(todoName) {
    const rawFormData = {
        name: todoName,
    }

    const response = await fetch('http://127.0.0.1:5000/todo_lists', {
        method: 'POST',
        headers: {
            'Authorization': cookies().get('token')['value'],
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(rawFormData),
    })

    const data = await response.json();
    return data;

}