<script>
  import { showCensus } from "$lib/stores.js";
</script>

<div class="p-8">
  <div class="flex items-center mb-1">
    <input bind:checked={$showCensus} id="census-filter" type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500">
    <label for="census-filter" class="ms-2 text-sm text-gray-900">Show Census Layer</label>
  </div>
</div>