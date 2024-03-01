<script>
  import { getContext } from 'svelte';
  import { showCensus, showHeat, selectedCensusBlock } from "$lib/stores.js";

  let map = getContext('map')();
  let censusLayer = null;
  let selectedLayer = null;

  const showLayer = (show) => {
    if (censusLayer === null) return;

    censusLayer.eachLayer(function (layer) {
      if (show) {
        censusLayer.resetStyle(layer);
      } else {
        layer.setStyle({
          color: "none",
          fillColor: "none",
        });
      }
    });
  }

  const onEachFeature = (feature, layer) => {
    layer.on({
      click: function (e) {
        if (selectedLayer) censusLayer.resetStyle(selectedLayer);

        selectedLayer = layer;
        selectedLayer.bringToFront();
        selectedLayer.setStyle({
          color: "DarkBlue",
          weight: 5,
        })

        console.log("on click", feature.properties);
        $selectedCensusBlock = feature.properties;
      }
    });
  }

  $: showLayer($showCensus);


  let heatLayer = null;
  const toggleHeat = (show) => {
    if (show) {
      heatLayer = L.tileLayer(
        'https://api.mapbox.com/styles/v1/dacvt/clt7ztr0o004301p3f10xcr5z/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiZGFjdnQiLCJhIjoiY2o4dWVnczZmMHoxdDJ3cXFya3FzMGRqdSJ9.GxRPCSfZ6lbzjfNBosFwXg', {
          opacity: 0.75
        }
      ).addTo(map);
    } else {
      if (heatLayer) {
        map.removeLayer(heatLayer);
      }
    }
  };

  $: toggleHeat($showHeat);



  fetch("/geo/justice40.geojson")
    .then((response) => response.json())
    .then((data) => {
      console.log("justice40", data);
      censusLayer = L.geoJSON(data, {
          style: function (feature) {
            return {
              stroke: true,
              color: "LightBlue",
              weight: 1,
              fill: true,
              fillColor: "#C0C0C0",
              fillOpacity: feature.properties.TC ? 0.5 : 0,
            };
          },
          onEachFeature: onEachFeature
      }).addTo(map);
    });
</script>

<slot/>
