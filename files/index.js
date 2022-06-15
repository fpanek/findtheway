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
    request.open("GET", "testdata.json", false);
    request.send(null);
    let my_JSON_object = JSON.parse(request.responseText);
    console.log(my_JSON_object);

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