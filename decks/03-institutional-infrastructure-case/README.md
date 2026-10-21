# Institutional Cybersecurity Infrastructure · Case Study

**Gün 2 · Salı 3 Kasım 2026 · 11:30–12:30** · Cyberbiosecurity Training Workshop · Hitit Üniversitesi, Çorum
Prof. Dr. Ahmet Altun · Sivas Cumhuriyet Üniversitesi Tıp Fakültesi

## Sürümler

| Klasör | Ne | Claude'daki canlı sunum |
|---|---|---|
| `v2-slides/` | Canlı tema **Signal**, 3B/animasyonlu öğeler, kinetik ara slayt (27 slayt) | https://claude.ai/artifact/FgYoXjr3wPHRCEQ3YH3yzy |
| `v1-slides/` | Skill Tracker tarzı, lacivert–kâğıt tema (26 slayt) | https://claude.ai/artifact/WmjXMHCXCE4G7ekL1ifjDs |
| `v0-html/` | İlk tek dosyalık HTML sunum motoru (tarayıcıda açılır) | — |
| `exports/` | v1'in PPTX ve PDF çıktıları | — |
| `media/` | Açılış filmleri: `opener-v1.*` (v1), `opener-v2.*` (v2) | — |

## Dosya yapısı (v1 / v2)

`project/deck.json` slayt sırası ve bölümleri, `project/slides/<id>.html` her slayt için tek bir `<section>`; konuşmacı notları `<aside>` içinde.
Filmler slaytlarda `/_blob/…` adresiyle geçer; bu adresler Claude'daki ilgili sunuma özeldir. Dosyanın kendisi `media/` klasöründedir.

## Değişiklik iş akışı

Bu klasördeki değişiklikler **`deck/03-infrastructure`** dalında yapılır ve `main`e pull request ile alınır. Ayrıntı: kök dizindeki README.

Üreten kod: `tools/slides-builder/d3.py` (v1) ve `tools/slides-builder/build_v2.py kase` (v2).
