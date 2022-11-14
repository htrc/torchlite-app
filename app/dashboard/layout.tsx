import styles from './styles.module.css';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode,
}) {
    return <main className={styles.container}>
             <header>Dashboard</header>
             {children}
           </main>
}
