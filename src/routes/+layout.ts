import '../app.css';
import { dev } from '$app/env';
import { inject } from '@vercel/analytics';
if (dev) {
  inject({ mode: dev ? 'development' : 'production' });
}
