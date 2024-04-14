'use client'
import Image from "next/image";
import Logo from "./squareLogo.png";
import styles from "./Header.module.css";
import { Button } from "react-bootstrap";

export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>
         <Image src={Logo} alt="Logo" width={40} height={40} />
      </div>
      <div className={styles.title}>I M P E R I U M</div>
      <div className={styles.buttons}>
        <Button variant="dark">
          <i className="bi bi-brightness-high"></i> 
          {/* we should add functionality where when clicked, it changes icon to "bi bi-brightness-high-fill" */}
        </Button>
        <Button variant="dark">
          <i className="bi bi-gear-wide-connected"></i>
        </Button>
        <Button variant="dark">
          <i className="bi bi-person-circle"></i>
        </Button>
      </div>
    </header>
  );
}
