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




