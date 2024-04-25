'use client'

import Link from "next/link";

import styles from "./sidebar.module.css"

export default function Sidebar() {
    return (
        <div className={styles.sidebar}>
            <ul className={`list-group ${styles.list}`}>
                <li className={`list-group-item ${styles.item}`}>
                    <Link href="/" className={styles.link}>Home</Link>
                </li>
                <li className={`list-group-item ${styles.item}`}>
                    <Link href="/calendar" className={styles.link}>Calendar</Link>
                </li>
                <li className={`list-group-item ${styles.item}`}>
                    <Link href="/todo" className={styles.link}>To Do</Link>
                </li>
                <li className={`list-group-item ${styles.item}`}>
                    <Link href="/clock" className={styles.link}>Clock</Link>
                </li>
            </ul>
        </div>
    );
}