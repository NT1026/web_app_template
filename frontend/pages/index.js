import Link from "next/link";

import Layout from "../components/layout";

export default function Home() {
    return (
        <Layout>
            <h1>{process.env.NEXT_PUBLIC_TITLE}</h1>
            <Link href="/login">login</Link>
            <br />
            <Link href="/refresh">Refresh TEST</Link>
            <br />
            <Link href="/changeUsername">Change Username</Link>
        </Layout>
    );
}
