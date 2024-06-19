<script>
  import { getContext } from 'svelte';

  let map = getContext('map')();
  let geojsonlayer;

  export let source;
  export let onFeatureStyle;
  export let onEachFeature;

  fetch(source)
    .then((response) => response.json())
    .then((data) => {
      geojsonlayer = L.geoJSON(data, {
          style: onFeatureStyle,
          onEachFeature: onEachFeature,
      }).addTo(map);
    });
</script>

<slot/>
