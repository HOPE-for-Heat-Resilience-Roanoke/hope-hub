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
      // .on('zoomend', () => console.log(map.getBounds()));
    setTimeout(() => {
      if (map) {
        map.invalidateSize();
        map.fitBounds(bounds);
      }
    }, 250);


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
