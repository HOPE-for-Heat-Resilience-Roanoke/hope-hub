<script>
  import TreeDetails from "$lib/components/TreeDetails.svelte";
  import Leaflet from "$lib/components/map/Leaflet.svelte";
  import BaseLayer from "$lib/components/map/BaseLayer.svelte";
  import GeoJSONLayer from "$lib/components/map/GeoJSONLayer.svelte";

  export let data;
  const treeLayer = data.trees;
  console.log(treeLayer)

  const initialBounds = L.latLngBounds(
      [37.24262844611252, -80.06080627441408], 
      [37.35405735474607, -79.88502502441406]
  );

  let map;
  function resizeMap() {
    if (map) {
      map.invalidateSize();
    }
  }

  let loaded = false;
  var popup = L.popup();


  // function buildPopup(feature) {
  //   let popupHTML = `<div class="popup overflow-scroll h-36">
  //     <dl>
  //       <dt>Address</dt>
  //       <dd>${feature.properties.Address}</dd>
  //       <dt>Botanical Name</dt>
  //       <dd>${feature.properties.Botanical_}</dd>
  //       <dt>Common Name</dt>
  //       <dd>${feature.properties.Common_Nam}</dd>
  //       <dt>Location</dt>
  //       <dd>${feature.properties.Tree_Loc_T}</dd>
  //     </dl>
  //     <dl>  
  //       <dt>Reported By</dt>
  //       <dd>${feature.properties.Reporter_N}</dd>
  //       <dt>Ownership</dt>
  //       <dd>${feature.properties.Ownership}</dd>
  //       <dt>Story</dt>
  //       <dd>${feature.properties.TreeStory_}</dd>`;

  //   if (feature.properties.Survey_Lin) {
  //     popupHTML += 
  //       `  <dt>Survey Link</dt>
  //         <dd><a href="${feature.properties.Survey_Lin}">Click here</a></dd>`;
  //   }
  //   popupHTML += `</dl></div>`;

  //   return popupHTML;
  // }

  function buildPopup(feature) {
    return `<strong>${feature.properties.Common_Nam}</strong> at ${feature.properties.Address}`
  }

  let selectedTree = undefined;
</script>

<svelte:window on:resize={resizeMap} on:load={() => (loaded = true)} />

<article class="">
  <div class="flex flex-row">
    <section class="prose">
      <h3>What is a Legacy Shade Tree?</h3>

      <p>A legacy shade tree is a big, old tree that means something to you! Some legacy trees may be less big, or less old, but overall these trees stand out because they provide shade, beauty, stability… and they mean something to our community.</p>

      <p class="m-0">Have you ever thought:</p>

      <p class="m-0 text-right">&mdash; “That old tree has seen some stuff!”</p>
      <p class="m-0">Or,</p>
      <p class="m-0 text-right">&mdash; “That big tree makes this place feel like home!”</p>
      <p class="m-0">Or,</p>
      <p class="m-0 text-right">&mdash; “If that tree came down, I would really miss it.”</p>

      <p>If so, then <strong>you know a legacy tree!</strong></p>


      <h3>What is this program trying to achieve?</h3>

      <p>We’re collecting stories about legacy shade trees because we want to celebrate them.</p>

      <p>Back in the day, before widespread air conditioning, shade trees were essential to our neighborhood’s well being in the summer. Nowadays, summers are getting hotter, and we need trees more than ever. Between the shade they cast and the way they pump moisture through the air, trees cool our neighborhood. Sure, we need our air conditioning – but we also need our trees.</p>

      <p>It’s easy to forget about the trees. They become “background.” But they are a hidden strength in our neighborhood and they deserve our respect. They are <em>witnesses to history</em>, often outliving the people who planted them!</p>

      <p>Let’s honor the trees by telling their stories. Tell us which trees have meaning for you. Did you climb trees as a child? Did you play or have picnics in their shade? Do you know someone who planted a tree long ago? Do you always look to see when they bloom in the spring or turn colors in the fall? Please tell us all about your legacy shade tree experiences!</p>

      Please share your trees and stories by following <a href="https://virginiatech.questionpro.com/t/Aa0KTZ2wUR">this link to the survey page.</a>

      <p>If you have any questions or would like any additional information please contact Dr. Eric Wiseman by email at vtuf@vt.edu.</p>

      <h3>Map of Legacy Trees</h3>
      <p>Each marker on the map below represents a legacy tree in Roanoke! Click on a marker to see photos and read their stories. And, if any of these trees are familiar to you, tell us your own story!</p>
    </section>
    <div>
      <a href="https://virginiatech.questionpro.com/t/Aa0KTZ2wUR" class="sticky top-32 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm ml-4 mt-8 px-5 py-2.5 focus:outline-none">Tell us about a legacy tree!</a>
    </div>
  </div>
  <section class="tall py-8 flex flex-row">
    <div class="h-full w-8/12">
    {#if loaded || document.readyState === 'complete'}
    <Leaflet bind:this={map} bounds={initialBounds}>
      <BaseLayer />
      
      <GeoJSONLayer
        source="/trees/LegacyShadeeTrees.json"
        onEachFeature={(feature, layer) => {
          layer.bindPopup(buildPopup(feature));

          layer.on("click", () => {
            selectedTree = feature;
          });

        }}
        onFeatureStyle={(feature) => {
          return {
            stroke: true,
            color: "blue",
            weight: 1,
            fill: true,
            fillColor: "#C0C0C0",
            fillOpacity: feature.properties.TC ? 0.5 : 0,
          };
        }}
      />
    </Leaflet>
    {/if}
    </div>
    <div class="p-4 w-4/12">
      {#if selectedTree}
        <TreeDetails tree={selectedTree}/>
      {:else}
        Click on a marker on the map to see the details for that tree.
      {/if}
    </div>
  </section>
</article>

<style>
  h4 {
    text-align: center;
  }

  .tall {
    height: 75vh;
  }
</style>
