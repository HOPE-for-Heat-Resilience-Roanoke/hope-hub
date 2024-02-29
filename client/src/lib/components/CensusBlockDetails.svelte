<script>
  import { showCensus, selectedCensusBlock } from "$lib/stores.js";

  function getNumberWithOrdinal(n) {
    var s = ["th", "st", "nd", "rd"],
        v = n % 100;
    return n + (s[(v - 20) % 10] || s[v] || s[0]);
  }
  const format = (number) => getNumberWithOrdinal(parseInt((number * 100).toLocaleString(undefined, {minimumFractionDigits: 0})));

  const callout = (number) => number > 0.899999999999;
</script>

{#if $showCensus}
{#if $selectedCensusBlock === null}
  <p>Select an area of the map to see details.</p>
{:else}
  <h4 class="font-bold">Tract information</h4>
  <ul>
    <li>Number: {$selectedCensusBlock.GEOID10}</li>
    <li>Population: {$selectedCensusBlock.TPF}</li>
    <li>Asthma: <span class:callout={callout($selectedCensusBlock.AF_PFS)}>{format($selectedCensusBlock.AF_PFS)} percentile</span></li>
    <li>Diabetes: <span class:callout={callout($selectedCensusBlock.DF_PFS)}>{format($selectedCensusBlock.DF_PFS)} percentile</span></li>
    <li>Heart Disease: <span class:callout={callout($selectedCensusBlock.HDF_PFS)}>{format($selectedCensusBlock.HDF_PFS)} percentile</span></li>
    <li>Low Life Expectancy: <span class:callout={callout($selectedCensusBlock.LLEF_PFS)}>{format($selectedCensusBlock.LLEF_PFS)} percentile</span></li>
  </ul>
{/if}
{/if}

<style>
  .callout {
    font-weight: bold;
  }
</style>
