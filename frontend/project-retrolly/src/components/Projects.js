import React, { Component } from 'react';
import { getProjects } from '../services/api';

class Projects extends Component {
	// renderProjects(){
	// 	sampleJSON.forEach(json => {console.log(json['name'] + ' ' + json['photo'])});
	// }
	constructor(props){
		super(props);
		// this.state = {projects: undefined};
	}

	renderProjects(){
		console.log(this.props.projects);
		if (this.props.projects) {
			return (this.props.projects.map(project =>
			 <h1 styles={{'color': 'white'}}>{project.name}</h1>
			 ));
		}
	}

	render(){
		// getProjects('trash cans that auto sort')
		// .then(projects => this.setState({ projects }));
		return(
			<div>{this.renderProjects.bind(this)}</div>
			)
	}
}

export default Projects;