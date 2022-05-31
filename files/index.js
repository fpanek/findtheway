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

function getSortOrder(prop) {
    return function(a, b) {
        if (a[prop] > b[prop]) {
            return 1;
        } else if (a[prop] < b[prop]) {
            return -1;
        }
        return 0;
    }
}

function jsonToArray(my_JSON_object) {
    const obj = JSON.parse(my_JSON_object);
    const res = [];

    for(const i in obj) {
        res.push(obj[i]);
    }
    return res;
}

function getResults() {
    getLocation();
    let request = new XMLHttpRequest();
    request.open("GET", "../../files/testdata.json", false);
    request.send(null);
    let my_JSON_object = JSON.parse(request.responseText);

    request.onload = function() {
        for (let x in my_JSON_object) {
            let listElement = document.createElement("li");
            let itemName = document.createElement("span");
            itemName.textContent = "Station: " + my_JSON_object[x].name + " [" + my_JSON_object[x].stationType + "], " + my_JSON_object[x].distance + "m";
            listElement.append(itemName);
            document.querySelector("#list-of-results").append(listElement);
        }
    }
    request.open("POST", "mainpage.html", true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("x=" + my_JSON_object);
}