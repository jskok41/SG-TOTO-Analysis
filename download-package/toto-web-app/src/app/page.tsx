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
                <CardTitle className="text-sm font-medium">Prediction Methods</CardTitle>
                <Target className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{predictions.length}</div>
                <p className="text-xs text-muted-foreground">
                  Different analysis approaches
                </p>
              </CardContent>
            </Card>
          </div>
        )}

        {/* Main Content */}
        <Tabs defaultValue="predictions" className="space-y-6">
          <TabsList className="grid w-full grid-cols-4">
            <TabsTrigger value="predictions">Predictions</TabsTrigger>
            <TabsTrigger value="statistics">Statistics</TabsTrigger>
            <TabsTrigger value="charts">Charts</TabsTrigger>
            <TabsTrigger value="data">Raw Data</TabsTrigger>
          </TabsList>

          {/* Predictions Tab */}
          <TabsContent value="predictions" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Zap className="h-5 w-5" />
                  Number Predictions
                </CardTitle>
                <CardDescription>
                  AI-powered predictions using multiple statistical methods
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {predictions.map((prediction, index) => (
                    <PredictionCard key={index} prediction={prediction} index={index} />
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Statistics Tab */}
          <TabsContent value="statistics" className="space-y-6">
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
                            CI: {item.confidenceInterval.lower.toFixed(1)}% - {item.confidenceInterval.upper.toFixed(1)}%
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
                            CI: {item.confidenceInterval.lower.toFixed(1)}% - {item.confidenceInterval.upper.toFixed(1)}%
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Position Analysis */}
            <Card>
              <CardHeader>
                <CardTitle>Position Analysis</CardTitle>
                <CardDescription>Analysis by number position</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {summary?.positionAnalysis.map((pos, index) => (
                    <Card key={index} className="border">
                      <CardHeader>
                        <CardTitle className="text-lg">{pos.position}</CardTitle>
                      </CardHeader>
                      <CardContent className="space-y-3">
                        <div>
                          <div className="text-sm font-medium text-green-600">Most Frequent:</div>
                          <div className="flex flex-wrap gap-1 mt-1">
                            {pos.mostFrequent.map(num => (
                              <Badge key={num} variant="secondary" className="text-xs">
                                {num}
                              </Badge>
                            ))}
                          </div>
                        </div>
                        <div>
                          <div className="text-sm font-medium text-red-600">Least Frequent:</div>
                          <div className="flex flex-wrap gap-1 mt-1">
                            {pos.leastFrequent.map(num => (
                              <Badge key={num} variant="outline" className="text-xs">
                                {num}
                              </Badge>
                            ))}
                          </div>
                        </div>
                        <div className="text-sm">
                          <span className="font-medium">Average:</span> {pos.average.toFixed(1)}
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </CardContent>
            </Card>
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
                    <BarChart data={chartData?.frequencyChart}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="number" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="frequency" fill="#3b82f6" />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>

              {/* Confidence Intervals */}
              <Card>
                <CardHeader>
                  <CardTitle>Confidence Intervals</CardTitle>
                  <CardDescription>95% confidence intervals for each number</CardDescription>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <AreaChart data={chartData?.confidenceIntervals}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="number" />
                      <YAxis />
                      <Tooltip />
                      <Area type="monotone" dataKey="upper" stackId="1" stroke="#8884d8" fill="#8884d8" />
                      <Area type="monotone" dataKey="lower" stackId="1" stroke="#82ca9d" fill="#82ca9d" />
                      <Area type="monotone" dataKey="percentage" stroke="#ff7300" fill="#ff7300" fillOpacity={0.3} strokeWidth={2} />
                    </AreaChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Data Tab */}
          <TabsContent value="data" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Raw TOTO Data</CardTitle>
                <CardDescription>Historical TOTO results data</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b">
                        <th className="text-left p-2">Date</th>
                        <th className="text-left p-2">Num 1</th>
                        <th className="text-left p-2">Num 2</th>
                        <th className="text-left p-2">Num 3</th>
                        <th className="text-left p-2">Num 4</th>
                        <th className="text-left p-2">Num 5</th>
                        <th className="text-left p-2">Num 6</th>
                        <th className="text-left p-2">Additional</th>
                      </tr>
                    </thead>
                    <tbody>
                      {data.slice(0, 20).map((row, index) => (
                        <tr key={index} className="border-b hover:bg-gray-50">
                          <td className="p-2">{row.Date}</td>
                          <td className="p-2">
                            <Badge variant="outline">{row['Winning Number 1']}</Badge>
                          </td>
                          <td className="p-2">
                            <Badge variant="outline">{row['2']}</Badge>
                          </td>
                          <td className="p-2">
                            <Badge variant="outline">{row['3']}</Badge>
                          </td>
                          <td className="p-2">
                            <Badge variant="outline">{row['4']}</Badge>
                          </td>
                          <td className="p-2">
                            <Badge variant="outline">{row['5']}</Badge>
                          </td>
                          <td className="p-2">
                            <Badge variant="outline">{row['6']}</Badge>
                          </td>
                          <td className="p-2">
                            <Badge variant="secondary">{row['Additional Number']}</Badge>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <div className="mt-4 text-center">
                  <p className="text-sm text-muted-foreground">
                    Showing first 20 results of {data.length} total draws
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
        
        {/* Footer */}
        <Footer />
      </div>
    </div>
  );
}
