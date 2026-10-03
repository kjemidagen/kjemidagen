<script lang="ts">
  interface Props {
    children?: import('svelte').Snippet;
    [key: string]: any;
  }

  let { children, class: className = '', ...rest }: Props = $props();
</script>

<div class="inline-flex items-center justify-center rounded px-2 py-1 {className}" {...rest}>
  {#if children}
    {@render children()}
  {:else}
    <strong class="leading-none text-white">New</strong>
  {/if}
</div>
