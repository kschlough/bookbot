"use strict";

function returnHome() {
    location.href = "/"
    // needs to return to homepage, no web address right now while in localhost
}

$("resubmit-button").on('click', returnHome);







