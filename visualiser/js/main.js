
window.addEventListener('load', function() {
    var updateStatus = (function() {
        var status = document.querySelector('.status');
        return function(newStatus) {
            status.textContent = newStatus;
        }
    })();

    var fileInput = document.querySelector('.galiasFileInput');
    var selector = new JsonFileSelector(fileInput, updateStatus, visualiseData);


    function visualiseData(input) {
        console.log('visualise', input);
        // TODO: Implement Cesium visualisation here.
    }

});
