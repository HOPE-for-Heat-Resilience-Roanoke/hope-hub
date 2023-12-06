<script>
  import { inview } from 'svelte-inview';

  export let data;
  console.log({data});

  const sections = data.sections;

  let currentTitle = "";

  function handleInView(e, newTitle) {
    if (e.detail.inView) {
      currentTitle = newTitle;
    }
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
  <article class="prose overflow-scroll pt-4 pr-2 pb-20">
    {#each sections as {metadata, markdown: MarkdownComponent}}
        <h2 
          id={metadata.id}
          use:inview
          on:inview_change={(e) => handleInView(e, metadata.title)}
        >
          {metadata.title}
        </h2>
        <MarkdownComponent/>
    {/each}
  </article>

  <aside>
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
  section {
    height: calc(100vh - 6rem);
  }
</style>
