import { useState } from "react";

import Layout from "../components/layout";
import { changeUsername } from "../api/user";

export default function ChangeUsername() {
    const [username, setUsername] = useState("");
    const [newUsername, setNewUsername] = useState("");
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleChangeUsername = async (username, newUsername) => {
        setResponse(null);
        setError(null);
        setLoading(true);

        const res = await changeUsername(username, newUsername);
        setLoading(false);
        if (res.error) {
            setError(res.error);
        } else {
            setResponse(res);
        }
    };

    return (
        <Layout returnBack>
            <div>
                <h1>Change Username</h1>
                <form
                    onSubmit={(e) => {
                        e.preventDefault();
                        handleChangeUsername(username, newUsername);
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
                        type="text"
                        placeholder="new username"
                        value={newUsername}
                        onChange={(e) => setNewUsername(e.target.value)}
                        required
                    />
                    <button type="submit" disabled={loading}>
                        {loading ? "Changing Username..." : "Change"}
                    </button>
                </form>
                {error && <p style={{ color: "red" }}>{error}</p>}
                {response && <p>Your username changes successfully!</p>}
            </div>
        </Layout>
    );
}
