<script>
  export let data;

  const { posts } = data;

  const options = {
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  const topubdate = (date) => new Date(date).toLocaleDateString("en-US", options);
</script>

{#each posts as {metadata, slug}, index}  
  {@const href = `/news/${slug}`}
  <article class="mt-4 sm:items-center sm:flex sm:space-x-4">
    <div class="prose py-2 sm:py-0">
      <a {href}>
        <h3 class="mb-0 text-left">{metadata.title}</h3>
      </a>
      <p>{metadata.author}</p>
      <small class="mb-4">Published {topubdate(metadata.publishedAt)}</small>
      <p>{metadata.blurb}</p>
      <a {href}>Read more...</a>
    </div>
    <a {href}>
      <div
        class="w-96 rounded-lg overflow-hidden flex justify-center"
      >
        <img
          src={metadata.imageUrl}
          alt={metadata.imageAlt}
          class="object-cover"
        />
      </div>
    </a>
  </article>
{/each}

<style>
  h3 {
    text-decoration: none;
  }
</style>
