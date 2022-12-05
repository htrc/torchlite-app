import Link from 'next/link';
import React from 'react';
import styles from './nav.module.scss';

type Props = {
    children: React.ReactNode;
};

export default function Navbar() {
    return <nav className={styles.navbar}>
             <ul>
               <li><Link href="/">Home</Link></li>
               <li><Link href="dashboard">Dashboard</Link></li>
               <li><Link href="/">Work Sets</Link></li>
               <li><Link href="/">Widgets</Link></li>
             </ul>
           </nav>
}
