// Node Modules
import React from 'react';
import Head from 'next/head';
import underscore from 'underscore';
import axios from 'axios';

// Components
import Page from '../../components/Page';
import styles from './styles.css';

const _ = underscore;
const Tabledata = props => (<tr>
    <td>{props.name ? props.name : ''}</td>
    <td>{props.type ? props.type : ''}</td>
    <td>{props.breed ? props.breed : ''}</td>
    <td>{props.age && parseFloat(props.age) <= 1 ? 1 : props.age}</td>
    <td>{props.birthdate ? (new Date(
        parseInt(props.birthdate.split('-')[0]),
        parseInt(props.birthdate.split('-')[1]) - 1,
        parseInt(props.birthdate.split('-')[2])
    )).toLocaleDateString('en-US') : ''}</td>
    <td>{props.weight ? `${props.weight}kg` : ''}</td>
    <td>{props.owner ? props.owner : ''}</td>
</tr>);
export default class Companions extends React.Component {
    constructor(props) {
        super(props);
        this.state = _.extend({
            companions: null
        }, this.props);
    }

    componentDidMount() {
        const self = this;
        axios.get('/api/v1/companions').then(res => {
            self.setState({
                companions: res.data.companions
            });
        })
    }

    render() {
        const { companions } = this.state;
        return (<Page active="companions">
            <Head>
                <title>Companions | ICT 4370 Python Programming</title>
            </Head>
            <main id="main-content">
                <header className="jumbotron jumbotron-fluid">
                    <div className="container">
                        <h1 className="display-4">Companions</h1>
                        <p className="lead">Meet these lovely pets and their owners.</p>
                    </div>
                </header>
                <div className={[styles.content].join(' ')}>
                    <div className="container">
                        <div className="table-responsive"><table className="table table-striped">
                            <thead className="thead-dark"><tr>
                                <th>Name</th>
                                <th>Type</th>
                                <th>Breed</th>
                                <th>Age</th>
                                <th>Birthdate</th>
                                <th>Weight</th>
                                <th>Owner</th>
                            </tr></thead>
                            <tbody>{companions && companions.map((companion, idx) => <Tabledata key={`react.key.companion.${companion.id}.${idx}`} {...companion} />)}</tbody>
                        </table></div>
                    </div>
                </div>
            </main>
        </Page>);
    }
}

