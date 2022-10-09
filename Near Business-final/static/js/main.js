let access_permission = document.getElementById("access_location");
let location_element = document.getElementById("location");
let long = document.getElementById("longitude");
let lat = document.getElementById("latitude");
const searchForm = document.forms["form"];


access_permission.addEventListener("change", (e) => {
    if (e.target.checked) {
        console.log("Checkbox is checked..");
        location_element.value = "";
        location_element.disabled = true;
        getLocation();
    } else {
        location_element.disabled = false;
        console.log("Checkbox is not checked..");
    }
});


function submitSearchForm(event) {
    console.log("submit button");
    const formData = new FormData(event.target);
    formObj = {};

    for (const [fieldName] of formData) {
        const fieldValue = formData.getAll(fieldName);
        formObj[fieldName] = fieldValue.length == 1 ? fieldValue.toString() : fieldValue
    }
    console.log('formObj', formObj)

    $(document).ready(function () {
        $.ajax({
            method: 'POST',
            url: 'http://127.0.0.1:5000/search/',
            contentType: "application/json",
            data: JSON.stringify({ 'formObj': formObj }),
            success: function (data) {
                //this gets called when server returns an OK response
                console.log("it worked!");
            },
            error: function (data) {
                console.log("it didnt work");
            }
        });
    });

}


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);

    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    // x.innerHTML = "Latitude: " + position.coords.latitude +
    // "<br>Longitude: " + position.coords.longitude;
    lat.value = position.coords.latitude;
    long.value = position.coords.longitude;
    console.log("longitude: ", position.coords.longitude);
    console.log("latitude: ", position.coords.latitude);
}
