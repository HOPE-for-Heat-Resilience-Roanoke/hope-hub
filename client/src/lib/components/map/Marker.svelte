<script lang="ts">
  import {
    createEventDispatcher,
    getContext,
    setContext,
    onDestroy,
  } from 'svelte';
  import * as L from 'leaflet';

  export let latLng;
  // export let color: string;
  // export let weight: number | undefined = undefined;
  // export let opacity: number | undefined = undefined;
  export let pane = undefined;
  // export let lineCap:
  //   | 'butt'
  //   | 'round'
  //   | 'square'
  //   | 'inherit'
  //   | undefined = undefined;
  // export let lineJoin:
  //   | 'round'
  //   | 'inherit'
  //   | 'miter'
  //   | 'bevel'
  //   | undefined = undefined;
  // export let fill: boolean | undefined = undefined;
  // export let fillColor: string | undefined = undefined;
  // export let className: string | undefined = undefined;
  // export let dashArray: string | undefined = undefined;
  // export let dashOffset: string | undefined = undefined;
  // export let fillOpacity: number | undefined = undefined;
  // export let fillRule:
  //   | 'inherit'
  //   | 'nonzero'
  //   | 'evenodd'
  //   | undefined = undefined;
  // export let interactive = true;
  // export let style: string | undefined = undefined;

  const dispatch = createEventDispatcher();

  let layerPane = pane || getContext('pane');

  let layerGroup = getContext('layerGroup')();
  export let marker = new L.marker(
    latLng,
    // flush({
    //   interactive,
    //   className,
    //   pane: layerPane,
    // })
  )
    .on('click', (e) => dispatch('click', e))
    // .on('mouseover', (e) => dispatch('mouseover', e))
    // .on('mouseout', (e) => dispatch('mouseout', e))
    .addTo(layerGroup);

  setContext('layer', () => marker);

  // $: lineStyle = flush({
  //   color,
  //   className,
  //   weight,
  //   opacity,
  //   dashArray,
  //   dashOffset,
  //   lineCap,
  //   lineJoin,
  //   fill,
  //   fillColor,
  //   fillOpacity,
  //   fillRule,
  // });

  onDestroy(() => {
    marker.remove();
  });

  // $: if (style) {
  //   line.getElement()?.setAttribute('style', style);
  // }

  // $: line.setStyle(lineStyle);

  // $: {
  //   marker.setLatLng(latLng);
  //   marker.redraw();
  // }
</script>

<slot />
