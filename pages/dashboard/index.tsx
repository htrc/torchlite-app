import Head from 'next/head';
import Link from 'next/link';
import Image from 'next/image';
import Layout from '../../components/layout';
import Navbar from '../../components/navbar';
import Pane from '../../components/pane';
import Widget from '../../components/widget';

export default function Dashboard() {
  return (
      <Layout>
        <Navbar />
        <main>
          <Pane>
            <Widget
              img="https://picsum.photos/300/200"
              title="A Widget"
              desc="A widget that displays some data about a workset."
            />
            <Widget
              img="https://picsum.photos/300/200"
              title="A Widget"
              desc="A widget that displays some data about a workset."
            />
          </Pane>
        </main>
      </Layout>
  )
}
