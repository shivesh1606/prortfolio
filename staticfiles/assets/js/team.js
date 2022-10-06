let alumni=document.querySelector("div .alumni");
let team=document.querySelector("div .team");
let alumnibutton=document.getElementById("alumnibutton");
let teambutton=document.getElementById("teambutton");

alumni.style.display="none";
team.style.display="grid";

teambutton.addEventListener("click",function(){
    team.style.display="grid";
    alumni.style.display="none";
})
alumnibutton.addEventListener("click",function(){
    alumni.style.display="grid";
    team.style.display="none";
   
})



