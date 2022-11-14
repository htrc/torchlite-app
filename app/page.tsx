import Head from 'next/head';
import Link from 'next/link';
import styles from '../styles/Home.module.css';


export default function Home() {

  return (
    <div className={styles.container}>
      <Head>
        <title>HTRC Torchlite</title>
        <meta name="description" content="HathiTrust" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to Torchlite</h1>

          <p>Go to your <Link href="dashboard">Dashboard</Link></p>
      </main>
      <footer className={styles.footer}>
          HathiTrust Research Center
      </footer>
    </div>
  );
}
