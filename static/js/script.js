const popup = document.getElementById("pop-up");
const backdrop = document.getElementById("backdrop");

function openPopup() {
    popup.classList.replace("opacity-0", "opacity-1");
    popup.classList.replace("pointer-events-none", "pointer-events-default");
    backdrop.classList.replace("opacity-0", "opacity-75");
    backdrop.classList.replace("pointer-events-none", "pointer-events-default");
}

function closePopup() {
    popup.classList.replace("opacity-1", "opacity-0");
    popup.classList.replace("pointer-events-default", "pointer-events-none");
    backdrop.classList.replace("opacity-75", "opacity-0");
    backdrop.classList.replace("pointer-events-default", "pointer-events-none");
}