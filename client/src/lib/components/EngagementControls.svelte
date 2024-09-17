<script>
  import EngagementFilters from "$lib/components/EngagementFilters.svelte";
  import EngagementDetails from "$lib/components/EngagementDetails.svelte";
  import EngagementList from "$lib/components/EngagementList.svelte";

  import { selectedEngagement } from "$lib/stores.js";

  export let engagements = [];
  export let filteredEngagements = [];

  let value = "";

  $: options = engagements.map((e) => e.title);
  $: listEngagements = buildListEngagements(value, filteredEngagements, engagements);

  function buildListEngagements() {
    if (value.length > 0 && filteredEngagements.length == 0) {
      console.log("doing the right one ")
      return engagements.filter((e) => e.title.toLowerCase().indexOf(value.toLowerCase()) !== -1);
    } else if (value.length > 0) {
      return filteredEngagements.filter((e) => e.title.toLowerCase().indexOf(value.toLowerCase()) !== -1);
    }
    return filteredEngagements;
  }
</script>

<EngagementFilters />

<form>
  <input type="text" name="engagement-search" placeholder="Search..." bind:value/>
</form>
<small>Listing {listEngagements.length} of {engagements.length} engagements</small>

{#if $selectedEngagement}
  <EngagementDetails engagement={$selectedEngagement} />
{:else if listEngagements.length}
  <EngagementList engagements={listEngagements} />
{:else}
  <p class="px-12 mt-4 text-center">Use the search box or filters above to view engagements</p>
{/if}

<style>
  input {
      width: 100%;
      font-size: 1rem;
      padding: 0.5rem;
      margin: 0.5rem 0;
      border: 1px solid #e0e0e0;
      border-radius: 0.25rem;
  }
</style>