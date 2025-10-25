export interface User {
  id: string;
  name: string;
  avatar?: string;
  isOnline: boolean;
  lastSeen?: Date;
}

export interface Message {
  id: string;
  content: string;
  senderId: string;
  senderName: string;
  timestamp: Date;
  type: 'text' | 'image' | 'file' | 'system';
  replyTo?: string;
  edited?: boolean;
  reactions?: Reaction[];
}

export interface Reaction {
  emoji: string;
  userId: string;
  userName: string;
  timestamp: Date;
}

export interface ChatRoom {
  id: string;
  name: string;
  description?: string;
  type: 'direct' | 'group';
  participants: User[];
  lastMessage?: Message;
  unreadCount: number;
  createdAt: Date;
  updatedAt: Date;
}

export interface TypingUser {
  userId: string;
  userName: string;
  roomId: string;
}

export interface ChatState {
  currentUser: User | null;
  rooms: ChatRoom[];
  currentRoom: ChatRoom | null;
  messages: Message[];
  onlineUsers: User[];
  typingUsers: TypingUser[];
  isConnected: boolean;
}
