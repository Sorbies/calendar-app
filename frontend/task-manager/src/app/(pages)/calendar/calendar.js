"use client";
import React, { useCallback, useState, useEffect } from "react";
import { Calendar as BigCalendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import "react-big-calendar/lib/css/react-big-calendar.css";

const localizer = momentLocalizer(moment);

// array storing all the events - temporary for testing
const events = [
  {
    start: moment("2024-05-07T05:30:00").toDate(),
    end: moment("2024-05-07T07:30:00").toDate(),
    title: "Databases Project Due",
  },
  {
    start: moment("2024-05-14T05:30:00").toDate(),
    end: moment("2024-05-14T07:30:00").toDate(),
    title: "Troeger Quiz #3",
    desc: "study, study, and study lolz",
  },
];


const handleSelectSlot = (setEvents) => ({ start, end }) => {
  const title = window.prompt("New Event name");
  if (title) {
    setEvents((prev) => [...prev, { start, end, title }]);
  }
};

const handleSelectEvent = (event) => {
  // First check if desc property exists - avoid displaying undefined
  const description = event.desc ? event.desc : "";
  window.alert(`${event.title}\n${description}`);
};


export default function Calendar({ events, calendars }) {
  // functional, but doesnt actually add the event yet
  // needs to be connected to the db of the users events

  function colorCalendarEvents(event, start, end, isSelected) {
    const relevantCalendar = calendars.filter(calendar => calendar['id'] == event['calendar_id'])[0];
    const relevantColor = relevantCalendar['color'];

    // Ensure the color is a valid CSS color string
    if (typeof relevantColor !== 'string') {
      console.error('Invalid color value:', relevantColor);
    }

    const style = {
      backgroundColor: relevantColor,
    }
    return { style: style };
  }

  return (
    <BigCalendar
      defaultView={"month"} //something to consider
      events={events}
      startAccessor="start"
      endAccessor="end"
      style={{ margin: "50px" }}
      selectableF
      onSelectEvent={handleSelectEvent}
      onSelectSlot={handleSelectSlot}
      eventPropGetter={colorCalendarEvents}
      localizer={localizer} />
  );
}