'use strict'


// jquery to change background color based on dynamically rendered shift id

for(let i = 0; i < $('.shift').length; i++) {
    // grey
    $('.need0').css("background-color", "#d3d3d3");
    $('.need0').css("color", "grey");
    // green
    $('.need1').css("background-color", '#32cd32');
    // yelow
    $('.need2').css("background-color", "#ffff00");
    $('.need2').css("color", "grey");
    // red
    $('.need3').css("background-color", "#dc143c");
}
