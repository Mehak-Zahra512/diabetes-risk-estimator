# Diabetes Risk Estimator
A clinical risk scoring system that estimates diabetes risk
from 5 health indicators — built with pre-medical domain
knowledge, not just programming logic.

## The Problem
Most people don't know their diabetes risk until it's serious.
Early awareness through simple tools can change that.

## What I Built
A rule-based scoring system analysing:
- Glucose level
- BMI
- Blood pressure
- Age
- Family history of diabetes

Each indicator contributes to a final score out of 100.
Users are classified into Low / Moderate / High risk
with plain-language explanations for every result.

## Scoring Logic
| Indicator | Threshold | Weight |
|---|---|---|
| Glucose | > 140 mg/dL | 30 points |
| Family History | Yes | 20 points |
| BMI | > 30 | 20 points |
| Age | > 45 | 25 points |
| Blood Pressure | > 140 mmHg | 15 points |

## Example Output
Risk Score: 75/100 → High Risk
Reasons: High glucose level · Obesity risk · Genetic risk factor

![Risk Output](output.png)

## Tech Stack
Python · Rule-Based Logic · Clinical Domain Knowledge

## What Makes This Different
The thresholds weren't chosen randomly.
Three years of pre-medical studies meant I understood
why glucose above 140 mg/dL matters clinically —
not just as a number in a dataset.

## How to Run
python diabetes_risk_estimator.py

## Honest Limitation
Rule-based only — no machine learning yet.
Next version: train on a real dataset like Pima Indians
Diabetes Dataset from Kaggle with proper ML pipeline.
