function login_window_button() {
    var t_login = document.getElementById("login_input")
    var t_password = document.getElementById("password_input")
    // console.log(t_login.value)
    // console.log(t_password.value)
    if (t_login.value == "admin" && t_password.value == "admin") {
        document.getElementById("login_window").style.display = "none"
        document.getElementById("registred_window").style.display = "block"
    }
}
function home_window_button() {
    document.getElementById("home_window").style.display = "block";
    document.getElementById("new_window").style.display = "none";
    document.getElementById("account_window").style.display = "none";
}
function new_window_button() {
    document.getElementById("home_window").style.display = "none";
    document.getElementById("new_window").style.display = "block";
    document.getElementById("account_window").style.display = "none";
}
function account_window_button() {
    document.getElementById("home_window").style.display = "none";
    document.getElementById("new_window").style.display = "none";
    document.getElementById("account_window").style.display = "block";
}

function dropHandler(ev) {
  console.log('File(s) dropped');

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();

  if (ev.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    for (var i = 0; i < ev.dataTransfer.items.length; i++) {
      // If dropped items aren't files, reject them
      if (ev.dataTransfer.items[i].kind === 'file') {
        var file = ev.dataTransfer.items[i].getAsFile();
        console.log('... file[' + i + '].name = ' + file.name);
      }
    }
  } else {
    // Use DataTransfer interface to access the file(s)
    for (var i = 0; i < ev.dataTransfer.files.length; i++) {
      console.log('... file[' + i + '].name = ' + ev.dataTransfer.files[i].name);
    }
  }
}

function handleFiles(files) {
    console.log('got')
    console.log(files)
}

//delete it
function login() {
    document.getElementById("login_window").style.display = "none"
}
