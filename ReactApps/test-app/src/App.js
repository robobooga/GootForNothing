import React, { Component } from 'react';
import Todo from './components/Todo'

import './App.css';

class App extends Component {
  state = {
    todo: [
      {
        id: 1,
        title: 'Buy something',
        completed: false
      },
      {
        id: 2,
        title: 'Buy another thing',
        completed: false
      },
      {
        id: 3,
        title: 'Third status',
        completed: true
      }
    ]
  }

  render() {
    return (
      <div className="App">
        <Todo todo1 = {this.state.todo} />
      </div>
    );
  }
}

export default App;
