'use server'
import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export async function sendRegisterData(formData) {
    const rawFormData = {
        username: formData.get('username'),
        email: formData.get('username'),
        password: formData.get('password'),
    }

    console.log(rawFormData);

    const response = await fetch("http://127.0.0.1:5000/auth/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(rawFormData),
    });

    const data = await response.json();
    console.log(data);

    if ('error' in data) {
        console.log("Error:", data['error']);
        return null;
    } else {
        console.log("Success:", data['message']);
        return data['user_id'];
    }
}

export async function sendLoginData(formData) {
    const rawFormData = {
        username: formData.get('username'),
        password: formData.get('password'),
    }

    console.log(rawFormData);

    const response = await fetch("http://127.0.0.1:5000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(rawFormData),
    });

    const data = await response.json();
    console.log(data);

    if ('error' in data) {
        console.log("Error:", data['error']);
        return null;
    } else {
        console.log("Success:", data['message']);
        return data['token'];
    }
}

export async function validateToken() {
    const response = await fetch("http://127.0.0.1:5000/auth/secured_route", {
        method: "GET",
        headers: {
            "Authorization": cookies().get('token')["value"],
        },
    })

    const data = await response.json();

    return data["message"].includes("Congratulations!");
}

export async function verifyLogin() {
    if (!cookies().has('token')) {redirect("/login-error");}
    const validation = await validateToken();
    if (!cookies(validation)) {redirect("/login-error");} 
}

export async function setTokenCookie(token) {
    cookies().set('token', `Bearer ${token}`, {sameSite: "strict"});
}

export async function deleteTokenCookie() {
    cookies().delete('token');
}

export async function fetchUsername() {
    const response = await fetch("http://127.0.0.1:5000/auth/secured_route", {
        method: "GET",
        headers: {
            "Authorization": cookies().get('token')['value'],
        },
    })

    const data = await response.json();

    if (data["message"].includes("Congratulations!")) {
        return data["user"];
    } else {
        return null;
    }
}