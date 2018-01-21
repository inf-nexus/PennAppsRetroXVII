import React, { Component } from 'react';
// import styles from 'material-components-web/dist/material-components-web.min.css';
import styles from '../styles/retrostyles.css';

class Footer extends Component {

	renderRows(){
		let rows = [];
		for (let i=0; i < 150; i++){
			rows.push(i);
		}
		return (rows.map(r => <div className="grid__tile"></div>));
	}

	render(){
		return (
			<div className='grid'>{this.renderRows()}</div>
			);
	}
}

export default Footer;