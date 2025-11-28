# -*- coding: utf-8 -*-
"""
@Author: GU Linghao
@File: calculator.py
@Description: Load the model and calculate logkNO3.
"""

import pandas as pd
import catboost
from lib.featurization import get_fps, screen_fps, generate_features


class Calculator:

    def __init__(self):
        tmp = catboost.CatBoostRegressor()
        tmp.load_model("model/final_model.cbm")
        self.model = tmp

    def run(self, smiles, ionic_conc):

        fps = get_fps(smiles=smiles)

        df_columns = pd.read_csv("data/RDKit_features.csv")
        columns = df_columns["features"]
        fps = screen_fps(fps=fps, columns=columns)

        features = generate_features(fps=fps, ionic_conc=ionic_conc)

        return self.model.predict(features)

    def run_cloud(self, smiles):
        ionic_conc = {"H_+":0.0001, "ClO4_-":0.1001, "K_+":0.16, "S2O8_2-":0.03, "NO3_-":0.1}
        return self.run(smiles=smiles, ionic_conc=ionic_conc)

    def run_alw(self, smiles):
        ionic_conc = {"H_+": 1, "ClO4_-": 6, "K_+": 0.16, "S2O8_2-": 0.03, "NO3_-": 0.1, "Na_+": 5}
        return self.run(smiles=smiles, ionic_conc=ionic_conc)
