import { writable } from 'svelte/store';

export const past = writable(false);
export const present = writable(false);
export const future = writable(false);

export const equity = writable(false);
export const community = writable(false);
export const nature = writable(false);
export const environment = writable(false);

export const showCensus = writable(false);
export const showHeat = writable(false);
export const selectedCensusBlock = writable(null);
export const selectedEngagement = writable(null);
