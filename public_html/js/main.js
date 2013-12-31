
//NICE SCROLLS
var options = {cursorwidth:10,cursorcolor:'#469F46',horizrailenabled:false};
jQuery('#article-list-inner').niceScroll(options);
jQuery('#tweet-list-inner').niceScroll(options);

//AJAX FOR DATA POST
/* Get some values from elements on the page: */
//var values = $(this).serialize();

jQuery(document).ready(function(){
    uploadData();
});

function uploadData(){
    jQuery.ajax({
        url: "test.php",
        type: "post",
        data: values,
        success: function(){
            alert("success");
            $("#result").html('Submitted successfully');
        },
        error:function(){
            alert("failure");
            $("#result").html('There is error while submit');
        }
    });
}

function createArticles(result){
    var list = '';
    jQuery.each(result,function(index,value){
        list += '<li>';
        list += '<h4><a href="//'+value.link+'">'+value.title+'</a></h4>';
        list += '<small class="text">'+value.desc+'</small>';
        list += '</li>';
    });
    jQuery('#article-list-inner ul').html(list);
}

function createTweets(result){
    var list = '';
    jQuery.each(result,function(index,value){
        list += '<li>';
        list += '<h4><a href="//'+value.link+'">'+value.title+'</a></h4>';
        list += '<small class="text">'+value.desc+'</small>';
        list += '</li>';
    });
    jQuery('#tweet-list-inner ul').html(list);
}

/* for dev only !!!!!!!!!! */

var rs = [
                {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"}
];

var rs2 = [
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description real"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? "},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u nee"}
];
        
createArticles(rs);
createTweets(rs);
/* end for dev only */