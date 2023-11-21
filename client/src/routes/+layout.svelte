<script>
  import { fly } from "svelte/transition";
  import "../app.css";

  export let data;

  $: pagePath = data.pathname;
</script>

{#key pagePath}
  <main
    in:fly={{ y: -15, duration: 200, delay: 300 }}
    out:fly={{ y: 15, duration: 200 }}
    class="pt-24 max-w-5xl mx-auto"
  >
    <slot />
  </main>
{/key}
