'use server'
import { cookies } from "next/headers";

export async function getEventsFromSpecificCalendars(calIds) {
    let result = []

    //returns an array of promises
    const promises = calIds.map(async (calId) => {
        const response = await fetch(`http://127.0.0.1:5000/calendars/${calId}/events`, {
            method: 'GET',
            headers: {
                'Authorization': cookies().get('token')['value'],
            }
        })

        const data = await response.json();
        return data;
    })

    //wait for promises to resolve
    result = await Promise.all(promises);

    //before: list of sublists, where each sublist is a list of a calendar's events
    //after: all events from all selected calendars in one list
    result = result.flat();

    //remove elements that were actually just errors
    result = result.filter(element => !('error' in element));

    return result
}

export async function addEvent(formData) {
    const rawFormData = {
        calendar_id: formData.get('calendarId'),
        name: formData.get('eventTitle'),
        description: formData.get('eventDesc'),
        start_date_time: formData.get('eventStartDate'),
        end_date_time: formData.get('eventEndDate'),
    }

    const response = await fetch('http://127.0.0.1:5000/events', {
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