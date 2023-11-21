
export const load = async () => {
  const markdownPost = await import(
    "../posts/index.md"
  );

  const markdownSidebar = await import(
    "../posts/index_sidebar.md"
  );

  return {
    metadata: markdownPost.metadata,
    markdown: markdownPost.default,
    sidebar: markdownSidebar.default,
  };
};
