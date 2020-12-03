"use strict";

// return to homepage
function returnHome() {
    window.location.href = "/form";
};

$('#resubmit-button').on('click', returnHome);


// custom form fillout validation message
function invalidName() {
    alert("Please fill out your name");
};

$('#search-name').on('invalid', invalidName);

// get homepage options on hover
function Options() {
    var bookbotMenu = $('<div className="homepage-text">Text</div>');
    document.body.appendChild(bookbotMenu);
}

$('#root').on('click', Options);








