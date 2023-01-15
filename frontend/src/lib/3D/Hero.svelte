<script lang="ts">
  import * as THREE from 'three';
  import { Canvas, T, useTexture } from '@threlte/core';
  import Backdrop from './Backdrop.svelte';
  import Logo from './Logo.svelte';
  import bgUrl from '$lib/assets/hero-bg.png';
  import { DirectionalLight } from 'three';

  let w = 1;
  let h = 1;
  let y = 0;

  let loaded = false;

  const map = useTexture(bgUrl, {
    onError(error) {console.warn(`An error ${error.message}`)},
    onLoad() {
      loaded = true;
    },
  });
</script>

<svelte:window bind:scrollY={y} bind:innerWidth={w} bind:innerHeight={h} />

<div
  class="hero top-0 left-0 w-full md:left-[8px] md:w-[calc(100%_-_16px)]"
  class:visible={loaded}
>
<Canvas
  shadows={true}
  shadowMapType={THREE.PCFSoftShadowMap}
  rendererParameters={{powerPreference: 'low-power', antialias: false}}  
>
  <!-- objects -->
  <Backdrop {map} />
  <Logo/>

  <!-- camera -->
  <T.PerspectiveCamera
    makeDefault
    fov={65}
    position={[0, 0 - y * 0.01, 7]}
  />

  <!-- lights -->
  <T.AmbientLight intensity={1} />

  <T.SpotLight
    angle={1.0}
    penumbra={0.8}
    position={[2, 3, 8]}
    intensity={0.6}
    castShadow
  />

  <T.SpotLight
    angle={0.8}
    penumbra={0.8}
    position={[2, 0, 2]}
    intensity={0.9}
    castShadow
  />

  <T.DirectionalLight
    intensity={0.6}
    position={[0, 0, 1]}
  />

</Canvas>
</div>

<style>
  .hero {
    position: fixed;
    height: 100vh;
    opacity: 0;
    transition: opacity 0.2s;
  }

  .hero::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 20%;
    left: 0;
    bottom: 0;
  }

  .visible {
    opacity: 1;
  }
</style>
