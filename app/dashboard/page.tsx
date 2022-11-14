import styles from './styles.module.css';

function WorkSetPane() {
    return (
        <section className={styles.control}>
          <header>
          <h2>Worksets</h2>
          </header>
          <p className="slug">The workset pane</p>
        </section>
    );
};

function WidgetSelectorPane() {
    return (
        <section className={styles.control}>
            <header>
                <h2>Widgets</h2>
            </header>
            <p className="slug">The widget selector pane</p>
        </section>
    );
};

function DataFilterPane(){
    return (
        <section className={styles.control}>
            <header>
                <h2>Data Filters</h2>
            </header>
            <p className="slug">The data filter pane</p>
        </section>
    );
};

function DataCleanPane(){
    return (
        <section className={styles.control}>
            <header>
                <h2>Data Filters</h2>
            </header>
            <p className="slug">The data filter pane</p>
        </section>
    );
};

function ControlPane() {
    return (
        <section className={styles.controlPane}>
          <WorkSetPane />
          <WidgetSelectorPane />
          <DataFilterPane />
          <DataCleanPane />
        </section>
    );
};

function Widget() {
    return (
        <div className={styles.widget}>
          <header>
            <h1 className={styles.widgetTitle}>a widget</h1>
            <p className={styles.slug}>contents of the widget should be graphic</p>
          </header>
        </div>
    );
};

function WidgetPane() {
    return (
        <section className={styles.widgetPane} id="widgetPane">
          <header>
            <h2>Widget Pane</h2>
          </header>
          <p className={styles.slug}>The data widget pane</p>
          <Widget />
          <Widget />
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
