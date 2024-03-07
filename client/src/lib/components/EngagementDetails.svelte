<script>
  import ArtifactDetails from "$lib/components/ArtifactDetails.svelte";

  export let engagement;
</script>

<h2 class="font-bold py-2">{engagement.title}</h2>
<p class="py-2">{engagement.relevant_location}</p>
<p>{engagement.description}</p>

<section class="flex flex-row justify-between mt-4 pb-2 mb-4 border-gray-900 border-b">
  <div class="w-1/2">
    <h4 class="text-sm text-gray-900 border-gray-900 border-b pb-1 mb-2">Time</h4>
    <ul>
      {#if engagement.conn_past}
        <li class="ms-2 text-sm text-gray-900">Processing the Past</li>
      {/if}
      {#if engagement.conn_present}
        <li class="ms-2 text-sm text-gray-900">Understanding the Present</li>
      {/if}
      {#if engagement.conn_future}
        <li class="ms-2 text-sm text-gray-900">Visioning the Future</li>
      {/if}
    </ul>
  </div>
  <div width="w-1/2">
    <h4 class="text-sm text-gray-900 border-gray-900 border-b pb-1 mb-2">Theme</h4>
    <ul>
      {#if engagement.comp_equity}
        <li class="ms-2 text-sm text-gray-900">Interwoven Equity</li>
      {/if}
      {#if engagement.comp_community}
        <li class="ms-2 text-sm text-gray-900">Healthy Community</li>
      {/if}
      {#if engagement.comp_nature}
        <li class="ms-2 text-sm text-gray-900">Harmony with Nature</li>
      {/if}
      {#if engagement.comp_environment}
        <li class="ms-2 text-sm text-gray-900">Livable Built Environment</li>
      {/if}
    </ul>
  </div>
</section>

{#if engagement.artifacts}
  <h4 class="font-bold mt-4 mb-2">Selected Artifacts</h4>
{/if}

{#each engagement.artifacts as artifact (artifact.alt_text)}
  <ArtifactDetails
    {artifact}
  />
{/each}

<style>
  ul {
    list-style: disc;
  }
</style>