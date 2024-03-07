<script>
  export let artifact;
</script>

<figure>
  <img src="images/engagements{artifact.upload}" alt="{artifact.alt_text}" />
  <figcaption class="text-sm">{artifact.alt_text}{#if artifact.attribution}&nbsp;by {artifact.attribution}{/if}</figcaption>
</figure>

{#if artifact.statement}  
  <h4 class="my-4">Artist Statement</h4>
  <p class="my-4">{artifact.statement}</p>
{/if}
