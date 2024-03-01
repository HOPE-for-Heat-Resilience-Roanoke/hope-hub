<script lang="typescript">
  import { createEventDispatcher, setContext } from 'svelte';
  import * as L from 'leaflet';
  import markerIconUrl from "../../../../node_modules/leaflet/dist/images/marker-icon.png";
  import markerIconRetinaUrl from "../../../../node_modules/leaflet/dist/images/marker-icon-2x.png";
  import markerShadowUrl from "../../../../node_modules/leaflet/dist/images/marker-shadow.png";
  import 'leaflet/dist/leaflet.css';

  export let height = '100%';
  export let width = '100%';
  export let bounds;//: L.LatLngBounds;
  let mapProp;//: L.Map | undefined = undefined;
  export { mapProp as map };

  export const invalidateSize = () => map?.invalidateSize();

  const dispatch = createEventDispatcher();

  let map;//: L.Map | undefined;
  $: mapProp = map;

  export const getMap = () => map;
  setContext('layerGroup', getMap);
  setContext('layer', getMap);
  setContext('map', getMap);

  function createLeaflet(node) {
    map = L.map(node)
      .fitBounds(bounds)
      .on('zoom', (e) => dispatch('zoom', e));
    setTimeout(() => {
      if (map) {
        map.invalidateSize();
        map.fitBounds(bounds);
      }
    }, 250);

    // L.tileLayer(
    //   'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
    //   {
    //     attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
    //       &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
    //     subdomains: 'abcd',
    //     maxZoom: 14,
    //   }
    // ).addTo(map);

    // L.tileLayer(
    //   'https://api.mapbox.com/v4/dacvt.12qbs19m/{z}/{x}/{y}{r}.png?access_token=pk.eyJ1IjoiZGFjdnQiLCJhIjoiY2o4dWVnczZmMHoxdDJ3cXFya3FzMGRqdSJ9.GxRPCSfZ6lbzjfNBosFwXg',
    //   {

    //   }
    // ).addTo(map);

    L.tileLayer(
      'https://api.mapbox.com/styles/v1/dacvt/clt567ded01bg01qf9qgr741o/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiZGFjdnQiLCJhIjoiY2o4dWVnczZmMHoxdDJ3cXFya3FzMGRqdSJ9.GxRPCSfZ6lbzjfNBosFwXg'
    ).addTo(map);




    L.Icon.Default.prototype.options.iconUrl = markerIconUrl;
    L.Icon.Default.prototype.options.iconRetinaUrl = markerIconRetinaUrl;
    L.Icon.Default.prototype.options.shadowUrl = markerShadowUrl;
    L.Icon.Default.imagePath = "";

    // map.on("moveend", () => {
    //   console.log(map.getBounds())
    // });

    return {
      destroy() {
        if (map) map.remove();
        // map!.remove();
        map = undefined;
      },
    };
  }

  $: map?.fitBounds(bounds);
</script>

<style>
  :global(.leaflet-control-container) {
    position: static;
  }
</style>

<div style="height:{height};width:{width}" use:createLeaflet>
  {#if map}
    <slot {map} />
  {/if}
</div>
