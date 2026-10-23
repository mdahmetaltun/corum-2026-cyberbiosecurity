"""Deck S4 · Yeterlik kontrolü, son test ve kapanış (2. Gün 15:45–16:30)."""
import sys
from scommon import *

D = Deck("Yeterlik kontrolü ve kapanış · Sivas 2026")


def dark(sid, notes, transition="fade", glow=(T2, V2)):
    def wrap(body):
        def f(i, n):
            inner = progress(i, n, True) + bg_glow(len(sid) * 7, *glow) + body(i, n) + footer(i + 1, True)
            return section(sid, inner, True, transition, notes)
        D.add(sid, f)
        return body
    return wrap


def timed(sid, eyebrow_, title, facts, minutes, notes, glow=(T3, V2), title_size=110):
    """Dark task slide: big title, fact rows, live countdown."""
    def f(i, n):
        s = progress(i, n, True) + bg_glow(len(sid) * 3, *glow)
        s += eyebrow(eyebrow_, 220)
        s += f'<h1 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:280px;width:1020px;font-family:{DISPLAY};font-size:{title_size}px;font-weight:800;letter-spacing:-3px;line-height:1.02;color:{CREAM}">{title}</h1>'
        y0 = 280 + round(title_size * 1.1 * (title.count("<br>") + 1)) + 50
        for k, (ic, t, c) in enumerate(facts):
            s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{y0 + k * 96}px;width:960px;display:flex;flex-direction:row;gap:22px;align-items:center">'
                  f'<x-icon name="{ic}" style="width:44px;height:44px;color:{c}"></x-icon><p style="flex:1;font-size:32px;line-height:1.3;color:{CREAM}">{t}</p></div>')
        s += emb("countdown", 1180, 230, 600, 600, PAL, min=minutes, cap="kalan süre", done="süre doldu")
        s += footer(i + 1, True)
        return section(sid, s, True, "fade", notes)
    D.add(sid, f)


# 1 cover
cover(D, "cover", "2. Gün · Salı 17 Kasım 2026 · 15:45–16:30",
      [("Ne öğrendik?", None), ("Yeterlik kontrolü", T2), ("ve kapanış", None)],
      "Son test, oltalama tanıma, yazılı olay senaryosu ve geri bildirim",
      emb("capsid", 1180, 190, 640, 640, PAL, rings=True, burst=True, spin=.3, t1=T1, v1=V1, v3=V3),
      """Son oturum. Kırk beş dakikanın yaklaşık yarım saati ölçme, kalanı kapanış.
Herkes katılımcı kodunu hazır tutsun: dün sabah ön testte yazdığınız kod.""", size=96)

# 2 morph recap
morph(D, "k-recap", "İki günün özeti", [("İKİ GÜN", None), ("8 OTURUM", T2), ("3 ALIŞTIRMA", P2), ("1 EKİP", AMBER)],
      """Morf ara slaytı: iki gün, sekiz oturum, üç alıştırma, bir ekip. Kısa bir nefes; sonra hep birlikte haritaya bakacağız.""", size=210)

# 3 recap grid
RC = [("1. Gün", "Siber biyogüvenliğin temelleri", "Prof. Dr. Ayşen Gargılı Keleş", V2), ("1. Gün", "Laboratuvarda bilgi güvenliği ve siber riskler", "Prof. Dr. Gökçe Merey", V2),
      ("1. Gün", "Alıştırma 1 · Varlık haritası ve riskler", "Merey · Altun", T3), ("1. Gün", "Biyoteknolojiyi siber hırsızlıktan korumak", "Prof. Dr. Ahmet Altun", V2),
      ("1. Gün", "Uluslararası iş birliğinde araştırma güvenliği", "Doç. Dr. Ahmet Şevki Taşkıran", V2), ("2. Gün", "Yaşam bilimlerinde yapay zekâ", "Prof. Dr. Gökçe Merey", P2),
      ("2. Gün", "Alıştırma 2 · Politikalar, SOP’ler, masa başı tatbikat", "Müjdeci · Altun", T3), ("2. Gün", "Alıştırma 3 · MFA ve donanım anahtarları", "Prof. Dr. Ahmet Altun", AMBER)]
