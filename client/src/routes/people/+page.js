
export const load = async () => {
  const leadership = await import("../../posts/people/leadership.json");
  const nonprofits = await import("../../posts/people/nonprofit_partners.json");
  const city = await import("../../posts/people/city_partners.md");
  
  return {
    leadership,
    nonprofits,
    city: city.default,
  };
};
