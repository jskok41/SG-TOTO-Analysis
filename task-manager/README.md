# Task Manager

A modern, responsive task management application built with Next.js 15, TypeScript, shadcn/ui, and Radix UI.

## Features

- ✅ Create, edit, and delete tasks
- 🏷️ Priority levels (Low, Medium, High)
- 📅 Due date tracking
- 🔍 Search and filter tasks
- 📊 Progress tracking dashboard
- 🌙 Dark mode support
- 💾 Local storage persistence
- 📱 Responsive design

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui + Radix UI
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
│   └── ui/          # shadcn/ui components
└── types/
    └── task.ts      # TypeScript interfaces
```

## Features Overview

### Task Management
- Add new tasks with title, description, priority, and due date
- Mark tasks as complete/incomplete
- Delete tasks
- Real-time updates

### Filtering & Sorting
- Filter by: All, Active, Completed, High Priority
- Sort by: Created date, Due date, Priority, Title
- Search tasks by title or description

### Dashboard
- Total task count
- Completed tasks count
- In-progress tasks count
- Overall progress percentage

### Data Persistence
- Tasks are automatically saved to localStorage
- Data persists between browser sessions
- No external database required

## Customization

The application uses shadcn/ui components which can be easily customized through:
- Tailwind CSS classes
- CSS variables in `globals.css`
- Component variants and props

## License

MIT License
