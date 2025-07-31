'use client';

import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { AlertTriangle, Info } from 'lucide-react';

export function Footer() {
  return (
    <footer className="mt-12 py-8 border-t border-gray-200">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Disclaimer */}
          <Card className="border-orange-200 bg-orange-50">
            <CardContent className="pt-6">
              <div className="flex items-start gap-3">
                <AlertTriangle className="h-5 w-5 text-orange-600 mt-0.5" />
                <div>
                  <h3 className="font-semibold text-orange-800 mb-2">Important Disclaimer</h3>
                  <p className="text-sm text-orange-700">
                    This application is for educational and entertainment purposes only. 
                    Lottery predictions are not guaranteed and should not be used as the 
                    sole basis for gambling decisions. Please gamble responsibly.
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Information */}
          <Card className="border-blue-200 bg-blue-50">
            <CardContent className="pt-6">
              <div className="flex items-start gap-3">
                <Info className="h-5 w-5 text-blue-600 mt-0.5" />
                <div>
                  <h3 className="font-semibold text-blue-800 mb-2">About This App</h3>
                  <p className="text-sm text-blue-700 mb-3">
                    Built with Next.js 15, TypeScript, and shadcn/ui. 
                    Uses statistical analysis to analyze TOTO patterns.
                  </p>
                  <div className="flex flex-wrap gap-2">
                    <Badge variant="outline" className="text-xs">Next.js 15</Badge>
                    <Badge variant="outline" className="text-xs">TypeScript</Badge>
                    <Badge variant="outline" className="text-xs">shadcn/ui</Badge>
                    <Badge variant="outline" className="text-xs">Tailwind CSS</Badge>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Copyright */}
        <div className="mt-6 text-center">
          <p className="text-sm text-gray-600">
            © 2024 TOTO Analysis System. Built with ❤️ for educational purposes.
          </p>
        </div>
      </div>
    </footer>
  );
} 