export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <head />
      <body>
        <header>Torchlite</header>
        {children}
      </body>
    </html>
  )
}
