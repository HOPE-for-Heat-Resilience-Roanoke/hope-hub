<script>
  export let data;

  console.log({data})

  const { metadata, markdown: Markdown, sidebar: Sidebar } = data;
</script>

<section class="flex gap-8 py-4">
  <article class="prose">
    <Markdown/>
  </article>

  <aside class="prose">
    <Sidebar/>
  </aside>
</section>
