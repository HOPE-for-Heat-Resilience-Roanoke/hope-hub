<script>
  export let data;

  const { metadata, post: Post } = data;

  const options = {
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  const pubdate = new Date(metadata.publishedAt).toLocaleDateString("en-US", options);
</script>

<article class="prose mt-4">
  <h1 class="mb-0">{metadata.title}</h1>
  <p>{metadata.authorLong}</p>
  <small class="mb-4">Published {pubdate}</small>
  <Post />
  {#if metadata.youtubeID}
    <section class="pb-20 md:max-w-xl">
      <iframe width="100%" height="350" src="https://www.youtube.com/embed/{metadata.youtubeID}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </section>
  {/if}
</article>
