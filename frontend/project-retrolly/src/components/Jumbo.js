import React, { Component } from 'react';
import { Form, Projects } from './';
import { Jumbotron, Button, Progress, FormGroup, Label, Input } from 'reactstrap';
import retrostyles from '../styles/retrostyles.css';
import bootstrapStyles from 'bootstrap/dist/css/bootstrap.css';
import { getProjects } from '../services/api';


const styles = {
	jumbotronStyle: {
		backgroundImage: 'url(http://ak6.picdn.net/shutterstock/videos/28467886/thumb/1.jpg)',
		// 'backgroundRepeat': 'no-repeat',
		'backgroundSize': '100% auto',
		'height': '1100px',
		'width': '100vw',
		'marginBottom': '0px'
	},
	titleStyle: {
		'textAlign': 'center'
	}

}

class Jumbo extends Component {

	constructor(props){
		super(props);
		this.state={
			originalityPercentage: undefined,
			retroPercentage: undefined,
			projectDescription: "",
			projects: [],
			placeholderText: 'enter project description',
			tag_links: [],
			tags: []
		}
	}

	change = e => {
    const { value } = e.target;
    this.setState({projectDescription: value})
  	};

  	onSubmit = e => {
	    e.preventDefault();
	    getProjects(this.state.projectDescription)
	    .then(res => {
	    	const { originality_score, retro_score, projects, tag_links, tags} = res;
	    	this.setState({
	    		projectDescription: "",
	    		originalityPercentage: originality_score,
	    		retroPercentage: retro_score,
	    		projects: projects,
	    		placeholderText: 'enter project description',
	    		tag_links: tag_links,
	    		tags: tags
	    	});
	    });
}

	renderTagTutorials() {
		if (this.state.tag_links && this.state.tag_links.length > 0) {
			const listitems = this.state.tag_links.map((item) =>
				<li>
					<a href={item}>{item}</a>
				</li>
			);
			return (<div><h1>Resources</h1><ul>{listitems}</ul></div>);
		}
	}

	renderOriginalityBar() { 
		if (this.state.originalityPercentage) {
			return (
				<div><center><h3>Originality Score</h3></center><Progress value={this.state.originalityPercentage * 100} style={{'barColor': '#d94ac5', 'textAlign': 'center', 'width': '50%', 'marginLeft': '25%'}}>{parseInt(this.state.originalityPercentage * 100) + '%'}</Progress></div>
				);
		}
	}

	renderRetroBar() {
		if (this.state.retroPercentage) {
			return (
				<div><center><h3>Retro Score</h3></center><Progress value={this.state.retroPercentage * 100} style={{'barColor': '#d94ac5', 'textAlign': 'center', 'width': '50%', 'marginLeft': '25%'}}>{parseInt(this.state.retroPercentage * 100) + '%'}</Progress></div>
				);
		}
	}

	render(){
		return (
			<div style={{'paddingBottom': '0px'}}>
		      <Jumbotron style={styles.jumbotronStyle}>
		        <h1 className="title--metallic" style={styles.titleStyle}></h1>
		        <hr className="my-2" />
		        <p className="lead" style={{'textAlign': 'center', 'margin': 'auto'}}>
			        <FormGroup>
	          			<Input 
	          			type="search" 
	          			name="search" 
	          			id="exampleSearch" 
	          			autoComplete="off" 
	          			placeholder={this.state.placeholderText}
	          			value={this.state.projectDescription}
	          			onClick={e => {this.setState({placeholderText: ''})}}
		    			onChange={e => this.change(e)}
	          			style={{width: '60%', 'textAlign': 'center', 'margin': 'auto'}}/>
	          			<br />
	          			<Button 
	          				color="primary"
	          				style={{'backgroundColor': '#d94ac5', 'textAlign': 'center', 'margin': 'auto'}}
	          				onClick={e => this.onSubmit(e)}
	          				>
	          				Search
	          				</Button>
	       			 </FormGroup>
		        </p>
		        <br />
		        {this.renderOriginalityBar()}
		        <br />
		        {this.renderRetroBar()}
		        <hr className="my-2" />
		        <br />
		        <Projects
		        	projects={this.state.projects}
		         />
		         {this.renderTagTutorials()}
		      </Jumbotron>
    		</div>
		);
	}
}

export default Jumbo;