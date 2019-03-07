// Components
import Navbar from '../Navbar';
import Footer from '../Footer'

import styles from './styles.css';

export default props => {
    const { className } = props;
    return (<div className={[styles.content, className].join(' ')}>
        <Navbar />
        <div className={styles.wrapper}>{props.children}</div>
        <Footer />
    </div>);
}
