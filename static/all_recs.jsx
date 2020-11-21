function allRecommendations() {
    return (
        <React.Fragment>
            <div class="container">
                <div class="row">
                    <div class="col">
                        <h2>View all of Bookbot's recent recommendations</h2>

                        {/* display 3 books per row */}
                        <div class="response books">
                            <label for="response-books">Bookbot's Recent Recommendations:</label>
                            {/* loops through recommendation_responses_in_db */}
                            for (book of rec_responses_in_db) {
                                <div class="book">{ book } by { rec_responses_in_db[book] }</div>
                            } 
                            {/* 'user' received a recommendation for 'book' by 'author' from Bookbot */}

                        </div>
                    </div>
                </div>
            </div>

        </React.Fragment>
    );
};

ReactDOM.render(
    <allRecommendations />,
    document.querySelector('#root')
);