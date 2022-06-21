import i18n from 'sveltekit-i18n';
import lang from './lang.json';

/** @type {import('sveltekit-i18n').Config} */
const config = {
  translations: {
    no: { lang },
    en: { lang }
  },
  loaders: [
    {
      locale: 'no',
      key: 'common',
      loader: async () => (await import('./no/common.json')).default
    },
    {
      locale: 'en',
      key: 'common',
      loader: async () => (await import('./en/common.json')).default
    },
    {
      locale: 'no',
      key: 'frontpage',
      routes: ['/frontpage'],
      loader: async () => (await import('./no/frontpage.json')).default
    },
    {
      locale: 'en',
      key: 'frontpage',
      routes: ['/frontpage'],
      loader: async () => (await import('./en/frontpage.json')).default
    },
    {
      locale: 'no',
      key: 'about',
      routes: ['/about'],
      loader: async () => (await import('./no/about.json')).default
    },
    {
      locale: 'en',
      key: 'about',
      routes: ['/about'],
      loader: async () => (await import('./en/about.json')).default
    }
  ]
};

export const defaultLocale = 'no';

export const { t, locale, locales, loading, loadTranslations } = new i18n(config);
