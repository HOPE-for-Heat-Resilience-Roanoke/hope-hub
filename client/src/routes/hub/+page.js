export const ssr = false;

export const load = async ({fetch}) => {
  const response = await fetch("/engagements.json")
  const engagements = response.json();

  return {
    engagements
  };
};