items = [f'<p style="font-family:{MONO};font-size:24px;font-weight:600;color:{ {P2: PT, AMBER: AMBERT, T3: TT}.get(c, c)}">{d_}</p>' + H(t, 27, lh=1.2) + P(w, 24, MUTE)
         for d_, t, w, c in RC]
content(D, "map", "Harita", "Birlikte yürüdüğümüz yol",
        cards_row(items, top=300, n=4, height=270, row_gap=24, accents=[c for *_, c in RC], pad="26px 28px", gap=20, kind="pop")
        + src("Bu oturumdan hemen önce: Doç. Dr. Taşkıran ile deneysel laboratuvarlarda veri bütünlüğü.", top=900),
        ill="flag",
        notes="""Birlikte yürüdüğümüz yol. Sekiz kart, sekiz oturum; tıkladıkça açılıyor. Her birinde bir cümle söyleyin, en çok akılda kalan neydi diye salona sorun.
Bu oturumdan hemen önce Doç. Dr. Taşkıran veri bütünlüğünü anlattı; o da ölçmenin bir parçası olacak.""")

# 4 kinetic
kinetic(D, "k-turn", "Yeterlik kontrolü", [("ŞİMDİ", None), ("SIRA", None), ("SİZDE.", T2)],
        """Kinetik ara slayt. Ölçmeye geçiyoruz. Hatırlatma: puan sizi değil, eğitimi ölçüyor.""", size=180)

# 5 structure
PARTS = [("A", "Son test", "15 soru · ön testle aynı", "10 dk", V2), ("B", "Oltalama tanıma", "6 örnek: güvenli mi, şüpheli mi, neden?", "5 dk", P2),
         ("C", "Yazılı olay senaryosu", "İlk 15 dakika, kimi ararsınız, ne kaydedersiniz", "10 dk", AMBER), ("D", "MFA doğrulaması", "Alıştırma 3’te tamamlandı · 5 madde", "✓", T3)]
items = [f'<div style="display:flex;flex-direction:row;justify-content:space-between;align-items:center"><p style="width:72px;height:72px;border-radius:36px;background:{c};color:{"#FFFFFF" if c in (V2, T3) else INK};font-family:{DISPLAY};font-size:34px;font-weight:800;text-align:center;line-height:72px">{a}</p>'
         f'<p style="font-family:{MONO};font-size:30px;font-weight:600;color:{TEXT}">{m}</p></div>' + H(t, 32) + P(sub, 26, BODY2, lh=1.38) for a, t, sub, m, c in PARTS]
content(D, "parts", "Yeterlik kontrolü", "Dört bölüm, yaklaşık 25 dakika",
        cards_row(items, top=320, height=380, accents=[c for *_, c in PARTS], pad="32px 32px")
        + callout(740, "Her kâğıdın üstüne katılımcı kodunuzu yazın. Adınızı yazmayın; sonuçlar grup düzeyinde raporlanır.", label="Kod", icon="Fingerprint", build="rise 5 auto"),
        ill="checklist",
        notes="""Yeterlik kontrolü dört bölüm. A, son test: ön testle aynı on beş soru, on dakika. B, oltalama tanıma: altı örnek, beş dakika. C, yazılı olay senaryosu: on dakika. D, MFA doğrulaması: Alıştırma 3'te kolaylaştırıcılar tarafından işaretlendi.
Her kâğıda katılımcı kodu; isim yok.""")

# 6 post-test
timed("posttest", "Bölüm A · Son test", "Son test", [("ListChecks", "15 çoktan seçmeli soru, ön testle aynı", T2), ("Fingerprint", "Kâğıdın üstüne katılımcı kodunuz", AMBER),
                                                   ("CircleHelp", "Emin değilseniz “Bilmiyorum” seçeneği", P1)], 10,
      """Bölüm A. Sayaç slayt açıldığında başlar; kâğıtları dağıttıktan sonra bu slayda geçin. On dakika.
Ön testteki gibi: emin değilseniz "bilmiyorum" işaretleyin. Ön ve son test arasındaki farkı kapanışta değil, raporda paylaşacağız.""")

