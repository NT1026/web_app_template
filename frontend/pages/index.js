import Link from "next/link";

import Layout from "../components/layout";

export default function Home() {
    return (
        <Layout>
            <p>Web Application Template</p>
            <Link href="/login">login</Link>
        </Layout>
    );
}
