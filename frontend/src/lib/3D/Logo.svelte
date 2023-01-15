<script lang="ts">
  import * as THREE from 'three';
  import { SVGLoader } from 'three/examples/jsm/loaders/SVGLoader.js';
  import { T, useFrame } from "@threlte/core";
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

  export let ry = 0;

  useFrame((_, delta) => {
        ry -= 0.4 * delta;
    });
  

// TODO: fix mouse handler
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
</script>

<T.Mesh
  {geometry}
  material={new THREE.MeshStandardMaterial({
    color: 0xa92f0f,
    metalness: 1
  })}
  position={[0, 0, 0]}
  rotation={[0, ry, 0]}
  scale={0.015}
  castShadow
  interactive 
>
</T.Mesh>
