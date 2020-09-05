import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    debugger;
    fetch("/snippets/")
      .then(response => {
        debugger;
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        debugger;
        var results = data.results;
        this.setState({
            data: results,
            loaded: true
        });
      });
  }

  render() {
    debugger;
    return (
      <ul>
        {this.state.data.map(snippet => {
          return (
            <li key={snippet.id}>
              {snippet.language} - {snippet.code}
            </li>
          );
        })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
