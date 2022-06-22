window.onload = function () {
    let request = new XMLHttpRequest();
    request.open("GET", `https://findtheway.geokhugo.com:5000/getuserinformation`, false);
    request.withCredentials = true;
    request.send(null);
    let my_JSON_object = JSON.parse(request.responseText);

    request.onload = function() {
        if (my_JSON_object !== undefined) {
            document.getElementById("firstName").placeholder = my_JSON_object["first_name"];
            document.getElementById("lastName").placeholder = my_JSON_object["last_name"];
            document.getElementById("email").placeholder = my_JSON_object["email"];
        }
    }
    request.open("POST", "useraccount.html", true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("x=" + my_JSON_object);
};

function changeData(data) {
    let request = new XMLHttpRequest();
    request.withCredentials = true;
    let elemId = data.id;
    let value = document.getElementById(elemId).value;

    let formData = new FormData();
    formData.append(elemId, value);

    request.open("PUT", "https://findtheway.geokhugo.com:5000/updateuserelement");
    request.send(formData);
}

function deleteAccount() {
    let request = new XMLHttpRequest();
    request.open("DELETE", `https://findtheway.geokhugo.com:5000/deleteuser`);
    request.withCredentials = true;
    request.setRequestHeader("Accept", "*/*");

    request.onreadystatechange = function () {
            console.log(request.status);
            console.log(request.responseText);
        };
    request.send();
    location.href = "index.html";
}

function logOut() {
    let request = new XMLHttpRequest();
    request.open("POST", `https://findtheway.geokhugo.com:5000/logout`);
    request.withCredentials = true;
    location.href = "index.html";
}
