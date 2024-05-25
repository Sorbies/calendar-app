import Todo from "./todo";

import { verifyLogin } from "@/app/lib/authenticationStuff";

export default async function Page() {
    await verifyLogin();

    return (
        <>
            <Todo/>
        </>
    );
}