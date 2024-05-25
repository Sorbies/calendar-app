'use client'
import Image from "next/image";
import styles from "./Header.module.css";
import { Button } from "react-bootstrap";
import Link from "next/link";

import { deleteTokenCookie } from "../lib/authenticationStuff";


export default function Header({ showBurger = true }) {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>
        <Image src={"/squareLogo.png"} alt="Logo" width={40} height={40} />
      </div>
      <div className={styles.title}>IMPERIUM</div>

      {/* Burger menu */}
      {showBurger ?
        <div className={styles.buttons}>
          <Button variant="dark" data-bs-toggle="dropdown" aria-expanded="false">
            <i className="bi bi-list"></i>
          </Button>
          <ul className="dropdown-menu">
            <li><a className="dropdown-item" href="#">Dark Mode</a></li>
            <li><a className="dropdown-item" href="#">Account</a></li>
            <li><a className="dropdown-item" href="#">Settings</a></li>
            <li><hr className="dropdown-divider"></hr></li>
            <li><Link href="/signout" className="dropdown-item" onClick={async () => {await deleteTokenCookie();}}>Sign Out</Link></li>
          </ul>
        </div> : ""}
    </header>
  );
}
