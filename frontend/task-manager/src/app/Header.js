'use client'
import Image from "next/image";
import Logo from "./squareLogo.png";
import styles from "./Header.module.css";
import { Button } from "react-bootstrap";
import 'bootstrap/dist/js/bootstrap.bundle';


export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>
         <Image src={Logo} alt="Logo" width={40} height={40}/>
      </div>
      <div className={styles.title}>IMPERIUM</div>
      {/* <div className={styles.buttons}>
        <Button variant="dark">
          <i className="bi bi-box-arrow-right"></i>
        </Button>
        <Button variant="dark">
          <i className="bi bi-brightness-high"></i>
        </Button>
        <Button variant="dark">
          <i className="bi bi-gear-wide-connected"></i>
        </Button>
        <Button variant="dark">
          <i className="bi bi-person-circle"></i>
        </Button>
      </div> */}

      <div className={styles.buttons}>
        <Button variant="dark" data-bs-toggle="dropdown" aria-expanded="false">
          <i className="bi bi-list"></i>
        </Button>
      <ul className="dropdown-menu">
        <li><a className="dropdown-item" href="#">Dark Mode</a></li>
        <li><a className="dropdown-item" href="#">Account</a></li>
        <li><a className="dropdown-item" href="#">Settings</a></li>
        <li><hr className="dropdown-divider"></hr></li>
        <li><a className="dropdown-item" href="#">Sign Out</a></li>
          {/* <Link href="/welcome" className={styles.link}></Link> */}
      </ul>
    </div>
    </header>
  );
}
