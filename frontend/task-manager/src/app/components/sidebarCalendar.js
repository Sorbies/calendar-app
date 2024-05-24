'use client'

// Import statements
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./sidebar.module.css";

export default function SidebarCalendar() {
    // Get the current pathname to determine which section is active
    const pathname = usePathname();

    // State to manage selected calendars, to-do lists, selected list, and temporary states for new and renaming lists
    const [selectedCalendars, setSelectedCalendars] = useState([]);
    const [calendarNames, setCalendarNames] = useState([
        "Calendar 1",
        "Calendar 2",
        "Calendar 3",
        "Calendar 4",
    ]);
    const [newCalendarName, setNewCalendarName] = useState("");
    const [renamingCalendar, setRenamingCalendar] = useState(null);
    const [newCalendarNameTemp, setNewCalendarNameTemp] = useState("");

    // Toggle calendar selection in the list
    const handleToggleCalendar = (calendarName) => {
        if (selectedCalendars.includes(calendarName)) {
            setSelectedCalendars(
                selectedCalendars.filter((name) => name !== calendarName)
            );
        } else {
            setSelectedCalendars([...selectedCalendars, calendarName]);
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
        setCalendarNames(calendarNames.filter((name) => name !== calendarName));
        if (selectedCalendars.includes(calendarName)) {
            setSelectedCalendars(
                selectedCalendars.filter((name) => name !== calendarName)
            );
        }
    };


    // Add a new calendar if it doesn't already exist
    const handleAddCalendar = () => {
        if (
            newCalendarName.trim() !== "" &&
            !calendarNames.includes(newCalendarName.trim())
        ) {
            setCalendarNames([...calendarNames, newCalendarName.trim()]);
            setNewCalendarName("");
        }
    };

    // Rename a calendar
    const handleRenameCalendar = (e) => {
        e.preventDefault();
        const updatedCalendars = calendarNames.map((name) =>
            name === renamingCalendar ? newCalendarNameTemp : name
        );
        setCalendarNames(updatedCalendars);
        setRenamingCalendar(null);
    };

    return (
        <>
            {/* listing  calendars section */}
            <div className={styles.calendarListContainer}>
                <div className={styles.calendarList}>
                    {calendarNames.map((name, index) => (
                        <div key={index} className={styles.calendarItem}>
                            <input
                                type="checkbox"
                                id={`calendar-${index}`}
                                checked={selectedCalendars.includes(name)}
                                onChange={() => handleToggleCalendar(name)} />
                            <label htmlFor={`calendar-${index}`} className={styles.calendarLabel}>
                                {name}
                            </label>
                            <div className={styles.dropdownMenu}>
                                <i className={`bi bi-three-dots-vertical ${styles.ellipsisButton}`} />
                                <div className={styles.dropdownContent}>
                                    <button onClick={() => handleMenuOption("Change Name", name)}>
                                        Change Name
                                    </button>
                                    <button
                                        onClick={() => handleMenuOption("Change Color", name)}>
                                        Change Color
                                    </button>
                                    <button
                                        onClick={() => handleMenuOption("Delete", name)}>
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