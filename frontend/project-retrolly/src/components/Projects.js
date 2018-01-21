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
import customstyles from '../styles/customstyles.css';

class Projects extends Component {


	constructor(props){
		super(props);
		this.state = {
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
    const nextIndex = this.state.activeIndex === this.props.projects.length - 1 ? 0 : this.state.activeIndex + 1;
    this.setState({ activeIndex: nextIndex });
  }

  previous() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === 0 ? this.props.projects.length - 1 : this.state.activeIndex - 1;
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
		const { activeIndex } = this.state;
		const { projects } = this.props;
		const slides = projects.map(project => {
			return (
			<CarouselItem
	          onExiting={this.onExiting}
          		onExited={this.onExited}
          		key={project.photo_url}
        	>
        	<a target="_blank" href={project.project_url}>
        	<img 
        	src={project.photo_url}
        	alt={project.project_name}
        	style={{'width': '400px', 'height': '300px', 'marginLeft': '35%'}}/>
        	</a>
          <CarouselCaption 
          captionText={project.tags}
           captionHeader={project.project_name}
            />
        </CarouselItem>

			);
		})
		return(
		<div>
	        <style>
	          {
	            `.custom-tag {
	                max-width: 100%;
	                height: 400px;
	                background: black;
	              },
	              .carousel-caption {
	              	color: black;
	              }
	              `
	          }
	        </style>
	        <Carousel
	          activeIndex={activeIndex}
	          next={this.next}
	          previous={this.previous}
	        >
	          <CarouselIndicators items={projects} activeIndex={activeIndex} onClickHandler={this.goToIndex} />
	          {slides}
	          <CarouselControl direction="prev" directionText="Previous" onClickHandler={this.previous} />
	          <CarouselControl direction="next" directionText="Next" onClickHandler={this.next} />
	        </Carousel>
      </div>
			)
	}
}

export default Projects;