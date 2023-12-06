<script>
  export let data;

  const { metadata, markdown: Markdown } = data;
</script>

<section class="flex gap-8 py-4 pt-8 justify-evenly">
  <article class="prose">
    <Markdown/>
  </article>

  <aside class="flex flex-col items-center">
    <a href="https://nsfcivicinnovation.org">
      <img src="/images/civic.png" alt="Civic Innovation Challenge logo">
    </a>
    <a href="https://www.nsf.gov">
      <img src="/images/nsf.png" alt="NSF logo">
    </a>
  </aside>
</section>

<section class="pb-20">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/N5xTqLFCmVs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</section>
