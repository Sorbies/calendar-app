'use client'
import moment from 'moment';
import Calendar from "./calendar.js";
import EventAdder from "@/app/components/EventAdder";

// array storing all the events
const events = [
  {
    start:moment('2024-05-07T05:30:00').toDate(),
    end:moment('2024-05-07T07:30:00').toDate(),
    title: "Databases Project Due",
  },
  {
    start:moment('2024-05-09T05:30:00').toDate(),
    end:moment('2024-05-09T07:30:00').toDate(),
    title: "Troeger Quiz #3",
  },
]

export default function Page() {
    return (
      <>
        <div style={{textAlign:'left'}}>
            <h5>This is where our insperational quote goes</h5>
        </div>

        <div style={{ height: 500 }}>
          <Calendar
            events={events}
            startAccessor="start"
            endAccessor="end"
            style={{ margin: '50px' }}
          />
        </div>

        <EventAdder/>
      </>
    );
  }