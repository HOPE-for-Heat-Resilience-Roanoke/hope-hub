<script>
  export let engagement;
</script>


<h2 class="font-bold pb-2">{engagement.title}</h2>
<p>{engagement.description}</p>
{#each engagement.images as {src, alt}}
  <img class="p-8" src="images/engagements/{src}" {alt} />
{/each}
