# E-commerce Dashboard

A comprehensive e-commerce management dashboard built with Next.js 15, TypeScript, shadcn/ui, and Radix UI.

## Features

- 📊 **Analytics Dashboard**: Revenue, orders, customers, and product metrics
- 📈 **Interactive Charts**: Sales trends, category distribution, and performance metrics
- 🛍️ **Product Management**: Add, edit, view, and manage products
- 📦 **Order Management**: Track orders, status updates, and customer information
- 👥 **Customer Management**: Customer profiles, order history, and spending analytics
- 🔍 **Search & Filter**: Advanced filtering and search capabilities
- 📱 **Responsive Design**: Works on all device sizes
- 🌙 **Dark Mode**: Built-in dark mode support

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui + Radix UI
- **Charts**: Recharts
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
├── components/
│   └── ui/              # shadcn/ui components
└── types/
    └── ecommerce.ts     # TypeScript interfaces
```

## Features Overview

### Dashboard Analytics
- Real-time revenue tracking
- Order count and trends
- Customer acquisition metrics
- Product inventory overview
- Interactive charts and graphs

### Product Management
- Add new products with categories
- Edit product details
- Stock management
- Product search and filtering
- Category-based organization

### Order Management
- Order tracking and status updates
- Customer order history
- Order details and product information
- Status-based filtering

### Customer Management
- Customer profiles and contact information
- Order history and spending analytics
- Customer status tracking
- Purchase behavior insights

### Data Visualization
- Line charts for sales trends
- Pie charts for category distribution
- Bar charts for performance metrics
- Interactive tooltips and legends

## Mock Data

The application includes comprehensive mock data for:
- Products with categories, pricing, and inventory
- Orders with customer information and status
- Customer profiles with purchase history
- Sales data for chart visualization

## Customization

The dashboard is highly customizable through:
- Tailwind CSS classes for styling
- shadcn/ui component variants
- Chart configurations in Recharts
- TypeScript interfaces for data structures

## License

MIT License
