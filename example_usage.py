# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Metabolic Flexibility Respiratory Quotient Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentMetabolicFlexibilityRespiratoryQuotient

def main():
    agent = PersonalAgentMetabolicFlexibilityRespiratoryQuotient()

    print("=" * 70)
    print("DEMO: Personal Agent Metabolic Flexibility & RER Calorimetry")
    print("=" * 70)

    # 1. Indirect Calorimetry Analysis (Resting VO2 = 320 ml/min, VCO2 = 240 ml/min -> RER = 0.750)
    res_rer = agent.calculate_substrate_oxidation_and_rer(
        vo2_ml_min=320.0,
        vco2_ml_min=240.0
    )

    print(f"\n1. Substrate Oxidation & Calorimetry Profile:")
    print(f"   VO2: {res_rer['vo2_consumption_ml_min']} ml/min | VCO2: {res_rer['vco2_production_ml_min']} ml/min")
    print(f"   Respiratory Exchange Ratio (RER): {res_rer['respiratory_exchange_ratio_rer']}")
    print(f"   Substrate Partitioning: Fat = {res_rer['fat_oxidation_percentage']} | CHO = {res_rer['carbohydrate_oxidation_percentage']}")
    print(f"   Metabolic State: {res_rer['metabolic_state']}")
    print(f"   Caloric Expenditure: {res_rer['energy_expenditure_kcal_min']} kcal/min ({res_rer['energy_expenditure_kcal_hour']} kcal/hr)")
    print(f"   Substrate Burn Rate: Fat = {res_rer['fat_oxidation_rate_g_hour']} g/hr | CHO = {res_rer['carbohydrate_oxidation_rate_g_hour']} g/hr")
    print(f"   Metabolic Flexibility Score: {res_rer['metabolic_flexibility_score_100']}/100 ({res_rer['metabolic_flexibility_status']})")

    # 2. Evaluate Fasting Metabolic Switch at 16.5 hours fasted with RQ 0.73
    res_switch = agent.evaluate_fasting_metabolic_switch(
        fasting_hours=16.5,
        current_rq=0.73
    )

    print(f"\n2. Fasting Metabolic Switch Evaluation (16.5 Hours Fasted):")
    print(f"   Fasting Duration: {res_switch['fasting_duration_hours']} hrs | RQ: {res_switch['respiratory_quotient']}")
    print(f"   Switch Achieved: {res_switch['metabolic_switch_achieved']}")
    print(f"   Physiological Status: {res_switch['physiological_status']}")
    print(f"   Cellular Profile: {res_switch['cellular_benefit_profile']}")
    print(f"   Prescription: {res_switch['prescribed_intervention']}")

    print("\nVerification complete: Metabolic flexibility engine executed flawlessly.")

if __name__ == "__main__":
    main()
