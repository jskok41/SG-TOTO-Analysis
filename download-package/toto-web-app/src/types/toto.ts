export interface TotoResult {
  Date: string;
  'Winning Number 1': number;
  '2': number;
  '3': number;
  '4': number;
  '5': number;
  '6': number;
  'Additional Number': number;
}

export interface NumberFrequency {
  number: number;
  frequency: number;
  percentage: number;
  confidenceInterval: {
    lower: number;
    upper: number;
  };
}

export interface PredictionResult {
  numbers: number[];
  confidence: number;
  method: string;
  reasoning: string;
}

export interface PositionAnalysis {
  position: string;
  mostFrequent: number[];
  leastFrequent: number[];
  average: number;
}

export interface StatisticalSummary {
  totalDraws: number;
  dateRange: {
    start: string;
    end: string;
  };
  mostFrequentNumbers: NumberFrequency[];
  leastFrequentNumbers: NumberFrequency[];
  positionAnalysis: PositionAnalysis[];
  overallFrequency: NumberFrequency[];
} 