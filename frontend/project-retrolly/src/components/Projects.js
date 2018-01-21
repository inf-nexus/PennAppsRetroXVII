import React, { Component } from 'react';
import { getProjects } from '../services/api';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import GridList, { GridListTile, GridListTileBar } from 'material-ui/GridList';
import Subheader from 'material-ui/Subheader';
import IconButton from 'material-ui/IconButton';
import InfoIcon from 'material-ui-icons/Info';
import {
  Carousel,
  CarouselItem,
  CarouselControl,
  CarouselIndicators,
  CarouselCaption
} from 'reactstrap';

class Projects extends Component {


	constructor(props){
		super(props);
		this.state = {
			projects: [],
			activeIndex: 0
		};
		this.next = this.next.bind(this);
	    this.previous = this.previous.bind(this);
	    this.goToIndex = this.goToIndex.bind(this);
	    this.onExiting = this.onExiting.bind(this);
	    this.onExited = this.onExited.bind(this);
	}


  onExiting() {
    this.animating = true;
  }

  onExited() {
    this.animating = false;
  }

  next() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === this.state.projects.length - 1 ? 0 : this.state.activeIndex + 1;
    this.setState({ activeIndex: nextIndex });
  }

  previous() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === 0 ? this.state.projects.length - 1 : this.state.activeIndex - 1;
    this.setState({ activeIndex: nextIndex });
  }

  goToIndex(newIndex) {
    if (this.animating) return;
    this.setState({ activeIndex: newIndex });
  }

	// renderProjects(){
	// 	console.log(this.props.projects);
	// 	if (this.props.projects) {
	// 		return (this.props.projects.map(project =>
	// 			//const {project_name, photo_url, tagline, project_url, tags, similariy} = project;
	// 	));
	// 	}
	// }

	render(){
		const { activeIndex, projects } = this.state;
		const slides = projects.map(project => {
			return (
			<CarouselItem
	          className="custom-tag"
	          tag="div"
	          key={project.project_name}
	          onExiting={this.onExiting}
	          onExited={this.onExited}
        	>
          <CarouselCaption className="text-danger" captionText={project.tags} captionHeader={project.project_name} />
        </CarouselItem>

			);
		})
		// getProjects('trash cans that auto sort')
		// .then(projects => this.setState({ projects }));
		return(
		<div style={{'height': '300px'}}>
	        <style>
	          {
	            `.custom-tag {
	                max-width: 100%;
	                height: 500px;
	                background: black;
	              }`
	          }
	        </style>
	        <Carousel
	          activeIndex={activeIndex}
	          next={this.next}
	          previous={this.previous}
	        >
	          <CarouselIndicators items={this.state.projects} activeIndex={activeIndex} onClickHandler={this.goToIndex} />
	          {slides}
	          <CarouselControl direction="prev" directionText="Previous" onClickHandler={this.previous} />
	          <CarouselControl direction="next" directionText="Next" onClickHandler={this.next} />
	        </Carousel>
      </div>
			)
	}
}

export default Projects;