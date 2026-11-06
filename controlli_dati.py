"""Calcola i KPI del report e controlla la coerenza dei dati simulati."""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"


def carica():
    return {nome: pd.read_csv(DATA / f"{nome}.csv", encoding="utf-8-sig")
            for nome in ("transazione", "dettagli_transazioni", "visite", "prodotti")}


def kpi(d):
    t, v = d["transazione"], d["visite"]
    return {
        "transazioni": len(t),
        "fatturato": round(float(t.valore_ordine.sum()), 2),
        "valore_medio_ordine": round(float(t.valore_ordine.mean()), 2),
        "sessioni": int(v.sessioni.sum()),
        "conversione_su_sessioni_pct": round(float(len(t) / v.sessioni.sum() * 100), 2),
        "rimbalzo_pct": round(float(v.rimbalzi.sum() / v.sessioni.sum() * 100), 1),
    }


def ordini_incoerenti(d):
    """Ordini il cui valore differisce dalla somma delle righe di dettaglio."""
    r = d["dettagli_transazioni"]
    calcolato = (r.quantità * r.prezzo_unitario).groupby(r.id_transazione).sum().rename("da_dettagli")
    x = d["transazione"].set_index("id_transazione").join(calcolato)
    x["differenza"] = (x.valore_ordine - x.da_dettagli).round(2)
    return x.loc[x.differenza != 0, ["valore_ordine", "da_dettagli", "differenza"]]


if __name__ == "__main__":
    dati = carica()
    print(kpi(dati))
    print(ordini_incoerenti(dati).to_string())
