<script context="module" lang="ts">
  /** @type {import('@sveltejs/kit').Load} */
  export async function load({ url }) {
    return {
      status: 301,
      redirect: '/no/' + url.pathname + url.search + url.hash // Only works for hashes and params since any pathname matches locale even if it isnt
    };
  }
</script>
