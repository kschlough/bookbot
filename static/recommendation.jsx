// test - single page for form submit
// // listen for form button click

function SubmitForm(props) {
    const { genres } = props;
    return (
        <React.Fragment>
            <div className="container">
                <div className="row">
                    <div className="col">
                        <h2>Request a recommendation from Bookbot</h2>
                    </div>
                </div>
            </div>
        </React.Fragment>
    );
};

ReactDOM.render(<SubmitForm/>, document.getElementById('root'))





// use fetch post request with async/wait?



// react fragment


// <h2>Request a recommendation from Bookbot</h2>

// <form action='/recommendation-request' method="POST">
//     <div className="form-group">
//         <label for="username">Your Name</label>
//         <input
//         id="search-name"
//         className="form-control"
//         type="text"
//         name="username"
//         placeholder="Edmond Dantès"
//         required></input>
//     </div>

//     <div className="instructions">Please input your requested search criteria below and Bookbot will find your match!</div>

//     <div className="form-group">
//         <label for="request-genre">Genre</label>
//         <option></option>
//         <select name="genre"
//         id="search-genre"
//         className="form-control"
//         required>
        
//         <option value="" disabled="disabled">Please select an option</option>
//         {/* add loop here over genres in db */}
//         for (genre of genres_list) {
//             <option value="{ genre }">{ genre }</option>
//         }
//         </select>

//     </div>

// </form>
