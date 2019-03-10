// Node Moduules
import Link from 'next/link';
import styles from './styles.css';

export default props => (<nav className={['navbar', 'navbar-dark', 'bg-dark', styles.navbar].join(' ')} role="navigation"><div className="container">
    <Link href="/"><a className={['navbar-brand', props.active ? 'active' : '', styles.brandname].join(' ').trim()}>Kyle A. Carter</a></Link>
    <ul className={['nav', 'justify-content-end', styles.navlist].join(' ').trim()}>
        <li className="nav-item"><Link href="/companions"><a className={['nav-link', /companions/g.test(props.active) ? 'active' : ''].join(' ').trim()}>Companions</a></Link></li>
        <li className="nav-item"><Link href="/stocks"><a className={['nav-link', /stocks/g.test(props.active) ? 'active' : ''].join(' ').trim()}>Stocks</a></Link></li>
    </ul>
</div></nav>);
