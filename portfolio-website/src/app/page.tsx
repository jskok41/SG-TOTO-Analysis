"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { 
  Github, 
  Linkedin, 
  Mail, 
  Download, 
  ExternalLink,
  Code,
  Palette,
  Database,
  Smartphone,
  Globe,
  Award,
  Calendar,
  MapPin
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const fadeInUp = {
  initial: { opacity: 0, y: 60 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.6 }
};

const stagger = {
  animate: {
    transition: {
      staggerChildren: 0.1
    }
  }
};

const projects = [
  {
    id: 1,
    title: "E-commerce Dashboard",
    description: "A comprehensive dashboard for managing online stores with analytics, product management, and order tracking.",
    image: "/placeholder-project.jpg",
    technologies: ["Next.js", "TypeScript", "Tailwind CSS", "shadcn/ui", "Recharts"],
    category: "Web App",
    github: "https://github.com",
    live: "https://example.com",
    featured: true
  },
  {
    id: 2,
    title: "Task Management App",
    description: "A modern task management application with priority levels, due dates, and progress tracking.",
    image: "/placeholder-project.jpg",
    technologies: ["Next.js", "TypeScript", "shadcn/ui", "Radix UI"],
    category: "Web App",
    github: "https://github.com",
    live: "https://example.com",
    featured: true
  },
  {
    id: 3,
    title: "Real-time Chat App",
    description: "A real-time messaging application with WebSocket integration and modern UI.",
    image: "/placeholder-project.jpg",
    technologies: ["React", "Node.js", "Socket.io", "MongoDB"],
    category: "Web App",
    github: "https://github.com",
    live: "https://example.com",
    featured: false
  },
  {
    id: 4,
    title: "Mobile Weather App",
    description: "A responsive weather application with location-based forecasts and beautiful animations.",
    image: "/placeholder-project.jpg",
    technologies: ["React Native", "TypeScript", "Expo"],
    category: "Mobile App",
    github: "https://github.com",
    live: "https://example.com",
    featured: false
  }
];

const skills = [
  { name: "Frontend Development", icon: <Code className="h-6 w-6" />, level: 95 },
  { name: "UI/UX Design", icon: <Palette className="h-6 w-6" />, level: 85 },
  { name: "Backend Development", icon: <Database className="h-6 w-6" />, level: 80 },
  { name: "Mobile Development", icon: <Smartphone className="h-6 w-6" />, level: 75 },
  { name: "DevOps", icon: <Globe className="h-6 w-6" />, level: 70 }
];

const experience = [
  {
    company: "Tech Solutions Inc.",
    position: "Senior Full Stack Developer",
    duration: "2022 - Present",
    location: "San Francisco, CA",
    description: "Led development of multiple web applications using React, Node.js, and cloud technologies. Improved application performance by 40% and mentored junior developers.",
    technologies: ["React", "Node.js", "AWS", "TypeScript", "PostgreSQL"]
  },
  {
    company: "Digital Agency Co.",
    position: "Frontend Developer",
    duration: "2020 - 2022",
    location: "New York, NY",
    description: "Developed responsive web applications and collaborated with design teams to create engaging user experiences.",
    technologies: ["React", "Vue.js", "Sass", "Webpack", "Figma"]
  },
  {
    company: "StartupXYZ",
    position: "Junior Developer",
    duration: "2019 - 2020",
    location: "Remote",
    description: "Built and maintained web applications using modern JavaScript frameworks and contributed to open-source projects.",
    technologies: ["JavaScript", "React", "Express.js", "MongoDB", "Git"]
  }
];

const education = [
  {
    degree: "Bachelor of Computer Science",
    school: "University of Technology",
    year: "2015 - 2019",
    description: "Focused on software engineering, algorithms, and data structures. Graduated with honors."
  },
  {
    degree: "Full Stack Web Development Bootcamp",
    school: "Tech Academy",
    year: "2019",
    description: "Intensive 6-month program covering modern web development technologies and best practices."
  }
];

