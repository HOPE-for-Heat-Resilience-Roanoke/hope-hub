
export const load = async () => {
  const sections = [];

  const backgroundPost = await import("../../posts/about/background.md");
  sections.push({
    markdown: backgroundPost.default,
    metadata: backgroundPost.metadata
  });

  const approachPost = await import("../../posts/about/approach.md");
  sections.push({
    markdown: approachPost.default,
    metadata: approachPost.metadata
  });

  console.log({sections})

  return {sections};
};
