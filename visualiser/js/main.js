window.addEventListener('load', function() {
    var updateStatus = (function() {
        var status = document.querySelector('.status');
        return function(newStatus) {
            status.textContent = newStatus;
        }
    })();

    var fileInput = document.getElementById('files');
    var selector = new JsonFileSelector(fileInput, updateStatus, visualiseData);

    function visualiseData(drones) {
        computeCirclularFlight(drones);
        // TODO: Implement Cesium visualisation here.
    }

    var viewer = new Cesium.Viewer('cesiumContainer', {
        terrainProviderViewModels : [], //Disable terrain changing
        infoBox : false, //Disable InfoBox widget
        selectionIndicator : false //Disable selection indicator
    });

    //Enable lighting based on sun/moon positions
    viewer.scene.globe.enableLighting = true;

    //Use STK World Terrain
    viewer.terrainProvider = new Cesium.CesiumTerrainProvider({
        url : 'https://assets.agi.com/stk-terrain/world',
        requestWaterMask : true,
        requestVertexNormals : true
    });

    //Enable depth testing so things behind the terrain disappear.
    viewer.scene.globe.depthTestAgainstTerrain = true;

    //Set the random number seed for consistent results.
    Cesium.Math.setRandomNumberSeed(3);

    //////////////////////// DISPLAY CLOCK ON THE SCREEN ////////////////////////

    //Set bounds of our simulation time
    var start = Cesium.JulianDate.fromDate(new Date(2015, 2, 25, 5));
    var stop = Cesium.JulianDate.addSeconds(start, 160, new Cesium.JulianDate());

    //Make sure viewer is at the desired time.
    viewer.clock.startTime = start.clone();
    viewer.clock.stopTime = stop.clone();
    viewer.clock.currentTime = start.clone();
    viewer.clock.clockRange = Cesium.ClockRange.LOOP_STOP; //Loop at the end
    viewer.clock.multiplier = 1;

    //Set timeline to simulation bounds
    viewer.timeline.zoomTo(start, stop);

    //////////////////////////////////////////////////////////////////////////////

    //Generate a random circular pattern with varying heights.
    function computeCirclularFlight(drones) {
        drones.forEach(function(droneFlight,k) {
               

                representDrone(droneFlight);
                
              
              
        });
        viewer.zoomTo(viewer.entities, new Cesium.HeadingPitchRange(Cesium.Math.toRadians(-90), Cesium.Math.toRadians(-15), 7500));
    }

    //Compute the entity position property.

    function representDrone(droneFlight) {
        var property = new Cesium.SampledPositionProperty();
        var waypoints = droneFlight.waypoints;
        var colour = Cesium.Color.RED;

        waypoints.forEach(function(point, i) {
            var time = Cesium.JulianDate.addSeconds(start, point.timestamp, new Cesium.JulianDate());
            var position = Cesium.Cartesian3.fromDegrees(point.lon, point.lat, point.alt);
             property.addSample(time, position);
                //Also create a point for each sample we generate.
            viewer.entities.add({
                position : position,
                point : {
                    pixelSize : 8,
                    color : Cesium.Color.TRANSPARENT,
                    outlineColor : colour,
                    outlineWidth : 3
                }
            });
        });

          //Actually add the drone entity
        addEntity(property, colour);
    }

    function addEntity(property, colour) {
        viewer.entities.add({

            //Set the entity availability to the same interval as the simulation time.
            availability : new Cesium.TimeIntervalCollection([new Cesium.TimeInterval({
                start : start,
                stop : stop
            })]),

            //Use our computed positions
            position : property,

            //Automatically compute orientation based on position movement.
            orientation : new Cesium.VelocityOrientationProperty(property),

            //Load the Cesium plane model to represent the entity
            model : {
                uri : 'Cesium/models/CesiumAir/Cesium_Air.gltf',
                minimumPixelSize : 64
            },

            //Show the path as a pink line sampled in 1 second increments.
            path : {
                resolution : 1,
                material : new Cesium.PolylineGlowMaterialProperty({
                    glowPower : 0.1,
                    color : colour
                }),
                width : 10
            }
        });
    }


});
