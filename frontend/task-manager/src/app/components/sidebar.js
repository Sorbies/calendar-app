"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./sidebar.module.css";

export default function Sidebar() {
  // get the current pathname
  const pathname = usePathname();

  const [selectedCalendars, setSelectedCalendars] = useState([]);

  // function to handle toggle of calendar
  const handleToggleCalendar = (calendarName) => {
    if (selectedCalendars.includes(calendarName)) {
      setSelectedCalendars(
        selectedCalendars.filter((name) => name !== calendarName)
      );
    } else {
      setSelectedCalendars([...selectedCalendars, calendarName]);
    }
  };

  // function to handle dropdown menu options
  const handleMenuOption = (option, calendarName) => {
    // Placeholder function to handle menu options
    console.log(`Selected option "${option}" for calendar "${calendarName}"`);
  };

  // calendar dummy data
  const calendarNames = [
    "Calendar 1",
    "Calendar 2",
    "Calendar 3",
    "Calendar 4",
  ];

  return (
    <div className={styles.sidebar}>
      <ul className={`list-group ${styles.list}`}>
        <li className={`list-group-item ${styles.item}`}>
          <Link href="/" className={styles.link}>
            Home
          </Link>
        </li>
        <li className={`list-group-item ${styles.item}`}>
          <Link href="/calendar" className={styles.link}>
            Calendar
          </Link>
        </li>
        <li className={`list-group-item ${styles.item}`}>
          <Link href="/todo" className={styles.link}>
            To Do
          </Link>
        </li>
        <li className={`list-group-item ${styles.item}`}>
          <Link href="/clock" className={styles.link}>
            Notes
          </Link>
        </li>
      </ul>
      {pathname === "/calendar" && (
        <div className={styles.calendarListContainer}>
          <div className={styles.calendarList}>
            {calendarNames.map((name, index) => (
              <div key={index} className={styles.calendarItem}>
                <input
                  type="checkbox"
                  id={`calendar-${index}`}
                  checked={selectedCalendars.includes(name)}
                  onChange={() => handleToggleCalendar(name)}
                />
                <label
                  htmlFor={`calendar-${index}`}
                  className={styles.calendarLabel}
                >
                  {name}
                </label>
                <div className={styles.dropdownMenu}>
                  <i
                    className={`bi bi-three-dots-vertical ${styles.ellipsisButton}`}
                  />
                  <div className={styles.dropdownContent}>
                    <button
                      onClick={() => handleMenuOption("Change Name", name)}
                    >
                      Change Name
                    </button>
                    <button
                      onClick={() => handleMenuOption("Change Color", name)}
                    >
                      Change Color
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      {pathname === "/calendar" && (
        <div className={styles.calendarListContainer2}>
          <button className="btn btn-secondary">Add New Calendar</button>
        </div>
      )}
    </div>
  );
}
