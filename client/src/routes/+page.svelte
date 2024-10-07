<script>
  export let data;

  const { metadata, markdown: Markdown } = data;
</script>

<section class="flex flex-col md:flex-row gap-8 px-8 md:px-0 py-4 pt-8 justify-evenly">
  <article class="prose">
    <Markdown/>

    
    <section class="my-8 md:max-w-xl">
      <h4 class="font-bold my-2">2024 Summary Video of our Project</h4>
      <iframe width="100%" height="350" src="https://www.youtube.com/embed/WEM5ASM-QXY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </section>

    <section class="mb-20 md:max-w-xl">
      <h4 class="font-bold my-2">2023 Video Explaining Our Project Approach</h4>
      <iframe width="100%" height="350" src="https://www.youtube.com/embed/N5xTqLFCmVs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </section>

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
