<script lang="ts">
  import { t } from '$lib/translations/translations';
  import FaqItem from '$lib/components/Faq.svelte';
</script>

<svelte:head>
  <title>{$t('common.for-companies')}</title>
</svelte:head>

<section class="for-companies">
  <div class="content" id="for-companies">
    <h1 class="text-3xl mb-8">{$t('for-companies.information_header')}</h1>

    <div class="mt-6 space-y-4">
      <FaqItem
        question={$t('for-companies.order_screen_q')}
        answer={$t('for-companies.order_screen_a')}
        linkUrl="https://example.com/order"
        linkLabel={$t('for-companies.order_screen_link_label')}
      />
      <FaqItem
      question={$t('for-companies.equipment_q')}
      answer={$t('for-companies.equipment_a')}
      linkUrl="https://example.com/order"
      linkLabel={$t('for-companies.equipment_link_label')}
      />
      <FaqItem
      question={$t('for-companies.address_q')}
      answer={$t('for-companies.address_a')}
      />
      <FaqItem
      question={$t('for-companies.stand_q')}
      answer={$t('for-companies.stand_a')}
      />
      <FaqItem
        question={$t('for-companies.job_positions_q')}
        answer={$t('for-companies.job_positions_a')}
      />
    </div>
  </div>
</section>