# 7 phishing recognition
timed("phish", "Bölüm B · Oltalama tanıma", "Altı mesaj,<br>altı karar", [("Mail", "Her mesaj için: güvenli mi, şüpheli mi?", T2), ("Search", "Şüpheliyse, sizi uyaran işareti yazın", AMBER),
                                                                       ("Unlink", "Kâğıttaki bağlantılar gerçek değildir", P1)], 5,
      """Bölüm B. Altı basılı mesaj; bazıları gerçek, bazıları oltalama. Her biri için güvenli ya da şüpheli işaretleyin; şüpheliyse uyaran işareti yazın: gönderen adresi, aciliyet, beklenmeyen ek, alan adı.
Beş dakika. Kâğıttaki bağlantılar tıklanabilir değil; hepsi örnek.""", glow=(P2, V2), title_size=96)


# 8 incident scenario
@dark("scenario", """Bölüm C, yazılı olay senaryosu. Senaryoyu yüksek sesle okuyun, sonra sayaç başlasın; kâğıtta aynı metin ve dört soru var.
Bu senaryo Alıştırma 2'deki masa başı tatbikatla aynı mantıkta. Değerlendirme: ilk adımlar, iletişim sırası, kayıt ve yasal yükümlülük. Her biri 0–2 puan.""", glow=(AMBER, P2))
def _(i, n):
    s = eyebrow("Bölüm C · Yazılı olay senaryosu · 10 dakika", 200)
    s += (f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:260px;width:1020px;display:flex;flex-direction:column;gap:18px;padding:36px 40px;background:{INK2};border-radius:22px;border-left:8px solid {AMBER}">'
          f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{AMBER}">SALI · 08:40</p>'
          + P("Dizileme cihazına bağlı bilgisayarda bir dış müşterinin ham veri klasörü boş. Masaüstünde “OKUBENI.txt” adlı bir fidye notu var. Ağ paylaşımındaki iki klasörde dosya uzantıları değişmiş.", 30, CREAM, lh=1.45)
          + "</div>")
    qs = ["İlk 15 dakikada hangi üç şeyi yaparsınız?", "Kimi, hangi sırayla ararsınız?", "Hangi bilgileri kayda geçirirsiniz?", "Müşteri ve KVKK açısından ne gerekir?"]
    for k, q in enumerate(qs):
        s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{600 + k * 78}px;width:1020px;display:flex;flex-direction:row;gap:20px;align-items:center">'
              f'<p style="width:52px;height:52px;border-radius:26px;background:{AMBER};color:{INK};font-family:{DISPLAY};font-size:26px;font-weight:800;text-align:center;line-height:52px">{k + 1}</p>'
              f'<p style="flex:1;font-size:30px;color:{CREAM}">{q}</p></div>')
    s += emb("countdown", 1240, 260, 540, 540, PAL, min=10, cap="kalan süre", done="süre doldu")
    s += src("Senaryo kurgusaldır; eğitim amaçlıdır.", top=930, dark=True)
    return s


# 9 how we score
SCO = [("A", "Son test", "Doğru sayısı; ön testle fark katılımcı koduyla eşleşir.", V2), ("B", "Oltalama", "6 mesajda doğru karar ve gerekçe.", P2),
       ("C", "Senaryo", "4 ölçüt × 0–2 puan: ilk adımlar, iletişim, kayıt, yükümlülük.", AMBER), ("D", "MFA", "Alıştırma 3 kontrol listesindeki 5 madde.", T3)]
body = ""
for k, (a, t, d_, c) in enumerate(SCO):
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{300 + k * 120}px;width:1300px;height:104px;display:flex;flex-direction:row;gap:26px;align-items:center;padding:0px 30px;background:{WHITE};border-radius:18px;border-left:8px solid {c};box-shadow:0 8px 24px rgba(29,37,84,0.07)">'
             f'<p style="width:48px;font-family:{DISPLAY};font-size:40px;font-weight:800;color:{ {P2: PT, AMBER: AMBERT, T3: TT}.get(c, c)}">{a}</p><p style="width:200px;font-size:30px;font-weight:700;color:{TEXT}">{t}</p><p style="flex:1;font-size:27px;line-height:1.35;color:{BODY2}">{d_}</p></div>')
