import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import Sidebar from "./components/Sidebar";

import "./globals.css";
import Header from "./Header.js";
import Head from 'next/head';
import BootstrapJS from "./BootstrapJS";

export const metadata = {
  title: "IMPERIUM",
  description: "Organization tool with calander, notes, task lists, and clock.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <Head>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap" />
      </Head>
      <body>
        <BootstrapJS />
        <Header />
        <Sidebar />
        {children}
      </body>
    </html>
  );
}
