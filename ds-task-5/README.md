# Prodigy InfoTech Data Science Track - Task 05
## Traffic Accident Hotspots & Pattern Analysis

### 📌 Overview
Analyze US traffic accident data to identify contributing factors (weather conditions, road surface state, time of day, lighting) and isolate accident hotspot cities and peak commuter risk windows.

### 🛠️ Analytics Workflow
1. **Dataset Generation**: `generate_accidents.py` constructs a 2,500-incident accident dataset across major metro locations (`Los Angeles`, `Miami`, `Houston`, `Chicago`, `New York`, etc.).
2. **Temporal & Environmental Analysis**: `accident_analysis.py` evaluates peak accident hours (Rush Hour analysis 7-8 AM and 4-5 PM), weather severity impact, and road surface conditions (Icy, Wet, Construction Zone).
3. **Hotspot Identification**: Aggregates state and city coordinates to rank top traffic accident hotspots.

### 🚀 How to Run

```bash
# Run Accident Analytics Script
python accident_analysis.py
```
