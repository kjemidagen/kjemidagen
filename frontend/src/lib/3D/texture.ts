import { browser } from '$app/environment';
import * as THREE from 'three';

const cache = new Map();

// Caches Textures for THREE js texture loader
export function load(url: string, callback: () => void) {
  if (!browser) return;

  if (cache.has(url)) {
    callback();
  } else {
    cache.set(url, new THREE.TextureLoader().load(url, callback));
  }

  return cache.get(url);
}
