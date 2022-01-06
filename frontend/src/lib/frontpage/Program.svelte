<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="program" id="program">
  <div class="content">
    <h3>{$t('program.header')}</h3>

    <p class="program-desc">{$t('program.text1')}</p>

    <div class="program-table">
      <table>
        <tbody>
          <tr><td class="left-col"><b>{$t('date_short')}</b></td> </tr>
          <tr><td class="left-col">{$t('program.time1')}</td><td>{$t('program.table1')} </td></tr>
          <tr><td class="left-col">{$t('program.time2')}</td><td>{$t('program.table2')} </td></tr>
          <tr><td class="left-col">{$t('program.time3')}</td><td>{$t('program.table3')} </td></tr>
          <tr><td class="left-col">{$t('program.time4')}</td><td>{$t('program.table4')} </td></tr>
          <tr><td class="left-col">{$t('program.time5')}</td><td>{$t('program.table5')} </td></tr>
          <tr><td class="left-col">{$t('program.time6')}</td><td>{$t('program.table6')} </td></tr>
          <tr><td class="left-col">{$t('program.time7')}</td><td>{$t('program.table7')} </td></tr>
        </tbody>
      </table>
    </div>

    <p>{$t('program.text2')}</p>
    <p>{$t('program.text3')}</p>
  </div>
</section>
