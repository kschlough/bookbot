function Homepage() {
    return (
        <React.Fragment className="homepage">
            <h1>Welcome to Bookbot</h1>
            <h2>Would you like to:</h2>
            <ul>
                <li className = "homepage">
                    <a href='/form'>Request a recommendation</a>
                </li>
                
                <p>or:</p>
                
                <li className = "homepage">
                    <a href='/recent-requests'>View all of Bookbot's previous recommendations</a>
                </li>
            </ul>
            
        
        </React.Fragment>
    );
};


ReactDOM.render(<Homepage />, document.querySelector('#root'));