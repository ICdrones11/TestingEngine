/*
    JsonFileSelector - calls a function when a file is selected
    through a provided file input and parsed as JSON.

    Initially tries to read current URL hash as a filename and parse that as JSON.
*/

function JsonFileSelector(fileInput, updateStatus, onJSONCb) {
    /*
        fileInput - HTML input element to use for file selection.
        JSONcb  - function to call when a file is read as JSON.
        updateStatus - function to give status updates to.
    */

    var inputFilename = parseInputFilename(); // returns null if error
    if (inputFilename) {
        fetchJSON(inputFilename).then(onJSONCb)
        .catch(function(err) {
            updateStatus('Error loading file at "' + inputFilename + '".');
        });
    }
    // TODO: Init manual file select from filesys here.

    function fetchJSON(url) {
        return window.fetch(url).then(function(res) {
            return res.json().then(function() {
                updateStatus('Loaded file at "' + url + '".');
            });
        });
    }

    function parseInputFilename() {
        var filenameHash = window.location.hash;
        if (filenameHash[0] !== '#') {
            return null;
        }

        return filenameHash.substr(1);
    }
}