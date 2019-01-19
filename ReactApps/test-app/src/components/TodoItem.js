import React, { Component } from 'react'
import PropTypes from 'prop-types';

export class TodoItem extends Component {
  getStyle = () => {
    return {
      background: '#f4f4f4',
      padding: '10px',
      borderBottom: '1px #ccc dotted',
      textDecoration: this.props.x.completed ? 'line-through' : 'none'
    }
  }
  render() {
    return (
      <div style={this.getStyle()}>
        <p>
          <input type="checkbox" /> {' '}
          { this.props.x.title } 
        </p>
      </div>
    )
  }
}

// PropTypes
TodoItem.propTypes = {
    x: PropTypes.object.isRequired
}

export default TodoItem;