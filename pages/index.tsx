import Head from 'next/head';
import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/Home.module.css';
import React, { useState, useEffect } from 'react';


export default function Home() {
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('/time').then(res => res.json()).then(data => {
        setCurrentTime(data.time);
        });
    }, []);

  return (
    <div className={styles.container}>
      <Head>
        <title>HTRC Torchlite</title>
        <meta name="description" content="HathiTrust" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to Torchlite</h1>
        <p className={styles.description}>
          Current time is {currentTime}.
        </p>

          <p>Go to your <Link href="dashboard">Dashboard</Link></p>
      </main>
      <footer className={styles.footer}>
          HathiTrust Research Center
      </footer>
    </div>
  );
}
