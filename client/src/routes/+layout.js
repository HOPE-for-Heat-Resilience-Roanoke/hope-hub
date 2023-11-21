// add this to root layout
// to prerender all our pages
// during build time
export const prerender = true;

// get url path whenever visiting a new page
export const load = ({ url }) => {
  return {
    pathname: url.pathname
  };
};
