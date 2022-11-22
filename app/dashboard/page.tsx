import Head from 'next/head';
import Link from 'next/link';
import styles from './styles.module.scss';


function WorkSetPane() {
    return (
        <section className={styles.workset_pane}>
          <header>
          <h2>Worksets</h2>
          </header>
          <p className="slug">The workset pane</p>
        </section>
    );
};

function WidgetSelectorPane() {
    return (
        <section className={styles.selector_pane}>
            <header>
                <h2>Widgets</h2>
            </header>
            <p className="slug">The widget selector pane</p>
        </section>
    );
};

function DataFilterPane(){
    return (
        <section className={styles.data_filter_pane}>
            <header>
                <h2>Data Filters</h2>
            </header>
            <p className="slug">The data filter pane</p>
        </section>
    );
};

function DataCleanPane(){
    return (
        <section className={styles.data_clean_pane}>
            <header>
                <h2>Data Cleaners</h2>
            </header>
            <p className="slug">The data cleaners pane</p>
        </section>
    );
};

function ControlPane() {
    return (
        <section className={styles.control_pane}>
          <WorkSetPane />
          <WidgetSelectorPane />
          <DataFilterPane />
          <DataCleanPane />
        </section>
    );
};


function Widget(props){
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

function WidgetPane() {
    return (
        <section className={styles.widget_pane} id="widgetPane">
          <Widget img="https://picsum.photos/300/200"
                  title="widget one"
          desc="A widget that displays some data about a workset."/>
          <Widget img="https://picsum.photos/300/200"
                  title="widget two"
          desc="A widget that displays some data about a workset."/>
        </section>
    );
};

export default function Dashboard() {
    return (
        <main className={styles.dashboard}>
          <ControlPane />
          <WidgetPane />
        </main>
    );
}
