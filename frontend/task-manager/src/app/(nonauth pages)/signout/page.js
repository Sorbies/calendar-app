import SignUp from "@/app/components/SignUp";

export default function Page() {

  return (
    <>
      <div className="mt-3">
        <h1 style={{textAlign: "center"}}>Welcome to Imperium!</h1>
        <SignUp initShow={true} initMsg="You have been signed out." initStyle="success"/>
      </div>
    </>
  );
}
