export const load = async ({ params }) => {
  const slug = params.slug;

  const markdownPost = await import(
    `../../../posts/news/${slug}.md`
  );

  return {
    metadata: markdownPost.metadata,
    post: markdownPost.default
  };
};
