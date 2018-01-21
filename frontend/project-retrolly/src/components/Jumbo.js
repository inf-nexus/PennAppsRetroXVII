import React, { Component } from 'react';
import { Form, Projects } from './';
import { Jumbotron, Button, Progress, FormGroup, Label, Input } from 'reactstrap';
import retrostyles from '../styles/retrostyles.css';
import bootstrapStyles from 'bootstrap/dist/css/bootstrap.css';
import { getProjects } from '../services/api';


const styles = {
	jumbotronStyle: {
		backgroundImage: 'url(http://ak6.picdn.net/shutterstock/videos/28467886/thumb/1.jpg)',
		'backgroundRepeat': 'no-repeat',
		'backgroundSize': '100% auto',
		'height': '700px',
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
			projectDescription: "",
			projects: [],
			placeholderText: 'enter project description'

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
	    	const { originality_score, projects} = res;
	    	this.setState({
	    		projectDescription: "",
	    		originalityPercentage: originality_score,
	    		projects: projects,
	    		placeholderText: 'enter project description'
	    	});
	    });
}

	renderOriginalityBar(){
		if (this.state.originalityPercentage) {
			return (
				<Progress value={this.state.originalityPercentage * 100} style={{'barColor': '#d94ac5', 'textAlign': 'center', 'width': '50%', 'marginLeft': '25%'}}>{parseInt(this.state.originalityPercentage * 100) + '%'}</Progress>
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
		        <hr className="my-2" />
		        <br />
		        <br />
		        <Projects
		        	projects={this.state.projects}
		         />
		      </Jumbotron>
    		</div>
		);
	}
}

export default Jumbo;