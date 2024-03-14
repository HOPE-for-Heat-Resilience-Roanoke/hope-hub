import { json } from "@sveltejs/kit";

export const GET = async () => {
  // use vite glob import to get all markdown posts
  const markdownPostModules = import.meta.glob(
    "/src/posts/news/*"
  );

  const postPromises = [];

  for (const path in markdownPostModules) {
    const loadMarkdownPostModule = markdownPostModules[path];

    const loadPostSlugAndMetadata = async function () {
      // dynamically import markdown post
      const markdownPostModule = await loadMarkdownPostModule();

      // slug is everything after last / without the file extension
      const slug = path
        .slice(path.lastIndexOf("/") + 1)
        .replace(".md", "");

      const markdownPost = await import(
          `../../../posts/news/${slug}.md`
        );

      return {
        slug,
        metadata: markdownPostModule.metadata,
      };
    };

    postPromises.push(loadPostSlugAndMetadata());
  }

  // load all posts concurrently
  const posts = await Promise.all(postPromises);

  // sort by publication date (descending/most recent first)
  const sortedPosts = posts.sort((post1, post2) => {
    return (
      new Date(post2.metadata.publishedAt).getTime() -
      new Date(post1.metadata.publishedAt).getTime()
    );
  });

  return json(sortedPosts);
};