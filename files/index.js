$('#body').css('min-height', screen.height);
let userPosition = null;
let googleMap = null;

function getCookie(name) {
    let match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
}

function initMap() {
    let mapProp = {
        center: new google.maps.LatLng(48.210033,16.363449),
        zoom: 12,
    };
    googleMap = new google.maps.Map(document.querySelector("#map"), mapProp);
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getResults);
    } else {
        document.querySelector("#getResultsButton").appendChild(document.createTextNode("Geolocation is not supported by this browser."));
    }
}

function showCurrentPosition() {
    let infoWindow = new google.maps.InfoWindow();
    infoWindow.setPosition(userPosition);
    infoWindow.setContent("You are here! ");
    infoWindow.open(googleMap);
    googleMap.setCenter(userPosition);
    googleMap.setZoom(16);
}

function getResults(position) {
    let latitude = position.coords.latitude; // 48.210033
    let longitude = position.coords.longitude; // 16.363449
    let userDistance = document.querySelector("#chosenDistance").value;
    userPosition = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
    };

    let request = new XMLHttpRequest();
    request.open("GET", `//findtheway.geokhugo.com:5000/getstations?long=${latitude}&lat=${longitude}&rad=${userDistance}`, false);
    request.withCredentials = true;
    request.send(null);
    let my_JSON_object = JSON.parse(request.responseText);
    reload();

    request.onload = function() {
        let count = 1;
        for (let x in my_JSON_object) {
            for (let y in my_JSON_object[x]) {
                if (my_JSON_object[x][y]["stationName"] !== undefined) {
                    let tr = document.createElement("tr");
                    tr.setAttribute("class", "hover");

                    let thCount = document.createElement("th");
                    thCount.textContent = String(count);

                    let stationName = document.createElement("td");
                    let stationType = document.createElement("td");
                    let stationDistance = document.createElement("td");

                    stationName.textContent = (my_JSON_object[x][y]["stationName"]);
                    stationType.textContent = (my_JSON_object[x][y]["stationType"]);
                    stationDistance.textContent = (my_JSON_object[x][y]["distance"] + "m");

                    let stationPosition = { lat: Number(my_JSON_object[x][y]["long"]), lng: Number(my_JSON_object[x][y]["lat"]) };
                    if (count <= 5) {
                        const marker = new google.maps.Marker({
                            position: stationPosition,
                            label: String(count),
                            map: googleMap,
                        });
                    }

                    let thButton = document.createElement("th");
                    let btn = document.createElement("button");
                    btn.textContent = 'details';
                    btn.setAttribute("class", "btn btn-ghost btn-xs");
                    thButton.appendChild(btn);

                    tr.append(thCount);
                    tr.append(stationName);
                    tr.append(stationType);
                    tr.append(stationDistance);
                    tr.append(thButton);
                    document.querySelector("#stations").appendChild(tr);
                    ++count;
                }
            }
        }
    }

    request.open("POST", "mainpage.html", true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("x=" + my_JSON_object);
    showCurrentPosition();
}

function reload() {
    let stationsList = document.querySelector("#stations");
    let child = stationsList.lastElementChild;
    while (child) {
        stationsList.removeChild(child);
        child = stationsList.lastElementChild;
    }
    initMap();
}

function makeRequest() {
    const url = "https://findtheway.geokhugo.com:5000/login";
    fetch(url, {
        method : "POST",
        body: new FormData(document.getElementById("inputform")),
    }).then(response => {
        if (response.status === 200) {
            response.open("POST", "mainpage.html", true);
            response.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        }
    }).catch(error => {
        console.error('There was an error!', error);
    });
}

function signupRequest() {
    const url = "https://findtheway.geokhugo.com:5000/signup";
    fetch(url, {
        method : "POST",
        body: new FormData(document.getElementById("registration-form")),
    }).then(response => {
        if (response.status === 200) {
            response.open("POST", "index.html", true);
            response.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        }
    }).catch(error => {
        console.error('There was an error!', error);
    });
}

function logOut() {
    let request = new XMLHttpRequest();
    request.open("POST", `https://findtheway.geokhugo.com:5000/logout`);
    request.withCredentials = true;
    location.href = "index.html";
}