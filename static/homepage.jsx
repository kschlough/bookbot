function Homepage() {
    return (
        <React.Fragment>
            

            <div className="homepage-container">

                        
                <div className="homepage" id="homepage-img">

                    <div className="homepage">

                        <div className="homepage-text">
                            <h1 id="welcome">Welcome to Bookbot!</h1>
                            <h2 id="choice">Would you like to:</h2>

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