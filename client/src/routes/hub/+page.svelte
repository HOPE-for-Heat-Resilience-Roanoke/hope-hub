<script>
  import Leaflet from "$lib/components/map/Leaflet.svelte";

  const initialBounds = L.latLngBounds([24, -126], [50, -66]);

  let map;
  function resizeMap() {
    if (map) {
      map.invalidateSize();
    }
  }

  let loaded = false;
</script>

<svelte:window on:resize={resizeMap} on:load={() => (loaded = true)} />

<article class="w-100 py-8">
  {#if loaded || document.readyState === 'complete'}
  <Leaflet bind:this={map} bounds={initialBounds}>
  </Leaflet>
  {/if}
</article>


<style>
  h4 {
    text-align: center;
  }

  article {
    height: calc(100vh - 6rem);
  }
</style>