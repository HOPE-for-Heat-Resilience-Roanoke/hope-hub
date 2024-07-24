<script>
  import ArtifactDetails from "$lib/components/ArtifactDetails.svelte";
  import { selectedEngagement } from "$lib/stores.js";

  export let engagement;
</script>

<p class="mb-2 cursor-pointer underline" on:click={() => $selectedEngagement = null}>Back to list</p>

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

{#if engagement.youtubelinks.length > 0}

  {#each engagement.youtubelinks as youtubelink (youtubelink.link)}

    <h4 class="font-bold mt-4 mb-2">Video</h4>
    <iframe width="100%" height="300" src="https://www.youtube.com/embed/{youtubelink.link}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

    <p class="mt-4">{youtubelink.statement}</p>
    {#if youtubelink.attribution}<p class="text-right text-sm mb-4">&mdash; {youtubelink.attribution}</p>{/if}

  {/each}

{/if}

{#if engagement.artifacts.length > 0}
  <h4 class="font-bold mt-4 mb-2">Selected Artifacts</h4>

  {#each engagement.artifacts as artifact (artifact.alt_text)}
    <ArtifactDetails
      {artifact}
    />
  {/each}
{/if}

{#if engagement.downloadablefiles.length > 0}
  <h4 class="font-bold mt-4 mb-2">Files</h4>

  {#each engagement.downloadablefiles as download}
    <h4 class="font-bold prose">{download.title}</h4>
    {#if download.is_audio}
      <audio controls src="/images/engagements{download.upload}"></audio>    
    {/if}
    <a class="prose underline" download href="/images/engagements{download.upload}">Download Here</a>
    {#if download.statement}    
      <p class="mt-4">{download.statement}</p>
      {#if download.attribution}<p class="text-right text-sm mb-4">&mdash; {download.attribution}</p>{/if}
    {/if}
  {/each}

{/if}

<style>
  ul {
    list-style: disc;
  }
</style>