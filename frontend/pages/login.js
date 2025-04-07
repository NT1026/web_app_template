import { useState } from "react";

import Layout from "../components/layout";
import { login } from "../api/auth";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [user, setUser] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleLogin = async (username, password) => {
        setUser(null);
        setError(null);
        setLoading(true);

        const user = await login(username, password);
        setLoading(false);

        if (user.error) {
            setError(user.error);
        } else {
            setUser(user);
        }
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
                        required
                    />
                    <input
                        type="password"
                        placeholder="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <button type="submit" disabled={loading}>
                        {loading ? "Logging in..." : "Login"}
                    </button>
                </form>
                {error && <p style={{ color: "red" }}>{error}</p>}
                {user && <p>Welcome, {user.name}!</p>}

                <form
                    onSubmit={async (e) => {
                        e.preventDefault();
                        const response = await fetch(
                            `${process.env.NEXT_PUBLIC_API_END_POINT}/auth/logout`,
                            {
                                method: "POST",
                                headers: {
                                    accept: "application/json",
                                    "Content-Type": "application/json",
                                },
                                credentials: "include",
                            }
                        );
                        if (response.ok) {
                            setUser(null);
                            setUsername("");
                            setPassword("");
                        } else {
                            setError("Failed to logout");
                        }
                    }}
                >
                    <button type="submit" disabled={!user}>
                        Logout
                    </button>
                </form>
            </div>
        </Layout>
    );
}
