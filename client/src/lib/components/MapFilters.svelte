<script>
  import {
    past,
    present,
    future,
    equity,
    community,
    nature,
    environment,
  } from "$lib/stores.js";

</script>


<section class="flex flex-row justify-between pb-1 mb-4 border-gray-900 border-b">
  <div class="w-1/2">
    <h4 class="text-sm text-gray-900 border-gray-900 border-b pb-1 mb-2">Time</h4>
    <div class="flex items-center mb-1">
      <input bind:checked={$past} id="past-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="past-filter" class="ms-2 text-sm text-gray-900">Processing the Past</label>
    </div>
    <div class="flex items-center mb-1">
      <input bind:checked={$present} id="present-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="present-filter" class="ms-2 text-sm text-gray-900">Understanding the Present</label>
    </div>
    <div class="flex items-center mb-1">
      <input bind:checked={$future} id="future-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="future-filter" class="ms-2 text-sm text-gray-900">Visioning the Future</label>
    </div>
  </div>
  <div width="w-1/2">
    <h4 class="text-sm text-gray-900 border-gray-900 border-b pb-1 mb-2">Theme</h4>
    <div class="flex items-center mb-1">
      <input bind:checked={$equity} id="equity-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="equity-filter" class="ms-2 text-sm text-gray-900">Interwoven Equity</label>
    </div>
    <div class="flex items-center mb-1">
      <input bind:checked={$community} id="community-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="community-filter" class="ms-2 text-sm text-gray-900">Healthy Community</label>
    </div>
    <div class="flex items-center mb-1">
      <input bind:checked={$nature} id="nature-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="nature-filter" class="ms-2 text-sm text-gray-900">Harmony with Nature</label>
    </div>
    <div class="flex items-center mb-1">
      <input bind:checked={$environment} id="environment-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
      <label for="environment-filter" class="ms-2 text-sm text-gray-900">Livable Built Environment</label>
    </div>
  </div>
</section>
