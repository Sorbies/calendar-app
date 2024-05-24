"use client"

// Import statements
import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import styles from "./sidebar.module.css";
import { addTodo, getTodos } from "../lib/todoStuff";

export default function SidebarTodo() {
    // Get the current pathname to determine which section is active
    const pathname = usePathname();
    const router = useRouter();
    const searchParams = useSearchParams();

    const [todoLists, setTodoLists] = useState([]);
    const [selectedList, setSelectedList] = useState({});
    const [newListName, setNewListName] = useState("");
    const [renamingList, setRenamingList] = useState(null);
    const [newListNameTemp, setNewListNameTemp] = useState("");
    const [refreshTodoLists, setRefreshTodoLists] = useState(false);

    //get to-do lists from db, preselect an active one if applicable
    useEffect(() => {
        async function getTodoLists() {
            const todoLists = await getTodos();
            setTodoLists(todoLists);

            const filteredTodos = todoLists.filter((todo) => todo['id'] == searchParams.get('id'));
            setSelectedList(filteredTodos[0]);
        }
        getTodoLists();
    }, [refreshTodoLists]);

    //when the page is not a specific todo list, reset the selected list state
    useEffect(() => {
        if (pathname.endsWith('/todo')) setSelectedList({});
    }, [pathname]);

    function forceTodoListRefresh() {
        setRefreshTodoLists(prev => !prev);
    }

    // Handle options from the dropdown menu (change name, change color, delete)
    const handleMenuOption = (option, itemName) => {
        if (option === "Change Name") {
            setRenamingList(itemName);
            setNewListNameTemp(itemName);
        } else if (option === "Delete") { handleDeleteList(itemName); }
    };

    // Add a new to-do list if it doesn't already exist
    const handleAddList = async () => {
        const todoListNames = todoLists.map(todoObj => todoObj['name']);
        if (newListName.trim() !== "" && !todoListNames.includes(newListName.trim())) {
            const result = await addTodo(newListName);
            forceTodoListRefresh();

            setNewListName("");
            alert('New Todo list added!');
        }
    };

    // Select a to-do list
    const handleListSelection = (list) => {
        setSelectedList(list);
        router.push(`/todo?id=${list['id']}`)
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

    return (
        <>
            < div className={styles.todoListContainer}>
                {/* listing todo lists section */}
                <div className={styles.todoList}>
                    {todoLists.map((list, index) => (
                        <div key={index} className={styles.todoItem}>
                            <input
                                type="radio"
                                id={`todo-${index}`}
                                name="todoList"
                                checked={selectedList === list}
                                onChange={() => handleListSelection(list)} />
                            <label htmlFor={`todo-${index}`} className={styles.todoLabel}>
                                {list['name']}
                            </label>
                            <div className={styles.dropdownMenu}>
                                <i className={`bi bi-three-dots-vertical ${styles.ellipsisButton}`} />
                                <div className={styles.dropdownContent}>
                                    <button onClick={() => handleMenuOption("Change Name", list['name'])}>
                                        Change Name
                                    </button>
                                    <button onClick={() => handleMenuOption("Delete", list['name'])}>
                                        Delete
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                {/* renaming todo list widget */}
                {renamingList && (
                    <form onSubmit={handleRenameList} className={styles.renameForm}>
                        <input
                            type="text"
                            className="form-control"
                            value={newListNameTemp}
                            onChange={(e) => setNewListNameTemp(e.target.value)}
                            placeholder="Rename List" />
                        <button className="btn btn-primary mt-2" type="submit">
                            Rename
                        </button>
                        <button className="btn btn-secondary mt-2" onClick={() => setRenamingList(null)}>
                            Cancel
                        </button>
                    </form>
                )}

                {/* adding todo list widget */}
                <div className={styles.addListContainer}>
                    <input
                        type="text"
                        className="form-control"
                        value={newListName}
                        onChange={(e) => setNewListName(e.target.value)}
                        placeholder="New List Name" />
                    <button className="btn btn-primary mt-2" onClick={handleAddList}>
                        Add List
                    </button>
                </div>
            </div>


        </>
    );
}
