"use client";
import moment from "moment";
import Calendar from "./calendar.js";
import React, { useCallback, useState } from 'react'

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

export default function Page() {
  
  // functional, but doesnt actually add the event yet
  // needs to be connected to the db of the users events
  const [myEvents, setEvents] = useState(events)

  const handleSelectSlot = useCallback(
    ({ start, end }) => {
      const title = window.prompt('New Event name')
      if (title) {
        setEvents((prev) => [...prev, { start, end, title }])
      }
    },
    [setEvents]
  )

  const handleSelectEvent = useCallback(
    (event) => {
      // first check if desc property exists - avoid displaying undefined
      const description = event.desc ? event.desc : '';
      window.alert(`${event.title}\n${description}`);
    },
    []
  );

  return (
    <>
      <div style={{ textAlign: "left" }}>
        <h5>This is where our insperational quote goes</h5>
      </div>

      <div style={{ height: 500 }}>
        <Calendar
          defaultView={"week"} //something to consider
          events={events}
          startAccessor="start"
          endAccessor="end"
          style={{ margin: "50px" }}
          selectable
          onSelectEvent={handleSelectEvent}
          onSelectSlot={handleSelectSlot}
        />
      </div>
    </>
  );
}
