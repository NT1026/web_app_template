import { jwtDecode } from "jwt-decode";
import { useState } from "react";
import Cookie from "js-cookie";

import Layout from "../components/layout";

export async function login_api(username, password) {
    const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_END_POINT}/auth/login`,
        {
            method: "POST",
            body:
                "grant_type=&username=" +
                username +
                "&password=" +
                password +
                "&scope=&client_id=&client_secret=",
            headers: {
                "Content-Type": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }
    );
    const data = await response.json();
    if (data.access_token) {
        Cookie.set("access_token", data.access_token, { expires: 7 });
    }
    return jwtDecode(data.access_token);
}

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [user, setUser] = useState(null);

    const handleLogin = async (username, password) => {
        const user = await login_api(username, password);
        setUser(user);
        console.log(user);
    };

    return (
        <Layout returnBack>
            <div>
                <h1>Login</h1>
                <form
                    onSubmit={(e) => {
                        e.preventDefault();
                        handleLogin(username, password);
                    }}
                >
                    <input
                        type="text"
                        placeholder="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <input
                        type="password"
                        placeholder="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <button type="submit">Login</button>
                </form>
            </div>
        </Layout>
    );
}
