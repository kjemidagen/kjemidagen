<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="program" id="program">
  <div class="content">
    <h3>{$t('program.header')}</h3>
    <p class="program-ingress">{$t('program.text1')}</p>
    <div class="program-body">
      <img src="raworth-lecture.jpg" alt="lecture room" width="400px" height="400px" object-fit />
      <div class="program-text">
        <table class="program-table">
          <tr><td class="left-col"><b>{$t('date_short')}</b></td> </tr>
          <tr><td class="left-col">{$t('program.time1')}</td><td>{$t('program.table1')} </td></tr>
          <tr><td class="left-col">{$t('program.time2')}</td><td>{$t('program.table2')} </td></tr>
          <tr><td class="left-col">{$t('program.time3')}</td><td>{$t('program.table3')} </td></tr>
          <tr><td class="left-col">{$t('program.time4')}</td><td>{$t('program.table4')} </td></tr>
          <tr><td class="left-col">{$t('program.time5')}</td><td>{$t('program.table5')} </td></tr>
          <tr><td class="left-col">{$t('program.time6')}</td><td>{$t('program.table6')} </td></tr>
          <tr><td class="left-col">{$t('program.time7')}</td><td>{$t('program.table7')} </td></tr>
        </table>
        <div>
          <p>{$t('program.text2')}</p>
          <p>{$t('program.text3')}</p>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .program {
    padding: 40px 0;
  }
  .content {
    max-width: var(--document-width);
    margin: auto;
  }
  .program-body {
    display: flex;
  }
  h3 {
    grid-column: span 2;
  }
  table {
    margin-bottom: 1rem;
  }
  .left-col {
    padding-right: min(4vw, 2rem);
  }
  img {
    border: 0px solid;
    border-radius: 1000px;
    object-fit: cover;
    object-position: 0 50%;
    margin: 2rem;
  }
  @media only screen and (min-width: 768px) {
    .program-body {
      flex-direction: row;
      justify-content: center;
    }
    .program-text {
      max-width: 50%;
    }
  }
</style>
