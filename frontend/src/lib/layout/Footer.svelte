<script lang="ts">
  import { t } from '$lib/translations/translations';
</script>

<footer class="bg-red text-gray-200 py-7 grid-area-footer px-2 z-10">
  <div class="grid max-w-5xl m-auto grid-cols-2 gap-7 md:grid-cols-3">
    <div>
      <h6 class="text-lg underline">Kjemidagen 2022</h6>
      <p class="mb-3">Org.nr 992 641 231</p>
      <p>Realfagbygget (NTNU)</p>
      <p>Høgskoleringen 5</p>
      <p>7034 Trondheim</p>
    </div>
    <div class="text-gray-200">
      <h6 class="text-lg underline">SoMe</h6>
      <a href="https://www.linkedin.com/company/kjemidagen/" class="text-gray-200">LinkedIn</a><br
      />
      <a href="https://www.facebook.com/Kjemidagen/" class="text-gray-200">Facebook</a><br />
      <a href="https://www.instagram.com/kjemidagen/" class="text-gray-200">Instagram</a><br />
    </div>
    <div>
      <h6 class="text-lg underline">{$t('common.contactus')}</h6>
      <a href="mailto:kontakt@kjemidagen.no" class="text-gray-200">kontakt@kjemidagen.no</a>
    </div>
    <a class="text-gray-300 underline" href="#banner">Tilbake til toppen</a>
  </div>
</footer>
