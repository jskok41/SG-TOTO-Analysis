"use client";

import { useState, useEffect, useRef } from "react";
import { 
  Send, 
  Smile, 
  Paperclip, 
  MoreVertical, 
  Search, 
  Phone, 
  Video, 
  Settings,
  Users,
  MessageCircle,
  Plus,
  LogOut
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { ScrollArea } from "@/components/ui/scroll-area";
import { User, Message, ChatRoom, ChatState } from "@/types/chat";

// Mock data
const mockUsers: User[] = [
  { id: "1", name: "John Doe", isOnline: true, avatar: "/placeholder-avatar.jpg" },
  { id: "2", name: "Jane Smith", isOnline: true, avatar: "/placeholder-avatar.jpg" },
  { id: "3", name: "Mike Johnson", isOnline: false, lastSeen: new Date(Date.now() - 300000) },
  { id: "4", name: "Sarah Wilson", isOnline: true, avatar: "/placeholder-avatar.jpg" },
  { id: "5", name: "Alex Brown", isOnline: false, lastSeen: new Date(Date.now() - 600000) }
];

const mockRooms: ChatRoom[] = [
  {
    id: "1",
    name: "General",
    description: "General discussion",
    type: "group",
    participants: mockUsers,
    lastMessage: {
      id: "1",
      content: "Hey everyone! How's it going?",
      senderId: "2",
      senderName: "Jane Smith",
      timestamp: new Date(Date.now() - 300000),
      type: "text"
    },
    unreadCount: 2,
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: "2",
    name: "John Doe",
    type: "direct",
    participants: [mockUsers[0]],
    lastMessage: {
      id: "2",
      content: "Thanks for the help with the project!",
      senderId: "1",
      senderName: "John Doe",
      timestamp: new Date(Date.now() - 600000),
      type: "text"
    },
    unreadCount: 0,
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: "3",
    name: "Project Team",
    description: "Project discussion and updates",
    type: "group",
    participants: [mockUsers[0], mockUsers[1], mockUsers[3]],
    lastMessage: {
      id: "3",
      content: "The new feature is ready for testing",
      senderId: "4",
      senderName: "Sarah Wilson",
      timestamp: new Date(Date.now() - 900000),
      type: "text"
    },
    unreadCount: 5,
    createdAt: new Date(),
    updatedAt: new Date()
  }
];

const mockMessages: Message[] = [
  {
    id: "1",
    content: "Hey everyone! How's it going?",
    senderId: "2",
    senderName: "Jane Smith",
    timestamp: new Date(Date.now() - 300000),
    type: "text"
  },
  {
    id: "2",
    content: "Great! Just finished the new feature",
    senderId: "1",
    senderName: "John Doe",
    timestamp: new Date(Date.now() - 240000),
    type: "text"
  },
  {
    id: "3",
    content: "Awesome! Can't wait to see it in action",
    senderId: "4",
    senderName: "Sarah Wilson",
    timestamp: new Date(Date.now() - 180000),
    type: "text"
  },
  {
    id: "4",
    content: "I'll share the demo link shortly",
    senderId: "1",
    senderName: "John Doe",
    timestamp: new Date(Date.now() - 120000),
    type: "text"
  },
  {
    id: "5",
    content: "Perfect! Thanks John",
    senderId: "2",
    senderName: "Jane Smith",
    timestamp: new Date(Date.now() - 60000),
    type: "text"
  }
];

export default function ChatApp() {
  const [currentUser] = useState<User>({ id: "current", name: "You", isOnline: true });
  const [rooms, setRooms] = useState<ChatRoom[]>(mockRooms);
  const [currentRoom, setCurrentRoom] = useState<ChatRoom | null>(mockRooms[0]);
  const [messages, setMessages] = useState<Message[]>(mockMessages);
  const [newMessage, setNewMessage] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [typingUsers, setTypingUsers] = useState<string[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = () => {
    if (!newMessage.trim() || !currentRoom) return;

    const message: Message = {
      id: Date.now().toString(),
      content: newMessage,
      senderId: currentUser.id,
      senderName: currentUser.name,
      timestamp: new Date(),
      type: "text"
    };

    setMessages([...messages, message]);
    setNewMessage("");
    setIsTyping(false);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleTyping = (e: React.ChangeEvent<HTMLInputElement>) => {
    setNewMessage(e.target.value);
    if (!isTyping && e.target.value) {
      setIsTyping(true);
      // Simulate typing indicator
      setTimeout(() => setIsTyping(false), 2000);
    }
  };

  const filteredRooms = rooms.filter(room =>
    room.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const formatTime = (date: Date) => {
    return new Intl.DateTimeFormat('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      hour12: true
    }).format(date);
  };

  const formatDate = (date: Date) => {
    const now = new Date();
    const diffTime = now.getTime() - date.getTime();
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return "Today";
    if (diffDays === 1) return "Yesterday";
    if (diffDays < 7) return `${diffDays} days ago`;
    return date.toLocaleDateString();
  };

  return (
    <div className="flex h-screen bg-gray-100 dark:bg-gray-900">
      {/* Sidebar */}
      <div className="w-80 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-gray-200 dark:border-gray-700">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-xl font-bold text-gray-900 dark:text-white">Chats</h1>
            <div className="flex space-x-2">
              <Button variant="ghost" size="sm">
                <Plus className="h-4 w-4" />
              </Button>
              <Button variant="ghost" size="sm">
                <Settings className="h-4 w-4" />
              </Button>
            </div>
          </div>
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
            <Input
              placeholder="Search conversations..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10"
            />
          </div>
        </div>

        {/* Rooms List */}
        <ScrollArea className="flex-1">
          <div className="p-2">
            {filteredRooms.map((room) => (
              <Card
                key={room.id}
                className={`mb-2 cursor-pointer transition-colors ${
                  currentRoom?.id === room.id
                    ? "bg-blue-50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800"
                    : "hover:bg-gray-50 dark:hover:bg-gray-700"
                }`}
                onClick={() => setCurrentRoom(room)}
              >
                <CardContent className="p-3">
                  <div className="flex items-center space-x-3">
                    <div className="relative">
                      {room.type === "group" ? (
                        <div className="w-12 h-12 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center text-white font-bold">
                          {room.name.charAt(0)}
                        </div>
                      ) : (
                        <Avatar className="w-12 h-12">
                          <AvatarImage src={room.participants[0]?.avatar} />
                          <AvatarFallback>
                            {room.participants[0]?.name.charAt(0)}
                          </AvatarFallback>
                        </Avatar>
                      )}
                      {room.type === "group" && (
                        <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-green-500 rounded-full border-2 border-white dark:border-gray-800"></div>
                      )}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between">
                        <h3 className="font-medium text-gray-900 dark:text-white truncate">
                          {room.name}
                        </h3>
                        {room.lastMessage && (
                          <span className="text-xs text-gray-500 dark:text-gray-400">
                            {formatTime(room.lastMessage.timestamp)}
                          </span>
                        )}
                      </div>
                      <div className="flex items-center justify-between">
                        <p className="text-sm text-gray-500 dark:text-gray-400 truncate">
                          {room.lastMessage ? room.lastMessage.content : "No messages yet"}
                        </p>
                        {room.unreadCount > 0 && (
                          <Badge variant="destructive" className="text-xs">
                            {room.unreadCount}
                          </Badge>
                        )}
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </ScrollArea>

        {/* User Profile */}
        <div className="p-4 border-t border-gray-200 dark:border-gray-700">
          <div className="flex items-center space-x-3">
            <Avatar className="w-10 h-10">
              <AvatarImage src={currentUser.avatar} />
              <AvatarFallback>{currentUser.name.charAt(0)}</AvatarFallback>
            </Avatar>
            <div className="flex-1">
              <p className="font-medium text-gray-900 dark:text-white">{currentUser.name}</p>
              <p className="text-sm text-green-500">Online</p>
            </div>
            <Button variant="ghost" size="sm">
              <LogOut className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {currentRoom ? (
          <>
            {/* Chat Header */}
            <div className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 p-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  {currentRoom.type === "group" ? (
                    <div className="w-10 h-10 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center text-white font-bold">
                      {currentRoom.name.charAt(0)}
                    </div>
                  ) : (
                    <Avatar className="w-10 h-10">
                      <AvatarImage src={currentRoom.participants[0]?.avatar} />
                      <AvatarFallback>
                        {currentRoom.participants[0]?.name.charAt(0)}
                      </AvatarFallback>
                    </Avatar>
                  )}
                  <div>
                    <h2 className="font-semibold text-gray-900 dark:text-white">
                      {currentRoom.name}
                    </h2>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {currentRoom.type === "group" 
                        ? `${currentRoom.participants.length} members`
                        : "Online"
                      }
                    </p>
                  </div>
                </div>
                <div className="flex space-x-2">
                  <Button variant="ghost" size="sm">
                    <Search className="h-4 w-4" />
                  </Button>
                  <Button variant="ghost" size="sm">
                    <Phone className="h-4 w-4" />
                  </Button>
                  <Button variant="ghost" size="sm">
                    <Video className="h-4 w-4" />
                  </Button>
                  <Button variant="ghost" size="sm">
                    <MoreVertical className="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </div>

            {/* Messages */}
            <ScrollArea className="flex-1 p-4">
              <div className="space-y-4">
                {messages.map((message) => (
                  <div
                    key={message.id}
                    className={`flex ${
                      message.senderId === currentUser.id ? "justify-end" : "justify-start"
                    }`}
                  >
                    <div
                      className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                        message.senderId === currentUser.id
                          ? "bg-blue-500 text-white"
                          : "bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white"
                      }`}
                    >
                      <p className="text-sm">{message.content}</p>
                      <p
                        className={`text-xs mt-1 ${
                          message.senderId === currentUser.id
                            ? "text-blue-100"
                            : "text-gray-500 dark:text-gray-400"
                        }`}
                      >
                        {formatTime(message.timestamp)}
                      </p>
                    </div>
                  </div>
                ))}
                {typingUsers.length > 0 && (
                  <div className="flex justify-start">
                    <div className="bg-gray-200 dark:bg-gray-700 px-4 py-2 rounded-lg">
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        {typingUsers.join(", ")} {typingUsers.length === 1 ? "is" : "are"} typing...
                      </p>
                    </div>
                  </div>
                )}
                <div ref={messagesEndRef} />
              </div>
            </ScrollArea>

            {/* Message Input */}
            <div className="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 p-4">
              <div className="flex items-center space-x-2">
                <Button variant="ghost" size="sm">
                  <Paperclip className="h-4 w-4" />
                </Button>
                <div className="flex-1 relative">
                  <Input
                    ref={inputRef}
                    placeholder="Type a message..."
                    value={newMessage}
                    onChange={handleTyping}
                    onKeyPress={handleKeyPress}
                    className="pr-10"
                  />
                  <Button
                    variant="ghost"
                    size="sm"
                    className="absolute right-1 top-1/2 transform -translate-y-1/2"
                  >
                    <Smile className="h-4 w-4" />
                  </Button>
                </div>
                <Button onClick={handleSendMessage} disabled={!newMessage.trim()}>
                  <Send className="h-4 w-4" />
                </Button>
              </div>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center">
            <div className="text-center">
              <MessageCircle className="h-16 w-16 text-gray-400 mx-auto mb-4" />
              <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-2">
                Select a conversation
              </h3>
              <p className="text-gray-500 dark:text-gray-400">
                Choose a conversation from the sidebar to start chatting
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
