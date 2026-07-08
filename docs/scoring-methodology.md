# Scoring Methodology

## Approach

Each neighborhood gets a 0–100 score per category. A weighted composite produces the final ranking. API responses will include both the composite and the category breakdown so clients can explain why a neighborhood ranked where it did.

## Categories

| Category | Input signal | Score direction |
|----------|--------------|-----------------|
| Demand | Estimated customer need / spending potential | Higher raw value → higher score |
| Competition | Count or density of similar businesses | Higher raw value → lower score (inverted) |
| Affordability | Commercial rent / cost pressure | Higher raw value → lower score (inverted) |
| Transit | Transit access and walkability | Higher raw value → higher score |
| Growth | Development activity and trajectory | Higher raw value → higher score |

## Inverted scoring

**Competition** — More nearby competitors mean a harder market. The engine converts high competition into a lower category score before combining.

**Affordability** — Higher rent and operating costs reduce feasibility. The engine converts high cost pressure into a lower affordability score.

## Composite score

```
composite = (demand × w1) + (competition × w2) + (affordability × w3)
          + (transit × w4) + (growth × w5)
```

v1 uses equal weights (0.20 each). Business-type-specific weights are a possible follow-up.

## Data (v1)

Category inputs will come from seeded mock data stored in PostgreSQL. There is no ETL pipeline or live public data integration in the initial build — that keeps the first phase focused on API structure and scoring logic.
