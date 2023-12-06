
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

  const traumaPost = await import("../../posts/about/trauma.md");
  sections.push({
    markdown: traumaPost.default,
    metadata: traumaPost.metadata
  });

  const activitiesPost = await import("../../posts/about/activities.md");
  sections.push({
    markdown: activitiesPost.default,
    metadata: activitiesPost.metadata
  });

  console.log({sections})

  return {sections};
};
