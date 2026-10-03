<script lang="ts">
  interface Props {
    picture: any;
    border?: boolean;
    link?: string;
  }

  let { picture, border = false, link = '#' }: Props = $props();
</script>

<div class:bordered={border} class="company-box">
  <a href={link} target="_blank" rel="noopener noreferrer">
    <img src={picture} alt="Company logo" />
  </a>
</div>

<style>
  .company-box {
    --kjemi-red: #ab2d0e;
    --kjemi-salmon: #f4846a;
    --kjemi-red-rgb: 171, 45, 14;

    box-sizing: border-box;
    width: 220px;
    height: 140px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: white;
    border: 3px solid rgba(244, 132, 106, 0.45);
    border-radius: 12px;

    transition:
      transform 0.2s ease,
      box-shadow 0.2s ease,
      border-color 0.2s ease;
  }

  .company-box.bordered {
    border: 7px solid var(--kjemi-red);
    box-shadow:
      inset 0 0 0 3px var(--kjemi-salmon),
      0 4px 14px rgba(var(--kjemi-red-rgb), 0.25);
  }

  .company-box:hover {
    transform: translateY(-3px);
    border-color: var(--kjemi-salmon);
    box-shadow: 0 6px 16px rgba(var(--kjemi-red-rgb), 0.2);
  }

  .company-box.bordered:hover {
    border-color: var(--kjemi-red);
    box-shadow:
      inset 0 0 0 3px var(--kjemi-salmon),
      0 8px 20px rgba(var(--kjemi-red-rgb), 0.35);
  }

  .company-box a {
    width: 100%;
    height: 100%;

    display: flex;
    align-items: center;
    justify-content: center;
  }

  .company-box img {
    max-width: 75%;
    max-height: 75%;
    object-fit: contain;
  }
</style>
