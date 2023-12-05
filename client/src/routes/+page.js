
export const load = async () => {
  const markdownPost = await import(
    "../posts/index.md"
  );

  return {
    markdown: markdownPost.default,
  };
};
