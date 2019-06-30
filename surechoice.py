# Project:     SureChoice
# Filename:    surechoice.py
# Authors:     Joshua J. Daymude (jdaymude@asu.edu)
# Description: Compares health insurance plans based on annual out-of-pocket
#              cost to the client as a function of total medical costs.

"""
SureChoice: Make better informed decisions about health insurance.
"""

import argparse
import json
import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Parse arguments.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', required=True, help='JSON file of plans data')
    parser.add_argument('--max_annual_cost', default=30000, help='Maximum ' \
                        + 'total annual medical cost to consider')
    args = parser.parse_args()

    # Load plans data.
    with open(args.data) as f_in:
        data = json.load(f_in)

    # Compute costs for each plan.
    oop_costs = {}
    amnts = [i for i in range(int(args.max_annual_cost) + 1)]
    for plan in data['plans']:
        plan_oop = []
        max_oop = math.inf if plan['max_oop'] == 'None' else plan['max_oop']
        for amnt in amnts:
            prem_cost = plan['premium'] * 12
            to_deduct = min(amnt, plan['deductible'])
            remaining = (amnt - to_deduct) * plan['copay']
            plan_oop.append(prem_cost + min(to_deduct + remaining, max_oop))
        oop_costs[plan['short_name']] = plan_oop

    # Plot the results.
    fig, ax = plt.subplots()
    for plan in data['plans']:
        ax.plot(amnts, oop_costs[plan['short_name']], label=plan['short_name'])
    ax.set(title='Health Insurance Comparison', xlabel='Annual Medical ' \
           + 'Costs ($)', ylabel='Out-of-Pocket Costs ($)')
    ax.legend(loc='upper left')
    ax.grid()
    fig.savefig('plot.png', dpi=300)
