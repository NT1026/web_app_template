import Head from "next/head";
import Link from "next/link";

import styles from "../styles/layout.module.css";

const title = "Web Application Template";

export default function Layout({ children, returnBack }) {
    return (
        <div className={styles.layout}>
            <Head>
                <meta charSet="utf-8" />
                <meta
                    name="viewport"
                    content="width=device-width, initial-scale=1"
                />
                <title>{title}</title>
            </Head>
            <main>{children}</main>
            {returnBack && (
                <Link href="/" className="home">
                    Home
                </Link>
            )}
        </div>
    );
}
