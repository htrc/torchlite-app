import Head from 'next/head';
import Link from 'next/link';
import Layout from '../../components/layout';
import Navbar from '../../components/navbar';

export default function Widgets() {
  return (
      <Layout>
        <Navbar />
        <main>
          <h1>Widgets Page</h1>
        </main>
      </Layout>
  )
}
