import Head from 'next/head';
import styles from './styles.module.scss';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <Head>
        <title>Torchlite</title>
      </Head>
      <body id="root">
        <header className={styles.header}>Torchlite</header>
        {children}
        <footer className={styles.footer}>HathiTrust Research Center</footer>
      </body>
    </html>
  )
}
