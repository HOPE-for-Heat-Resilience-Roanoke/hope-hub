<script>
  import CensusPercentileItem from "$lib/components/CensusPercentileItem.svelte";
  import { showCensus, selectedCensusBlock } from "$lib/stores.js";
  import { format } from "d3-format";

  const tempChange = (value) => {
    return `${sigfig2(Math.abs(value))}ºF ${value < 0 ? "cooler" : "warmer"}`;
  }

  const comma = format(",.0f");
  const sigfig2 = format(".1f");
</script>

<div class="my-2">
{#if $showCensus}
  {#if $selectedCensusBlock === null}
    <p>Select an area of the map to see details.</p>
  {:else}
    <h4 class="font-bold">Census Tract {$selectedCensusBlock.GEOID10}</h4>
    <ul>
      <li>Population: {comma($selectedCensusBlock.TPF)}</li>
      <hr class="my-2">
      <li>Asthma: <CensusPercentileItem value={$selectedCensusBlock.AF_PFS}/></li>
      <li>Diabetes: <CensusPercentileItem value={$selectedCensusBlock.DF_PFS}/></li>
      <li>Heart Disease: <CensusPercentileItem value={$selectedCensusBlock.HDF_PFS}/></li>
      <li>Low Life Expectancy: <CensusPercentileItem value={$selectedCensusBlock.LLEF_PFS}/></li>
      <hr class="my-2">
      <li>Park Area: {sigfig2($selectedCensusBlock.park_area_percent)}%</li>
      <li>Heat Average: {sigfig2($selectedCensusBlock.heat_index_mean)}º</li>
      <li>Deviation from Summer Air Temperature: {tempChange($selectedCensusBlock.heat_index_deviation)}</li>
      <hr class="my-2">
      <li>Total Impervious Area: {sigfig2($selectedCensusBlock.impervious_and_gap_area_percent)}%</li>
      <li>Impervious Public Area: {sigfig2($selectedCensusBlock.impervious_and_gap_area_percent_public_and_gap_public)}%</li>
      <li>Impervious Private Area: {sigfig2($selectedCensusBlock.impervious_and_gap_area_percent_non_public)}%</li>
      <hr class="my-2">
      <li>Impervious Public and Vacant: {comma($selectedCensusBlock.total_impervious_for_public_and_vacant_in_sqfeet)} ft<sup>2</sup></li>
      <li>Impervious Public and Non-Vacant: {comma($selectedCensusBlock.total_impervious_for_public_and_not_vacant_in_sqfeet)} ft<sup>2</sup></li>
      <li>Impervious Private and Vacant: {comma($selectedCensusBlock.total_impervious_for_non_public_and_vacant_in_sqfeet)} ft<sup>2</sup></li>
      <li>Impervious Private and Non-Vacant: {comma($selectedCensusBlock.total_impervious_for_non_public_and_not_vacant_in_sqfeet)} ft<sup>2</sup></li>
      <hr class="my-2">
      <li>Total Tree Cover Area: {sigfig2($selectedCensusBlock.tree_area_percent_not_forest + $selectedCensusBlock.tree_area_percent_forest)}%</li>
      <li>Total Forest Cover: {sigfig2($selectedCensusBlock.tree_area_percent_forest)}%</li>
      <li>Total Non-Forest Cover: {sigfig2($selectedCensusBlock.tree_area_percent_not_forest)}%</li>
      <li>Tree Cover Public Area: {sigfig2($selectedCensusBlock.tree_area_percent_public_and_gap_public)}%</li>
      <li>Tree Cover Private Area: {sigfig2($selectedCensusBlock.tree_area_percent_non_public)}%</li>

    </ul>
  {/if}
{/if}
</div>

<style>
  .callout {
    font-weight: bold;
  }
</style>
