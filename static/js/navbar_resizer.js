/* automatically shift body down by whatever is the size of navbar */
/* from https://stackoverflow.com/questions/14735274/bootstrap-css-hides-portion-of-container-below-navbar-navbar-fixed-top */


var onResize = function() {
  // apply dynamic padding at the top of the body according to the fixed navbar height
  $("body").css("padding-top", $(".navbar-fixed-top").height()+20 );
};

// attach the function to the window resize event
$(window).resize(onResize);

// call it also when the page is ready after load or reload
$(function() {
  onResize();
});
