# SureChoice

Understanding health insurance plans can be difficult, and comparing the pros and cons of different plans can be especially complex. This Python script plots your out-of-pocket cost for different plans as a function of total annual incurred medical costs so you can make better-informed decisions about your health insurance plan.

![example plot](https://github.com/jdaymude/SureChoice/blob/master/_assets/example_plot.png)

Some plans may be quite cost-effective if your total medical costs are low, but will be extremely costly if an expensive medical event happens unexpectedly. Some scale more linearly. Others cost a lot out-of-pocket up front, but pay off with higher total medical costs. Comparing plans in this way enables you to choose the best plan for your expected medical costs.


## Background and Key Terms

When using this code, it helps to understand a few key health insurance terms:

- _premium_: a fixed monthly payment for being on a plan.
- _deductible_: the total out-of-pocket amount to be paid before insurance covers anything.
- _copay_: the percentage of a total cost to be paid out-of-pocket after the deductible is met.
- _maximum out-of-pocket_: the maximum total out-of-pocket cost before insurance covers 100% of all subsequent payments.


## Installation

This is a fairly simple Python script. You need:

- Any installation of [Python 3.x](https://www.python.org/downloads/).
- The `matplotlib` [package](https://matplotlib.org/users/installing.html).

Clone this repository using your Git client of choice, or on the command line:

```
git clone https://github.com/jdaymude/SureChoice.git
```


## Preparing Plans for Comparison

To compare health insurance plans, you'll need to edit the various costs in `plans.json` (or make your own data file with the same structure). The schema of this file is:

```
{
  "info" : {
    "project" : "SureChoice",
    "author" : "Joshua J. Daymude",
    "license" : "MIT"
  },
  "plans" : [
    {
      "name" : <string>,            # Name of insurance plan
      "short_name" : <string>,      # Short name of plan to show in plot legend
      "description" : <string>,     # Description of plan
      "premium" : <float>,          # Monthly payment
      "deductible" : <float>,       # Plan deductible
      "copay" : <float>,            # Plan copay, number in [0,1]
      "max_oop" : <float or "Inf">  # Max out-of-pocket charge, or "Inf" if none
    },
    ...
  ]
}
```


## Running SureChoice

To run SureChoice, use:

```
python3 surechoice.py --data <path to plans.json>
```

Optionally, one can also use the `--max_annual_cost` variable to define the maximum total annual medical cost to consider. All options can be viewed with `python3 surechoice.py -h`.


## Feedback & Contibutions

SureChoice is a very minimal piece of software that could have many improvements (e.g., supporting Financial Savings Accounts). If you'd like to leave feedback, please post an [issue](https://github.com/jdaymude/SureChoice/issues). If you'd like to contribute, please submit your code via a [pull request](https://github.com/jdaymude/SureChoice/pulls).
