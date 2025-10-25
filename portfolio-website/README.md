# Portfolio Website

A modern, responsive portfolio website built with Next.js 15, TypeScript, shadcn/ui, and Framer Motion.

## Features

- 🎨 **Modern Design**: Clean, professional layout with smooth animations
- 📱 **Responsive**: Fully responsive design that works on all devices
- 🌙 **Dark Mode**: Built-in dark mode support
- ⚡ **Fast Performance**: Optimized with Next.js 15 and modern best practices
- 🎭 **Smooth Animations**: Beautiful animations powered by Framer Motion
- 🎯 **Interactive**: Engaging user interactions and hover effects
- 📊 **Skills Visualization**: Animated progress bars for skill levels
- 💼 **Project Showcase**: Featured projects with technology tags
- 📈 **Experience Timeline**: Professional experience and education history
- 📞 **Contact Section**: Multiple ways to get in touch

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui + Radix UI
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **State Management**: React hooks

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Run the development server:
```bash
npm run dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
└── components/
    └── ui/              # shadcn/ui components
```

## Sections

### Hero Section
- Professional introduction with animated avatar
- Call-to-action buttons
- Smooth scroll animations

### About Section
- Personal introduction and background
- Animated skill progress bars
- Social media links

### Projects Section
- Featured project showcase
- Technology tags for each project
- Links to GitHub and live demos
- Responsive grid layout

### Experience Section
- Professional work history
- Education background
- Technology stacks used
- Timeline-style layout

### Contact Section
- Multiple contact methods
- Social media links
- Professional contact information

## Customization

### Personal Information
Update the following in `src/app/page.tsx`:
- Name and title
- Bio and description
- Contact information
- Social media links
- Professional experience
- Education history
- Skills and proficiency levels
- Featured projects

### Styling
- Modify colors in `tailwind.config.ts`
- Update CSS variables in `globals.css`
- Customize component styles
- Adjust animation timings in Framer Motion

### Content
- Replace placeholder project data
- Update experience and education
- Add your own projects and skills
- Customize the hero section

## Animation Features

- **Fade In Up**: Elements animate from bottom to top
- **Stagger**: Sequential animation of child elements
- **Hover Effects**: Interactive hover animations
- **Progress Bars**: Animated skill level indicators
- **Smooth Transitions**: Fluid page transitions

## Performance Optimizations

- Next.js 15 with App Router
- Optimized images and assets
- Lazy loading for better performance
- Minimal bundle size
- Fast loading times

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License

## Deployment

This portfolio can be deployed to:
- Vercel (recommended)
- Netlify
- GitHub Pages
- Any static hosting service

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

If you have any questions or need help customizing this portfolio, please open an issue on GitHub.
