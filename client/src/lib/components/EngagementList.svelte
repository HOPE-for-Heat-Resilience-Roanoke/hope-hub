<script>
  import { selectedEngagement } from "$lib/stores.js";

  export let engagements;

  function select(engagement) {
    $selectedEngagement = engagement;
  }
</script>

<ul>
{#each engagements as engagement, index}
  <li>
    <div class="my-4">
      <h6 class="font-bold cursor-pointer hover:underline" on:click={select(engagement)}>{engagement.title}</h6>
      <small>{engagement.date}</small>
      <p>{engagement.relevant_location}</p>
    </div>
  <li>
{/each}
</ul>
