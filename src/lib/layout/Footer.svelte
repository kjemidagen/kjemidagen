<script lang="ts">
  import { t } from '$lib/translations/translations';
  import linkedinSrc from '$lib/assets/linkedin.svg';
  import facebookSrc from '$lib/assets/facebook.svg';
  import instagramSrc from '$lib/assets/instagram.svg';
  import { Envelope } from '@steeze-ui/heroicons';
  import { Icon } from '@steeze-ui/svelte-icon';
</script>

<footer class="grid-area-footer z-10 bg-red px-2 py-7 text-gray-200">
  <div class="m-auto grid max-w-5xl grid-cols-2 gap-7 md:grid-cols-3">
    <div>
      <h6 class="text-lg">Kjemidagen</h6>
      <p class="mb-3">Org.nr 992 641 231</p>
      <p>Realfagbygget (NTNU)</p>
      <p>Høgskoleringen 5</p>
      <p>7034 Trondheim</p>
    </div>
    <div class="text-gray-200">
      <h6 class="text-lg">SoMe</h6>
      <a href="https://www.linkedin.com/company/kjemidagen/" class="text-gray-200"
        ><img src={linkedinSrc} alt="" class="inline mr-1 h-4" /> LinkedIn</a
      ><br />
      <a href="https://www.facebook.com/Kjemidagen/" class="text-gray-200"
        ><img src={facebookSrc} alt="" class="inline mr-1 h-4" /> Facebook</a
      ><br />
      <a href="https://www.instagram.com/kjemidagen/" class="text-gray-200"
        ><img src={instagramSrc} alt="" class="inline mr-1 h-4" /> Instagram</a
      ><br />
    </div>
    <div>
      <h6 class="text-lg">{$t('common.contactus')}</h6>
      <div class="inline-flex items-center justify-center">
        <a href="mailto:kontakt@kjemidagen.no" class="text-gray-200">
          <Icon
            src={Envelope}
            size="1.2em"
            theme="solid"
            class="my-auto mr-1 inline leading-none text-white"
          />
          <span class="leading-1 text-white"> kontakt@kjemidagen.no </span>
        </a>
      </div>
    </div>
    <a class="text-gray-300" href="#banner">Tilbake til toppen</a>
  </div>
</footer>
