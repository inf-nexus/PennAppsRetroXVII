import React, { Component } from 'react';
import TextField from 'material-ui/TextField';

class Form extends Component {
	constructor(props){
		super(props);
		this.state = {
			firstName: "",
		    lastName: "",
		    username: "",
		    email: "",
		    password: ""
		}
	}

change = e => {
    // this.props.onChange({ [e.target.name]: e.target.value });
    // this.setState({
    //   [e.target.name]: e.target.value
    // });
    const { firstName, value } = e.target;
    this.setState({firstName: value})
  };

  onSubmit = e => {
    e.preventDefault();
    // this.props.onSubmit(this.state);
    this.setState({
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: ""
    });
    this.props.onChange({
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: ""
    });
  };

	render() {
		const { classes } = this.props;
		return (
      <form>
        <TextField
        name="firstName"
		    hintText="First Name"
		    floatingLabelText="First Name"
		    value={this.state.firstName}
		    onChange={e => this.change(e)}
		    floatingLabelFixed={true}
	    />
	    <br />
        <button onClick={e => this.onSubmit(e)}>Submit</button>
      </form>
    );
  }
			
}

export default Form;