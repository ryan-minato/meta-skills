---
title: Time Series & Forecasting
description: Forecasting, feature-extraction, and change-point detection libraries for time-series data.
tags: [machine-learning, data-science, time-series]
---

# Time Series & Forecasting

Fetch when the target forecasts, decomposes, or detects anomalies and change points in time series. Each entry is one line and a documentation entry point; fetch install commands and API details from the entry point, never from memory. No entry is a recommendation.

## Tools

| Tool | One line | Docs |
|---|---|---|
| StatsForecast | fast classical forecasting at scale | <https://nixtlaverse.nixtla.io/statsforecast/> — llms.txt: <https://nixtlaverse.nixtla.io/llms.txt> |
| MLForecast | ML-based forecasting pipelines | <https://github.com/Nixtla/mlforecast> |
| NeuralForecast | neural forecasting models | <https://nixtlaverse.nixtla.io/neuralforecast/> — llms.txt: <https://nixtlaverse.nixtla.io/llms.txt> |
| Prophet | decomposable trend-seasonality forecasting | <https://facebook.github.io/prophet/> |
| sktime | unified sklearn-style time-series framework | <https://www.sktime.net/> — llms.txt: <https://www.sktime.net/llms.txt> |
| tsfresh | automatic time-series feature extraction | <https://tsfresh.readthedocs.io/> |
| ruptures | offline change-point detection | <https://centre-borelli.github.io/ruptures-docs/> |

## Gotchas

- pandas's time-series interface (datetime indexing, resampling, rolling windows) documents inside pandas — see the [dataframes-and-storage](dataframes-and-storage.md) page; a pandas-only target needs the pandas entry point, not a forecasting library's.
- statsmodels covers classical statistical and time-series models — its row lives on the [numerical-computing](numerical-computing.md) page.
- PyOD covers outlier and anomaly detection — its row lives on the [tabular-and-automl](tabular-and-automl.md) page.
