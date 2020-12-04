function Homepage() {
    return (
        <React.Fragment>

            <div className="view"></div>
            <div id="homepage-text">
            <div className="container">
            
                    <div className="row-homepage py-5">
                    
                    <div className="col-homepage">
                        <h1>Welcome to Bookbot!</h1>
                        <h2>Would you like to:</h2>

                        <ul id="homepage-options">
                            <li>
                                <i className="fas fa-book"></i>
                                <a href='/form'> Request a recommendation</a>
                            </li>
                        
                        
                            <li>
                                <i className="fas fa-bookmark"></i>
                                <a href='/recent-requests'> View all of Bookbot's previous recommendations</a>
                            </li>
                        </ul>
                        
                    </div>
              
                    </div>
                    </div>
            
                </div>
             
        
        </React.Fragment>
    );
};


ReactDOM.render(<Homepage />, document.querySelector('#root'));
