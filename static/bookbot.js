"use strict";

// return to homepage
function returnHome() {
    window.location.href = "/";
};

$('#home').on('click', returnHome);

// return to resubmit form again
function resubmitForm() {
    window.location.href = "/form";
};

$('#resubmit-button').on('click', resubmitForm);


// // test - single page for form submit
// // listen for form button click
// function submitForm() {
    
// };

// $('#submit-form-button').on('click', submitForm);







