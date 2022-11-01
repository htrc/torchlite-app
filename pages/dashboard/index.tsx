import Head from 'next/head';
import Image from 'next/image';
import styles from '../../styles/Dashboard.module.css';
import Link from 'next/link';

export default function Dashboard() {
    return (
        <>
          <Head>
            <title>HTRC Torchlite Dashboard</title>
            <meta name="description" content="HathiTrust" />
            <link rel="icon" href="/favicon.ico" />
          </Head>

          <header>
            <h1>Dashboard</h1>
          </header>

          <main>
            The dashboard
          </main>
          <footer className={styles.footer}>
            HathiTrust Research Center
          </footer>
        </>
    );
}
