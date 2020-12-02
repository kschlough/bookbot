function Homepage() {
    return (
        <React.Fragment>
            <div className = "homepage">

            <div className="homepage" id="homepage-img"></div>

            
                <div className="row">
                    <div className="col">
                        <h1 id="welcome">Welcome to Bookbot!</h1>
                        <h2 id="choice">Would you like to:</h2>
                        <ul id="homepage-options">
                            <li>
                                <a href='/form'>Request a recommendation</a>
                            </li>
                        
                        
                            <li>
                                <a href='/recent-requests'>View all of Bookbot's previous recommendations</a>
                            </li>
                        </ul>
                    </div>
                </div>  
            </div>  
   
            
        
        </React.Fragment>
    );
};


ReactDOM.render(<Homepage />, document.querySelector('#root'));