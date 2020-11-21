function Homepage() {
    return (
        <React.Fragment>
            <h1>Welcome to Bookbot</h1>
            <h2>Would you like to:</h2>
            <ul>
                <li>
                    <p>Request a recommendation</p>
                </li>
                
                <p>or:</p>
                
                <li>
                    <p>View all of Bookbot's previous recommendations</p>
                </li>
            </ul>
            
        
        </React.Fragment>
    );
};


ReactDOM.render(
    <Homepage />,
    document.querySelector('#root')
);