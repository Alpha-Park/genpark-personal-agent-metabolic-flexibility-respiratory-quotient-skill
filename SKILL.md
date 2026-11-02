---
name: genpark-personal-agent-metabolic-flexibility-respiratory-quotient-skill
version: "1.0.0"
description: "Zero-dependency indirect calorimetry Respiratory Exchange Ratio (RER) partitioner, substrate oxidation modeler (fat vs carbohydrate grams/min), and metabolic switch evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Metabolic Flexibility Respiratory Quotient Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to evaluate cellular metabolic flexibility, compute indirect calorimetry Respiratory Exchange Ratio ($RER = V_{\text{CO}_2} / V_{\text{O}_2}$), quantify absolute grams/hour of lipid vs carbohydrate oxidation using Frayn equations, calculate caloric expenditure via the Weir formula, and model fasting metabolic switch latency.

## Agent In-Context Capabilities

- **Substrate Oxidation Partitioning**: Translates respiratory gas exchange into precise fat vs carbohydrate burning percentages.
- **Caloric & Gram Flux Modeling**: Computes energy expenditure (kcal/min and kcal/hour) and grams of fat vs glycogen oxidized per hour.
- **Fasting Switch Tracking**: Detects when hepatic glycogen depletion and portal insulin drop allow full ketogenesis and lipolysis engagement ($RER \le 0.75$).

## Tools Summary

1. `calculate_substrate_oxidation_and_rer`: Returns RER, fat/CHO percentages, burn rates in g/hr, and metabolic flexibility score.
2. `evaluate_fasting_metabolic_switch`: Analyzes fasting duration and RQ to determine whether the cellular metabolic switch is engaged.
