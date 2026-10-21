# NIST AI RMF · Research Laboratories

**Gün 2 · Salı 3 Kasım 2026 · 09:15–10:15** · Cyberbiosecurity Training Workshop · Hitit Üniversitesi, Çorum
Prof. Dr. Ahmet Altun · Sivas Cumhuriyet Üniversitesi Tıp Fakültesi

## Sürümler

| Klasör | Ne | Claude'daki canlı sunum |
|---|---|---|
| `v2-slides/` | Canlı tema **Ultraviolet**, 3B/animasyonlu öğeler, kinetik ara slayt (24 slayt) | https://claude.ai/artifact/9hNnpAwgZYxxuC97XN5o6z |
| `v1-slides/` | Skill Tracker tarzı, lacivert–kâğıt tema (23 slayt) | https://claude.ai/artifact/Nt9tJ7piGE9QXKzubohMo7 |
| `v0-html/` | İlk tek dosyalık HTML sunum motoru (tarayıcıda açılır) | — |
| `exports/` | v1'in PPTX ve PDF çıktıları | — |
| `media/` | Açılış filmleri: `opener-v1.*` (v1), `opener-v2.*` (v2) | — |

## Dosya yapısı (v1 / v2)

`project/deck.json` slayt sırası ve bölümleri, `project/slides/<id>.html` her slayt için tek bir `<section>`; konuşmacı notları `<aside>` içinde.
Filmler slaytlarda `/_blob/…` adresiyle geçer; bu adresler Claude'daki ilgili sunuma özeldir. Dosyanın kendisi `media/` klasöründedir.

## Değişiklik iş akışı

Bu klasördeki değişiklikler **`deck/02-ai-rmf`** dalında yapılır ve `main`e pull request ile alınır. Ayrıntı: kök dizindeki README.

Üreten kod: `tools/slides-builder/d2.py` (v1) ve `tools/slides-builder/build_v2.py ai` (v2).
