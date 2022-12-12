<script lang="ts">
  import type { Company } from '$lib/company';

  export let data: {
    company: Company;
    id: string;
  };
</script>

<div class="content grid grid-cols-3">
  <div class=" col-span-2">
    <h1 class="text-lg">User admin</h1>
    {#if data.company}
      <div>
        <span>
          {data.company.title}
        </span>
        <span>
          {data.company.public_email}
        </span>
        <span>
          {data.company.additional_data}
        </span>
      </div>
    {:else}
      <div>No company with id {data.id}</div>
    {/if}
  </div>
  {#if data.company}
    <div>
      <a
        href="/admin/users/{data.id}/edit"
        class="text-bold border-red bg-red-light px-2 py-1 text-white"
      >
        Edit company
      </a>
    </div>
  {/if}
</div>
