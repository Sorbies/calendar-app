import { Inter } from "next/font/google";

import Sidebar from "./components/sidebar";

import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "OrgAN1ze",
  description: "Web Design Project by Team Lisan Al Gaib",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Sidebar/>
        {children}
      </body>
    </html>
  );
}
