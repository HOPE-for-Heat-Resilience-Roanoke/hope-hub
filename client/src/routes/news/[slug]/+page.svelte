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
</article>
