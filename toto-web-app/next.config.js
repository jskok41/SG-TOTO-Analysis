/** @type {import('next').NextConfig} */
const nextConfig = {
  // Removed output: 'export' for Vercel deployment
  trailingSlash: true,
  images: {
    unoptimized: true
  }
}

module.exports = nextConfig 