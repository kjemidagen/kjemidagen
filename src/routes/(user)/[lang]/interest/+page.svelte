<script lang="ts">
  import { t, locale } from '$lib/translations/translations';
  
  $: other_lang = $locale === "en" ? "no" : "en";
  let name_regex = ".{2,}";

  let name = "";
  let email = "";
  let message = "";
</script>

<svelte:head>
  <title>{$t('common.companies')}</title>
</svelte:head>

<noscript>Enable JavaScript to run this form</noscript>
<div class="content">
<h1 class="py-3 text-3xl text-center">{$t('interest.title')}</h1>
<a href="/{other_lang}/interest" class="text-center block text-xl">{$t('interest.other_language')}</a>
<form class="p-1 group" novalidate>
  <section>
    <h2 class="mb-2 mt-4 text-lg md:text-3xl">{$t('interest.company')}</h2>
    <p class="mb-2 text-sm">{$t('interest.company_desc')}</p>

    <div class="border-2 border-gray-300 border-dashed p-3 pb-1 rounded-lg">
      <label for="company" class="font-bold">{$t('interest.company_name')} *</label>
      <input 
        id="company" 
        type="text" 
        placeholder="{$t('interest.placeholder_company')}"
        required
        class="w-full mt-1 mb-3 p-2 border rounded peer
        invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500"
        pattern="{name_regex}" 
      />
      <span class="hidden mt-1 text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block">
        {$t('interest.error_message_company')}
      </span>
    </div>
  </section>

  <section>
    <h2 class="mb-2 mt-8 text-lg md:text-3xl">{$t('interest.contact')}</h2>
    <p class="mb-2 text-sm">{$t('interest.contact_desc')}</p>

    <div class="border-2 border-gray-300 border-dashed p-3 pb-1 rounded-lg">
      <label for="email" class="font-bold">{$t('interest.email')} *</label>
      <input 
        id="email" 
        type="text" 
        placeholder="{$t('interest.placeholder_email')}"
        required
        class="w-full mt-1 mb-3 p-2 border rounded peer
        invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500"
        pattern="[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]&#123;2,&#125;$"
      />
      <span class="hidden mt-1 text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block">
        {$t('interest.error_message_email')}
      </span>

      <label for="name" class="font-bold">{$t('interest.name')} *</label>
      <input 
        id="name" 
        type="text" 
        placeholder="{$t('interest.placeholder_name')}"
        required
        class="w-full mt-1 mb-3 p-2 border rounded peer
        invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500"
        pattern=".&#123;2,&#125;" 
      />
      <span class="hidden mt-1 text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block">
        {$t('interest.error_message_name')}
      </span>

      <label for="telephone" class="font-bold">{$t('interest.telephone')} *</label>
      <input 
        id="telephone" 
        type="text" 
        placeholder="{$t('interest.placeholder_telephone')}"
        required
        class="w-full mt-1 mb-3 p-2 border rounded peer
        invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-500"
        pattern=".&#123;2,&#125;" 
      />
      <span class="hidden mt-1 text-sm text-red-500 peer-[&:not(:placeholder-shown):not(:focus):invalid]:block">
        {$t('interest.error_message_telephone')}
      </span>
    </div>
  </section>

  <section>
    <h2 class="mb-2 mt-8 text-lg md:text-3xl">{$t('interest.choices')}</h2>
    <p class="mb-2 text-sm">{$t('interest.choices_desc')}</p>

    <div class="border-2 border-gray-300 border-dashed p-3 pb-2 rounded-lg">
      <label for="job_marathon" class="font-bold">{$t('interest.job_marathon_header')} *</label>
      <p class="text-sm pl-2">{$t('interest.job_marathon_information')}</p>
      <div id="job_marathon" class="flex flex-col mb-5 mt-3 space-y-1">
        <label>
          <input name="job_marathon" id="marathon" type="radio" value="yes" required>
          {$t('interest.marathon_yes')}
        </label>
        <label>
          <input name="job_marathon" id="marathon" type="radio" value="no" required>
          {$t('interest.marathon_no')}
        </label>
        <label>
          <input name="job_marathon" id="marathon" type="radio" value="dont_know" required>
          {$t('interest.marathon_dont_know')}
        </label>
      </div>
      
      <label for="other" class="font-bold">{$t('interest.other_header')}</label>
      <p class="text-sm pl-2">{$t('interest.other_information')}</p>
      <textarea 
        id="other" 
        placeholder="{$t('interest.placeholder_other')}"
        class="w-full h-40 mt-2 p-2 border rounded resize-none"
      />
    </div>
  </section>

  <div class="p-4 flex items-center space-x-2">
    <input type="checkbox" id="checkbox" class="form-checkbox h-5 w-5" required>
    <label for="checkbox" class="text-base text-gray-700 flex-wrap">
      * {$t('interest.confirm_understand_checkbox')}
    </label>
  </div>

  <br>
  <p class="justify-center hidden group-invalid:flex">{$t('interest.form_invalid')}</p>
  <div class="flex justify-center pt-2">
    <button type="submit" class="group-invalid:pointer-events-none group-invalid:opacity-50 
    text-white bg-red hover:bg-red-light focus:ring-4 focus:ring-blue-300 font-medium 
    rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 
    focus:outline-none dark:focus:ring-blue-800">{$t('interest.submit')}</button>
  </div>
</form>
</div>
