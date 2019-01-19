import React, { Component } from 'react';
import TodoItem from './TodoItem';
import PropTypes from 'prop-types';

class Todo extends Component {
  render() {
    return this.props.todo1.map((x) => (
      <TodoItem key={x.id} x = {x}/>
    ));
  }
}

// PropTypes
Todo.propTypes = {
  todo1: PropTypes.array.isRequired
}

export default Todo;
