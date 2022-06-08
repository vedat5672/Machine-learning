# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:41:42 2022

@author: Monster
"""

import pandas as pd

air_quality=pd.read_csv("air_quality_no2.csv")
# =============================================================================
# yeni sütün ekliyor londonun degerlerinin 1.882 katı
# =============================================================================
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)