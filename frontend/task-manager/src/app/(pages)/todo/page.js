import { verifyLogin } from "@/app/lib/authenticationStuff";

export default async function Page() {
    await verifyLogin();

    return (
        <>
            This is the TODO page
        </>
    );
}