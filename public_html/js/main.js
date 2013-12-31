
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
		 {"title": "For privacy and security, use public keys everywhere", "link":"http://delivery.acm.org/10.1145/2510000/2500482/p8-staff.pdf", "desc":"Communications of the ACM Sept 2013"},
        {"title":"Seeing Double: Reconstructing Obscured Typed Input from Repeated Compromising Reflections","link":"http://delivery.acm.org/10.1145/2520000/2516709/p1063-xu.pdf","desc":"2013"},
        {"title":"Retweeting the Fukushima nuclear radiation disaster","link":"http://dl.acm.org/citation.cfm?id=2500881","desc":"2014"},
        {"title":"Three keys to the radiation of angiosperms into freezing environments","link":"http://www.nature.com/nature/journal/vaop/ncurrent/full/nature12872.html","desc":"Nature Dec 2013"},
        {"title":"Performance Troubleshooting in Data Centers: An Annotated Bibliography","link":"http://www.cc.gatech.edu/~flinter/annotated.pdf","desc":"ACM SIGOPS 2013"},
        {"title":"Bodily maps of emotions","link":"http://www.pnas.org/content/early/2013/12/26/1321664111","desc":"PNAS Dec 2013"},
];

var rs2 = [
        {"title":"@miakiza20100906: 論文（有料）： 福島原子力災害をリツイート http://dl.acm.org/citation.cfm?id=2500881 … 　2014年、Li（米国）ら。詳細不明。おそらく、日本政府のツイッターによる情報発信に関するもの。","link":"www.google.co.il","desc":"really??? do u need a description,really??? do u need a description really??? "},
		{"title":"@mikko: Most novel research I saw in 2013: http://t.co/Bg0KrPEeiM Stealing your smartphone PIN - by shooting a video of your eyeball's r…", "link": "https://twitter.com/mojosd/status/371070280774324224", "desc":""},
    {"title":"@henare: \"Retweeting the Fukushima nuclear radiation disaster\"  http://feedly.com/k/1kSlPfs ","link":"https://twitter.com/henare/status/417246186177699840","desc":"really??? do u need a description,really??? do u need a description real"},
    {"title":"@petermeyers: The bohemian bookshelf https://dl.acm.org/citation.cfm?id=2207676.2208607&coll=DL&dl=GUIDE&CFID=392891878&CFTOKEN=86794380#.Ur5CJ7x8C_Y.twitter … \"exploration into the use of information visualization to support serendipity.\"","link":"https://twitter.com/petermeyers/status/416769558788071426","desc":"really??? do u need a description,really??? do u need a description real"},
{"title":"Nature: Three keys to the radiation of angiosperms into freezing environments http://www.nature.com/nature/journal/vaop/ncurrent/full/nature12872.html … http://sco.lt/63Xh6P ","link":"https://twitter.com/PlantTeaching/status/417697491631755264","desc":"really??? do u need a description,really??? do u need a description real"}
];
        
createArticles(rs);
createTweets(rs2); 
/* end for dev only */
