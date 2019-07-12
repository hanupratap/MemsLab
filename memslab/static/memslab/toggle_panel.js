function togglePanel (){
    var w = $(window).width();
    if (w <= 768) {
       $('#collapseExample').removeClass('show');
       $('#collapseExample1').removeClass('show');
       $('#coll').removeClass('show');
    } else {
       $('#collapseExample').addClass('show ');
       $('#collapseExample1').addClass('show');
       $('#coll').addClass('show');
 
    }
 }
 $(window).resize(function(){
      togglePanel();
 });
 
 togglePanel();