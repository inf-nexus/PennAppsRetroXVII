import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { RetroHeader, Body, Footer} from './components';

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