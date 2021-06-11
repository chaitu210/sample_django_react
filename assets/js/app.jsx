import React, { Component } from "react";

class App extends Component {
  constructor(props) {
    super(props);
  }

  renderItems() {
    const newItems = this.props.dataList;

    return ( 
      newItems.length > 0 ? newItems.map((obj,index) =>
      <tr key={ obj.id }>
        <td>{ index+1 }</td>
        <td>
          {obj.title}
        </td>
        <td>{obj.url}</td>
        <td>{obj.abstract}</td>
        
      </tr>
      ) : <tr><td>No items</td></tr>
    )
  };
  render() {
    return (
      <main className="container">
        <h1 className="text-center my-4">Books app</h1>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
            <a href ="/graphs/">Graphs</a>
            <div className="">
              
              <table className="table table-hover table-striped ">
                <thead>
                  <tr>
                    <th>S.No</th>
                    <th>Title</th>
                    <th>URL</th>
                    <th>Abstract</th>
                  </tr>
                </thead>
                <tbody>
                  {this.renderItems()}
                  
                </tbody>
              </table>
            </div>
          </div>
        </div>

      </main>
    );
  }
}

export default App;