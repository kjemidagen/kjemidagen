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
    <p class="text-lg mb-8">
      {$t('for-companies.information_description')}
    </p>
    <div class="mt-6 space-y-4">
      <FaqItem
        question={$t('for-companies.order_screen_q')}
        answer={$t('for-companies.order_screen_a')}
      />
      <FaqItem
      question={$t('for-companies.equipment_q')}
      answer={$t('for-companies.equipment_a')}
      />
      <FaqItem
      question={$t('for-companies.address_q')}
      answer={$t('for-companies.address_a')}
      />
      <FaqItem
      question={$t('for-companies.deadline_q')}
      answer={$t('for-companies.deadline_a')}
      />
      <FaqItem
        question={$t('for-companies.signup_q')}
        answer={$t('for-companies.signup_a')}
      />
      <FaqItem
        question={$t('for-companies.job_positions_q')}
        answer={$t('for-companies.job_positions_a')}
      />
    </div>
  </div>
</section>
