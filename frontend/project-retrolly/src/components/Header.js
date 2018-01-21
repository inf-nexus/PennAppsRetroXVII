import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
//import styles from 'material-components-web/dist/material-components-web.min.css';

class Header extends Component {
	render(){
		return(
			<div>
			<AppBar
				title="Retrolly"
				iconClassNameRight="muidocs-icon-navigation-expand-more"
				// style={{backgroundColor: '#d94ac5', textColor: '#d94ac5'}}
			 />
			 </div>
			);
		}
}

export default Header;