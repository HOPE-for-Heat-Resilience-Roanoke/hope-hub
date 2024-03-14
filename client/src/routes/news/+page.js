export const load = async ({ fetch }) => {
  // get posts from api with sveltekit special fetch
  const response = await fetch("/api/posts");

  // get posts from response
  const posts = await response.json();

  return {
    posts
  };
};
