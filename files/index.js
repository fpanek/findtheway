$(document).ready(function() {
    let buttons = document.querySelectorAll(".close-btn");
    buttons.forEach(function (btn) {
      let parent = btn.parentElement.parentElement.id;
        $(btn).click(function(){
            if (parent === "popup-1") {
                document.querySelector("#login-form").reset();
            }
            if (parent === "popup-2") {
                document.querySelector("#signup-form").reset();
            }
        });
    });
});

function toggleLoginPopup() {
    document.querySelector("#popup-1")
        .classList.toggle("active");
}

function toggleSignUpPopup() {
    document.querySelector("#popup-2")
        .classList.toggle("active");
}

function getLocation() {
    const result = document.querySelector("#location");
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            result.innerHTML = "Geolocation is not supported by this browser.";
        }

    function showPosition(position) {
        result.innerHTML = "Your current coordinates are: " + position.coords.latitude + " Latitude, " + position.coords.longitude + " Longitude";
    }
}

function getResults() {
    getLocation();
    let request = new XMLHttpRequest();
    request.open("GET", "http://84.115.66.50:5000/getstations?long=48.20995&lat=16.37416&rad=80", false);
    request.send(null);
    let my_JSON_object = JSON.parse(request.responseText);

    request.onload = function() {
        let ul = document.createElement("ul");
        ul.setAttribute("id", "list-of-results");

        for (let x in my_JSON_object) {
            let listElement = document.createElement("li");
            listElement.appendChild(document.createTextNode(my_JSON_object[x].name + " [" + my_JSON_object[x].stationType + "], " + my_JSON_object[x].distance + "m"));
            ul.appendChild(listElement);
        }
        let title = document.createElement("p");
        title.textContent = "Your results:";
        document.querySelector("#results").appendChild(title);
        document.querySelector("#results").appendChild(ul);
    }
    request.open("POST", "mainpage.html", true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("x=" + my_JSON_object);
}