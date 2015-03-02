function toggle(elementId) {
var ele = document.getElementById(elementId);
if(ele.style.display == "block") {
ele.style.display = "none";
}
else {
ele.style.display = "block";
}}
function hide(elementId) {
var ele = document.getElementById(elementId);
ele.style.display = "none";
}
function load(example, path) {
var ele = document.getElementById(example);
ele.innerHTML = '<iframe id=\''+ example+'_frame\' seamless src=\'' + path + '\' frameborder=\'0\' width=\'800px\' height=\'700\'></iframe>';
if(ele.style.display == "block") {
ele.style.display = "none";
}
else {
ele.style.display = "block";
}}

function autoResize(id){
var newheight=document.getElementById(id).document.body.scrollHeight;
var newwidth=document.getElementById(id).document.body.scrollHeight;
document.getElementById(id).height= (newheight) + "px";
document.getElementById(id).width= (newwidth) + "px";
}


document.write('\
</head>\
\
<body>\
<table style="width:100%;" >\
<tr>\
<td valign="top" border="1">\
<div id="content">\
');

