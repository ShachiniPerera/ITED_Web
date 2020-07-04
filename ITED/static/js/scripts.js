/*!
    * Start Bootstrap - Agency v6.0.1 (https://startbootstrap.com/template-overviews/agency)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-agency/blob/master/LICENSE)
    */




    $(document).ready(function(){

    var stopAutohide;

    function showWindow(){
    $('#main').show();
    // stop scroll
    $('html body').css('overflow','hidden');
     stopAutohide = setTimeout(hideWindow,10000);
    }
   // showWindow()
    function hideWindow(){

    $('#main').hide();
    // on scroll
    $('html body').css('overflow','scroll');
    // auto hide



    }
   // hideWindow()
   // now call  function automatically after some time

   setTimeout(showWindow,1000);

   //close after click
   $("#close-btn").click(function(){

   hideWindow();
   celarTimeout(stopAutohide);


   hideWindow();
   })

    })



    (function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 72,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav",
        offset: 74,
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top


    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery); // End of use strict
