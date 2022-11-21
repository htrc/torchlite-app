export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <head />
      <body id="root">
        <header>Torchlite</header>
        {children}
      </body>
    </html>
  )
}
