# NIST CSF 2.0 · Core Functions & Profiles

**Gün 1 · Pazartesi 2 Kasım 2026 · 13:30–14:30** · Cyberbiosecurity Training Workshop · Hitit Üniversitesi, Çorum
Prof. Dr. Ahmet Altun · Sivas Cumhuriyet Üniversitesi Tıp Fakültesi

## Sürümler

| Klasör | Ne | Claude'daki canlı sunum |
|---|---|---|
| `v2-tr-slides/` | **Türkçe** v2: aynı tema, animasyonlar ve geçişler; Türkçe metin, notlar ve açılış filmi (26 slayt) | https://claude.ai/artifact/HqsXATRUwfKPmgMmKdVisR |
| `v2-slides/` | Canlı tema **Electric Cobalt**, 3B/animasyonlu öğeler, kinetik ara slayt (26 slayt) | https://claude.ai/artifact/FK2sPqKNbQTGCFvn28VwLk |
| `v1-slides/` | Skill Tracker tarzı, lacivert–kâğıt tema (25 slayt) | https://claude.ai/artifact/EQCMgWNceZwYgnAJbDuShd |
| `v0-html/` | İlk tek dosyalık HTML sunum motoru (tarayıcıda açılır) | — |
| `exports/` | v1'in PPTX ve PDF çıktıları | — |
| `media/` | Açılış filmleri: `opener-v1.*` (v1), `opener-v2.*` (v2), `opener-v2-tr.*` (v2 Türkçe) | — |

## Dosya yapısı (v1 / v2)

`project/deck.json` slayt sırası ve bölümleri, `project/slides/<id>.html` her slayt için tek bir `<section>`; konuşmacı notları `<aside>` içinde.
Filmler slaytlarda `/_blob/…` adresiyle geçer; bu adresler Claude'daki ilgili sunuma özeldir. Dosyanın kendisi `media/` klasöründedir.

## Değişiklik iş akışı

Bu klasördeki değişiklikler **`deck/01-csf`** dalında yapılır ve `main`e pull request ile alınır. Ayrıntı: kök dizindeki README.

Üreten kod: `tools/slides-builder/d1.py` (v1) ve `tools/slides-builder/build_v2.py csf` (v2).
