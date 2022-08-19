function showWorkingIndicator(data) {
    showIndicatorRegion(data, "workingIndicator");
}
function showIndicatorRegion(data, spinnerRegionId) {
    if (data.status === "begin") {
        showElement(spinnerRegionId);
    } else if (data.status === "complete") {
        hideElement(spinnerRegionId);
    }
}

function showElement(id) {
    document.getElementById(id).style.display = "block";
}
function hideElement(id) {
    document.getElementById(id).style.display = "none";
}
