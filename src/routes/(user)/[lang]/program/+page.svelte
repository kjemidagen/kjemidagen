<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<svelte:head>
  <title>{$t('common.program')}</title>
</svelte:head>

<section class="program" id="program">
  <div class="content">
    <h1 class="text-3xl mb-8">{$t('program.title')}</h1>
    <p>
      {$t('program.description')}
    </p>
    <hr class="h-px my-8 bg-gray-200 border-0" />
    <h1 class="text-3xl mb-8">{$t('program.last_year')}</h1>
    <div class="flex flex-col">
      <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
          <div class="overflow-hidden">
            <table
              class="table-auto mb-16 text-lg min-w-full text-center font-medium border-spacing-80"
            >
              <tbody>
                <tr>
                  <td>10:00</td>
                  <td>
                    {$t('program.opening_loc')} -
                    {$t('program.opening')}
                  </td>
                </tr>
                <tr>
                  <td> 10:15 - 15:00 </td>
                  <td>
                    {$t('program.stands')}
                  </td>
                </tr>
                <tr>
                  <td> 10:15 - 15:00 </td>
                  <td>
                    {$t('program.speedinterview')}
                  </td>
                </tr>
                <tr>
                  <td> 11:00 - 13:00 </td>
                  <td>
                    {$t('program.cvphoto')}
                  </td>
                </tr>
                <tr>
                  <td> 11:15 - 12:00 </td>
                  <td>
                    R9 - {$t('program.summerjob')}
                  </td>
                </tr>
                <tr>
                  <td> 12:30 - 13:15 </td>
                  <td>
                    R5 - {$t('program.motivationalspeaking')}
                  </td>
                </tr>
                <tr>
                  <td> 14:15 - 14:45 </td>
                  <td>
                    R9 - {$t('program.jobmarathon')}
                  </td>
                </tr>
                <tr>
                  <td>18:30</td>
                  <td>{$t('program.banquet')}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="my-8">
      <h3 class="font-medium text-xl my-4">{$t('program.speedinterview')}</h3>
      <p>
        {$t('program.speedinterview_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.summerjob')}</h3>
      <p>
        {$t('program.summerjob_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.jobmarathon')}</h3>
      <p>
        {$t('program.jobmarathon_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.motivationalspeaking')}</h3>
      <p>
        {$t('program.motivationalspeaking_p')}
      </p>
      <h3 class="font-medium text-xl my-4">{$t('program.banquet')}</h3>
      <p>
        {$t('program.banquet_p')}
      </p>
    </div>
  </div>
</section>

<style>
  td {
    text-align: left;
  }
</style>
