'use client'

import Link from "next/link";

import styles from "./sidebar.module.css"

export default function Sidebar() {
    return (
        <>
            <Link className={styles.block} href="/">Home</Link>
            <Link className={styles.block} href="/calendar">Calendar</Link>
            <Link className={styles.block} href="/todo">To Do</Link>
            <Link className={styles.block} href="/clock">Clock</Link>
        </>
    );
}