import i18n from 'sveltekit-i18n';
import lang from './lang.json';

/** @type {import('sveltekit-i18n').Config} */
const config = {
  translations: {
    no: { lang },
    nn: { lang },
    en: { lang }
  },
  loaders: [
    {
      locale: 'no',
      key: 'common',
      loader: async () => (await import('./no/common.json')).default
    },
    {
      locale: 'nn',
      key: 'common',
      loader: async () => (await import('./nn/common.json')).default
    },
    {
      locale: 'en',
      key: 'common',
      loader: async () => (await import('./en/common.json')).default
    },
    {
      locale: 'no',
      key: 'frontpage',
      routes: ['/frontpage/'],
      loader: async () => (await import('./no/frontpage.json')).default
    },
    {
      locale: 'nn',
      key: 'frontpage',
      routes: ['/frontpage/'],
      loader: async () => (await import('./nn/frontpage.json')).default
    },
    {
      locale: 'en',
      key: 'frontpage',
      routes: ['/frontpage/'],
      loader: async () => (await import('./en/frontpage.json')).default
    },
    {
      locale: 'no',
      key: 'about',
      routes: ['/about/'],
      loader: async () => (await import('./no/about.json')).default
    },
    {
      locale: 'nn',
      key: 'about',
      routes: ['/about/'],
      loader: async () => (await import('./nn/about.json')).default
    },
    {
      locale: 'en',
      key: 'about',
      routes: ['/about/'],
      loader: async () => (await import('./en/about.json')).default
    },
    {
      locale: 'no',
      key: 'companies',
      routes: ['/companies/'],
      loader: async () => (await import('./no/companies.json')).default
    },
    {
      locale: 'nn',
      key: 'companies',
      routes: ['/companies/'],
      loader: async () => (await import('./nn/companies.json')).default
    },
    {
      locale: 'en',
      key: 'companies',
      routes: ['/companies/'],
      loader: async () => (await import('./en/companies.json')).default
    },
    {
      locale: 'no',
      key: 'program',
      routes: ['/program/'],
      loader: async () => (await import('./no/program.json')).default
    },
    {
      locale: 'nn',
      key: 'program',
      routes: ['/program/'],
      loader: async () => (await import('./nn/program.json')).default
    },
    {
      locale: 'en',
      key: 'program',
      routes: ['/program/'],
      loader: async () => (await import('./en/program.json')).default
    },
    {
      locale: 'no',
      key: 'sponsors',
      routes: ['/sponsors/'],
      loader: async () => (await import('./no/sponsors.json')).default
    },
    {
      locale: 'nn',
      key: 'sponsors',
      routes: ['/sponsors/'],
      loader: async () => (await import('./nn/sponsors.json')).default
    },
    {
      locale: 'en',
      key: 'sponsors',
      routes: ['/sponsors/'],
      loader: async () => (await import('./en/sponsors.json')).default
    }
  ]
};

export const defaultLocale = 'no';

export const { t, locale, locales, loading, loadTranslations } = new i18n(config);
