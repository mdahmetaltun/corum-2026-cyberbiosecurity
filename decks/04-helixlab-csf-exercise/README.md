# Hands-on · HelixLab CSF 2.0 Exercise

**Gün 2 · Salı 3 Kasım 2026 · 14:30–15:15** · Cyberbiosecurity Training Workshop · Hitit Üniversitesi, Çorum
Prof. Dr. Ahmet Altun · Sivas Cumhuriyet Üniversitesi Tıp Fakültesi

## Sürümler

| Klasör | Ne | Claude'daki canlı sunum |
|---|---|---|
| `v2-tr-slides/` | **Türkçe** v2: aynı tema, animasyonlar ve geçişler; Türkçe metin, notlar ve açılış filmi (18 slayt) | https://claude.ai/artifact/EpNwis6Fs9DPXktqP5WFVr |
| `v2-slides/` | Canlı tema **Bio Lime**, 3B/animasyonlu öğeler, kinetik ara slayt (18 slayt) | https://claude.ai/artifact/F58LzVBU8MXYxmsPvEjUfS |
| `v1-slides/` | Skill Tracker tarzı, lacivert–kâğıt tema (17 slayt) | https://claude.ai/artifact/FXLx1wQoGRiNEeioJ4Cnih |
| `v0-html/` | İlk tek dosyalık HTML sunum motoru (tarayıcıda açılır) | — |
| `exports/` | v1'in PPTX ve PDF çıktıları | — |
| `media/` | Açılış filmleri: `opener-v1.*` (v1), `opener-v2.*` (v2), `opener-v2-tr.*` (v2 Türkçe) | — |

- `v0-html/index.html` ayrıca **etkileşimli profil oluşturucu ve faz sayacını** içerir (Example + Grup 1–6 sekmeleri). Claude'daki etkileşimli araç: https://claude.ai/artifact/1LZkxgu56oodvpnb2BBqLr
## Dosya yapısı (v1 / v2)

`project/deck.json` slayt sırası ve bölümleri, `project/slides/<id>.html` her slayt için tek bir `<section>`; konuşmacı notları `<aside>` içinde.
Filmler slaytlarda `/_blob/…` adresiyle geçer; bu adresler Claude'daki ilgili sunuma özeldir. Dosyanın kendisi `media/` klasöründedir.

## Değişiklik iş akışı

Bu klasördeki değişiklikler **`deck/04-helixlab`** dalında yapılır ve `main`e pull request ile alınır. Ayrıntı: kök dizindeki README.

Üreten kod: `tools/slides-builder/d4.py` (v1) ve `tools/slides-builder/build_v2.py lab` (v2).
