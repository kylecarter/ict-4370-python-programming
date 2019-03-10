// Node Modules
import Head from 'next/head';
import Link from 'next/link';

// Components
import Page from '../components/Page';
import styles from './styles.css';

export default props => (<Page>
    <Head>
        <title>Home | ICT 4370 Python Programming</title>
    </Head>
    <main id="main-content" className="jumbotron jumbotron-fluid">
        <div className="container">
            <h1 className="display-4">Kyle A. Carter | ICT 4370 Python Programming</h1>
            <p className="lead">Use the links to view the project code.</p>
            <hr className="my-4" />
            <nav role="navigation">
                <ul className={['nav', styles.navlist].join(' ').trim()}>
                    <li className="nav-item"><Link href="/companions"><a className={['nav-link'].join(' ').trim()}>Companions</a></Link></li>
                    <li className="nav-item"><Link href="/stocks"><a className={['nav-link'].join(' ').trim()}>Stocks</a></Link></li>
                </ul>
            </nav>
        </div>
    </main>
</Page>);
