<script>
  export let tree;
</script>

<div class="not-prose">
  <h5 class="text-lg mt-4 md:mt-0 mb-2"><strong>{tree.properties.Common_Nam}</strong> at {tree.properties.Address}</h5>
  <p class="mb-6"><em>{tree.properties.Botanical_}</em></p>

  <div class="my-8">
    {#if tree.properties.Survey_Lin.substring(0, 4) === 'http'}
    <p class="mb-4">We don't have any stories about this tree yet!</p>

    <div class="text-center">
      <a href="{tree.properties.Survey_Lin}" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm my-4 px-5 py-2.5 focus:outline-none">Tell us a story about this tree</a>
    </div>
    {:else}
    <p class="mb-4">{tree.properties.TreeStory_}</p>
    {#if tree.properties.Reporter_N}<p class="text-right text-sm mb-4">&mdash; {tree.properties.Reporter_N}</p>{/if}
    {/if}
  </div>

  {#if tree.properties.images && tree.properties.images.length > 0}
    {#each tree.properties.images as src}
      <img {src} alt="{tree.properties.Common_Nam} tree at {tree.properties.Address}" />
    {/each}
  {/if}
</div>
