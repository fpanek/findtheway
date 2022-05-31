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
    document.getElementById("popup-1")
        .classList.toggle("active");
}

function toggleSignUpPopup() {
    document.getElementById("popup-2")
        .classList.toggle("active");
}
