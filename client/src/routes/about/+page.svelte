<script>
  import { inview } from 'svelte-inview';

  export let data;

  const sections = data.sections;

  let currentTitle = "";

  function handleInView(e, newTitle) {
    // if (e.detail.inView) {
      currentTitle = newTitle;
    // }
  }

  function scrollTo(elementId) {
    const el = document.querySelector(`#${elementId}`);
    if (!el) return;
    el.scrollIntoView({
      behavior: "smooth"
    });
  }
</script>

<section class="flex overflow-hidden">
  <article class="prose overflow-scroll pt-4 px-8 md:px-2 pb-20">
    {#each sections as {metadata, markdown: MarkdownComponent}}
        <h2 
          id={metadata.id}
        >
          {metadata.title}
        </h2>
        <section
          use:inview
          on:enter={(e) => handleInView(e, metadata.title)}
        >
          <MarkdownComponent/>
        </section>
    {/each}
  </article>

  <aside class="p-4 hidden md:block">
    <nav>
      <ul>
      {#each sections as {metadata}}
        <li class:font-bold={currentTitle == metadata.title}>
          <a 
            href="#{metadata.id}"
            on:click|preventDefault={() => scrollTo(metadata.id)}
          >
            {metadata.title}
          </a>
        </li>
      {/each}
      </ul>
    </nav>
  </aside>
</section>

<style>
  section.overflow-hidden {
    height: calc(100vh - 6rem);
  }
</style>
