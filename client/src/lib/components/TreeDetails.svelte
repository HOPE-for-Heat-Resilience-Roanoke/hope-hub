<script>
  export let tree;
</script>

<div>
  <h5 class="text-lg mt-4 mb-2"><strong>{tree.properties.Common_Nam}</strong> at {tree.properties.Address}</h5>
  <p class="mb-6"><em>{tree.properties.Botanical_}</em></p>

  {#if tree.properties.Survey_Lin}
  <div class="my-8">
    <p class="mb-4">We don't have any stories about this tree yet!</p>

    <a href="{tree.properties.Survey_Lin}" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm my-4 px-5 py-2.5 focus:outline-none">Tell us a story</a>
  </div>
  {/if}

  {#if tree.properties.images && tree.properties.images.length > 0}
    {#each tree.properties.images as src}
      <img {src} alt="{tree.properties.Common_Nam} tree at {tree.properties.Address}" />
    {/each}
  {/if}
</div>
