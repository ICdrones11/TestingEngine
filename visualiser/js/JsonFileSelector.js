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
        return new Promise(function(resolve) {
            window.fetch(url).then(function(res) {
                    res.json().then(function(f) {
                        updateStatus('Loaded file at "' + url + '".');
                        resolve(f);
                });
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

    function handleFileSelect(evt) {
        var files = evt.target.files; // FileList object

        // files is a FileList of File objects. Display information from json file.
        var output = [];
        for (var i = 0, f; f = files[i]; i++) {
          var reader = new FileReader();

          // Closure to capture the file information.
          reader.onloadend = (function(theFile) {
            return function(e) {
                $.getJSON(reader.result)
                .done(function(drones) {
                    onJSONCb(drones);
                })

            };
          })(f);

          // Read in the json file as a data URL.
          reader.readAsDataURL(f);
        }
    }

    fileInput.addEventListener('change', handleFileSelect, false);
}

