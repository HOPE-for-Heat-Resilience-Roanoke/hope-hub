<script>
  export let artifact;
</script>

<figure>
  <img src="images/engagements{artifact.upload}" alt="{artifact.alt_text}" />
  <figcaption class="text-sm">{artifact.alt_text}</figcaption>
</figure>

{#if artifact.statement}  
  <h4 class="my-4">Artist Statement</h4>
  <p class="mt-4">{artifact.statement}</p>
  {#if artifact.attribution}<p class="text-right text-sm mb-4">&mdash; {artifact.attribution}</p>{/if}
{/if}
