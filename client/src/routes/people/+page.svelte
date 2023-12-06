<script>
  export let data;
  console.log({data});

  const leadership = data.leadership.leadership;
  const nonprofits = data.nonprofits.partners;
  const {city: CityMarkdown} = data;
</script>

<div style="height: calc(100vh - 6rem);" class="flex overflow-hidden">
  <article class="prose overflow-scroll pt-4 pr-2 pb-20">
    <h2>Leadership</h2>
    <div>
      {#each leadership as {name, bio, image}}
        <section class="flex items-center">
          <img class="px-4" src="{image}" alt="{name}">
          <div class="px-4">
            <h4>{name}</h4>
            <p>{bio}</p>
          </div>
        </section>
      {/each}
    </div>
    <div>
      <h3>Nonprofit Partners</h3>
      <div class="flex gap-4">
        {#each nonprofits as {src, alt, href}}
          <a {href}>
            <img {src} {alt}>
          </a>
        {/each}
      </div>
    </div>
    <div>
      <h3>City Partners</h3>
      <CityMarkdown/>
    </div>
  </article>

  <aside>
    Here is an aside
  </aside>
</div>

<style>
  section {
    flex-direction: row;
  }

  section:nth-child(odd) {
    flex-direction: row-reverse;
  }
</style>
