#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: Quiocho_Pandas-P1.ipynb
Conversion Date: 2025-09-25T00:18:22.644Z
"""

import pandas as pd

cars = pd.read_csv('cars.csv')
cars

cars.iloc[:5, ::2]

cars.loc[(cars['Model']=='Mazda RX4')]

cars.loc[cars['Model']=='Camaro Z28', ['cyl']]

cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl','gear']]