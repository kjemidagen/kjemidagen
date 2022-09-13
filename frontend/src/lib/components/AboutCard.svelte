<script lang="ts">
  export let imgSrc: string;
  export let name: string;
  export let title: string;
  export let email: string;
</script>

<article class="mb-8 mx-auto">
  <img src={imgSrc} alt={title} class="h-96 w-80 object-cover xl:h-72 xl:w-48" />
  <h4 class="text-lg">{name}</h4>
  <h5 class="text-md">{title}</h5>
  <h5 class="text-red text-sm xl:text-xs"><a href="mailto:{email}">{email}</a></h5>
</article>
