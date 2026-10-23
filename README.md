# Çorum 2026 · Cyberbiosecurity Training Workshop — sunumlar

Hitit Üniversitesi × HSP · Çorum · 2–3 Kasım 2026
Prof. Dr. Ahmet Altun · Sivas Cumhuriyet Üniversitesi Tıp Fakültesi

## Sunumlar

| # | Oturum | Zaman | Klasör | Dal | v2 (canlı tema) | v1 |
|---|---|---|---|---|---|---|
| 1 | NIST CSF 2.0 · Core Functions & Profiles | Gün 1 · 13:30 | [`decks/01-csf-core-functions-profiles`](decks/01-csf-core-functions-profiles) | `deck/01-csf` | [Electric Cobalt](https://claude.ai/artifact/FK2sPqKNbQTGCFvn28VwLk) | [Slides](https://claude.ai/artifact/EQCMgWNceZwYgnAJbDuShd) |
| 2 | NIST AI RMF | Gün 2 · 09:15 | [`decks/02-ai-rmf`](decks/02-ai-rmf) | `deck/02-ai-rmf` | [Ultraviolet](https://claude.ai/artifact/9hNnpAwgZYxxuC97XN5o6z) | [Slides](https://claude.ai/artifact/Nt9tJ7piGE9QXKzubohMo7) |
| 3 | Institutional Cybersecurity Infrastructure · Case | Gün 2 · 11:30 | [`decks/03-institutional-infrastructure-case`](decks/03-institutional-infrastructure-case) | `deck/03-infrastructure` | [Signal](https://claude.ai/artifact/FgYoXjr3wPHRCEQ3YH3yzy) | [Slides](https://claude.ai/artifact/WmjXMHCXCE4G7ekL1ifjDs) |
| 4 | Hands-on · HelixLab CSF 2.0 Exercise | Gün 2 · 14:30 | [`decks/04-helixlab-csf-exercise`](decks/04-helixlab-csf-exercise) | `deck/04-helixlab` | [Bio Lime](https://claude.ai/artifact/F58LzVBU8MXYxmsPvEjUfS) | [Slides](https://claude.ai/artifact/FXLx1wQoGRiNEeioJ4Cnih) |

Ek: [etkileşimli profil oluşturucu ve sayaç](https://claude.ai/artifact/1LZkxgu56oodvpnb2BBqLr) · [renk teması panosu](https://claude.ai/artifact/6YpyPv1A4VZVjCeqYCBTkY) (`design/palette-board/`)

Her sunum klasöründe: `v0-html/` · `v1-slides/` · `v2-slides/` · `media/` (açılış filmleri) · `exports/` (PPTX + PDF).

## Dal (branch) düzeni

- **`main`** — onaylanmış sürümler. Doğrudan değişiklik yapılmaz.
- **Her sunumun kendi dalı** var: `deck/01-csf`, `deck/02-ai-rmf`, `deck/03-infrastructure`, `deck/04-helixlab`.
  O sunumla ilgili her değişiklik bu dalda ve yalnızca o sunumun klasöründe yapılır.
- Küçük ve ayrı bir iş için alt dal açılabilir: `deck/02-ai-rmf/yeni-vaka-slayti` gibi; sonra sunumun dalına ya da doğrudan `main`e PR açılır.
- Onaylı bir sürümün üzerine yazılmaz: büyük değişiklik yeni klasör olarak gelir (`v3-slides/`).

```bash
git checkout deck/02-ai-rmf
git pull
# decks/02-ai-rmf/ içinde değişiklik
git commit -am "AI RMF: Govern slaytı güncellendi"
git push            # → GitHub'da deck/02-ai-rmf → main pull request
```

Claude'a iş verirken "**deck/02-ai-rmf dalında** şunu değiştir" demeniz yeterli; değişiklik o dala gönderilir ve PR açılır.

## Araçlar (`tools/`)

| Klasör | Ne üretir |
|---|---|
| `slides-builder/` | v1 slaytları (`d1.py`–`d4.py`), v2 temalı/animasyonlu sürüm (`build_v2.py`), 3B/kinetik gömüler (`anim.py`), PPTX/PDF dışa aktarım (`export.py`) |
| `html-engine/` | v0 tek dosyalık HTML sunum motoru |
| `remotion-openers-v1/`, `remotion-openers-v2/` | Açılış filmleri (Remotion 4). `npm i && npx remotion render <Composition> out.mp4` |
| `katana-sound-design/` | v2 açılışlarının ses işaretleri; sesli MP4'ler Higgsfield'da |

Not: Slayt dosyalarındaki `/_blob/…` adresleri Claude'daki ilgili sunuma özeldir; film dosyalarının kendisi `media/` altındadır.

---

# Sivas 2026 · Siber Biyogüvenlik Çalıştayı — sunumlar

Hilton Garden Inn Sivas · 16–17 Kasım 2026 · Kapsid kimliği, Canlı palet (Sora + IBM Plex) · dal: `deck/sivas-2026`

| # | Oturum | Zaman | Klasör | Slayt |
|---|---|---|---|---|
| 5 | Açılış ve ön test | 1. Gün · 09:00 | [`decks/05-sivas-acilis-on-test`](decks/05-sivas-acilis-on-test) | 14 |
| 6 | Biyoteknolojiyi siber hırsızlıktan korumak | 1. Gün · 14:45 | [`decks/06-sivas-siber-hirsizlik`](decks/06-sivas-siber-hirsizlik) | 28 |
| 7 | Alıştırma 3 · MFA ve donanım anahtarları | 2. Gün · 13:00 | [`decks/07-sivas-mfa-alistirma`](decks/07-sivas-mfa-alistirma) | 22 |
| 8 | Yeterlik kontrolü ve kapanış | 2. Gün · 15:45 | [`decks/08-sivas-kapanis-yeterlik`](decks/08-sivas-kapanis-yeterlik) | 14 |

Araçlar:
- `tools/sivas-builder/` — `skit.py` (Canlı palet, Kapsid işareti, izinli x-icon eşlemesi, Türkçe büyük harf), `sanim.py` (yeni canlı öğeler: `capsid` 3B kapsid, `morph` parçacık tipografi morfu, `zoom` yakınlaş/uzaklaş, `scramble`, `exfil`, `otp`, `keytap`, `countdown`), `scommon.py`, `s1–s4_*.py` üreteçler, `spreview.py` (render + taşma kontrolü).
- `tools/remotion-openers-sivas/` — açılış filmleri: `FilmWorkshop`, `FilmCybertheft`, `FilmMFA`.

```bash
cd tools/sivas-builder
S2_STILL=/_blob/<still> S2_CLIP=/_blob/<clip> python3 s2_cybertheft.py <outroot>
FONTPKGS=<@fontsource + lucide-static node_modules dizini> python3 spreview.py <outroot> <outdir>
```
