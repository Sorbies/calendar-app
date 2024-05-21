import { fetchUsername, verifyLogin } from "@/app/lib/authenticationStuff"

export default async function Page() {
    await verifyLogin();

    const username = fetchUsername();

    return (
        <>
            <h1>Welcome, {username}!</h1>
            We will put a dashboard here that has current events and todos, a quick notepad, and upcoming events and todos.
        </>
    )
}