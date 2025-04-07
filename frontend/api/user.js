import { refreshToken } from "./auth";

export async function changeUsername(username, newUsername) {
    try {
        const access_token = await refreshToken();

        console.log(access_token);

        const response = await fetch(
            `${process.env.NEXT_PUBLIC_API_END_POINT}/user/${username}`,
            {
                method: "PUT",
                headers: {
                    accept: "application/json",
                    "Content-Type": "application/json",
                    authorization: `Bearer ${access_token}`,
                },
                body: JSON.stringify({
                    name: newUsername,
                }),
            }
        );

        // Error handling
        if (!response.ok) throw new Error("Failed to change username");

        return { status: "success" };
    } catch (error) {
        return { error: error.message };
    }
}
