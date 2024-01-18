<script>
  import { inview } from 'svelte-inview';

  export let data;

  const leadership = data.leadership.leadership;
  const students = data.students.students;
  const nonprofits = data.nonprofits.partners;
  const {city: CityMarkdown} = data;

  let currentTitle = "";

  function handleInView(e, newTitle) {
    if (e.detail.inView) {
      currentTitle = newTitle;
    }
  }

  function scrollTo(elementId, title) {
    currentTitle = title;
    const el = document.querySelector(`#${elementId}`);
    window.history.replaceState(undefined, undefined, "#" + elementId);
    if (!el) return;
    el.scrollIntoView({
      behavior: "smooth"
    });
  }

  const sections = [{
    title: "Leadership",
    id: "leadership"
  }, {
    title: "HOPE Students",
    id: "students"
  }, {
    title: "Nonprofit Partners",
    id: "nonprofits"
  }, {
    title: "City Partners",
    id: "city"
  }];
</script>

<div style="height: calc(100vh - 6rem);" class="flex overflow-hidden">
  <article class="prose overflow-scroll pt-4 md:px-4 px-8 pb-20">
    <a href="#leadership" class="no-underline">
    <h2
      id="leadership"
    >Leadership</h2></a>
      {#each leadership as {name, bio, image}}
        <section 
            use:inview
            on:enter={(e) => handleInView(e, "Leadership")}
            class="flex flex-col-reverse md:flex-row md:odd:flex-row-reverse items-center"
        >
          <img class="px-4 min-w-fit" src="{image}" alt="{name}">
          <div class="px-4">
            <h4>{name}</h4>
            <p>{bio}</p>
          </div>
        </section>
      {/each}
    <a href="#students" class="no-underline">
    <h2
      id="students"
    >HOPE Students</h2></a>
      {#each students as {name, bio, image}}
        <section 
            use:inview
            on:enter={(e) => handleInView(e, "HOPE Students")}
            class="flex flex-col-reverse md:flex-row md:odd:flex-row-reverse items-center"
        >
          <img class="px-4 min-w-fit" src="{image}" alt="{name}">
          <div class="px-4">
            <h4>{name}</h4>
            <p>{bio}</p>
          </div>
        </section>
      {/each}
      <a href="#nonprofits" class="no-underline">
      <h2
        id="nonprofits"
        use:inview
        on:enter={(e) => handleInView(e, "Nonprofit Partners")}
      >Nonprofit Partners</h2></a>
      <div class="flex gap-4">
        {#each nonprofits as {src, alt, href}}
          <a {href}>
            <img {src} {alt}>
          </a>
        {/each}
      </div>
      <a href="#city" class="no-underline">
      <h2
        id="city"
        use:inview
        on:enter={(e) => handleInView(e, "City Partners")}
      >City Partners</h2></a>
      <CityMarkdown/>
  </article>

  <aside class="p-4 hidden md:block">
    <nav>
      <ul>
      {#each sections as metadata}
        <li class:font-bold={currentTitle == metadata.title}>
          <a 
            href="#{metadata.id}"
            on:click|preventDefault={() => scrollTo(metadata.id, metadata.title)}
          >
            {metadata.title}
          </a>
        </li>
      {/each}
      </ul>
    </nav>
  </aside>
</div>
