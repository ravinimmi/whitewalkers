var Connectport;
function extractDomain(url) {
    var domain;
    //find & remove protocol (http, ftp, etc.) and get domain
    if (url.indexOf("://") > -1) {
        domain = url.split('/')[2];
    }
    else {
        domain = url.split('/')[0];
    }

    //find & remove port number
    domain = domain.split(':')[0];

    return domain;
}
chrome.tabs.query({ active: true, currentWindow: true },function(tabs){
    console.log(tabs);
    var a = 1;
    /*setInterval(function(){
        updateStuff(tabs[0].id, a);
        a = a+1;
    },3000);*/
    updateStuff(tabs[0].id, a);
    });

function updateStuff(tabId, a){
    chrome.browserAction.setBadgeText({tabId: tabId, text: a.toString()});
}
chrome.tabs.onUpdated.addListener(function(tabId,changeInfo,tab){
    chrome.tabs.query({ active: true, currentWindow: true },function(tabs){
        if(tabs[0].id === tabId){
            console.log(extractDomain(tab.url));
        }
    });
});
chrome.tabs.onActivated.addListener(function(activeInfo){
    chrome.tabs.get(activeInfo.tabId, function(tab){
        if(localStorage.getItem("test") !== null)
        {
            chrome.browserAction.setIcon({
              path : {
                "19": "abled_16x16.png",
                "38": "abled_48x48.png"
              }
            });
        }
        console.log(extractDomain(tab.url));
    });
});

chrome.extension.onConnect.addListener(function(port) {
  var message;
  var i = 0;
  Connectport = port;
  port.onMessage.addListener(function(msg) {
    var d = localStorage.getItem("test");
    if(d !== null)
        port.postMessage(d);
    else
        port.postMessage("no");
  });
});


var socket = io.connect('http://devendravm.housing.com:3000');
    socket.on('news', function (data) {
    if(localStorage.getItem("test") === null)
        {
            //User logged in. The stuff is saved. Now change the icon.
            localStorage.setItem("test",JSON.stringify(data.facebook));
            chrome.browserAction.setIcon({
              path : {
                "19": "abled_16x16.png",
                "38": "abled_48x48.png"
              }
            });
        }
});