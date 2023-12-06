<script>
  export let data;

  const { metadata, markdown: Markdown } = data;
</script>

<section class="flex flex-col md:flex-row gap-8 px-8 md:px-0 py-4 pt-8 justify-evenly">
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

<section class="pb-20 md:max-w-xl">
  <iframe width="100%" height="350" src="https://www.youtube.com/embed/N5xTqLFCmVs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</section>
