<script lang="ts">
  import { t } from '$lib/translations/translations';
  import Event from '$lib/components/Event.svelte';
</script>

<svelte:head>
  <title>{$t('common.program')}</title>
</svelte:head>

<section class="program" id="program">
  <div class="content">
    <h1 class="mb-8 text-3xl">{$t('program.title')}</h1>
    <p>
      {$t('program.description')}
    </p>
    
    <h3 class="mb-2 mt-8 text-2xl">{$t('program.day_monday')}</h3>
    <div class="flex flex-col gap-2">
      <Event
        title={$t('program.cv_photo')}
        time="10:00 - 15:00"
        location={$t('program.undecided')}
        loc_link=""
      />
    </div>
    <h3 class="mb-2 mt-8 text-2xl">{$t('program.day_tuesday')}</h3>
    <div class="flex flex-col gap-2">
        <Event
          title={$t('program.stands')}
          time="10:00 - 15:00"
          location={$t('program.undecided')}
          loc_link=""
        >
        </Event>
        <div class="flex flex-col gap-2">
        <Event
          title={$t('program.speed_interview')}
          time="10:00 - 15:00"
          location={$t('program.undecided')}
          loc_link=""
        >
        </Event>
        <Event
          title={$t('program.job_marathon')}
          time="13:15 - 14:00"
          location={$t('program.undecided')}
          loc_link=""
        >
          <p class="mt-3 leading-7">
            {$t('program.job_marathon_desc')}
          </p>
      </Event>
      <Event
          title={$t('program.mingle')}
          time="18:15"
          location={$t('program.mingle_loc')}
          loc_link="https://maps.app.goo.gl/1Zkf92DZ7Bri1f9f7"
        >
          <p class="mt-3 leading-7">
            {$t('program.mingle_desc')}
          </p>
        </Event>

    
        
      </div>
    <h3 class="mb-2 mt-8 text-2xl">{$t('program.day_wednesday')}</h3>
    <div class="flex flex-col gap-2">
      <Event
        title={$t('program.opening')}
        time="10:00"
        location={$t('program.undecided')}
        loc_link=""
      />
      <Event
        title={$t('program.stands')}
        time="10:00 - 15:00"
        location={$t('program.undecided')}
        loc_link=""
      />
      <Event
      title={$t('program.speed_interview')}
      time="10:00 - 15:00"
      location={$t('program.undecided')}
      loc_link=""
      />
      <Event
        title={$t('program.job_marathon')}
        time="13:15 - 14:00"
        location={$t('program.undecided')}
        loc_link=""
      >
        <p class="mt-3 leading-7">
          {$t('program.job_marathon_desc')}
        </p>
      </Event>
      <Event
        title={$t('program.banquet')}
        time="18:30"
        location={$t('program.banquet_loc')}
        loc_link="google.com/maps/place//data=!4m2!3m1!1s0x466d319bd29d55b3:0xe0e4e3fdf8991cd1?sa=X&ved=1t:8290&ictx=111"
      >
        <p class="mt-3 leading-7">
          {$t('program.banquet_desc')}
        </p>
      </Event>
    </div>
  </div>
</section>

<style>
</style>

