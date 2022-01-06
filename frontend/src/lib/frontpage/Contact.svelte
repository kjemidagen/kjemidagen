<script lang="ts">
  import { t } from 'svelte-intl-precompile';
</script>

<section class="contact" id="contact">
  <div class="content">
    <h3>{$t('contact.header')}</h3>

    <figure class="contact-image">
      <img src="styret21.jpg" alt="styret 2021" />
      <!--
				<ul class="styret">
					<li>
						<a href="mailto:larsgholmen@kjemidagen.no">Lars G. Holmen</a><span class="desc"
							>PR-sjef</span
						>
					</li>
					<li>
						<a href="mailto:ingridandreassen@kjemidagen.no">Ingrid Andre&shy;assen</a><span
							class="desc">Nest&shy;leder</span
						>
					</li>
					<li>
						<a href="mailto:cathrineheuch@kjemidagen.no">Cathrine Ro Heuch</a><span class="desc"
							>Øko&shy;nomi&shy;ansvar&shy;lig</span
						>
					</li>
					<li>
						<a href="mailto:jakobvinje@kjemidagen.no">Jakob Vinje</a><span class="desc">Leder</span>
					</li>
				</ul>
			-->
      */
    </figure>

    <p>{$t('contact.text')}</p>
    <p class="contact-email"><a href="mailto:kontakt@kjemidagen.no">kontakt@kjemidagen.no</a></p>
    <p>{$t('contact.footer')}</p>
  </div>
</section>
