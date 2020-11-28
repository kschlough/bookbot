function Homepage() {
    return (
        <React.Fragment>
            <div id = "homepage">
            <h1 id="welcome">Welcome to Bookbot</h1>
            <h2>Would you like to:</h2>
            <ul>
                <li>
                    <a href='/form'>Request a recommendation</a>
                </li>
                
                
                <li>
                    <a href='/recent-requests'>View all of Bookbot's previous recommendations</a>
                </li>
            </ul>
            </div>
            
        
        </React.Fragment>
    );
};


ReactDOM.render(<Homepage />, document.querySelector('#root'));