body += callout(800, "Bireysel sonucunuzu katılımcı kodunuzla isteyebilirsiniz. HSP’ye yalnız grup düzeyindeki sonuçlar raporlanır.", label="Şeffaflık", icon="Eye", build="rise 5 auto")
content(D, "scoring", "Değerlendirme", "Nasıl puanlıyoruz?", body, ill="gauge",
        notes="""Puanlama şeffaf olsun. Son test: doğru sayısı ve ön testle fark. Oltalama: altı mesajda doğru karar ve gerekçe. Senaryo: dört ölçüt, her biri sıfır ile iki puan. MFA: beş maddelik kontrol listesi.
Bireysel sonucunuzu katılımcı kodunuzla isteyebilirsiniz; HSP'ye yalnız grup sonuçları gider.""")

# 10 feedback form
timed("feedback", "Geri bildirim", "Bizi siz<br>değerlendirin", [("Star", "Her oturum için 1–5 puan", AMBER), ("MessageSquareText", "En yararlı ve en eksik bulduğunuz konu", T2),
                                                                 ("Lightbulb", "Laboratuvarınız için bir sonraki ihtiyaç", P1)], 5,
      """Geri bildirim formu, beş dakika. Her oturum için puan, en yararlı ve en eksik konu, ve laboratuvarınız için bir sonraki ihtiyaç.
Bu form HSP'ye gidecek final raporun bir parçası ve gelecek eğitimleri şekillendirecek. Lütfen açık yazın.""", glow=(V2, AMBER), title_size=96)

# 11 institutional next steps
NS = [("BookOpen", "Eğitim el kitabı (TR/EN)", "Yeni personelin oryantasyonu için; çevrim içi portalda.", V2),
      ("FileWarning", "Olay müdahale protokolü", "Taslak, bu çalıştaydaki tatbikatlarla güncellenecek.", P2),
      ("CalendarSync", "Yıllık tazeleme", "Bu programın yapısı üzerine yılda bir eğitim.", T3),
      ("Radar", "Yıllık gözden geçirme", "Mevcut ve hedef güvenlik profili her yıl yeniden puanlanır.", AMBER)]
items = [icon(ic, 48, {P2: PT, AMBER: AMBERT, T3: TT}.get(c, c)) + H(t, 30) + P(d_, 26, BODY2, lh=1.38) for ic, t, d_, c in NS]
content(D, "next", "Kurumsal sonraki adımlar", "Çalıştay bitiyor, süreç devam ediyor",
        cards_row(items, top=320, height=380, accents=[c for *_, c in NS], pad="32px 32px")
        + callout(740, "El kitabı ve portal 4 Aralık’ta hazır olacak; katılımcı listesine bağlantı gönderilecek.", label="Takvim", icon="CalendarDays", build="rise 5 auto"),
        ill="timeline",
        notes="""Kurumsal sonraki adımlar. Türkçe ve İngilizce eğitim el kitabı ve çevrim içi portal; taslak olay müdahale protokolünün bu çalıştaydaki tatbikatlarla güncellenmesi; yıllık tazeleme eğitimi; ve güvenlik profilinin yılda bir yeniden puanlanması.
El kitabı ve portal 4 Aralık'ta hazır; bağlantıyı katılımcılara göndereceğiz.""")

# 12 personal 30 days
WK = [("1. hafta", "Kurumsal ve kişisel hesaplarınızda MFA; mümkünse geçiş anahtarı.", V2),
      ("2. hafta", "Laboratuvarınızdaki cihaz bilgisayarlarının listesi ve sahipleri.", T3),
      ("3. hafta", "En kritik veriniz için çevrimdışı yedek; bir dosyayı geri yükleyerek deneyin.", P2),
      ("4. hafta", "Ekibinize 15 dakikalık bir özet: oltalama, MFA, kimi arayacağız.", AMBER)]
