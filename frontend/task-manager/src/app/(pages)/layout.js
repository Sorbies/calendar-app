import Sidebar from "../components/sidebar"
import Header from "../components/Header";

import "@/app/globals.css";

export default function Layout({ children }) {
    return (
        <>
            <Header/>
            <div style={{ position: 'absolute', top: '-28px', left: 0 }}>
                <Sidebar />
            </div>
            <div style={{ marginLeft: '215px', paddingTop: '25px', paddingRight: '20px' }}>{children}</div>
        </>
    )
}