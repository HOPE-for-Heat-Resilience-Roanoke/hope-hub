<script>
  export let data;
  console.log({data});

  const sections = data.sections;
</script>

<section class="flex overflow-hidden">
  <article class="prose overflow-scroll pt-4 pr-2 pb-20">
    {#each sections as {markdown: MarkdownComponent}}
      <MarkdownComponent/>
    {/each}
  </article>

  <aside>
    <nav>
      <ul>
      {#each sections as section}
        <li>{section.metadata.title}</li>
      {/each}
      </ul>
    </nav>
  </aside>
</section>

<style>
  section {
    height: calc(100vh - 6rem);
  }
</style>
