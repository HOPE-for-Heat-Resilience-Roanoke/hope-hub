
export const load = async () => {
  const leadership = await import("../../posts/people/leadership.json");
  const students = await import("../../posts/people/students.json");
  const nonprofits = await import("../../posts/people/nonprofit_partners.json");
  const city = await import("../../posts/people/city_partners.md");
  
  return {
    leadership,
    students,
    nonprofits,
    city: city.default,
  };
};
