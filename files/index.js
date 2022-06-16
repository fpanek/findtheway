function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getResults);
    } else {
        document.querySelector("#getResultsButton").appendChild(document.createTextNode("Geolocation is not supported by this browser."));
    }
}

function getResults(position) {
    let lat = position.coords.latitude;
    let lon = position.coords.longitude;
    let userDistance = document.querySelector("#chosenDistance").value;

    let request = new XMLHttpRequest();
    request.open("GET", `http://findtheway.geokhugo.com:5000/getstations?long=${lon}&lat=${lat}&rad=${userDistance}`, false);
    request.send(null);
    let my_JSON_object = JSON.parse(request.responseText);
    reload();

    request.onload = function() {
        let count = 1;
        for (let x in my_JSON_object) {
            for(let y in my_JSON_object[x]){
                if(my_JSON_object[x][y]["stationName"] !== undefined) {
                    let tr = document.createElement("tr");
                    tr.setAttribute("class", "hover");

                    let thCount = document.createElement("th");
                    thCount.textContent = String(count);

                    let stationName = document.createElement("td");
                    let stationType = document.createElement("td");
                    let stationDistance = document.createElement("td");

                    stationDistance.textContent = (my_JSON_object[x][y]["distance"]);
                    stationType.textContent = (my_JSON_object[x][y]["stationType"]);
                    stationName.textContent = (my_JSON_object[x][y]["stationName"]);

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
    console.log("end of index.js");
}

function reload() {
    let stationsList = document.querySelector("#stations");
    let child = stationsList.lastElementChild;
    while (child) {
        stationsList.removeChild(child);
        child = stationsList.lastElementChild;
    }
    console.log("Refreshed");
}