function SubmitForm(props) {
    const [genres, setGenres] = React.useState([]);
    React.useEffect(() => {
        fetch('/api/genres').
        then((response) => response.json()).
        then((genres) => setGenres(genres.genres));
        }, [])

    
    return (
        <React.Fragment>
            <div className="container">
                <div className="row">
                    <div className="col">
                        <h2>Request a recommendation from Bookbot</h2>

                        <form action='/recommendation-request' method="POST">
                            <div className="form-group">
                                <label htmlFor="username">Your Name</label>
                                <input
                                id="search-name"
                                className="form-control"
                                type="text"
                                name="username"
                                placeholder="Edmond Dantès"
                                required></input>
                            </div>

                            <div className="instructions">Please input your requested search criteria below and Bookbot will find your match!</div>

                            <div className="form-group">
                                <label htmlFor="request-genre">Genre</label>
                                <option></option>
                                <select name="genre"
                                id="search-genre"
                                className="form-control"
                                required>


                                <option value="" disabled="disabled">Please select an option</option>
                                {genres.map((data,id)=>{
                                    return <option key={id}>{data}</option>
                                })}
                            
                                </select>
                                
                            </div>

                        
                        </form>
                        
                    </div>
                </div>
            </div>
        </React.Fragment>
    );
};

ReactDOM.render(<SubmitForm/>, document.getElementById('root'))




