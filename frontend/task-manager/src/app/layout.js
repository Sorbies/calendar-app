import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import Sidebar from "./components/sidebar";

import "./globals.css";
import Header from "./Header.js";
import Head from 'next/head';

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

      <div style={{ position: 'relative' }}>
        <Header />
        <div style={{ position: 'absolute', top: '-28px', left: 0 }}>
          <Sidebar />
        </div>
        <div style={{ marginLeft: '215px', paddingTop: '25px', paddingRight: '20px' }}>{children}</div>
      </div>
    </html>
  );
}