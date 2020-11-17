"use strict";

// return to homepage
function returnHome() {
    window.location.href = "/";
};

$('#resubmit-button').on('click', returnHome);


// custom form fillout validation message
function invalidName() {
    alert("Please fill out your name");
};

$('#search-name').on('invalid', invalidName);










