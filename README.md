# Personal Agent Metabolic Flexibility Respiratory Quotient Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency indirect calorimetry Respiratory Exchange Ratio (RER) partitioner, substrate oxidation modeler (fat vs carbohydrate grams/min), and metabolic switch evaluator.

## Architecture

```mermaid
flowchart TD
    GasExchange[VO2 ml/min & VCO2 ml/min] --> CalorimetryEngine[Weir Indirect Calorimetry Engine]
    CalorimetryEngine --> RERCalc[Respiratory Exchange Ratio: RER = VCO2 / VO2]
    RERCalc --> SubstratePartition[Lusk/Frayn Equations: Fat % vs CHO %]
    CalorimetryEngine --> CaloricOutput[Energy Expenditure: kcal/min & kcal/hr]
    SubstratePartition --> GramBurnRate[Oxidation Rates: Fat g/hr & CHO g/hr]
    FastingInput[Fasting Hours & RQ] --> SwitchEngine[Metabolic Switch Classifier]
    SwitchEngine --> AutophagyStatus[AMPK Activation & Hepatic Glycogen Status]
```

## Quickstart

```python
from client import PersonalAgentMetabolicFlexibilityRespiratoryQuotient

agent = PersonalAgentMetabolicFlexibilityRespiratoryQuotient()
res = agent.calculate_substrate_oxidation_and_rer(vo2_ml_min=320.0, vco2_ml_min=240.0)
print(f"RER: {res['respiratory_exchange_ratio_rer']} | Fat: {res['fat_oxidation_percentage']} | CHO: {res['carbohydrate_oxidation_percentage']}")
```
