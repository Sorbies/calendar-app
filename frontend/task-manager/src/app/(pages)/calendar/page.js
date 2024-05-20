import moment from 'moment';
import EventAdder from "@/app/components/EventAdder";
import getRandomQuotes from '@/app/lib/getRandomQuotes.js';
import Calendar, { handleSelectSlot, handleSelectEvent } from "./calendar.js";

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


export default async function Page() {

    const randomNumber = Math.floor(Math.random() * 50);
    const data = await getRandomQuotes();
    const randomQuote = data[randomNumber];

    return (
      <>
        <div style={{textAlign:'left'}}>
          <h4>{randomQuote["q"]}</h4>
          <h6>-{randomQuote["a"]}</h6>
          Inspirational quotes provided by <a href="https://zenquotes.io/" target="_blank">ZenQuotes API</a>
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

        <EventAdder/>
      </>
    );
  }