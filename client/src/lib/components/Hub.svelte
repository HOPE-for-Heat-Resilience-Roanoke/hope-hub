<script>
  import Leaflet from "$lib/components/map/Leaflet.svelte";
  import Marker from "$lib/components/map/Marker.svelte";
  import BaseLayer from "$lib/components/map/BaseLayer.svelte";
  import CensusLayer from "$lib/components/map/CensusLayer.svelte";
  import EngagementDetails from "$lib/components/EngagementDetails.svelte";
  import MapFilters from "$lib/components/MapFilters.svelte";
  import AnalysisControls from "$lib/components/AnalysisControls.svelte";
  import EngagementControls from "$lib/components/EngagementControls.svelte";
  import {
    past,
    present,
    future,
    equity,
    community,
    nature,
    environment,
    selectedEngagement,
  } from "$lib/stores.js";

  export let engagements;
  export let engagementSlug;

  if (engagementSlug) {
    const answer = engagements.filter((e) => e.slug == engagementSlug);

    if (answer.length > 0) {
      const e = answer[0];

      $past = e.conn_past;
      $present = e.conn_present;
      $future = e.conn_future;
      $equity = e.comp_equity;
      $community = e.comp_community;
      $nature = e.comp_nature;
      $environment = e.comp_environment;

      $selectedEngagement = e;
    }
  }

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

  function handleClick(engagement) {
    $selectedEngagement = engagement;
  }

  let value = "";
  $: filteredEngagements = searched(engagements.filter((e) => {
      return (
        ($past && e.conn_past) ||
        ($present && e.conn_present) ||
        ($future && e.conn_future) ||
        ($equity && e.comp_equity) ||
        ($community && e.comp_community) ||
        ($nature && e.comp_nature) ||
        ($environment && e.comp_environment)
      );
    }),
    value
  );

  function searched(sublist, value) {
    if (value.length > 0 && sublist.length == 0) {
      return engagements.filter((e) => e.title.toLowerCase().indexOf(value.toLowerCase()) !== -1);
    } else if (value.length > 0) {
      return sublist.filter((e) => e.title.toLowerCase().indexOf(value.toLowerCase()) !== -1);
    }
    return sublist;
  }

  let loaded = false;

</script>


<svelte:window on:resize={resizeMap} on:load={() => (loaded = true)} />

<article class="flex flex-col-reverse md:flex-row">
  <section class="md:w-1/2 h-full py-8">
    {#if loaded || document.readyState === 'complete'}
    <Leaflet bind:this={map} bounds={initialBounds}>
      <BaseLayer />
      <CensusLayer />
      {#each filteredEngagements as engagement}
        <Marker
          latLng={[engagement.latitude, engagement.longitude]}
          on:click={() => handleClick(engagement)}
        />
      {/each}
    </Leaflet>
    {/if}
  </section>
  <section class="md:w-1/2 p-8 overflow-y-scroll">

    <MapFilters name="Analysis">
      <AnalysisControls />
    </MapFilters>

    <MapFilters name="Engagements">
      <EngagementControls {engagements} {filteredEngagements} bind:value />
    </MapFilters>

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
