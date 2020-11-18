function Homepage() {
    return (
        <React.Fragment>
            <div class="container">
                <div class="row">
                    <div class="col">
                        <h2>Request a recommendation from Bookbot</h2>

                        <form action='/recommendation-request' method="POST">
                            <div class="form-group">
                                <label for="username">Your Name</label>
                                <input
                                id="search-name"
                                class="form-control"
                                type="text"
                                name="username"
                                placeholder="Edmond Dantès"
                                required
                                ></input>
                            </div>

                            <div class="instructions">Please input your requested search criteria below and Bookbot will find your match!</div>

                            <div class="form-group">
                                <label for="request-genre">Genre</label>
                                <option></option>
                                <select name="genre"
                                id="search-genre"
                                class="form-control"
                                required
                                >
                                
                                <option value="" disabled="disabled">Please select an option</option>
                                {/* add loop here over genres in db */}
                                {% for genre in genres_list %} 
                                    <option value="{{ genre }}">{{ genre }}</option>
                                {% endfor %}
                                </select>
                    
                            </div>

                            <div class="form-group">
                                <label for="request-kw">Keyword</label>

                                <input
                                id="search-kw"
                                class="form-control"
                                type="text"
                                name="request-kw"
                                placeholder="Château d'If"
                                ></input>
                            </div>

                            <div class="instructions">
                            <button id="submit-form-button" type="submit">Submit</button>
                            </div>
                        </form>

                    </div>

                </div>

                </div>

        </React.Fragment>
    );
}
