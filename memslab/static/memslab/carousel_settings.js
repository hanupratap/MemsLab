
$(window).on('load', function () {
 
    $("#owl-demo").owlCarousel({
       navigation : true, // Show next and prev buttons
       //decomment for text buttions     //navText:["<h3>Prev</h3>","<h3>Next</h3>"], 
       
       // decommecnt for arrow buttons   //  //decomment fro stock buttons     //
  
       slideSpeed : 300,
       paginationSpeed : 400,
       autoHeight:true,
       loop:true,
       items:1,
       dots:true,
       lazyLoad: true,
       autoplay:true,
       lazyload:true,
       autoplayTimeout:4000,
       autoplayHoverPause:true,
       center:true,
       responsiveClass:true,
  
       responsive:{
         0:{
             margin:10,
             nav:false,
           
         },
         600:{
             margin:20,
             nav:false,
             
         },
         1400:{
           margin:30,
             nav:true,
             navText : ["<button class='btn btn-default ' > <i class='fas fa-angle-left fa-3x' ></i></button>","<button class='btn btn-default  bg-transparent  '> <i class='fas fa-angle-right fa-3x'></i></button>"],
         }
     }
      
 
   });
 });
 
   