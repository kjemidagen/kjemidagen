<script lang="ts">
  interface Props {
    children?: import('svelte').Snippet;
    [key: string]: any
  }

  let { ...props }: Props = $props();

</script>

<div class="rounded px-2 py-1 inline-flex items-center justify-center {props.class}">
  {#if children}{@render props.children()}{:else}<strong class="text-white leading-none">New</strong>{/if}
</div>
