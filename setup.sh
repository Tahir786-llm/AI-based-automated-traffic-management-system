#!/bin/bash

echo "🚦 Setting up AI-Based Traffic Management System..."

# Step 1: Create a Virtual Environment
echo "🔧 Creating Virtual Environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install Dependencies
echo "📦 Installing required packages..."
pip install -r backend/requirements.txt

# Step 3: Check if traffic_model.h5 exists
if [ ! -f "backend/models/traffic_model.h5" ]; then
    echo "⚠️ traffic_model.h5 not found! Please add a trained model."
else
    echo "✅ AI Model detected!"
fi

# Step 4: Start the Flask App
echo "🚀 Running Flask Server..."
python backend/app.py
