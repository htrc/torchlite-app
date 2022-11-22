import Head from 'next/head';
import Link from 'next/link';
import styles from './styles.module.scss';

export default function Home() {

  return (
      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to Torchlite</h1>

          <p>Go to your <Link href="dashboard">Dashboard</Link></p>
      </main>
  );
}
