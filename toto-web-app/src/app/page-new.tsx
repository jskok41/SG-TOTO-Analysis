'use client';

import { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Badge } from '@/components/ui/badge';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { TotoAnalyzer } from '@/lib/toto-analysis';
import { TotoResult, PredictionResult, StatisticalSummary } from '@/types/toto';
import { TrendingUp, TrendingDown, Target, Calendar, Zap } from 'lucide-react';
import { PredictionCard } from '@/components/prediction-card';
import { Footer } from '@/components/footer';
import { getTotoData } from '@/lib/toto-data';

export default function Home() {
  const [data, setData] = useState<TotoResult[]>([]);
  const [analyzer, setAnalyzer] = useState<TotoAnalyzer | null>(null);
  const [predictions, setPredictions] = useState<PredictionResult[]>([]);
  const [summary, setSummary] = useState<StatisticalSummary | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadData = () => {
      try {
        // Use embedded data for standalone operation
        const totoData = getTotoData();
        setData(totoData);
        const analyzerInstance = new TotoAnalyzer(totoData);
        setAnalyzer(analyzerInstance);
        setPredictions(analyzerInstance.generatePredictions());
        setSummary(analyzerInstance.getStatisticalSummary());
      } catch (error) {
        console.error('Error loading data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-lg text-gray-600">Loading TOTO Analysis...</p>
        </div>
      </div>
    );
  }

  const chartData = analyzer?.getChartData();

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            🎯 TOTO Analysis & Prediction
          </h1>
          <p className="text-lg text-gray-600">
            Singapore TOTO Statistical Analysis and Number Prediction System
          </p>
        </div>

        {/* Summary Cards */}
        {summary && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Total Draws</CardTitle>
                <Calendar className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{summary.totalDraws}</div>
                <p className="text-xs text-muted-foreground">
                  {summary.dateRange.start} to {summary.dateRange.end}
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Most Frequent</CardTitle>
                <TrendingUp className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{summary.mostFrequentNumbers[0]?.number}</div>
                <p className="text-xs text-muted-foreground">
                  {summary.mostFrequentNumbers[0]?.frequency} times ({summary.mostFrequentNumbers[0]?.percentage.toFixed(1)}%)
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Least Frequent</CardTitle>
                <TrendingDown className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{summary.leastFrequentNumbers[0]?.number}</div>
                <p className="text-xs text-muted-foreground">
                  {summary.leastFrequentNumbers[0]?.frequency} times ({summary.leastFrequentNumbers[0]?.percentage.toFixed(1)}%)
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">Avg Prize</CardTitle>
                <Zap className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">${(summary.averagePrizeAmount / 1000000).toFixed(1)}M</div>
                <p className="text-xs text-muted-foreground">
                  Max: ${(summary.maxPrizeAmount / 1000000).toFixed(1)}M
                </p>
              </CardContent>
            </Card>
          </div>
        )}

        {/* Main Content */}
        <Tabs defaultValue="predictions" className="space-y-6">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="predictions">Predictions</TabsTrigger>
            <TabsTrigger value="analysis">Analysis</TabsTrigger>
            <TabsTrigger value="charts">Charts</TabsTrigger>
          </TabsList>

          {/* Predictions Tab */}
          <TabsContent value="predictions" className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {predictions.map((prediction, index) => (
                <PredictionCard key={index} prediction={prediction} />
              ))}
            </div>
          </TabsContent>

          {/* Analysis Tab */}
          <TabsContent value="analysis" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Most Frequent Numbers */}
              <Card>
                <CardHeader>
                  <CardTitle>Most Frequent Numbers</CardTitle>
                  <CardDescription>Top 10 most frequently drawn numbers</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {summary?.mostFrequentNumbers.slice(0, 10).map((item) => (
                      <div key={item.number} className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                          <Badge variant="outline">{item.number}</Badge>
                          <span className="text-sm text-muted-foreground">
                            {item.frequency} times
                          </span>
                        </div>
                        <div className="text-right">
                          <div className="text-sm font-medium">{item.percentage.toFixed(1)}%</div>
                          <div className="text-xs text-muted-foreground">
                            Frequency: {item.frequency} times
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Least Frequent Numbers */}
              <Card>
                <CardHeader>
                  <CardTitle>Least Frequent Numbers</CardTitle>
                  <CardDescription>Top 10 least frequently drawn numbers</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {summary?.leastFrequentNumbers.slice(0, 10).map((item) => (
                      <div key={item.number} className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                          <Badge variant="outline">{item.number}</Badge>
                          <span className="text-sm text-muted-foreground">
                            {item.frequency} times
                          </span>
                        </div>
                        <div className="text-right">
                          <div className="text-sm font-medium">{item.percentage.toFixed(1)}%</div>
                          <div className="text-xs text-muted-foreground">
                            Frequency: {item.frequency} times
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Charts Tab */}
          <TabsContent value="charts" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Frequency Chart */}
              <Card>
                <CardHeader>
                  <CardTitle>Number Frequency Distribution</CardTitle>
                  <CardDescription>Frequency of each number across all draws</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={chartData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="name" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="frequency" fill="#3b82f6" />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>

              {/* Percentage Chart */}
              <Card>
                <CardHeader>
                  <CardTitle>Number Percentage Distribution</CardTitle>
                  <CardDescription>Percentage distribution of numbers</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <AreaChart data={chartData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="name" />
                      <YAxis />
                      <Tooltip />
                      <Area type="monotone" dataKey="percentage" stroke="#10b981" fill="#10b981" fillOpacity={0.3} />
                    </AreaChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>

        {/* Footer */}
        <Footer />
      </div>
    </div>
  );
}