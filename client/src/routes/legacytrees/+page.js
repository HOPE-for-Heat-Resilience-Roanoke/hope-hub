export const ssr = false;

export const load = async ({fetch}) => {
  const response = await fetch("/trees/LegacyShadeeTrees.json")
  const trees = response.json();

  return {
    trees
  };
};
