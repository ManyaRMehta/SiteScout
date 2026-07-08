# Project Overview

## What SiteScout Does

SiteScout is a backend service that ranks Boston neighborhoods for a given business type. A client sends a business type (for example, coffee shop), and the API returns scored neighborhoods with a breakdown across five categories: demand, competition, affordability, transit, and growth.

The goal is explainability — each score should be traceable to its inputs, not just a single opaque number.

## Audience

This project is aimed at demonstrating backend API design, data modeling, and scoring logic. The primary use case is small business site selection in Boston, but the implementation focus is the data service layer, not a consumer-facing product.

## Why Boston (v1)

A single city keeps the data model and scoring inputs manageable while still reflecting a real location intelligence problem. Boston has distinct neighborhoods with varying commercial rent, transit access, and business density — enough variation to make ranking meaningful without multi-city infrastructure.

## Business Types (v1)

- Coffee shop
- Bakery
- Gym
- Salon
- Bookstore

Each type may weight scoring categories differently in a later iteration. v1 starts with equal weights across categories.

## Scoring Categories

| Category | Measures |
|----------|----------|
| Demand | Customer need and spending potential |
| Competition | Density of similar businesses (inverted — less competition scores higher) |
| Affordability | Commercial rent and cost pressure (inverted — lower cost scores higher) |
| Transit | Public transit access and walkability |
| Growth | Development and neighborhood trajectory |

See [scoring-methodology.md](scoring-methodology.md) for how categories combine into a composite score.
