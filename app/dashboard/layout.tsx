import styles from './styles.module.scss';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode,
}) {
    return <main className="dashboard">
             <header>Dashboard</header>
             {children}
           </main>
}
