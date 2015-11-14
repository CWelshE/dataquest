// ACE settings
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");

// Current Session
var sesh = editor.getSession();
sesh.setMode("ace/mode/python");

var codeForm = document.getElementById("form-runcode");
var output = document.getElementById("output");

// Won't work unless we send this along!
var csrf = Cookies.get('csrftoken');

// Sends the user's code off and waits for a response
var getCode = function(data)
{
  var params = "code=" + encodeURIComponent(data);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function()
  {
    if(xhttp.readyState == 4 && xhttp.status == 200)
    {
      output.innerHTML = xhttp.responseText;
    }
  };
  xhttp.open("POST", "get_code/", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  // Django-specific header
  xhttp.setRequestHeader("X-CSRFToken", csrf);

  xhttp.send(params);
}

// Asynchronous code running func
var runCode = function(ev)
{
  ev.preventDefault();
  console.log("Submit event emitted");
  getCode(editor.getValue());
};

codeForm.addEventListener("submit", runCode, false);