body = (f'<svg aria-label="" width="1664" height="16" viewBox="0 0 1664 16" style="position:absolute;left:128px;top:346px;width:1664px;height:16px"><style>.l{{stroke-dasharray:1664;stroke-dashoffset:1664;animation:l 3s cubic-bezier(.6,0,.2,1) forwards}}@keyframes l{{to{{stroke-dashoffset:0}}}}{RM}</style>'
        f'<line x1="0" y1="8" x2="1664" y2="8" stroke="{LINE}" stroke-width="4"/><line class="l" x1="0" y1="8" x2="1664" y2="8" stroke="{T2}" stroke-width="4"/></svg>')
for k, (w, t, c) in enumerate(WK):
    x = 128 + k * 424
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:320px;width:392px;display:flex;flex-direction:column;gap:16px">'
             f'<p style="width:68px;height:68px;border-radius:34px;background:{c};border:6px solid {PAPER}"></p>'
             f'<p style="font-family:{DISPLAY};font-size:36px;font-weight:800;color:{ {P2: PT, AMBER: AMBERT, T3: TT}.get(c, c)}">{w}</p>' + P(t, 28, TEXT, lh=1.4) + "</div>")
body += callout(740, "Dört haftanın sonunda bu slaydın fotoğrafına bakın: kaç kutu işaretli?", label="Sizin için", icon="Camera", build="rise 5 auto")
content(D, "30days", "Kişisel plan", "Önümüzdeki 30 gün", body, ill="flag",
        notes="""Kişisel plan, dört hafta. Birinci hafta MFA her yerde. İkinci hafta cihaz listesi. Üçüncü hafta yedek ve bir geri yükleme denemesi. Dördüncü hafta ekibinize on beş dakikalık özet.
Bu slaydın fotoğrafını çekmelerini isteyin.""")


# 13 thanks to everyone
@dark("credits", """Teşekkür. Health Security Partners'a hibe ve rehberlik için; University of Washington'a program ortaklığı için; Rektörlüğümüze ev sahipliği ve idari destek için.
Konuşmacılarımıza ve en çok da iki gün boyunca kendi laboratuvarını masaya koyan katılımcılarımıza.
Sertifikalar, son test ve geri bildirim formu teslim edildikten sonra dağıtılacak.""", glow=(V2, T2))
def _(i, n):
    s = eyebrow("Teşekkürler", 210)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:270px;width:1200px;font-family:{DISPLAY};font-size:76px;font-weight:800;letter-spacing:-2px;line-height:1.06;color:{CREAM}">Bu iki gün, <span style="color:{T2}">sizin sayenizde</span> çalıştı.</h2>'
    rows = [("Health Security Partners · University of Washington", "Hibe, program ortaklığı ve rehberlik", T2),
            ("Sivas Cumhuriyet Üniversitesi Rektörlüğü", "Ev sahipliği ve idari destek", AMBER),
            ("Konuşmacılar", "Gargılı Keleş · Merey · Müjdeci · Taşkıran", P1),
            ("Katılımcılar", "Kendi laboratuvarını masaya koyan herkes", V1)]
    for k, (a, b, c) in enumerate(rows):
        s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{500 + k * 100}px;width:1180px;display:flex;flex-direction:row;gap:22px;align-items:center">'
              f'<div style="width:8px;height:72px;border-radius:4px;background:{c}"></div><div style="flex:1;display:flex;flex-direction:column;gap:2px">'
              f'<p style="font-size:32px;font-weight:600;color:{CREAM}">{a}</p><p style="font-size:26px;color:{SKY}">{b}</p></div></div>')
    s += kapsid_svg(360, 1420, 330, animate=True)
    return s


# 14 closing
thanks(D, "thanks", "Sertifikalar son test ve geri bildirim formu teslim edildikten sonra dağıtılacak. Toplu fotoğraf için lütfen salonda kalın.",
       """Kapanış. Soru-cevap için birkaç dakika. Ardından sertifika dağıtımı ve toplu fotoğraf.""", title="Görüşmek üzere.", tsize=112)

SECTIONS = {"s1": {"description": "Özet", "start": "cover"}, "s2": {"description": "Yeterlik kontrolü", "start": "k-turn"},
            "s3": {"description": "Kapanış", "start": "feedback"}}

if __name__ == "__main__":
    write_deck(sys.argv[1], "Yeterlik kontrolü ve kapanış · Sivas 2026", SECTIONS, D.render())
    print("ok", len(D.slides))
