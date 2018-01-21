import React, { Component } from 'react';
import {
  Carousel,
  CarouselItem,
  CarouselControl,
  CarouselIndicators,
  CarouselCaption
} from 'reactstrap';
import customstyles from '../styles/customstyles.css';
import circlestyles from '../styles/progressCircleStyles.css';
import CircularProgressbar from 'react-circular-progressbar';

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

	render(){
		const { activeIndex } = this.state;
		const { projects } = this.props;
		if (projects.length > 0){
					const slides = projects.map(project => {
			return (
			<CarouselItem
	          onExiting={this.onExiting}
          		onExited={this.onExited}
          		key={project.project_name}
        	>
          <span>
        	<a target="_blank" href={project.project_url}>
        	<img 
        	src={project.photo_url ? project.photo_url : 'https://devpost-challengepost.netdna-ssl.com/assets/defaults/thumbnail-placeholder-42bcab8d8178b413922ae2877d8b0868.gif'}
        	alt={project.project_name}
        	style={{'width': '400px', 'height': '300px', 'marginLeft': '35%', 'borderRadius': '10px'}}/>
        	</a>
          <CircularProgressbar percentage={parseInt(parseFloat(project.similarity)*100)} />
          </span>
          <CarouselCaption 
          captionText={project.tagline}
           captionHeader={project.project_name}
            />
        </CarouselItem>

			);
		})
		return(
		<div>
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
	}else{
		return <div></div>
	}
}

}

export default Projects;