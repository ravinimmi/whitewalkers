$(function() {
    var chosenQuestion = 0;
    var stepSize = 0;
    var d = localStorage.getItem("test");
    var profile =  (d !== null) ? JSON.parse(d) : null;

    //var qlist = [{"question_id": 5, "question": "DeathNote rocks", "template_id": 4, "template_type": "image", "options": ["http://i.imgur.com/21AtcQH.png", "http://i.imgur.com/us9lq8G.jpg"]},{"question_id": 10, "question": "GOT rocks?", "template_id": 4, "template_type": "single", "options": ["agree", "disagree"]}];
    //var qlist = [{"question_id": 1, "question": "DeathNote rocks", "template_id": 4, "template_type": "single", "options": ["agree", "disagree"]},{"question_id": 2, "question": "GOT rocks?", "template_id": 4, "template_type": "single", "options": ["agree", "disagree"]}];
    var qlist = [];
  
  if(profile === null)
  { 
    //show login screen and stuff
    $("#question").html("");
    $("#question").append('<p>Get rewarded everytime you submit a survey!</p>');
    $("#question").append('<a target="_blank" href="http://devendravm.housing.com:3000/auth/facebook/"><img src="img/facebook_login.png"></a>');
    $("#couponProgress").hide();
  }
  else{
  $("#profileImage").attr("src",'http://graph.facebook.com/v2.2/'+profile.id+'/picture');
  var status = localStorage.getItem("status");
  if(status === "login" || status === null)
    populateCoupons();
  else
    {
      $("#couponProgress").show();
      $.ajax({
      url: "http://ravin.housing.com:8000/get_questions_extension?user_id="+profile.email
      }).done(function(data) {
        qlist = JSON.parse(data);
        console.log(data);
        console.log(qlist);
        stepSize = Math.ceil(100/qlist.length);
        parseQuestions(qlist,chosenQuestion);
      });
    }
  }
   /* $.ajax({
      url: "http://ravin.housing.com:8000/get_questions?email_id="+profile.email
    }).done(function(data) {
        qlist = JSON.parse(data);
        parseQuestions(qlist,chosenQuestion);
    });*/
  console.log(stepSize);
  function renderOptions(options,qtype){
    var str= "";
      options.forEach(function(op){
        if(qtype !== "image" ){
          str+= '<label class="mdl-radio" for="'+op+'">';
          str+= '<input type="radio" class="mdl-radio__button" name="options" value="'+op+'"/>';
          str+= '<span class="mdl-radio__label">'+op+'</span></label>';
        }
        else {
          str+= '<div class="qimages"><img class="crop" src="'+op+'"/>';
          str+= '<input type="radio" class="mdl-radio__button" name="options" value=""/></div>';
        }
      });
    return str;
  }
  function parseQuestions(qlist, qId){
      //console.log(qId);
      //console.log(qlist);
      //Show in pop up and remove from qlist
      if(qId < qlist.length){
        $("#question").html("");
        var str = "";
        var q = qlist[qId];
        str += "<p>"+q.question_text+"</p>";
        str += renderOptions(q.options,q.template_type);
        /*q.options.forEach(function(op){
          str+= '<label class="mdl-radio" for="'+op+'">';
          str+= '<input type="radio" class="mdl-radio__button" name="options" value="'+op+'"/>';
          str+= '<span class="mdl-radio__label">'+op+'</span></label>'
        });*/
        str+= '<br><br><button id="submit" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">Next</button>';
        $("#question").html(str);
        //Upgrade to Material Components :)
        componentHandler.upgradeElements(document.body);
        //update Quetion Number
        chosenQuestion = qId + 1;
        $("#qno").text("("+chosenQuestion+"/"+qlist.length+")");
      }
      /*if(result !== -1)
        qlist.splice(result, 1);*/
  }; 

  $( "#question" ).on( "click", "img.offers", function() {
      localStorage.setItem("status","questions");
      parseQuestions(qlist,chosenQuestion);
      $("#couponProgress").show();
  });

  $( "#question" ).on( "click", "#submit", function() {
      var data = {};
      req_val = '"'+$("#question input:radio[name=options]:checked").val()+'"';
      if(qlist[chosenQuestion-1].template_type == "image")
        {
          var a = $("#question input:radio[name=options]:checked").siblings();
          req_val = $(a[0]).attr("src");
        }
      data.options = [req_val];
      data.user_id = profile.email;
      data.question_id = qlist[chosenQuestion-1].question_id;
      console.log(data);
      $.ajax({
        method: "POST",
        url: "http://ravin.housing.com:8000/send_response",
        data: data
      })
       .done(function( msg ) {
          var progress = chosenQuestion*stepSize;
          
          if(chosenQuestion === qlist.length)
            { 
              progress = 100;
              localStorage.setItem("status","login");
              populateCoupons();
              //Show coupon chooser here
              //Also set the state in the background somewhere
            }
          document.querySelector('#p1').MaterialProgress.setProgress(progress);
          parseQuestions(qlist,chosenQuestion);
      });
  });

  var port = chrome.extension.connect({name: "Sample Communication"});
    port.postMessage("Hi BackGround");
    port.onMessage.addListener(function(msg) {
      if(msg !== "no"){
        //That means got data
        profile = JSON.parse(msg);       
        $("#status").html(profile.name);
      }
  });

  function populateCoupons(){
    $("#question").html("");
    $("#couponProgress").hide();
    var i =1;
    while(i<7)
    {
      var str= '<div class="cuopons"><img class="offers" src="../img/'+i+'.png" /></div>';
      $("#question").append(str);
      i++;
    }
  };
});