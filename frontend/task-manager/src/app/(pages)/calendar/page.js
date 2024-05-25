import moment from 'moment';
import EventAdder from "@/app/components/EventAdder";
import getRandomQuotes from '@/app/lib/getRandomQuotes.js';
import { verifyLogin } from '@/app/lib/authenticationStuff.js';
import { getCalendars } from '@/app/lib/calendarStuff.js';
import { getEventsFromSpecificCalendars } from '@/app/lib/eventStuff.js';
import Calendar from './calendar';

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


export default async function Page({ searchParams }) {
  await verifyLogin();

  //fetch all calendars
  const calendars = await getCalendars();

  //fetch all selected calendars (just their ids)
  const selectedString = searchParams['selected']
  let selected = [];
  if (selectedString != '') {
    selected = selectedString.split(',').map(idStr => parseInt(idStr));
  }

  //fetch all events from selected calendars
  const eventsFromSelectedCalendars = await getEventsFromSpecificCalendars(selected);

  //mutate the array a little bit for Big Calendar/leon's implementation
  eventsFromSelectedCalendars.forEach((event) => {
    //renaming some attributes
    event['title'] = event['name'];
    delete event['name'];
    event['start'] = event['start_date_time'];
    delete event['start_date_time'];
    event['end'] = event['end_date_time'];
    delete event['end_date_time'];
    event['desc'] = event['description'];
    delete event['description'];

    //convert date strings to date objects
    event['start'] = moment(event['start']).toDate();
    event['end'] = moment(event['end']).toDate();

  });

  //stuff for the random quote API
  const randomNumber = Math.floor(Math.random() * 50);
  const data = await getRandomQuotes();
  const randomQuote = data[randomNumber];

  return (
    <>
      <div style={{ textAlign: 'left' }}>
        <h4>{randomQuote["q"]}</h4>
        <h6>-{randomQuote["a"]}</h6>
        Inspirational quotes provided by <a href="https://zenquotes.io/" target="_blank">ZenQuotes API</a>
      </div>

      <div style={{ height: 500 }}>
        <Calendar
          calendars={calendars}
          events={eventsFromSelectedCalendars}
        />
      </div>

      <EventAdder calendars={calendars} />
    </>
  );
}