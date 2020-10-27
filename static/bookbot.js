"use strict";

// return to homepage
const returnHome = () => {
    window.location.href = "/";
};

$("#resubmit-button").on('click', returnHome);


// custom form fillout validation message
const invalidField = () => {
    alert("Please fill out this field");
};

$("#search-name").on('invalid', invalidField);
$('#search-kw').on('invalid', invalidField);






