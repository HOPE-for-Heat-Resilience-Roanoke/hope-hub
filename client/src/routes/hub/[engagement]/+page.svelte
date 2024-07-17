<script>
  import Hub from "$lib/components/Hub.svelte";

  export let data;
  const {engagements, engagementSlug} = data;
  console.log("slug", {engagements}, engagementSlug)

</script>

<Hub {engagements} {engagementSlug}/>