import React, { Component } from 'react';
import { Form } from './';
import styles from '../styles/retrostyles.css';
//import styles from 'material-components-web/dist/material-components-web.min.css';

class RetroHeader extends Component {

	renderRows(){
		let rows = [];
		for (let i=0; i < 150; i++){
			rows.push(i);
		}
		return (rows.map(r => <div className="grid__tile"></div>));
	}
	
	render(){
		return (
			<div style={{'width': '100%'}}>
				 <div className="container" >
					  <div className="triangle"></div>
					  <h1 className="title--fancy">Welcome</h1>
					  <h1 className="title--metallic">To</h1>
					  <h1 className="title--neon">Retrolly</h1>
				</div>
			<iframe className="grain" src="https://www.youtube.com/embed/8tZ_N3wP9Ko?autoplay=1&amp;loop=1&amp;controls=0&amp;iv_load_policy=3&amp;start=5&amp;showinfo=0&amp;autohide=1&amp;rel=0&amp;modestbranding=1"></iframe>
			</div>
		);
	}
}

export default RetroHeader;