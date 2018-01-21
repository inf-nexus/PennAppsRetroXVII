import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Button } from 'rmwc/Button';
import { Typography } from 'rmwc/Typography';
//import styles from 'material-components-web/dist/material-components-web.min.css';
import { RetroHeader, Header, Body, Footer, Form, Projects } from './components';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

// import injectTapEventPlugin from 'react-tap-event-plugin';

// injectTapEventPlugin();

const muiTheme = getMuiTheme({
  appBar: {
    backgroundColor: '#d94ac5'
  },
  pallette: {
    primary1Color: 'red'
  }
});

class App extends Component {
  render() {
    return (
      
        <div style={{'overflow-y':'auto', 'overflow-x': 'hidden', height: '800px', 'width': '100%'}}>
          <RetroHeader />
            <Body />
          <Footer />
        </div>
      
    );
  }
}

export default App;