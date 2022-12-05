import Link from 'next/link';
import React, { PropsWithRef } from 'react';
import styles from './pane.module.scss';

type Props = {
    children: React.ReactNode;
};

export default function Pane({children}: Props) {
    return <div className={styles.pane}>
             { children }
           </div>
}
