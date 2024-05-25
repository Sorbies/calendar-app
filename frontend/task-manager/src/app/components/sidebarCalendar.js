'use client'

// Import statements
import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import styles from "./sidebar.module.css";
import { addCalendar, getCalendars } from "../lib/calendarStuff";

export default function SidebarCalendar() {
    // Get the current pathname to determine which section is active
    const pathname = usePathname();
    const router = useRouter();
    const searchParams = useSearchParams();

    // State to manage selected calendars, to-do lists, selected list, and temporary states for new and renaming lists
    const [selectedCalendars, setSelectedCalendars] = useState([]);
    const [calendars, setCalendars] = useState([]);
    const [newCalendarName, setNewCalendarName] = useState("");
    const [newCalendarColor, setNewCalendarColor] = useState('#000000');
    const [renamingCalendar, setRenamingCalendar] = useState(null);
    const [newCalendarNameTemp, setNewCalendarNameTemp] = useState("");
    const [refreshCalendars, setRefreshCalendars] = useState(false);

    //get calendars from db, preselect active ones if applicable
    useEffect(() => {
        async function getCalendarsFromDB() {
            const calendars = await getCalendars();
            setCalendars(calendars);

            const selected = searchParams.get('selected');

            if (selected != null) {
                const selectedList = selected.split(',').map(ele => Number(ele));
                const matchingCalendars = calendars.filter(cal => selectedList.includes(cal['id']));
                setSelectedCalendars(matchingCalendars);
            }
        }
        getCalendarsFromDB();
    }, [refreshCalendars]);

    //whenever the selected calendars change, update the query params
    useEffect(() => {
        //update query params to match
        const selectedIds = selectedCalendars.map((cal) => cal['id']);
        const selectedIdsString = selectedIds.sort().join();

        router.push(`/calendar?selected=${selectedIdsString}`);
    }, [selectedCalendars])

    function forceCalendarsRefresh() {
        setRefreshCalendars(prev => !prev);
    }

    // Toggle calendar selection in the list
    const handleToggleCalendar = (calendar) => {
        if (selectedCalendars.includes(calendar)) {
            setSelectedCalendars(selectedCalendars.filter((cal) => cal !== calendar));
        } else {
            setSelectedCalendars([...selectedCalendars, calendar]);
        }
    };

    // Handle options from the dropdown menu (change name, change color, delete)
    const handleMenuOption = (option, itemName) => {
        if (option === "Change Name") {
            setRenamingCalendar(itemName);
            setNewCalendarNameTemp(itemName);
        } else if (option === "Delete") { handleDeleteCalendar(itemName); }
    };

    // Delete a calendar
    const handleDeleteCalendar = (calendarName) => {
        setCalendars(calendars.filter((calendar) => calendar['name'] !== calendarName));
        if (selectedCalendars.includes(calendarName)) {
            setSelectedCalendars(selectedCalendars.filter((name) => name !== calendarName));
        }
    };


    // Add a new calendar if it doesn't already exist
    const handleAddCalendar = async () => {
        const calendarNames = calendars.map((calendar) => calendar['name']);
        if (newCalendarName.trim() !== "" && !calendarNames.includes(newCalendarName.trim())) {
            const result = await addCalendar(newCalendarName, newCalendarColor);
            forceCalendarsRefresh();

            setNewCalendarName("");
            alert('New calendar added!');
        }
    };

    // Rename a calendar
    const handleRenameCalendar = (e) => {
        e.preventDefault();
        const updatedCalendars = calendars.map((calendar) =>
            calendar['name'] === renamingCalendar ? newCalendarNameTemp : calendar['name']
        );
        setCalendars(updatedCalendars);
        setRenamingCalendar(null);
    };

    return (
        <>
            <div className={styles.calendarListContainer}>
                {/* listing  calendars section */}
                <div className={styles.calendarList}>
                    {calendars.map((calendar, index) => (
                        <div key={index} className={styles.calendarItem}>
                            <input
                                type="checkbox"
                                id={`calendar-${index}`}
                                checked={selectedCalendars.includes(calendar)}
                                onChange={() => handleToggleCalendar(calendar)} />
                            <label htmlFor={`calendar-${index}`} className={styles.calendarLabel}>
                                <span style={{ color: calendar['color'] }}> &#9608; </span>
                                {calendar['name']}
                            </label>
                            <div className={styles.dropdownMenu}>
                                <i className={`bi bi-three-dots-vertical ${styles.ellipsisButton}`} />
                                <div className={styles.dropdownContent}>
                                    <button onClick={() => handleMenuOption("Change Name", calendar['name'])}>
                                        Change Name
                                    </button>
                                    <button
                                        onClick={() => handleMenuOption("Change Color", calendar['name'])}>
                                        Change Color
                                    </button>
                                    <button
                                        onClick={() => handleMenuOption("Delete", calendar['name'])}>
                                        Delete
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                {/* renaming calendar widget */}
                {renamingCalendar && (
                    <form onSubmit={handleRenameCalendar} className={styles.renameForm}>
                        <input
                            type="text"
                            className="form-control"
                            value={newCalendarNameTemp}
                            onChange={(e) => setNewCalendarNameTemp(e.target.value)}
                            placeholder="Rename Calendar" />
                        <button className="btn btn-primary mt-2" type="submit">
                            Rename
                        </button>
                        <button className="btn btn-secondary mt-2" onClick={() => setRenamingCalendar(null)}>
                            Cancel
                        </button>
                    </form>
                )}

                {/* Adding a new calendar widget */}
                <div className={styles.addListContainer}>
                    <input
                        type="color"
                        className="form-control"
                        value={newCalendarColor}
                        onChange={(e) => setNewCalendarColor(e.target.value)} />
                    <input
                        type="text"
                        className="form-control"
                        value={newCalendarName}
                        onChange={(e) => setNewCalendarName(e.target.value)}
                        placeholder="New Calendar Name" />
                    <button
                        className="btn btn-primary mt-2"
                        onClick={handleAddCalendar}>
                        Add Calendar
                    </button>
                </div>
            </div>
        </>
    );

}