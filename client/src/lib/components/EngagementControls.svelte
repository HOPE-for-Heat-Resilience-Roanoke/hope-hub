<script>
  import EngagementFilters from "$lib/components/EngagementFilters.svelte";
  import EngagementDetails from "$lib/components/EngagementDetails.svelte";

  import { selectedEngagement } from "$lib/stores.js";
</script>

<EngagementFilters />

{#if $selectedEngagement}
  <EngagementDetails engagement={$selectedEngagement} />
{:else}
  <p class="px-12 text-center">Click a marker on the map to see details of that event</p>
{/if}
