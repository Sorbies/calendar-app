import Header from "../components/Header";

import "@/app/globals.css";

export default function Layout({ children }) {
    return (
        <>
            <Header showBurger={false}/>
            {children}
        </>
    )
}