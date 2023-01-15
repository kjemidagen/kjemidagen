<script lang="ts">
  import * as THREE from 'three';
  import { T } from "@threlte/core";
  import type { Texture } from 'three';

  export let map: Texture;

  let w = 1;
  let h = 1;
  let y = 0;

  const backdrop = new THREE.PlaneGeometry(2, 2);
</script>

<svelte:window bind:scrollY={y} bind:innerWidth={w} bind:innerHeight={h} />

<T.Mesh
  geometry={backdrop}
  material={new THREE.MeshStandardMaterial({
    map,
    flatShading: true,
    metalness: 1
  })}
  position={[0, 0, -15]}
  scale={15 * Math.max(w / h, 1)}
  receiveShadow
>
</T.Mesh>

