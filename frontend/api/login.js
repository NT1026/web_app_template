import { jwtDecode } from "jwt-decode";

export async function login(username, password) {
    try {
        const params = new URLSearchParams();
        params.append("grant_type", "");
        params.append("username", username);
        params.append("password", password);
        params.append("scope", "");
        params.append("client_id", "");
        params.append("client_secret", "");

        const response = await fetch(
            `${process.env.NEXT_PUBLIC_API_END_POINT}/auth/login`,
            {
                method: "POST",
                body: params,
                headers: {
                    accept: "application/json",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                credentials: "include",
            }
        );
        const data = await response.json();

        // Error handling
        if (!response.ok) throw new Error("Username or password is incorrect");
        if (!data.access_token) throw new Error("Access token not found");

        return jwtDecode(data.access_token);
    } catch (error) {
        return { error: error.message };
    }
}

export async function refreshToken() {
    try {
        const response = await fetch(
            `${process.env.NEXT_PUBLIC_API_END_POINT}/auth/refresh`,
            {
                method: "POST",
                headers: {
                    accept: "application/json",
                    "Content-Type": "application/json",
                },
                credentials: "include",
            }
        );
        const data = await response.json();

        // Error handling
        if (!response.ok) throw new Error("Failed to refresh access token");

        return data.access_token;
    } catch (error) {
        return { error: error.message };
    }
}
