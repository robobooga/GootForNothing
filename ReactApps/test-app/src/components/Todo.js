import React, { Component } from 'react';
import TodoItem from './TodoItem';
import PropTypes from 'prop-types';

class Todo extends Component {
  render() {
    return this.props.todos.map((x) => (
      <TodoItem key={x.id} x = {x}/>
    ));
  }
}

// PropTypes
Todo.propTypes = {
  todos: PropTypes.array.isRequired
}

export default Todo;
