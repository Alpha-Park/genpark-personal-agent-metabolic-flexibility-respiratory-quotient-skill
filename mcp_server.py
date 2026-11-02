# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Metabolic Flexibility Respiratory Quotient Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentMetabolicFlexibilityRespiratoryQuotient

mcp = FastMCP("PersonalAgentMetabolicFlexibilityRespiratoryQuotient")
client = PersonalAgentMetabolicFlexibilityRespiratoryQuotient()

@mcp.tool()
def calculate_substrate_oxidation_and_rer(
    vo2_ml_min: float = 350.0,
    vco2_ml_min: float = 270.0
) -> str:
    """Calculates Respiratory Exchange Ratio (RER), fat vs carbohydrate oxidation rates, and caloric expenditure."""
    import json
    return json.dumps(client.calculate_substrate_oxidation_and_rer(
        vo2_ml_min, vco2_ml_min
    ), indent=2)

@mcp.tool()
def evaluate_fasting_metabolic_switch(
    fasting_hours: float = 16.0,
    current_rq: float = 0.74
) -> str:
    """Evaluates whether the physiological fasting metabolic switch to lipid beta-oxidation has been achieved."""
    import json
    return json.dumps(client.evaluate_fasting_metabolic_switch(
        fasting_hours, current_rq
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
