import React, { Component } from 'react';
import { Form, Jumbo, Projects } from './';
//import styles from 'material-components-web/dist/material-components-web.min.css';

const styles = {
	jumbotronStyle: {
		backgroundImage: 'url(https://pbs.twimg.com/media/DOkI3B0WkAEMf9H.jpg)',
		'background-repeat': 'no-repeat',
		'height': '100%'

	}

}

class Body extends Component {
	
	render(){
		return (
			<div>
				<Jumbo />				
			</div>
		);
	}
}

export default Body;