<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<footer class="bg-red text-gray-200 py-7 grid-area-footer">
  <div class="grid max-w-5xl m-auto grid-cols-3 mb-7">
    <div>
      Kjemidagen 2022<br />
      Org.nr 992 641 231<br />

      Realfagbygget (NTNU)<br />
      Høgskoleringen 5<br />
      7034 Trondheim<br />
    </div>
    <div>
      {$t('common.contactus')} <br />
      <a href="mailto:kontakt@kjemidagen.no" class="text-gray-200">kontakt@kjemidagen.no</a>
    </div>
    <div class="text-gray-200">
      <h6 class="text-lg underline">SoMe</h6>
      <a href="https://www.linkedin.com/company/kjemidagen/" class="text-gray-200">LinkedIn</a><br
      />
      <a href="https://www.facebook.com/Kjemidagen/" class="text-gray-200">Facebook</a><br />
      <a href="https://www.instagram.com/kjemidagen/" class="text-gray-200">Instagram</a><br />
    </div>
  </div>
  <a class="text-gray-300 ml-96 underline" href="#banner">Tilbake til toppen</a>
</footer>
