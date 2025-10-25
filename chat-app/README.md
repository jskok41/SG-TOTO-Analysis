# Real-time Chat Application

A modern, responsive real-time chat application built with Next.js 15, TypeScript, shadcn/ui, and Radix UI.

## Features

- 💬 **Real-time Messaging**: Send and receive messages instantly
- 👥 **Multiple Chat Rooms**: Support for both direct messages and group chats
- 🔍 **Search Functionality**: Search through conversations and messages
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 🌙 **Dark Mode**: Built-in dark mode support
- ⚡ **Fast Performance**: Optimized with Next.js 15 and modern best practices
- 🎨 **Modern UI**: Beautiful interface with shadcn/ui components
- 📊 **Message Status**: Read receipts and typing indicators
- 🔔 **Notifications**: Unread message counts and badges
- 👤 **User Management**: User profiles and online status

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui + Radix UI
- **Icons**: Lucide React
- **State Management**: React hooks
- **Real-time**: Socket.io (ready for integration)

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
    └── chat.ts          # TypeScript interfaces
```

## Features Overview

### Chat Interface
- **Sidebar**: List of conversations with search functionality
- **Message Area**: Real-time message display with smooth scrolling
- **Input Area**: Message composition with emoji and file support
- **User Profile**: Current user information and settings

### Message Features
- **Text Messages**: Send and receive text messages
- **Message Timestamps**: Display when messages were sent
- **Message Status**: Visual indicators for message states
- **Typing Indicators**: Show when users are typing
- **Message Reactions**: Add emoji reactions to messages (ready for implementation)

### Room Management
- **Direct Messages**: One-on-one conversations
- **Group Chats**: Multi-user conversations
- **Room Search**: Find conversations quickly
- **Unread Counts**: Track unread messages per room

### User Experience
- **Responsive Layout**: Adapts to different screen sizes
- **Smooth Animations**: Fluid transitions and interactions
- **Keyboard Shortcuts**: Enter to send, escape to cancel
- **Auto-scroll**: Automatically scroll to new messages

## Mock Data

The application includes comprehensive mock data for:
- Sample users with avatars and online status
- Multiple chat rooms (direct and group)
- Sample messages with timestamps
- User profiles and settings

## Real-time Integration

The app is structured to easily integrate with real-time features:

### Socket.io Integration
```typescript
// Example integration
import { io } from 'socket.io-client';

const socket = io('ws://localhost:3001');

socket.on('message', (message) => {
  setMessages(prev => [...prev, message]);
});

socket.on('typing', (user) => {
  setTypingUsers(prev => [...prev, user]);
});
```

### WebSocket Events
- `message`: New message received
- `typing`: User typing indicator
- `user_online`: User comes online
- `user_offline`: User goes offline
- `room_join`: User joins a room
- `room_leave`: User leaves a room

## Customization

### Styling
- Modify colors in `tailwind.config.ts`
- Update CSS variables in `globals.css`
- Customize component styles
- Adjust layout and spacing

### Features
- Add new message types (images, files, etc.)
- Implement message reactions
- Add voice/video call functionality
- Integrate with authentication system
- Add message encryption

### Data
- Replace mock data with real API calls
- Add database integration
- Implement user authentication
- Add message persistence

## Performance Optimizations

- Next.js 15 with App Router
- Optimized re-renders with React hooks
- Efficient message rendering
- Lazy loading for better performance
- Minimal bundle size

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment

This chat app can be deployed to:
- Vercel (recommended for Next.js)
- Netlify
- AWS
- Any Node.js hosting service

## Future Enhancements

- [ ] Real-time WebSocket integration
- [ ] Message encryption
- [ ] File and image sharing
- [ ] Voice and video calls
- [ ] Message reactions and replies
- [ ] Push notifications
- [ ] User authentication
- [ ] Message search
- [ ] Message editing and deletion
- [ ] Custom emoji support

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

If you have any questions or need help with the chat application, please open an issue on GitHub.
