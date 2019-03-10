import Document, { Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
    static async getInitialProps(ctx) {
        const initialProps = await Document.getInitialProps(ctx)
        return { ...initialProps }
    }

    render() {
        return (
            <html className="no-js">
                <Head>
                    <meta name="viewport" content="minimum-scale=1, width=device-width, initial-scale=1, user-scalable=no, shrink-to-fit=no" />
                    <meta httpEquiv="Content-Type" content="text/html; charset=utf-8" />
                    <meta charSet="utf-8" />
                    <meta name="robots" content="INDEX,FOLLOW" />
                    <meta name="HandheldFriendly" content="true" />
                    <link rel="canonical" href="https://kylecarter.info/" />
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossOrigin="anonymous" />
                    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,500,500i" />
                    <link rel="stylesheet" href="/static/styles.css" />
                </Head>
                <body style={{
                    boxSizing: 'border-box'
                }}>
                    <a href="#main-content" style={{
                        border: 0,
                        clip: 'rect(1px, 1px, 1px, 1px)',
                        clipPath: 'inset(100%)',
                        height: '1px',
                        overflow: 'hidden',
                        padding: 0,
                        position: 'absolute',
                        width: '1px'
                    }}>Skip to main content.</a>
                    <Main />
                    <NextScript />
                </body>
            </html>
        )
    }
}

export default MyDocument
