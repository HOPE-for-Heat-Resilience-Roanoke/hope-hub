<script>
  export let data;

  console.log({data})

  const { metadata, markdown: Markdown, sidebar: Sidebar } = data;
</script>

<div class="flex gap-8">
  <article class="prose">
    <Markdown/>
  </article>

  <aside class="prose">
    <Sidebar/>
  </aside>
</div>