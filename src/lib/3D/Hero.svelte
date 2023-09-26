<script lang="ts">
  import * as THREE from 'three';
  import * as SC from 'svelte-cubed';
  import Backdrop from './Backdrop.svelte';
  import Logo from './Logo.svelte';
  import bgUrl from '$lib/assets/hero-bg.png';

  let w = 1;
  let h = 1;
  let y = 0;

  let loaded = false;

  import { load } from './texture';
  const map = load(bgUrl, () => {
    loaded = true;
  });

  let ry = 0;

  // Handling click and drag
  function onMouseDown() {
    addEventListener('mousemove', onMouseMove);
    addEventListener('mouseup', onMouseUp);
  }

  function onMouseMove(event: MouseEvent) {
    ry += 0.01 * event.movementX;
  }

  function onMouseUp() {
    removeEventListener('mousemove', onMouseMove);
    removeEventListener('mouseup', onMouseUp);
  }

  // Same but for mobile
  let touchStartY: number = 0;
  function onTouchStart(event: TouchEvent) {
    touchStartY = event.targetTouches[0].clientX;
    addEventListener('touchmove', onTouchMove);
    addEventListener('touchend', onTouchEnd);
    addEventListener('touchcancel', onTouchEnd);
  }

  function onTouchMove(event: TouchEvent) {
    const dy = event.targetTouches[0].clientX - touchStartY;
    ry += 0.01 * dy;
    touchStartY = event.targetTouches[0].clientX;
  }

  function onTouchEnd() {
    removeEventListener('touchmove', onTouchMove);
    removeEventListener('touchend', onTouchEnd);
  }

  SC.onFrame(() => {
    ry -= 0.01;
  });
</script>

<svelte:window bind:scrollY={y} bind:innerWidth={w} bind:innerHeight={h} />

<div
  class="hero w-full top-0 left-0 md:w-[calc(100%_-_16px)] md:left-[8px]"
  class:visible={loaded}
  on:mousedown={onMouseDown}
  on:touchstart={onTouchStart}
>
  <SC.Canvas
    background={new THREE.Color(0xdedede)}
    shadows={THREE.VSMShadowMap}
    antialias
    powerPreference={'low-power'}
  >
    <!-- objects -->
    <Backdrop {map} />
    <Logo {ry} />

    <!-- camera -->
    <SC.PerspectiveCamera
      fov={65}
      zoom={1}
      position={[0, 0 - y * 0.005, 7]}
      target={[0, 0 - y * 0.005, 0]}
    />

    <!-- lights -->
    <SC.AmbientLight intensity={0.7} />

    <SC.SpotLight
      angle={0.8}
      penumbra={0.8}
      position={[3, 3, 8]}
      intensity={0.5}
      shadow={{
        radius: 10,
        bias: -0.001,
        mapSize: [1024, 1024]
      }}
    />

    <SC.SpotLight
      angle={0.8}
      penumbra={0.8}
      position={[2, 0, 2]}
      intensity={0.5}
      shadow={{
        radius: 10,
        bias: -0.001,
        mapSize: [1024, 1024]
      }}
    />
  </SC.Canvas>
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
