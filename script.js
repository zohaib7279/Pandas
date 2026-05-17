// DARK MODE SAVE
if(localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
}

function toggleMode() {
    document.body.classList.toggle("dark-mode");

    if(document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// LOGIN VALIDATION
function loginUser() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username === "admin" && password === "1234") {
        alert("Login Successful");
    } else {
        alert("Wrong Username or Password");
    }
}