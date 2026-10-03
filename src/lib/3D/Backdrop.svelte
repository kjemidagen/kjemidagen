<script lang="ts">
  import * as THREE from 'three';
  import * as SC from 'svelte-cubed';
  import type { Texture } from 'three';

  interface Props {
    map: Texture;
  }

  let { map }: Props = $props();

  let w = $state(1);
  let h = $state(1);
  let y = $state(0);

  const backdrop = new THREE.PlaneGeometry(2, 2);
</script>

<svelte:window bind:scrollY={y} bind:innerWidth={w} bind:innerHeight={h} />

<SC.Mesh
  geometry={backdrop}
  material={new THREE.MeshStandardMaterial({
    map
  })}
  position={[0, 0, -15]}
  scale={15 * Math.max(w / h, 1)}
  receiveShadow
/>
