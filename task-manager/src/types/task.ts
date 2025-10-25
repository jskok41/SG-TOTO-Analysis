export interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  priority: "low" | "medium" | "high";
  dueDate?: Date;
  createdAt: Date;
  updatedAt: Date;
  category?: string;
}

export interface TaskCategory {
  id: string;
  name: string;
  color: string;
}

export type TaskFilter = "all" | "active" | "completed" | "high-priority";
export type TaskSort = "created" | "due" | "priority" | "title";
