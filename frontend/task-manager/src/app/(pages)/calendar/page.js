'use client'
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';

const localizer = momentLocalizer(moment);

export default function Page() {
    // Dummy event data
    const events = [
      {
        title: 'Event 1',
        start: new Date(2024, 3, 20), // April 20, 2024
        end: new Date(2024, 3, 22), // April 22, 2024
      },
      {
        title: 'Event 2',
        start: new Date(2024, 3, 25), // April 25, 2024
        end: new Date(2024, 3, 27), // April 27, 2024
      },
    ];
  
    return (
      <>
        <div style={{textAlign:'left'}}>
            <h5>This is where our insperational quote goes</h5>
        </div>

        <div style={{ height: 500 }}>
          <Calendar
            localizer={localizer}
            events={events}
            startAccessor="start"
            endAccessor="end"
            style={{ margin: '50px' }}
          />
        </div>
      </>
    );
  }