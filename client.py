# -*- coding: utf-8 -*-
"""Personal Agent Metabolic Flexibility Respiratory Quotient Skill.

Zero-dependency indirect calorimetry Respiratory Exchange Ratio (RER) partitioner,
substrate oxidation modeler (fat vs carbohydrate grams/min), and metabolic switch evaluator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentMetabolicFlexibilityRespiratoryQuotient:
    """Quantitative indirect calorimetry and substrate utilization engine based on
    the Weir equation and Lusk/Frayn non-protein respiratory quotient mathematical models."""

    def calculate_substrate_oxidation_and_rer(
        self,
        vo2_ml_min: float = 350.0,
        vco2_ml_min: float = 270.0
    ) -> Dict[str, Any]:
        """Calculates Respiratory Exchange Ratio (RER), relative substrate partitioning (%),
        caloric expenditure (kcal/min), and absolute fat vs carbohydrate oxidation rates (g/min)."""
        vo2 = max(50.0, float(vo2_ml_min))
        vco2 = max(35.0, float(vco2_ml_min))

        rer = round(vco2 / vo2, 3)

        # Substrate oxidation partitioning between 0.707 (100% fat) and 1.000 (100% carbohydrate)
        if rer <= 0.707:
            fat_pct = 100.0
            cho_pct = 0.0
            metabolic_state = "Pure Lipolysis & Beta-Oxidation Dominance"
        elif rer >= 1.000:
            fat_pct = 0.0
            cho_pct = 100.0
            metabolic_state = "Pure Glycolytic Flux" if rer <= 1.02 else "Anaerobic Lactic Acid Buffering (Hypercapnia)"
        else:
            # Linear partition: (1.0 - rer) / (1.0 - 0.707)
            fat_fraction = (1.0 - rer) / (1.0 - 0.707)
            fat_pct = round(fat_fraction * 100.0, 1)
            cho_pct = round((1.0 - fat_fraction) * 100.0, 1)
            metabolic_state = "Dual-Fuel Hybrid Oxidation"

        # Weir Equation for Energy Expenditure:
        # EE (kcal/min) = 3.941 * (VO2 / 1000) + 1.106 * (VCO2 / 1000)
        vo2_l = vo2 / 1000.0
        vco2_l = vco2 / 1000.0
        kcal_per_min = round(3.941 * vo2_l + 1.106 * vco2_l, 2)
        kcal_per_hour = round(kcal_per_min * 60.0, 1)

        # Frayn Non-Protein Oxidation Rates (grams / minute):
        # Fat (g/min) = 1.67 * VO2_L - 1.67 * VCO2_L
        # Carbohydrate (g/min) = 4.55 * VCO2_L - 3.21 * VO2_L
        fat_g_min = max(0.0, round(1.67 * vo2_l - 1.67 * vco2_l, 3))
        cho_g_min = max(0.0, round(4.55 * vco2_l - 3.21 * vo2_l, 3))

        fat_g_hour = round(fat_g_min * 60.0, 1)
        cho_g_hour = round(cho_g_min * 60.0, 1)

        # Metabolic Flexibility Index (MFI: 0 - 100)
        # Evaluates distance from optimal resting fasting state (~0.72 - 0.78)
        if 0.71 <= rer <= 0.82:
            mfi_score = 95.0
            flex_status = "Superior Resting Metabolic Flexibility (Robust Lipid Oxidation)"
        elif 0.83 <= rer <= 0.88:
            mfi_score = 75.0
            flex_status = "Moderate Metabolic Flexibility"
        else:
            mfi_score = 45.0
            flex_status = "Impaired Resting Fat Oxidation / Inflexible Glycolytic Dependence"

        return {
            "vo2_consumption_ml_min": vo2,
            "vco2_production_ml_min": vco2,
            "respiratory_exchange_ratio_rer": rer,
            "fat_oxidation_percentage": f"{fat_pct}%",
            "carbohydrate_oxidation_percentage": f"{cho_pct}%",
            "metabolic_state": metabolic_state,
            "energy_expenditure_kcal_min": kcal_per_min,
            "energy_expenditure_kcal_hour": kcal_per_hour,
            "fat_oxidation_rate_g_hour": fat_g_hour,
            "carbohydrate_oxidation_rate_g_hour": cho_g_hour,
            "metabolic_flexibility_score_100": mfi_score,
            "metabolic_flexibility_status": flex_status
        }

    def evaluate_fasting_metabolic_switch(
        self,
        fasting_hours: float,
        current_rq: float = 0.77
    ) -> Dict[str, Any]:
        """Evaluates whether the physiological fasting metabolic switch from glycogenolysis
        to ketone/fatty-acid oxidation has been achieved."""
        hours = max(0.0, float(fasting_hours))
        rq = max(0.68, min(1.15, float(current_rq)))

        # Fasting Switch Threshold: hours >= 14 and RQ <= 0.75
        glycogen_depleted = hours >= 14.0
        lipid_dominant = rq <= 0.75
        switch_achieved = glycogen_depleted and lipid_dominant

        if switch_achieved:
            status = "Metabolic Switch Fully Engaged (Hepatic Glycogen Cleared / Ketogenesis Active)"
            cellular_benefit = "Elevated AMPK phosphorylation, enhanced autophagy flux, low systemic insulin signaling"
        elif hours >= 12.0:
            status = "Transition Phase (Glycogen Depletion Imminent)"
            cellular_benefit = "Declining portal insulin, initiating hormone-sensitive lipase (HSL) mobilization"
        else:
            status = "Postprandial / Early Fasting Phase (Glucose-Fed Metabolism)"
            cellular_benefit = "Standard alimentary nutrient absorption"

        return {
            "fasting_duration_hours": hours,
            "respiratory_quotient": rq,
            "metabolic_switch_achieved": switch_achieved,
            "physiological_status": status,
            "cellular_benefit_profile": cellular_benefit,
            "prescribed_intervention": (
                "Maintain hydration and electrolytes; continue fasted window to maximize cellular autophagy."
                if switch_achieved else
                "Perform light Zone 2 aerobic walking to accelerate remaining hepatic glycogen clearance."
            )
        }
