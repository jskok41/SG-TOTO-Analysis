import { NextResponse } from 'next/server';
import { promises as fs } from 'fs';
import path from 'path';

export async function GET() {
  try {
    const csvPath = path.join(process.cwd(), 'public', 'toto_results.csv');
    const csvData = await fs.readFile(csvPath, 'utf-8');
    
    // Parse CSV to JSON
    const lines = csvData.split('\n');
    const headers = lines[0].split(',');
    const results = [];
    
    for (let i = 1; i < lines.length; i++) {
      if (lines[i].trim()) {
        const values = lines[i].split(',');
        const row: any = {};
        headers.forEach((header, index) => {
          const value = values[index]?.trim();
          if (header.includes('Number') || header === '2' || header === '3' || header === '4' || header === '5' || header === '6' || header === 'Additional Number') {
            row[header] = parseInt(value) || 0;
          } else {
            row[header] = value;
          }
        });
        results.push(row);
      }
    }
    
    return NextResponse.json({ data: results });
  } catch (error) {
    console.error('Error reading CSV file:', error);
    return NextResponse.json({ error: 'Failed to load data' }, { status: 500 });
  }
} 