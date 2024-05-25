import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-icons/font/bootstrap-icons.css";


import "./globals.css";
import Head from 'next/head';
import BootstrapJS from "@/app/components/BootstrapJS";

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
      <body style={{ position: 'relative' }}>
        <BootstrapJS />
        {children}
      </body>
    </html>
  );
}