# Analisi vendite e-commerce

Esercizio di modellazione e visualizzazione in Power BI su **dati simulati**. Non deriva da un'azienda reale e non misura risultati di business.

## Cosa mostra

- Modello dati con transazioni, dettagli d'ordine, prodotti, visite e calendario
- Misure DAX per tasso di conversione, rimbalzo e totali
- Report con funnel, andamento nel tempo, vendite per prodotto e card KPI

## Contenuto

| File | Descrizione |
|---|---|
| `Analisi vendite ecommerce nuova.pbix` | Report Power BI |
| `data/` | CSV simulati usati per il modello |
| `controlli_dati.py` | Calcola i KPI e confronta ogni ordine con le sue righe di dettaglio |

```bash
pip install pandas
python controlli_dati.py
```

## Controllo dei dati

Sui dati di `data/` risultano 19 transazioni, 1.806,90 € di fatturato, 95,10 € di valore medio per ordine e un rimbalzo del 36,1%.

- **Ordini incoerenti:** 7 ordini su 19 hanno un valore diverso dalla somma delle proprie righe. Per un'analisi reale andrebbero chiariti prima di calcolare il fatturato.
- **Conversione:** le 19 transazioni su 28.660 sessioni danno lo 0,07%, perché i dati sono un piccolo campione simulato.

Altri esercizi sono raccolti nel [portfolio](https://portfolio-pollastrelliandrea.skywork.website/).
