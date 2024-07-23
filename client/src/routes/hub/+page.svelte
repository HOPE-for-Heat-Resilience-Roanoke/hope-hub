<script>
  import Hub from "$lib/components/Hub.svelte";

  export let data;
  const {engagements, engagementSlug} = data;
</script>

<Hub {engagements} {engagementSlug}/>
