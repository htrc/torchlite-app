'use client';

import Head from 'next/head';
import Link from 'next/link';
import styles from './widget.module.scss';

interface WidgetProps {
    title: string;
    desc: string;
    img: string;
}


export default function Widget(props: WidgetProps){
  return(
      <div className={styles.widget}>
        <div className= {styles.widget__body}>
          <img src={props.img} className={styles.widget__image}/>
          <h2 className={styles.widget__title}>{props.title}</h2>
          <p className={styles.widget__description}>{props.desc}</p>
      </div>
        <button className={styles.widget__btn}>Inspect</button>
    </div>
  )
}
