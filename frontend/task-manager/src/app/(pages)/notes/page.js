import { verifyLogin } from "@/app/lib/authenticationStuff";
import 'bootstrap/dist/css/bootstrap.min.css';
import Notes from "./notes";

export default async function Page() {
    await verifyLogin();

    return (
        <>
            <div className="container mt-5">
                <h1>Notes Page</h1>
                <Notes />
            </div>
        </>
    );
}
