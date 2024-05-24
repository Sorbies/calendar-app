'use server'
import { cookies } from "next/headers"

export async function getCalendars() {
    const response = await fetch('http://127.0.0.1:5000/calendars', {
        method: 'GET',
        headers: {
            'Authorization': cookies().get('token')['value'],
        },
    })

    const data = await response.json();
    return data;
}

export async function addCalendar(calendarName, calendarColor) {
    const rawFormData = {
        name: calendarName,
        color: calendarColor,
    }

    const response = await fetch('http://127.0.0.1:5000/calendars', {
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