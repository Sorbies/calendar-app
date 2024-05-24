import { fetchUsername, verifyLogin } from "@/app/lib/authenticationStuff";
import moment from 'moment';

// Array storing all the events - temporary for testing
const events = [
    {
        start: moment("2024-05-23T05:30:00").toDate(),
        end: moment("2024-05-23T07:30:00").toDate(),
        title: "Databases Project Due",
    },
    {
        start: moment("2024-05-23T05:30:00").toDate(),
        end: moment("2024-05-23T07:30:00").toDate(),
        title: "Troeger Quiz #3",
        desc: "study, study, and study lolz",
    },
    {
        start: moment("2024-05-24T10:00:00").toDate(),
        end: moment("2024-05-24T12:00:00").toDate(),
        title: "Meeting with Advisor",
    },
    {
        start: moment("2024-05-25T08:00:00").toDate(),
        end: moment("2024-05-25T09:00:00").toDate(),
        title: "Doctor's Appointment",
    },
];

// Array storing all the tasks - temporary for testing
const tasks = [
    {
        dueDate: moment("2024-05-23T12:00:00").toDate(),
        title: "Finish writing report",
    },
    {
        dueDate: moment("2024-05-23T15:00:00").toDate(),
        title: "Team meeting preparation",
    },
    {
        dueDate: moment("2024-05-24T09:00:00").toDate(),
        title: "Read research papers",
    },
    {
        dueDate: moment("2024-05-25T17:00:00").toDate(),
        title: "Submit project proposal",
    },
];

// Array storing all the notes - temporary for testing
const notes = [
    {
        date: moment("2024-05-23").toDate(),
        content: "Remember to check email for the meeting agenda.",
    },
    {
        date: moment("2024-05-23").toDate(),
        content: "Buy groceries on the way home.",
    },
];

export default async function Page() {
    await verifyLogin();

    const username = fetchUsername();
    const today = moment().startOf('day');

    const todaysEvents = events.filter(event => moment(event.start).isSame(today, 'day'));
    const upcomingEvents = events.filter(event => moment(event.start).isAfter(today, 'day'));
    
    const todaysTasks = tasks.filter(task => moment(task.dueDate).isSame(today, 'day'));
    const upcomingTasks = tasks.filter(task => moment(task.dueDate).isAfter(today, 'day'));

    const todaysNotes = notes.filter(note => moment(note.date).isSame(today, 'day'));

    return (
        <>
            <h1>Welcome, {username}!</h1>
            <p>We will put a dashboard here that has current events and todos, a quick notepad, and upcoming events and todos.</p>
            <h2 className="pt-3 text-center">Today's Dashboard</h2>
            <div className="container text-center mt-2">
                <div className="row align-items-start justify-content-between">
                    <div className="col border border-2 border-dark-subtle rounded m-2">
                        <h2 className="bi bi-calendar-event pt-2"></h2>
                        <h4 className="pt-1">Today's Events</h4>
                        <div className="text-start border-top border-dark-subtle pt-2">
                            <ul>
                                {todaysEvents.map((event, index) => (
                                    <li key={index}>{event.title} ({moment(event.start).format('hh:mm A')} - {moment(event.end).format('hh:mm A')})</li>
                                ))}
                            </ul>
                        </div>
                        <h4 className="pt-2 border-bottom border-dark-subtle pb-2">Upcoming Events</h4>
                        <div className="text-start pt-2">
                            <ul>
                                {upcomingEvents.map((event, index) => (
                                    <li key={index}>{event.title} ({moment(event.start).format('MMM D, hh:mm A')} - {moment(event.end).format('hh:mm A')})</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                    <div className="col border border-2 border-dark-subtle rounded m-2">
                        <div className="">
                        <h2 className="bi bi-list-check pt-2"></h2>
                            <h4 className="pt-1">Today's Tasks</h4>
                        </div>
                        <div className="text-start border-top border-dark-subtle pt-2">
                            <ul>
                                {todaysTasks.map((task, index) => (
                                    <li key={index}>{task.title} (Due by {moment(task.dueDate).format('hh:mm A')})</li>
                                ))}
                            </ul>
                        </div>
                        <h4 className="pt-2 border-bottom border-dark-subtle pb-2">Upcoming Tasks</h4>
                        <div className="text-start pt-2">
                            <ul>
                                {upcomingTasks.map((task, index) => (
                                    <li key={index}>{task.title} (Due by {moment(task.dueDate).format('MMM D, hh:mm A')})</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                    <div className="col border border-2 border-dark-subtle rounded m-2">
                        <div className="">
                            <h2 className="bi bi-pencil-square pt-2"></h2>
                            <h4 className="pt-1">My Notes</h4>
                        </div>
                        <div className="text-start border-top border-dark-subtle pt-2">
                            <ul>
                                {todaysNotes.map((note, index) => (
                                    <li key={index}>{note.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
