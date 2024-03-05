import unittest
import json
import sys as system
import io
import pandas as pd
import re
import numpy as np


with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            compile("".join(i['source']), '<string>', 'exec')


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def testLogitCorrectValues(self):
      data = pd.read_csv("assignment8Data.csv")
      x = data.loc[:100, ['sex','age','educ']]
      y = data.loc[:100, 'white']
      reg = RegressionModel(x, y, create_intercept=True, regression_type='logit')
      reg.fit_model()

      sex = {'coefficient': -1.1229156890097627,
      'standard_error': 0.39798772782618025,
      'z_stat': -2.821483202869492,
      'p_value': 0.004780214077269219}
      age = {'coefficient': -0.007012518056833769,
      'standard_error': 0.010835821823286998,
      'z_stat': -0.6471607019011091,
      'p_value': 0.5175279421902776}
      educ = {'coefficient': -0.046485475816343394,
      'standard_error': 0.10100278092776117,
      'z_stat': -0.46023956359766527,
      'p_value': 0.6453442758780246}
      intercept = {'coefficient': 5.735435005488546,
      'standard_error': 1.1266207023561843,
      'z_stat': 5.090830475148922,
      'p_value': 3.56498650369634e-07}
      sexEq = (round(sex['coefficient'], 1)==round(reg.results['sex']['coefficient'], 1)) & (round(sex['standard_error'], 1)==round(reg.results['sex']['standard_error'], 1)) & (round(sex['z_stat'], 1)==round(reg.results['sex']['z_stat'], 1)) & (round(sex['p_value'], 1)==round(reg.results['sex']['p_value'], 1))
      ageEq = (round(age['coefficient'], 1)==round(reg.results['age']['coefficient'], 1)) &  (round(age['standard_error'], 1)==round(reg.results['age']['standard_error'], 1)) & (round(age['z_stat'], 1)==round(reg.results['age']['z_stat'], 1)) & (round(age['p_value'], 1)==round(reg.results['age']['p_value'], 1))
      educEq = (round(educ['coefficient'], 1)==round(reg.results['educ']['coefficient'], 1)) & (round(educ['standard_error'], 1)==round(reg.results['educ']['standard_error'], 1)) & (round(educ['z_stat'], 1)==round(reg.results['educ']['z_stat'], 1)) & (round(educ['p_value'], 1)==round(reg.results['educ']['p_value'], 1))
      interceptEq = (round(intercept['coefficient'], 1)==round(reg.results['intercept']['coefficient'], 1)) & (round(intercept['standard_error'], 1)==round(reg.results['intercept']['standard_error'], 1)) & (round(intercept['z_stat'], 1)==round(reg.results['intercept']['z_stat'], 1)) & (round(intercept['p_value'], 1)==round(reg.results['intercept']['p_value'], 1))
      
      sexEq2 = (round(sex['coefficient'], 1)==round(reg.results['sex']['coefficient'], 1)) & (round(sex['standard_error'], 1)==round(reg.results['sex']['standard_error'], 1)) & (round(sex['z_stat'], 1)==round(reg.results['sex']['z_stat'], 1)) & (round(sex['p_value']/2, 1)==round(reg.results['sex']['p_value'], 1))
      ageEq2 = (round(age['coefficient'], 1)==round(reg.results['age']['coefficient'], 1)) &  (round(age['standard_error'], 1)==round(reg.results['age']['standard_error'], 1)) & (round(age['z_stat'], 1)==round(reg.results['age']['z_stat'], 1)) & (round(age['p_value']/2, 1)==round(reg.results['age']['p_value'], 1))
      educEq2 = (round(educ['coefficient'], 1)==round(reg.results['educ']['coefficient'], 1)) & (round(educ['standard_error'], 1)==round(reg.results['educ']['standard_error'], 1)) & (round(educ['z_stat'], 1)==round(reg.results['educ']['z_stat'], 1)) & (round(educ['p_value']/2, 1)==round(reg.results['educ']['p_value'], 1))
      interceptEq2 = (round(intercept['coefficient'], 1)==round(reg.results['intercept']['coefficient'], 1)) & (round(intercept['standard_error'], 1)==round(reg.results['intercept']['standard_error'], 1)) & (round(intercept['z_stat'], 1)==round(reg.results['intercept']['z_stat'], 1)) & (round(intercept['p_value']/2, 1)==round(reg.results['intercept']['p_value'], 1))
      
      self.assertTrue((sexEq & ageEq & educEq & interceptEq)|(sexEq2 & ageEq2 & educEq2 & interceptEq2), "Your coefficients are not corretly calculated.")
