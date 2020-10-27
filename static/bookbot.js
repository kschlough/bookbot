"use strict";

// return to homepage
function returnHome() {
    window.location.href = "/";
};

$('#resubmit-button').on('click', returnHome);


// custom form fillout validation message
function invalidField() {
    alert("Please fill out this field");
};

$('#search-name').on('invalid', invalidField);
$('#search-kw').on('invalid', invalidField);






