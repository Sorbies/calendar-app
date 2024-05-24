"use client"

// Import statements
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./sidebar.module.css";
import SidebarCalendar from "./sidebarCalendar";
import SidebarTodo from "./sidebarTodo";

export default function Sidebar() {
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

  const [todoLists, setTodoLists] = useState(["Default List"]);
  const [selectedList, setSelectedList] = useState("Default List");
  const [newListName, setNewListName] = useState("");
  const [renamingList, setRenamingList] = useState(null);
  const [newListNameTemp, setNewListNameTemp] = useState("");

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
  const handleMenuOption = (option, itemName, type) => {
    if (option === "Change Name") {
      if (type === "calendar") {
        setRenamingCalendar(itemName);
        setNewCalendarNameTemp(itemName);
      } else {
        setRenamingList(itemName);
        setNewListNameTemp(itemName);
      }
    } else if (option === "Delete") {
      if (type === "list") {
        handleDeleteList(itemName);
      } else if (type === "calendar") {
        handleDeleteCalendar(itemName);
      }
    }
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

  // Add a new to-do list if it doesn't already exist
  const handleAddList = () => {
    if (newListName.trim() !== "" && !todoLists.includes(newListName.trim())) {
      setTodoLists([...todoLists, newListName.trim()]);
      setNewListName("");
    }
  };

  // Select a to-do list
  const handleListSelection = (listName) => {
    setSelectedList(listName);
  };

  // Delete a to-do list
  const handleDeleteList = (listName) => {
    setTodoLists(todoLists.filter((list) => list !== listName));
    if (selectedList === listName) {
      setSelectedList(todoLists[0] || "");
    }
  };

  // Rename a to-do list
  const handleRenameList = (e) => {
    e.preventDefault();
    const updatedLists = todoLists.map((list) =>
      list === renamingList ? newListNameTemp : list
    );
    setTodoLists(updatedLists);
    setRenamingList(null);
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
    <div className={styles.sidebar}>
      <ul className={`list-group ${styles.list}`}>
        <li className={`list-group-item ${styles.item}`}>
          <Link href="/home" className={styles.link}>
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
          <Link href="/notes" className={styles.link}>
            Notes
          </Link>
        </li>
      </ul>

      {/* listing  calendars section */}
      {pathname.includes("/calendar") && (<SidebarCalendar/>)}


      {pathname.includes("/todo") && (<SidebarTodo/>)}
    </div >
  );
}
