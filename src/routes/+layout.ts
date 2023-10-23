import '../app.css';
import { dev } from '$app/environment';
import { inject } from '@vercel/analytics';
if (dev) {
  inject({ mode: dev ? 'development' : 'production' });
}
