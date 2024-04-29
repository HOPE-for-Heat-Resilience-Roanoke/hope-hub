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

        $selectedCensusBlock = feature.properties;
      }
    });
  }

  $: showLayer($showCensus);

  fetch("/geo/justice40_augmented.geojson?v2")
    .then((response) => response.json())
    .then((data) => {
      censusLayer = L.geoJSON(data, {
          style: function (feature) {
            return {
              stroke: true,
              color: "blue",
              weight: 1,
              fill: true,
              fillColor: "#C0C0C0",
              fillOpacity: feature.properties.TC ? 0.5 : 0,
            };
          },
          onEachFeature: onEachFeature
      }).addTo(map);
      showLayer($showCensus);
    });
</script>

<slot/>
