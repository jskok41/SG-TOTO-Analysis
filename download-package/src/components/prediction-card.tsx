'use client';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { PredictionResult } from '@/types/toto';
import { Zap, Target, TrendingUp, TrendingDown, Shuffle } from 'lucide-react';

interface PredictionCardProps {
  prediction: PredictionResult;
  index: number;
}

const getIcon = (method: string) => {
  switch (method) {
    case 'Most Frequent Numbers':
      return <TrendingUp className="h-5 w-5" />;
    case 'Position-Based Analysis':
      return <Target className="h-5 w-5" />;
    case 'Hot Numbers':
      return <Zap className="h-5 w-5" />;
    case 'Cold Numbers':
      return <TrendingDown className="h-5 w-5" />;
    case 'Balanced Approach':
      return <Shuffle className="h-5 w-5" />;
    default:
      return <Target className="h-5 w-5" />;
  }
};

const getConfidenceColor = (confidence: number) => {
  if (confidence >= 0.3) return 'text-green-600';
  if (confidence >= 0.2) return 'text-yellow-600';
  return 'text-red-600';
};

export function PredictionCard({ prediction, index }: PredictionCardProps) {
  return (
    <Card className="border-2 border-blue-100 hover:border-blue-200 transition-colors">
      <CardHeader>
        <CardTitle className="flex items-center gap-2 text-lg">
          {getIcon(prediction.method)}
          {prediction.method}
        </CardTitle>
        <CardDescription className="text-sm">
          {prediction.reasoning}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Numbers Display */}
        <div className="flex flex-wrap gap-2 justify-center">
          {prediction.numbers.map((num, numIndex) => (
            <Badge 
              key={numIndex} 
              variant="secondary" 
              className="text-lg px-4 py-2 font-bold bg-blue-100 text-blue-800 hover:bg-blue-200"
            >
              {num}
            </Badge>
          ))}
        </div>
        
        {/* Confidence Level */}
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span className="font-medium">Confidence Level:</span>
            <span className={`font-bold ${getConfidenceColor(prediction.confidence)}`}>
              {(prediction.confidence * 100).toFixed(1)}%
            </span>
          </div>
          <Progress 
            value={prediction.confidence * 100} 
            className="h-3"
          />
        </div>
        
        {/* Method Ranking */}
        <div className="text-center">
          <Badge variant="outline" className="text-xs">
            Method #{index + 1}
          </Badge>
        </div>
      </CardContent>
    </Card>
  );
} 