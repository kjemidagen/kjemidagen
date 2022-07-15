<script lang="ts">
  import * as THREE from 'three';
  import { SVGLoader } from 'three/examples/jsm/loaders/SVGLoader.js';
  import * as SC from 'svelte-cubed';
  import logo from './logo.svg?raw';

  const [shape0] = new SVGLoader().parse(logo).paths[0].toShapes(false);
  const [shape1] = new SVGLoader().parse(logo).paths[1].toShapes(false);
  const [shape2] = new SVGLoader().parse(logo).paths[2].toShapes(false);

  const geometry = new THREE.ExtrudeGeometry([shape0, shape1, shape2], {
    curveSegments: 6,
    depth: 5,
    bevelSegments: 1
  });
  geometry.center();

  export let rx = 0;
  export let ry = 0;
  export let rz = 0;
</script>

<SC.Mesh
  {geometry}
  material={new THREE.MeshStandardMaterial({
    color: 0xa92f0f
  })}
  position={[0, 0, 0]}
  rotation={[rx, ry, rz]}
  scale={0.015}
  castShadow
/>
