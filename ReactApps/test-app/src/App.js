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
        completed: false
      },
    ]
  }

  render() {
    console.log(this.state.todo)
    return (
      <div className="App">
        <Todo />
      </div>
    );
  }
}

export default App;
