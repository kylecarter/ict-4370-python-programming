// Node Modules
import React from 'react';
import Head from 'next/head';
import Link from 'next/link';
import underscore from 'underscore';
import axios from 'axios';

// Components
import Page from '../../components/Page';
import styles from './styles.css';

const _ = underscore;
const params = () => {
    var params = {};
    if (!/[\?\&]/g.test(window.location.href)) return params;
    window.location.href.substring(window.location.href.search(/[\?]/g) + 1).split(/[\&]/g).forEach(val => {
        if (/=/gi.test(val)) {
            params[decodeURIComponent(val.split(/=/)[0].replace(/[\+\-\s]/g, '_'))] = decodeURIComponent(val.split(/=/)[1]).replace('+', ' ');
        }
        return true;
    });
    return params;
};
const Listitem = props => (<li className="nav-item"><Link href={`/stocks?smbl=${props.id}`}>
    <a data-symbol={props.id} className={['nav-link', props.active == props.id ? 'active' : ''].join(' ').trim()} onClick={props.onclick} onTouchEnd={props.onclick}>{props.symbol}</a>
</Link></li>);
const Tabledata = props => (<tr>
    <td>{props.date ? (new Date(
        parseInt(props.date.split('-')[0]),
        parseInt(props.date.split('-')[1]) - 1,
        parseInt(props.date.split('-')[2])
    )).toLocaleDateString('en-US') : ''}</td>
    <td>{props.open ? parseFloat(props.open).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD'
    }) : ''}</td>
    <td>{props.low ? parseFloat(props.low).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD'
    }) : ''}</td>
    <td>{props.high ? parseFloat(props.high).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD'
    }) : ''}</td>
    <td>{props.close ? parseFloat(props.close).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD'
    }) : ''}</td>
    <td>{props.volume ? props.volume : ''}</td>
</tr>);
export default class Stocks extends React.Component {
    constructor(props) {
        super(props);
        this.state = _.extend({
            business: null,
            symbols: null,
            symbol: null,
            active: null,
            stocks: null
        }, this.props);
        this.onclick = this.onclick.bind(this);
    }

    componentDidMount() {
        const self = this;
        const qs = params();
        axios.get('/api/v1/symbols').then(res => {
            self.setState({
                symbols: res.data.symbols
            });
        }).catch(err => {
            console.log(err)
        });
        if (_.has(qs, 'smbl')) {
            axios.get(`/api/v1/stocks/${qs.smbl}`).then(res => {
                self.setState({
                    active: qs.smbl,
                    symbol: res.data.symbol,
                    stocks: res.data.stocks,
                    business: res.data.business
                });
            }).catch(err => {
                console.log(err)
            });
        }
    }

    render() {
        const { active, business, stocks, symbol, symbols } = this.state;
        return (<Page active="stocks">
            <Head>
                <title>Stocks | ICT 4370 Python Programming</title>
            </Head>
            <main id="main-content">
                <header className="jumbotron jumbotron-fluid">
                    <div className="container">
                        <h1 className="display-4">Stocks</h1>
                        <p className="lead">Check out all this stock data.</p>
                    </div>
                </header>
                <div className={[styles.content].join(' ')}>
                    <div className="container"><div className="row">
                        <div className="col-md-3">
                            <nav className="navbar" aria-labelledby="symbol-select">
                                <h5 id="symbol-select">Pick a symbol to view its data</h5>
                                <ul className="nav flex-md-column">
                                    {symbols && symbols.map((symbol, idx) => <Listitem key={`react.key.symbol.${symbol.id}.${idx}`} onclick={this.onclick} active={active} {...symbol} />)}
                                </ul>
                            </nav>
                        </div>
                        <div className="col">
                            <div className="table-responsive"><table className="table table-striped">
                                <thead className="thead-dark">
                                    {business && <tr>
                                        <th colSpan="6"><h2>{business} | {symbol}</h2></th>
                                    </tr>}
                                    <tr>
                                        <th>Date</th>
                                        <th>Opening Price</th>
                                        <th>Lowest Price</th>
                                        <th>Highest Price</th>
                                        <th>Closing Price</th>
                                        <th>Volume</th>
                                    </tr>
                                </thead>
                                <tbody>{stocks && stocks.map((stock, idx) => <Tabledata key={`react.key.stock.${stock.id}.${idx}`} {...stock} />)}</tbody>
                                {!stocks && <tfoot><tr><td colSpan="6">
                                    <p>Select a stock symbol from the left menu to view information about that stock.</p>
                                </td></tr></tfoot>}
                            </table></div>
                        </div>
                    </div></div>
                </div>
            </main>
        </Page>);
    }

    onclick(event) {
        event.preventDefault();
        const self = this;
        const symbol = event.target.getAttribute('data-symbol');
        axios.get(`/api/v1/stocks/${symbol}`).then(res => {
            console.log(res);
            self.setState({
                active: symbol,
                symbol: res.data.symbol,
                stocks: res.data.stocks,
                business: res.data.business
            });
        }).catch(err => {
            console.log(err)
        });
    }
}

