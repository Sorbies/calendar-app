import { redirect } from "next/navigation";

export default function Home() {
  redirect("/home");

  return "You shouldn't see this!";
}
