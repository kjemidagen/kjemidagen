<script lang="ts">
  import { t } from '$lib/translations/translations';
  import linkedinSrc from '$lib/assets/linkedin.svg';
  import facebookSrc from '$lib/assets/facebook.svg';
  import instagramSrc from '$lib/assets/instagram.svg';
  import emailSrc from '$lib/assets/email.svg';
</script>

<footer class="grid-area-footer z-10 bg-red py-7 px-2 text-gray-200">
  <div class="m-auto grid max-w-5xl grid-cols-2 gap-7 md:grid-cols-3">
    <div>
      <h6 class="text-lg">Kjemidagen 2022</h6>
      <p class="mb-3">Org.nr 992 641 231</p>
      <p>Realfagbygget (NTNU)</p>
      <p>Høgskoleringen 5</p>
      <p>7034 Trondheim</p>
    </div>
    <div class="text-gray-200">
      <h6 class="text-lg">SoMe</h6>
      <a href="https://www.linkedin.com/company/kjemidagen/" class="text-gray-200"
        ><img src={linkedinSrc} alt="" class="inline h-4" /> LinkedIn</a
      ><br />
      <a href="https://www.facebook.com/Kjemidagen/" class="text-gray-200"
        ><img src={facebookSrc} alt="" class="inline h-4" /> Facebook</a
      ><br />
      <a href="https://www.instagram.com/kjemidagen/" class="text-gray-200"
        ><img src={instagramSrc} alt="" class="inline h-4" /> Instagram</a
      ><br />
    </div>
    <div>
      <h6 class="text-lg">{$t('common.contactus')}</h6>
      <a href="mailto:kontakt@kjemidagen.no" class="text-gray-200"
        ><img src={emailSrc} alt="" class="inline h-4" /> kontakt@kjemidagen.no</a
      >
    </div>
    <a class="text-gray-300" href="#banner">Tilbake til toppen</a>
  </div>
</footer>
