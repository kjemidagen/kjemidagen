<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<section class="program" id="program">
  <div class="content">
    <h3>{$t('program.title')}</h3>
    <div class="program-body">
      <img src="/raworth-lecture.jpg" alt="lecture room" width="400px" height="400px" object-fit />
      <div class="program-text">
        <table class="program-table">
          <tr><th class="left-col"><b>19. oktober</b></th></tr>
          <tr><td class="left-col">10:00</td> <td>{$t('program.opening')}</td></tr>
          <tr><td class="left-col">10:15 - 15:00</td> <td>{$t('program.stands')}</td></tr>
          <tr><td class="left-col">10:15 - 15:00</td> <td> {$t('program.speedinterview')} </td></tr>
          <tr><td class="left-col">10:30 - 13:00</td> <td> {$t('program.cvphoto')} </td></tr>
          <tr><td class="left-col">11:15</td> <td> {$t('program.motivationalspeaking')} </td></tr>
          <tr><td class="left-col">13:15</td> <td> {$t('program.summerjob')} </td></tr>
          <tr><td class="left-col">14:00</td> <td>{$t('program.jobmarathon')} </td></tr>
          <tr><td class="left-col">18:30</td> <td>{$t('program.banquet')} </td></tr>
        </table>
        <div>
          <h3>{$t('program.speedinterview')}</h3>
          <p>
            {$t('program.speedinterview_p')}
          </p>
          <h3>{$t('program.summerjob')}</h3>
          <p>
            {$t('program.summerjob_p')}
          </p>
          <h3>{$t('program.jobmarathon')}</h3>
          <p>
            {$t('program.jobmarathon_p')}
          </p>
          <h3>{$t('program.banquet')}</h3>
          <p>
            {$t('program.banquet_p')}
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