export default function Portfolio() {
  const [activeTab, setActiveTab] = useState("about");

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      {/* Navigation */}
      <nav className="fixed top-0 w-full bg-white/80 dark:bg-gray-900/80 backdrop-blur-md z-50 border-b border-gray-200 dark:border-gray-700">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="text-2xl font-bold text-gray-900 dark:text-white"
            >
              Portfolio
            </motion.div>
            <div className="hidden md:flex space-x-8">
              {["about", "projects", "experience", "contact"].map((item) => (
                <button
                  key={item}
                  onClick={() => setActiveTab(item)}
                  className={`capitalize transition-colors ${
                    activeTab === item
                      ? "text-blue-600 dark:text-blue-400"
                      : "text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                  }`}
                >
                  {item}
                </button>
              ))}
            </div>
            <div className="flex space-x-4">
              <Button variant="outline" size="sm">
                <Download className="h-4 w-4 mr-2" />
                Resume
              </Button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20">
        <div className="container mx-auto px-4">
          <motion.div
            initial="initial"
            animate="animate"
            variants={stagger}
            className="text-center max-w-4xl mx-auto"
          >
            <motion.div
              variants={fadeInUp}
              className="w-32 h-32 mx-auto mb-8 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center text-white text-4xl font-bold"
            >
              JD
            </motion.div>
            <motion.h1
              variants={fadeInUp}
              className="text-5xl md:text-7xl font-bold text-gray-900 dark:text-white mb-6"
            >
              John Doe
            </motion.h1>
            <motion.p
              variants={fadeInUp}
              className="text-xl md:text-2xl text-gray-600 dark:text-gray-300 mb-8"
            >
              Full Stack Developer & UI/UX Designer
            </motion.p>
            <motion.p
              variants={fadeInUp}
              className="text-lg text-gray-500 dark:text-gray-400 mb-12 max-w-2xl mx-auto"
            >
              I create beautiful, functional, and user-centered digital experiences that solve real-world problems.
            </motion.p>
            <motion.div
              variants={fadeInUp}
              className="flex flex-col sm:flex-row gap-4 justify-center"
            >
              <Button size="lg" className="text-lg px-8 py-3">
                <Mail className="h-5 w-5 mr-2" />
                Get In Touch
              </Button>
              <Button variant="outline" size="lg" className="text-lg px-8 py-3">
                <Github className="h-5 w-5 mr-2" />
                View Work
              </Button>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Main Content */}
      <section className="pb-20">
        <div className="container mx-auto px-4">
          <Tabs value={activeTab} onValueChange={setActiveTab} className="max-w-6xl mx-auto">
            <TabsList className="grid w-full grid-cols-4 mb-12">
              <TabsTrigger value="about">About</TabsTrigger>
              <TabsTrigger value="projects">Projects</TabsTrigger>
              <TabsTrigger value="experience">Experience</TabsTrigger>
              <TabsTrigger value="contact">Contact</TabsTrigger>
            </TabsList>

            {/* About Tab */}
            <TabsContent value="about" className="space-y-12">
              <motion.div
                initial="initial"
                animate="animate"
                variants={stagger}
                className="grid grid-cols-1 lg:grid-cols-2 gap-12"
              >
                <motion.div variants={fadeInUp}>
                  <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6">About Me</h2>
                  <p className="text-lg text-gray-600 dark:text-gray-300 mb-6">
                    I'm a passionate full-stack developer with over 5 years of experience creating 
                    digital solutions that make a difference. I specialize in modern web technologies 
                    and have a keen eye for design and user experience.
                  </p>
                  <p className="text-lg text-gray-600 dark:text-gray-300 mb-8">
                    When I'm not coding, you can find me exploring new technologies, contributing to 
                    open-source projects, or sharing knowledge with the developer community.
                  </p>
                  <div className="flex space-x-4">
                    <Button variant="outline">
                      <Github className="h-4 w-4 mr-2" />
                      GitHub
                    </Button>
                    <Button variant="outline">
                      <Linkedin className="h-4 w-4 mr-2" />
                      LinkedIn
                    </Button>
                    <Button variant="outline">
                      <Mail className="h-4 w-4 mr-2" />
                      Email
                    </Button>
                  </div>
                </motion.div>

                <motion.div variants={fadeInUp}>
                  <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">Skills</h3>
                  <div className="space-y-4">
                    {skills.map((skill, index) => (
                      <div key={index} className="space-y-2">
                        <div className="flex items-center justify-between">
                          <div className="flex items-center space-x-2">
                            {skill.icon}
                            <span className="font-medium text-gray-900 dark:text-white">
                              {skill.name}
                            </span>
                          </div>
                          <span className="text-sm text-gray-500 dark:text-gray-400">
                            {skill.level}%
                          </span>
                        </div>
                        <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                          <div
                            className="bg-gradient-to-r from-blue-500 to-purple-600 h-2 rounded-full transition-all duration-1000"
                            style={{ width: `${skill.level}%` }}
                          />
                        </div>
                      </div>
                    ))}
                  </div>
                </motion.div>
              </motion.div>
            </TabsContent>

            {/* Projects Tab */}
            <TabsContent value="projects" className="space-y-8">
              <motion.div
                initial="initial"
                animate="animate"
                variants={stagger}
              >
                <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Featured Projects</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                  {projects.map((project, index) => (
                    <motion.div key={project.id} variants={fadeInUp}>
                      <Card className="group hover:shadow-xl transition-all duration-300">
                        <div className="aspect-video bg-gradient-to-br from-blue-500 to-purple-600 rounded-t-lg flex items-center justify-center text-white text-2xl font-bold">
                          {project.title.charAt(0)}
                        </div>
                        <CardHeader>
                          <div className="flex items-center justify-between">
                            <CardTitle className="text-xl">{project.title}</CardTitle>
                            <Badge variant="outline">{project.category}</Badge>
                          </div>
                          <CardDescription className="text-base">
                            {project.description}
                          </CardDescription>
                        </CardHeader>
                        <CardContent>
                          <div className="flex flex-wrap gap-2 mb-4">
                            {project.technologies.map((tech, techIndex) => (
                              <Badge key={techIndex} variant="secondary" className="text-xs">
                                {tech}
                              </Badge>
                            ))}
                          </div>
                          <div className="flex space-x-2">
                            <Button size="sm" variant="outline">
                              <Github className="h-4 w-4 mr-1" />
                              Code
                            </Button>
                            <Button size="sm">
                              <ExternalLink className="h-4 w-4 mr-1" />
                              Live Demo
                            </Button>
                          </div>
                        </CardContent>
                      </Card>
                    </motion.div>
                  ))}
                </div>
              </motion.div>
            </TabsContent>

            {/* Experience Tab */}
            <TabsContent value="experience" className="space-y-8">
              <motion.div
                initial="initial"
                animate="animate"
                variants={stagger}
              >
                <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Experience</h2>
                <div className="space-y-8">
                  {experience.map((job, index) => (
                    <motion.div key={index} variants={fadeInUp}>
                      <Card>
                        <CardHeader>
                          <div className="flex items-start justify-between">
                            <div>
                              <CardTitle className="text-xl">{job.position}</CardTitle>
                              <CardDescription className="text-lg font-medium text-blue-600 dark:text-blue-400">
                                {job.company}
                              </CardDescription>
                            </div>
                            <div className="text-right text-sm text-gray-500 dark:text-gray-400">
                              <div className="flex items-center mb-1">
                                <Calendar className="h-4 w-4 mr-1" />
                                {job.duration}
                              </div>
                              <div className="flex items-center">
                                <MapPin className="h-4 w-4 mr-1" />
                                {job.location}
                              </div>
                            </div>
                          </div>
                        </CardHeader>
                        <CardContent>
                          <p className="text-gray-600 dark:text-gray-300 mb-4">
                            {job.description}
                          </p>
                          <div className="flex flex-wrap gap-2">
                            {job.technologies.map((tech, techIndex) => (
                              <Badge key={techIndex} variant="outline">
                                {tech}
                              </Badge>
                            ))}
                          </div>
                        </CardContent>
                      </Card>
                    </motion.div>
                  ))}
                </div>

                <motion.div variants={fadeInUp} className="mt-12">
                  <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">Education</h3>
                  <div className="space-y-6">
                    {education.map((edu, index) => (
                      <Card key={index}>
                        <CardHeader>
                          <CardTitle className="text-lg">{edu.degree}</CardTitle>
                          <CardDescription className="text-base font-medium">
                            {edu.school} • {edu.year}
                          </CardDescription>
                        </CardHeader>
                        <CardContent>
                          <p className="text-gray-600 dark:text-gray-300">
                            {edu.description}
                          </p>
                        </CardContent>
                      </Card>
                    ))}
                  </div>
                </motion.div>
              </motion.div>
            </TabsContent>

            {/* Contact Tab */}
            <TabsContent value="contact" className="space-y-8">
              <motion.div
                initial="initial"
                animate="animate"
                variants={stagger}
                className="text-center max-w-2xl mx-auto"
              >
                <motion.div variants={fadeInUp}>
                  <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6">Get In Touch</h2>
                  <p className="text-lg text-gray-600 dark:text-gray-300 mb-8">
                    I'm always interested in new opportunities and exciting projects. 
                    Let's discuss how we can work together!
                  </p>
                </motion.div>

                <motion.div variants={fadeInUp} className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                  <Card className="text-center">
                    <CardContent className="pt-6">
                      <Mail className="h-8 w-8 mx-auto mb-4 text-blue-600 dark:text-blue-400" />
                      <h3 className="font-semibold mb-2">Email</h3>
                      <p className="text-sm text-gray-600 dark:text-gray-300">john@example.com</p>
                    </CardContent>
                  </Card>
                  <Card className="text-center">
                    <CardContent className="pt-6">
                      <Github className="h-8 w-8 mx-auto mb-4 text-blue-600 dark:text-blue-400" />
                      <h3 className="font-semibold mb-2">GitHub</h3>
                      <p className="text-sm text-gray-600 dark:text-gray-300">github.com/johndoe</p>
                    </CardContent>
                  </Card>
                  <Card className="text-center">
                    <CardContent className="pt-6">
                      <Linkedin className="h-8 w-8 mx-auto mb-4 text-blue-600 dark:text-blue-400" />
                      <h3 className="font-semibold mb-2">LinkedIn</h3>
                      <p className="text-sm text-gray-600 dark:text-gray-300">linkedin.com/in/johndoe</p>
                    </CardContent>
                  </Card>
                </motion.div>

                <motion.div variants={fadeInUp}>
                  <Button size="lg" className="text-lg px-8 py-3">
                    <Mail className="h-5 w-5 mr-2" />
                    Send Message
                  </Button>
                </motion.div>
              </motion.div>
            </TabsContent>
          </Tabs>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 dark:bg-gray-950 text-white py-8">
        <div className="container mx-auto px-4 text-center">
          <p className="text-gray-400">
            © 2024 John Doe. All rights reserved. Built with Next.js and Tailwind CSS.
          </p>
        </div>
      </footer>
    </div>
  );
}
