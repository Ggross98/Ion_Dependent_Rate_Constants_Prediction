# -*- coding: utf-8 -*-
"""
@Author: GU Linghao
@File: example.py
@Description: An example of calculating logkNO3 under cloud and ALW conditions
"""

import pandas as pd
import calculator

df = pd.read_csv("data/phenols.csv")
smiles = df["smiles"]

ret = pd.DataFrame()
ret['smiles'] = smiles

c = calculator.Calculator()
ret['cloud'] = c.run_cloud(smiles)
ret['ALW'] = c.run_alw(smiles)

print(ret)
