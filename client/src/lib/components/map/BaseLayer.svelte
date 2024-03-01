<script>
  import { getContext } from 'svelte';
  import { showHeat } from "$lib/stores.js";

  let map = getContext('map')();
  let baseLayer = null;

  const showLayer = (show) => {
    if (baseLayer !== null) {
      map.removeLayer(baseLayer);
    }

    if (show) {
      baseLayer = L.tileLayer(
        'https://api.mapbox.com/styles/v1/dacvt/clt90qy74006w01p775qrhfgu/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiZGFjdnQiLCJhIjoiY2o4dWVnczZmMHoxdDJ3cXFya3FzMGRqdSJ9.GxRPCSfZ6lbzjfNBosFwXg'
      ).addTo(map);
    } else {
      baseLayer = L.tileLayer(
        'https://api.mapbox.com/styles/v1/dacvt/clt90ze8a006601p32bkt3h8e/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiZGFjdnQiLCJhIjoiY2o4dWVnczZmMHoxdDJ3cXFya3FzMGRqdSJ9.GxRPCSfZ6lbzjfNBosFwXg'
      ).addTo(map);
    }
  }

  $: showLayer($showHeat);

</script>