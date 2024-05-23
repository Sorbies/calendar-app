"use client";

// Import statements
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./sidebar.module.css";

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
                      onClick={() =>
                        handleMenuOption("Change Name", name, "calendar")
                      }
                    >
                      Change Name
                    </button>
                    <button
                      onClick={() =>
                        handleMenuOption("Change Color", name, "calendar")
                      }
                    >
                      Change Color
                    </button>
                    <button
                      onClick={() =>
                        handleMenuOption("Delete", name, "calendar")
                      }
                    >
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
          {renamingCalendar && (
            <form onSubmit={handleRenameCalendar} className={styles.renameForm}>
              <input
                type="text"
                className="form-control"
                value={newCalendarNameTemp}
                onChange={(e) => setNewCalendarNameTemp(e.target.value)}
                placeholder="Rename Calendar"
              />
              <button className="btn btn-primary mt-2" type="submit">
                Rename
              </button>
              <button
                className="btn btn-secondary mt-2"
                onClick={() => setRenamingCalendar(null)}
              >
                Cancel
              </button>
            </form>
          )}
          <div className={styles.addListContainer}>
            <input
              type="text"
              className="form-control"
              value={newCalendarName}
              onChange={(e) => setNewCalendarName(e.target.value)}
              placeholder="New Calendar Name"
            />
            <button
              className="btn btn-primary mt-2"
              onClick={handleAddCalendar}
            >
              Add Calendar
            </button>
          </div>
        </div>
      )}
      {pathname === "/todo" && (
        <div className={styles.todoListContainer}>
          <div className={styles.todoList}>
            {todoLists.map((list, index) => (
              <div key={index} className={styles.todoItem}>
                <input
                  type="radio"
                  id={`todo-${index}`}
                  name="todoList"
                  checked={selectedList === list}
                  onChange={() => handleListSelection(list)}
                />
                <label htmlFor={`todo-${index}`} className={styles.todoLabel}>
                  {list}
                </label>
                <div className={styles.dropdownMenu}>
                  <i
                    className={`bi bi-three-dots-vertical ${styles.ellipsisButton}`}
                  />
                  <div className={styles.dropdownContent}>
                    <button
                      onClick={() =>
                        handleMenuOption("Change Name", list, "list")
                      }
                    >
                      Change Name
                    </button>
                    <button
                      onClick={() => handleMenuOption("Delete", list, "list")}
                    >
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
          {renamingList && (
            <form onSubmit={handleRenameList} className={styles.renameForm}>
              <input
                type="text"
                className="form-control"
                value={newListNameTemp}
                onChange={(e) => setNewListNameTemp(e.target.value)}
                placeholder="Rename List"
              />
              <button className="btn btn-primary mt-2" type="submit">
                Rename
              </button>
              <button
                className="btn btn-secondary mt-2"
                onClick={() => setRenamingList(null)}
              >
                Cancel
              </button>
            </form>
          )}
          <div className={styles.addListContainer}>
            <input
              type="text"
              className="form-control"
              value={newListName}
              onChange={(e) => setNewListName(e.target.value)}
              placeholder="New List Name"
            />
            <button className="btn btn-primary mt-2" onClick={handleAddList}>
              Add List
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
