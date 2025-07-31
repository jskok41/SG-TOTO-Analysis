export interface TotoResult {
  drawNumber: string;
  drawDate: string;
  numbers: number[];
  additionalNumber: number;
  prizeAmount: number;
}

export interface NumberFrequency {
  number: number;
  frequency: number;
  percentage: number;
}

export interface PredictionResult {
  numbers: number[];
  confidence: number;
  method: string;
  timestamp: string;
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
  averagePrizeAmount: number;
  maxPrizeAmount: number;
  minPrizeAmount: number;
} 