import Link from 'next/link';
import styles from './layout.module.css';
import React from 'react';
import Navbar from './navbar';

type Props = {
    children: React.ReactNode;
}

export default function Layout({ children }: Props) {
    return <div className={styles.container}>
             <header><p>Torchlite</p></header>
             {children}
             <footer><hr/><p>HathiTrust Research Center</p></footer>
    </div>;
}
