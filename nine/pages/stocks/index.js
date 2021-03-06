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
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

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

const _cookieify = (cookie) => {
    if (cookie.length < 1) return {};
    let cookies = {};
    _.each(cookie.split(/\s*;\s*/), pair => cookies[pair.split('=')[0]] = pair.split('=')[1].replace(/[\+]/g, ' '));
    return cookies;
};

const Listitem = props => (<li className="nav-item"><Link href={`/stocks?smbl=${props.id}`}>
    <a data-symbol={props.id} className={['nav-link', props.active == props.id ? 'active' : ''].join(' ').trim()} onClick={props.onclick} onTouchEnd={props.onclick}>{props.symbol}</a>
</Link></li>);

const Tabledata = props => (<tr>
    {props.isSearch && <td>{props.symbol}</td>}
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
            stocks: null,
            form: null,
            isSearch: false
        }, this.props);
        this.onclick = this.onclick.bind(this);
        this.onsubmit = this.onsubmit.bind(this);
    }

    componentDidMount() {
        const self = this;
        const qs = params();
        axios.get('/api/v1/symbols/').then(res => {
            self.setState({
                symbols: res.data.symbols,
            });
        }).catch(err => {
            console.log(err)
        });

        axios.get('/api/v1/forms/stockbydate/').then(res => {
            self.setState({
                form: res.data.form
            });
        }).catch(err => {
            console.log(err)
        });

        if (_.has(qs, 'smbl')) {
            axios.get(`/api/v1/stocks/${qs.smbl}/`).then(res => {
                self.setState({
                    active: qs.smbl,
                    symbol: res.data.symbol,
                    stocks: res.data.stocks,
                    business: res.data.business,
                    isSearch: false
                });
            }).catch(err => {
                console.log(err)
            });
        }
    }

    render() {
        const { active, business, form, isSearch, stocks, symbol, symbols } = this.state;
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
                            { form && <form method="post" action="/api/v1/stocks/search/" onSubmit={this.onsubmit}>
                                <fieldset className={styles.fieldset}>
                                    <legend className={styles.legend}>Search for stock information by date.</legend>
                                    <div className={[styles.field, styles.fieldDate].join(' ')}>
                                        <label htmlFor={form.label.attributes.for} className={[form.label.attributes.class, styles.label].join(' ')} {..._.omit(form.label.attributes, 'for', 'class')}>{form.label.label}</label>
                                        <input type="date" className={[form.input.attributes.class, styles.input].join(' ')} {..._.omit(form.input.attributes, 'class', 'type')} />
                                    </div>
                                    <div className={styles.actions}>
                                        <input type="submit" className="btn btn-primary" value="Search" />
                                    </div>
                                </fieldset>
                            </form> }
                            <nav className="navbar" aria-labelledby="symbol-select">
                                <h4 id="symbol-select">Pick a symbol to view its data</h4>
                                <ul className="nav flex-md-column">
                                    {symbols && symbols.map((symbol, idx) => <Listitem key={`react.key.symbol.${symbol.id}.${idx}`} onclick={this.onclick} active={active} {...symbol} />)}
                                </ul>
                            </nav>
                        </div>
                        <div className="col">
                            <div className="table-responsive"><table className="table table-striped">
                                <thead className="thead-dark">
                                    {business && !isSearch && <tr>
                                        <th colSpan="6"><h2>{business} | {symbol}</h2></th>
                                    </tr>}
                                    <tr>
                                        {isSearch && <th>Symbol</th>}
                                        <th>Date</th>
                                        <th>Opening Price</th>
                                        <th>Lowest Price</th>
                                        <th>Highest Price</th>
                                        <th>Closing Price</th>
                                        <th>Volume</th>
                                    </tr>
                                </thead>
                                <tbody>{stocks && stocks.map((stock, idx) => <Tabledata key={`react.key.stock.${stock.id}.${idx}`} isSearch={isSearch} {...stock} />)}</tbody>
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
        axios.get(`/api/v1/stocks/${symbol}/`).then(res => {
            self.setState({
                active: symbol,
                symbol: res.data.symbol,
                stocks: res.data.stocks,
                business: res.data.business,
                isSearch: false
            });
        }).catch(err => {
            console.log(err)
        });
    }

    onsubmit(event) {
        event.preventDefault();
        const self = this;
        const csrftoken = _cookieify(document.cookie).csrftoken;

        const ajax = axios.create({
            headers: {
                'X-CSRFToken': csrftoken
            }
        });

        ajax.post('/api/v1/stocks/search/', `date=${event.target.date.value}`).then(res => {
            self.setState({
                stocks: res.data.stocks,
                isSearch: true
            });
        }).catch(err => console.log(err));
    }
}
