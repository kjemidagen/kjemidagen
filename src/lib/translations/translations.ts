import i18n from 'sveltekit-i18n';
import type { Config } from 'sveltekit-i18n';

import lang from './lang.json';

const config: Config = {
  translations: {
    no: { lang },
    nn: { lang },
    en: { lang }
  },
  loaders: [
    {
      locale: 'no',
      key: 'common',
      loader: async () => (await import('./nb-NO/common.json')).default
    },
    {
      locale: 'nn',
      key: 'common',
      loader: async () => (await import('./nn-NO/common.json')).default
    },
    {
      locale: 'en',
      key: 'common',
      loader: async () => (await import('./en/common.json')).default
    },
    {
      locale: 'no',
      key: 'frontpage',
      loader: async () => (await import('./nb-NO/frontpage.json')).default
    },
    {
      locale: 'nn',
      key: 'frontpage',
      loader: async () => (await import('./nn-NO/frontpage.json')).default
    },
    {
      locale: 'en',
      key: 'frontpage',
      loader: async () => (await import('./en/frontpage.json')).default
    },
    {
      locale: 'no',
      key: 'about',
      routes: ['/about'],
      loader: async () => (await import('./nb-NO/about.json')).default
    },
    {
      locale: 'nn',
      key: 'about',
      routes: ['/about'],
      loader: async () => (await import('./nn-NO/about.json')).default
    },
    {
      locale: 'en',
      key: 'about',
      routes: ['/about'],
      loader: async () => (await import('./en/about.json')).default
    },
    {
      locale: 'no',
      key: 'companies',
      routes: ['/companies'],
      loader: async () => (await import('./nb-NO/companies.json')).default
    },
    {
      locale: 'nn',
      key: 'companies',
      routes: ['/companies'],
      loader: async () => (await import('./nn-NO/companies.json')).default
    },
    {
      locale: 'en',
      key: 'companies',
      routes: ['/companies'],
      loader: async () => (await import('./en/companies.json')).default
    },
    {
      locale: 'no',
      key: 'program',
      routes: ['/program'],
      loader: async () => (await import('./nb-NO/program.json')).default
    },
    {
      locale: 'nn',
      key: 'program',
      routes: ['/program'],
      loader: async () => (await import('./nn-NO/program.json')).default
    },
    {
      locale: 'en',
      key: 'program',
      routes: ['/program'],
      loader: async () => (await import('./en/program.json')).default
    },
    {
      locale: 'no',
      key: 'sponsors',
      routes: ['/sponsors'],
      loader: async () => (await import('./nb-NO/sponsors.json')).default
    },
    {
      locale: 'nn',
      key: 'sponsors',
      routes: ['/sponsors'],
      loader: async () => (await import('./nn-NO/sponsors.json')).default
    },
    {
      locale: 'en',
      key: 'sponsors',
      routes: ['/sponsors'],
      loader: async () => (await import('./en/sponsors.json')).default
    },
    {
      locale: 'no',
      key: 'map',
      routes: ['/map'],
      loader: async () => (await import('./nb-NO/map.json')).default
    },
    {
      locale: 'nn',
      key: 'map',
      routes: ['/map'],
      loader: async () => (await import('./nn-NO/map.json')).default
    },
    {
      locale: 'en',
      key: 'map',
      routes: ['/map'],
      loader: async () => (await import('./en/map.json')).default
    },
    {
      locale: 'no',
      key: 'jobs',
      loader: async () => (await import('./nb-NO/jobs.json')).default
    },
    {
      locale: 'nn',
      key: 'jobs',
      loader: async () => (await import('./nn-NO/jobs.json')).default
    },
    {
      locale: 'en',
      key: 'jobs',
      loader: async () => (await import('./en/jobs.json')).default
    },
    {
      locale: 'no',
      key: 'interest',
      loader: async () => (await import('./nb-NO/interest.json')).default
    },
    {
      locale: 'nn',
      key: 'interest',
      loader: async () => (await import('./nn-NO/interest.json')).default
    },
    {
      locale: 'en',
      key: 'interest',
      loader: async () => (await import('./en/interest.json')).default
    }
  ],
  log: {
    level: 'error'
  }
};

export const defaultLocale = 'no';

export const { t, locale, locales, loading, loadTranslations } = new i18n(config);
