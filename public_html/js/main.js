
//NICE SCROLLS
var options = {cursorwidth:10,cursorcolor:'#469F46',horizrailenabled:false};
jQuery('#article-list-inner').niceScroll(options);
jQuery('#tweet-list-inner').niceScroll(options);

// get the search term 

// get the search string 
var search;
$(".search-btn").click(function() {
    search  = $('#searchfield').val();
  uploadData(search);
});

function uploadData(search){
    jQuery.ajax({
        url: "http://127.0.0.1:8080/search="+search,
        type: "get",
        data: search,
        success: function(){
            alert("success");
            $("#result").html('Submitted successfully');
        },
        error:function(err){
            console.log("failure", err);
            $("#result").html('There is error while submit');
        }
    });
}

function createArticles(result){
    var list = '';
    jQuery.each(result,function(index,value){
        list += '<li>';
      list += '<h4><a href="'+value.link+'">'+value.title+'</a></h4>';
        list += '<small class="text">'+value.desc+'</small>';
        list += '</li>';
		console.log(list);
    });
    jQuery('#article-list-inner ul').html(list);
}

function createTweets(result){
    var list = '';
	
    jQuery.each(result,function(index,value){
        list += '<li>';
		var  a= '<a href="'+ value.link+'">'+value.title+'</a>';
		console.log(a);
		list+=a;
 //       list += '<h4><a href="'value.link+'">'+value.title+'</a></h4>';
//        list += '<small class="text">'+value.desc+'</small>';
        list += '</li>';
    });
	
    jQuery('#tweet-list-inner ul').html(list);
}

/* for dev only !!!!!!!!!! */

var rs = [
		 {"title": "For privacy and security, use public keys everywhere", "link":"http://delivery.acm.org/10.1145/2510000/2500482/p8-staff.pdf?ip=195.234.136.80&id=2500482&acc=OPEN&key=6C7A71C0BB72CF03B63DD39781D6142F&CFID=393859988&CFTOKEN=19318825&__acm__=1388478780_485942e6ae2b8a7e5841919a4579f328", "desc":"really???"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u need a description really??? do u need a description really??? do u need a description"}
];

var rs2 = [
		{"title":"Tweet 1", "link": "https://twitter.com/mojosd/status/371070280774324224", "desc":"This is a tweet"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description real"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? "},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do"},
        {"title":"test 1","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? do u nee"}
];
        
createArticles(rs);
createTweets(rs2); 
/* end for dev only */
