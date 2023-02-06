import Head from 'next/head';
import styles from '@/styles/Home.module.css';
import useSWR from 'swr';
import axios from 'axios';

const fetcher = (url) => fetch(url).then((res) => res.json());

export function CurrentTime() {
    const { data, error } = useSWR("http://localhost:8000/time", fetcher);

    if (error) return <div>failed to load</div>;
    if (!data) return <div>loading...</div>;

    console.log("the data is", {data});
    return (
        <p>the current time is {data.display}</p>
    );
};

export function WorkSets() {
    const { data, error } = useSWR("http://localhost:8000/worksets", fetcher);

    if (error) return <div>failed to load</div>;
    if (!data) return <div>loading...</div>;

    console.log("the data is", {data});
    return (
        <ul>
          {
              data.map((ws, i) => {
                  return (
                      <li key={i}>{ws.title}</li>
                  );
              })}
        </ul>
    );
};

export function Widget ({ path }) {
    const data_path = path + "/data";
    console.log("widget with path", {data_path});
    const { data, error } = useSWR(`${data_path}`, fetcher);

    if (error) return <div>failed to load</div>;
    if (!data) return <div>loading...</div>;

    console.log(`the widget data are ${data}`);
    return (
        <div className="widget">
          <header>
            <h3>Widget</h3>
            <p>{data_path}</p>
          </header>
        <ul>
          {
              data.map((item, i) => {
                  return(
                      <li key={i}>{item.title}</li>
                  );
              })
          }
        </ul>
        </div>
    );
};

export function Widgets() {
    const { data, error } = useSWR("http://localhost:8000/dashboards/default/widgets", fetcher);

    if (error) return <div>failed to load</div>;
    if (!data) return <div>loading...</div>;

    console.log(`the widgets are ${data}`);
    return (
        <div className="widgetWrapper">
          {
              data.map((id, i) => {
                  const path = `http://localhost:8000/dashboards/default/widgets/${id}`;
                  console.log(`the path is ${path}`);
                  return (
                      <Widget path= {path}/>
                  );
              })
          }
        </div>
    );
};



export function Dashboards() {
    const { data, error } = useSWR("http://localhost:8000/dashboards", fetcher);

    if (error) return <div>failed to load</div>;
    if (!data) return <div>loading...</div>;

    console.log("the dashboards are", {data});
    return (
        <ul>
          {
              data.map((d, i) => {
                  return (
                      <li key={i}>{d}</li>
                  );
              })}
        </ul>
    );
};

export default function Home() {
    return (
        <>
          <Head>
            <title>Torchlite Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
          </Head>
          <main className={styles.main}>
            <h1>Dashboard</h1>

            <section>
              <h2>Available Dashboards</h2>
              <Dashboards />
            </section>
            <section>
              <h2>Available Worksets</h2>
              <WorkSets />
            </section>
            <section>
              <h2>Current Widgets</h2>
              <Widgets />
            </section>
          </main>
        </>
    );
};
