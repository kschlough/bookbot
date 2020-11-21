function recResponse() {
    return(
        <React.Fragment>
            <div className="container">
                <div className="row">
                    <div className="col">
                        <h2>Hi { username.title() }! Bookbot has generated your recommendation below.</h2>
                        <p>Here is what you're looking for: A book from the { genre.title() } genre, with the keyword "{ keyword }."</p>

                        <div id="book-recommendation">
                            <div id="book-image">
                                <img src = { image_url }></img>
                            </div>

                            <div id="book-info">
                                <h3>{{ book_title }}</h3>
                                <h4>{{ book_author }}</h4>
                                <p>Description: {{ description }}</p>
                                <p>Genre: {{ book_genre }}</p>
                                <p>Page count: {{ page_count }}</p>
                                <p>Average rating: {{ average_rating }}</p>
                                <p>{{ maturity_rating }}</p>
                            </div>
                        </div>

                        <div id="return_home" className="instructions">
                            <button id="resubmit-button" type="submit">Submit another</button>
                        </div>

                    </div>
                </div>
            </div>

            <script src="http://code.jquery.com/jquery.js"></script>
            <script src="static/bookbot.js"></script>
        </React.Fragment>
    );
};

ReactDOM.render(
    <recResponse />,
    document.querySelector('#root')
);
            
        