export const ssr = false;

export const load = async ({fetch, params}) => {
  const response = await fetch("/engagements.json")
  const engagements = await response.json();

  const engagementSlug = params.engagement;

  return {
    engagements,
    engagementSlug,
  };
};
