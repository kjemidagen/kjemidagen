<script lang="ts">
  import type { Company } from '$lib/company';

  export let data: {
    companies: Company[];
  };
</script>

<div class="content grid grid-cols-3">
  <div class=" col-span-2">
    <h1 class="text-lg">Company admin</h1>
    {#each data.companies as company}
      <div>
        <a href="/admin/companies/{company.id}" class="decoration-black hover:underline">
          <span class="text-black">
            {company.title}
          </span>
        </a>
      </div>
    {:else}
      <div>No companies</div>
    {/each}
  </div>
  <div>
    <a href="/admin/companies/create" class="text-bold border-red bg-red-light px-2 py-1 text-white"
      >Create company</a
    >
  </div>
</div>
