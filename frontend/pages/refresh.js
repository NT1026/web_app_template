import { useState } from "react";
import { jwtDecode } from "jwt-decode";

import Layout from "../components/layout";
import { refreshToken } from "../api/login";

export default function Login() {
    const [user, setUser] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleRefresh = async () => {
        setUser(null);
        setError(null);
        setLoading(true);

        const access_token = await refreshToken();
        const user = jwtDecode(access_token);
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
                <h1>Refresh</h1>
                <button onClick={handleRefresh}>
                    {loading ? "Loading..." : "Refresh TEST"}
                </button>
                {error && <p style={{ color: "red" }}>{error}</p>}
                {user && (
                    <p>
                        Congratulations, {user.uid}! You have successfully
                        refreshed your tokens.
                    </p>
                )}
            </div>
        </Layout>
    );
}
