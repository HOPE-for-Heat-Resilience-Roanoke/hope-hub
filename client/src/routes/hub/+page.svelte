<script>
  import Leaflet from "$lib/components/map/Leaflet.svelte";
  import Marker from "$lib/components/map/Marker.svelte";
  import EngagementDetails from "$lib/components/EngagementDetails.svelte";

  export let data;
  const {engagements} = data;

  const initialBounds = L.latLngBounds(
      [37.24262844611252, -80.06080627441408], 
      [37.35405735474607, -79.88502502441406]
  );

  let map;
  function resizeMap() {
    if (map) {
      map.invalidateSize();
    }
  }

  let selectedEngagement = undefined;
  function handleClick(engagement) {
    console.log("clicked on", engagement);
    selectedEngagement = engagement;
  }

  let loaded = false;
</script>

<svelte:window on:resize={resizeMap} on:load={() => (loaded = true)} />

<article class="flex flex-row">
  <section class="w-1/2 h-full py-8">
    {#if loaded || document.readyState === 'complete'}
    <Leaflet bind:this={map} bounds={initialBounds}>
      {#each engagements as engagement}
        <Marker
          latLng={[engagement.latitude, engagement.longitude]}
          on:click={() => handleClick(engagement)}
        />
      {/each}
    </Leaflet>
    {/if}
  </section>
  <section class="w-1/2 p-8 overflow-y-scroll">
    {#if selectedEngagement}
      <EngagementDetails engagement={selectedEngagement} />
    {/if}
  </section>
</article>

<style>
  h4 {
    text-align: center;
  }

  article {
    height: calc(100vh - 6rem);
  }
</style>