import { writable } from 'svelte/store';

export const past = writable(true);
export const present = writable(true);
export const future = writable(true);

export const equity = writable(true);
export const community = writable(true);
export const nature = writable(true);
export const environment = writable(true);

