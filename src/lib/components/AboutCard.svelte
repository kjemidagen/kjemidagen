<script lang="ts">
  import { Envelope } from '@steeze-ui/heroicons';
  import { Icon } from '@steeze-ui/svelte-icon';

  export let imgSrc: string;
  export let name: string;
  export let title: string;
  export let email: string;
</script>

<article class="mb-8 mx-auto">
  <div class="image-shell w-80 h-80 xl:w-60 xl:h-60">
    <img src={imgSrc} alt={title} class="h-full w-full object-cover" />
  </div>

  <div class="mt-2 flex items-center justify-between gap-2">
    <div>
      <h4 class="text-lg">{name}</h4>
      <h5 class="text-md">{title}</h5>
    </div>

    <a
      href="mailto:{email}"
      aria-label="Send email to {name}"
      class="mail-link"
      target="_self"
      rel="noopener noreferrer"
    >
      <Icon src={Envelope} size="1.25em" theme="solid" />
    </a>
  </div>
</article>

<style>
  .image-shell {
    overflow: hidden;
    border-radius: 50%;
    aspect-ratio: 1;
    display: block;
  }

  img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 18%;
  }

  .mail-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.2rem;
    height: 2.2rem;
    border-radius: 9999px;
    background: rgba(198, 58, 45, 0.1);
    color: #c63a2d;
    transition: background 0.15s ease, transform 0.15s ease;
    flex-shrink: 0;
  }

  .mail-link:hover {
    background: rgba(198, 58, 45, 0.18);
    transform: translateY(-1px);
  }
</style>
