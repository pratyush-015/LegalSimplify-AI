import React from 'react';
import Head from 'next/head';

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <>
      <Head>
        <title>LegalSimplify AI - Transform Legal Documents</title>
        <meta name="description" content="AI-powered legal document simplification" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="min-h-screen">
        {children}
      </main>
    </>
  );
};

export default Layout;
