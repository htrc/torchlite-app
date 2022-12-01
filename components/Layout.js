import styles from './layout.module.css';

export default function Layout({ children }) {
    return <div className={styles.container}>
        <header><p>Torchlite</p></header>
        {children}
        <footer><hr/><p>HathiTrust Research Center</p></footer>
    </div>;
}

