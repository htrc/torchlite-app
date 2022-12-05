import Head from 'next/head';
import Link from 'next/link';
import Layout from '../../components/layout';
import Navbar from '../../components/navbar';

export default function Dashboard() {
  return (
      <Layout>
        <Navbar />
        <main>
          <p>the contents of the dashboard</p>
        </main>
      </Layout>
  )
}
