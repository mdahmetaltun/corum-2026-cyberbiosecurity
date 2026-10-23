"""Deck S1 · Açılış ve ön test (1. Gün 09:00–09:30)."""
import os, sys
from scommon import *

VID = (os.environ.get("S1_STILL", "/_blob/still"), os.environ.get("S1_CLIP", "/_blob/clip"))
D = Deck("Açılış ve ön test · Sivas 2026")

# 1 cover
cover(D, "cover", "1. Gün · Pazartesi 16 Kasım 2026 · 09:00–09:30",
      [("Hoş geldiniz.", None), ("İki gün, bir ekip.", T2)],
      "Siber Biyogüvenlik Çalıştayı · Açılış, program ve ön test",
      emb("capsid", 1180, 190, 640, 640, PAL, rings=True, intro=True, spin=.35, t1=T1, v1=V1, v3=V3),
      """Günaydın, hoş geldiniz. Kayıt sürerken bu slayt açık kalsın; sağdaki kapsid kendi kendine döner.
Açılışta üç şey yapacağız: çalıştayın neden var olduğunu konuşacağız, iki günün programına bakacağız ve on dakikalık bir ön test dolduracağız.""", size=110)

# 2 film
video(D, "film", VID[0], VID[1], "Açılış filmi: Kapsid logosu parçalarından birleşir; Siber Biyogüvenlik yazısı ve çalıştay tarihleri gelir",
      """Açılış filmi, yaklaşık 12 saniye. Kapsid logosu parçalarından birleşiyor, sonra "laboratuvarınız artık bir ağ" cümlesi geliyor. Bittiğinde ilerleyin.""")

# 3 morph: the field
morph(D, "k-field", "İki günün konusu", [("SİBER", T2), ("BİYO", P2), ("GÜVENLİK", None), ("SİBER BİYOGÜVENLİK", AMBER)],
      """Morf ara slaytı. Harfler parçacıklara ayrılıp birleşiyor: siber, biyo, güvenlik ve sonunda üçü birlikte.
Tanım: siber biyogüvenlik, yaşam bilimlerinin dijital ve fiziksel sistemlerinin kesiştiği yerde ortaya çıkan riskleri anlamak ve azaltmakla ilgilenir. Murch ve arkadaşları 2018'de bunu yeni bir disiplin olarak tanımladı.""",
      sub="Yaşam bilimlerinin biyolojik, dijital ve fiziksel sistemlerinin kesiştiği yerdeki riskleri anlamak ve azaltmak (Murch ve ark., 2018).", size=200, per=3.4)


# 4 zoom out
def zoom_out(i, n):
    s = progress(i, n, True) + bg_glow(4, V3, T2)
    s += head("Ölçek", "Bir dosyadan bir ağa: uzaklaştırın", True)
    s += emb("zoom", 128, 300, 1664, 600, PAL, labels=["BÖLGE AĞI", "KAMPÜS", "LABORATUVAR", "CİHAZ BİLGİSAYARI", "HAM VERİ"], per=3.4, rev=True, bg=INK0)
    s += footer(i + 1, True)
    return section("scale", s, True, "fade", """Bu kez ters yönde gidiyoruz: bir dizileme dosyasından başlayıp cihaz bilgisayarına, laboratuvara, kampüse ve bölge ağına uzaklaşıyoruz.
Mesaj basit: tezgâhtaki bir dosya, ağdaki bir düğümdür. Ona ulaşan yol, ağın her yerinden geçebilir.
Bu öğleden sonra Prof. Merey ile laboratuvarın varlık haritasını tam olarak bu ölçeklerde çıkaracağız.""")


D.add("scale", zoom_out)

# 5 why now
items = [
    icon("Database", 48, V2) + H("Veri büyüdü", 32) + P("Yeni nesil dizileme, dijital görüntüleme ve otomatik cihazlar her gün gigabaytlarca ham veri üretiyor.", 26, BODY2, lh=1.38),
    icon("Cable", 48, TT) + H("Bağlantı arttı", 32) + P("Bulut depolama, uzaktan servis erişimi ve yapay zekâ araçları laboratuvarı dış dünyaya bağladı.", 26, BODY2, lh=1.38),
    icon("Scale", 48, PT) + H("Sorumluluk netleşti", 32) + P("7545 sayılı Kanun, KVKK ve müşteri sözleşmeleri, korumayı bir tercih olmaktan çıkardı.", 26, BODY2, lh=1.38),
]
content(D, "whynow", "Neden şimdi?", "Laboratuvar değişti, riskler de",
        cards_row(items, top=320, height=390, pad="34px 36px")
        + callout(750, "Biyogüvenlik kabinini kimse açık bırakmaz; bilgisayarı ise çoğu zaman açık bırakırız.", label="Benzetme", icon="FlaskConical", build="rise 4 auto"),
        ill="molecule",
        notes="""Neden şimdi? Üç değişim. Veri büyüdü: dizileme ve dijital cihazlar her gün büyük ham veri üretiyor. Bağlantı arttı: bulut, uzaktan servis, yapay zekâ araçları. Sorumluluk netleşti: 7545 sayılı Siber Güvenlik Kanunu, KVKK ve müşteri sözleşmeleri.
Benzetmeyle bitirin: biyogüvenlik kabinini kimse açık bırakmaz. Bilgisayarı ise bırakıyoruz. Bu iki gün, o alışkanlığı değiştirmek için.""")

# 6 learning objectives
OB = [("01", "Siber biyogüvenliği tanımlar, laboratuvarların neden hedef olduğunu açıklarsınız.", V2),
      ("02", "Kendi laboratuvarınızın varlıklarını ve risklerini haritalarsınız.", T3),
      ("03", "Oltalama ve sosyal mühendislik girişimlerini tanırsınız.", P2),
      ("04", "Laboratuvarınız için bir politika ve SOP taslağını değerlendirirsiniz.", AMBER),
      ("05", "Bir olayı taslak prosedüre göre bildirir, kayda geçirirsiniz.", V1),
      ("06", "Yapay zekâ araçlarını sorumlu kullanır, veri bütünlüğünü korursunuz.", T2)]
items = [f'<p style="font-family:{DISPLAY};font-size:46px;font-weight:800;letter-spacing:-1px;color:{ {P2: PT, AMBER: AMBERT, T2: TT}.get(c, c)}">{num}</p>' + P(t, 27, TEXT, lh=1.36) for num, t, c in OB]
content(D, "goals", "Öğrenme hedefleri", "İki günün sonunda yapabilecekleriniz",
        cards_row(items, top=300, n=3, height=280, row_gap=24, accents=[c for *_, c in OB], pad="28px 32px")
        + src("Son gün yeterlik kontrolü bu altı hedefi ölçer: son test, oltalama tanıma ve yazılı olay senaryosu.", top=900),
        ill="target",
        notes="""Altı öğrenme hedefi. Hepsi bir eylem fiiliyle bitiyor, çünkü yarın öğleden sonra bunları gerçekten ölçeceğiz.
Bir, iki ve üç bugünün konuları; dört ve beş yarın sabahki politikalar, SOP'ler ve masa başı tatbikat; altı, yapay zekâ ve veri bütünlüğü oturumları.
Kapanışta son test, oltalama tanıma ve yazılı bir olay senaryosu yapacağız.""")

# 7–8 programme
DAY1 = [("09:00–09:30", "AÇILIŞ", "Kayıt, hoş geldiniz ve ön test", "Prof. Dr. Ahmet Altun", V2),
        ("09:30–10:45", "DERS", "Siber biyogüvenliğin temelleri: dijital laboratuvarda biyogüvenlik ve biyoemniyet", "Prof. Dr. Ayşen Gargılı Keleş", V2),
        ("10:45–11:00", None, "Kahve arası", "", None),
        ("11:00–12:00", "DERS", "Biyoteknoloji ve araştırma laboratuvarlarında bilgi güvenliği ve siber riskler", "Prof. Dr. Gökçe Merey", V2),
        ("12:00–13:00", None, "Öğle arası", "", None),
        ("13:00–14:30", "ALIŞTIRMA 1", "Laboratuvar varlık haritalama ve risk belirleme", "Prof. Dr. Gökçe Merey · Prof. Dr. Ahmet Altun", T3),
        ("14:30–14:45", None, "Kahve arası", "", None),
        ("14:45–15:30", "DERS", "Üniversitelerde biyoteknolojiyi siber hırsızlıktan korumak", "Prof. Dr. Ahmet Altun", V2),
        ("15:30–16:30", "DERS", "Uluslararası iş birliğinde araştırma güvenliği: İngiltere pratiği", "Doç. Dr. Ahmet Şevki Taşkıran", V2)]
DAY2 = [("09:00–10:15", "DERS", "Yaşam bilimlerinde yapay zekâ: fırsatlar, riskler ve sorumlu kullanım", "Prof. Dr. Gökçe Merey", V2),
        ("10:15–10:30", None, "Kahve arası", "", None),
        ("10:30–12:00", "ALIŞTIRMA 2", "Laboratuvar politikaları ve SOP’ler · olay müdahalesi masa başı tatbikatı", "Prof. Dr. Gökçe Merey · Prof. Dr. Ahmet Altun", T3),
        ("12:00–13:00", None, "Öğle arası", "", None),
        ("13:00–14:00", "DERS", "Deneysel laboratuvarlarda veri bütünlüğü: ham veriden yayına", "Doç. Dr. Ahmet Şevki Taşkıran", V2),
        ("14:00–14:15", None, "Kahve arası", "", None),
        ("14:15–15:00", "DEĞERLENDİRME", "Yeterlik kontrolü, son test ve kapanış", "Prof. Dr. Ahmet Altun", P2)]


def programme(rows, top=300):
    out, y = "", top
    for k, (tm, kind, title, who, c) in enumerate(rows):
        if kind is None:
            out += (f'<div data-build-in="fade {k + 1} auto" style="position:absolute;left:128px;top:{y}px;width:1664px;height:44px;display:flex;flex-direction:row;gap:28px;align-items:center;padding:0px 28px">'
                    f'<p style="width:200px;font-family:{MONO};font-size:24px;color:{MUTE}">{tm}</p><p style="font-size:24px;color:{MUTE}">{title}</p></div>')
            y += 50
        else:
            tc = {P2: PT, AMBER: AMBERT, T3: TT}.get(c, c)
            bgc = {V2: VTINT, T3: TTINT, AMBER: ATINT, P2: PTINT}[c]
            out += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{y}px;width:1664px;height:84px;display:flex;flex-direction:row;gap:28px;align-items:center;padding:0px 28px;background:{WHITE};border-radius:16px;border-left:8px solid {c};box-shadow:0 8px 24px rgba(29,37,84,0.07)">'
                    f'<p style="width:200px;font-family:{MONO};font-size:26px;font-weight:600;color:{TEXT}">{tm}</p>'
                    f'<p style="width:220px;font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:1px;color:{tc};background:{bgc};padding:4px 12px;border-radius:8px;text-align:center">{kind}</p>'
                    f'<div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:26px;font-weight:600;line-height:1.25;color:{TEXT}">{title}</p><p style="font-size:24px;color:{MUTE}">{who}</p></div></div>')
            y += 92
    return out


content(D, "day1", "Program · Pazartesi 16 Kasım", "1. Gün: temeller ve laboratuvar riskleri", programme(DAY1, 272),
        notes="""Birinci gün. Sabah iki ders: Prof. Gargılı Keleş ile temeller, Prof. Merey ile laboratuvarlarda bilgi güvenliği. Öğleden sonra ilk alıştırma: kendi laboratuvarınızın varlık haritası.
Günü iki dersle kapatıyoruz: benim siber hırsızlık oturumum ve Doç. Dr. Taşkıran'ın uluslararası iş birliğinde araştırma güvenliği oturumu.""", title_id="prog-title")
content(D, "day2", "Program · Salı 17 Kasım", "2. Gün: yapay zekâ, politika ve veri bütünlüğü", programme(DAY2, 272),
        transition="magic",
        notes="""İkinci gün daha kısa; 15:00'te bitiyor. Sabah Prof. Merey ile yapay zekâ; ardından yine Prof. Merey ile politikalar, SOP'ler ve bir olay müdahalesi masa başı tatbikatı. Öğleden sonra Doç. Dr. Taşkıran ile araştırma verisi bütünlüğü.
14:15'teki son oturum yeterlik kontrolü ve kapanış. Sertifika için iki günün tamamına katılım ve son testi tamamlamak gerekiyor.""", title_id="prog-title")

# 9 speakers
SP = [("AA", "Prof. Dr. Ahmet Altun", "Sivas Cumhuriyet Üniversitesi · proje yürütücüsü", "Açılış · Siber hırsızlık · Kapanış", V2),
      ("AG", "Prof. Dr. Ayşen Gargılı Keleş", "Marmara Üniversitesi · Biyogüvenlik ve Biyoemniyet Derneği kurucu başkanı", "Siber biyogüvenliğin temelleri", T3),
      ("GM", "Prof. Dr. Gökçe Merey", "Çalıştay konuşmacısı · dört oturum", "Laboratuvarda siber riskler · Alıştırma 1 · Yapay zekâ · Politikalar ve SOP’ler", P2),
      ("AT", "Doç. Dr. Ahmet Şevki Taşkıran", "Sivas Cumhuriyet Üniversitesi", "Araştırma güvenliği · Veri bütünlüğü", V1)]
items = []
for ini, nm, af, ses, c in SP:
    items.append(f'<p style="width:96px;height:96px;border-radius:48px;background:{c};color:{"#FFFFFF" if c in (V2, V1, T3) else INK};font-family:{DISPLAY};font-size:36px;font-weight:800;text-align:center;line-height:96px">{ini}</p>'
                 + H(nm, 28) + P(af, 24, MUTE, lh=1.32) + f'<div style="height:2px;background:{LINE}"></div>' + P(ses, 24, TEXT, lh=1.32, weight=500))
content(D, "speakers", "Konuşmacılar", "Dört konuşmacı, iki gün",
        cards_row(items, top=300, height=560, pad="30px 26px", gap=20),
        notes="""Konuşmacılarımız. Prof. Ayşen Gargılı Keleş, Marmara Üniversitesi; Türkiye Biyogüvenlik ve Biyoemniyet Derneği'nin kurucu başkanı. Prof. Gökçe Merey dört oturumda bizimle: laboratuvarlarda siber riskler, varlık haritalama alıştırması, yapay zekâ ve politikalar ile SOP'ler. Doç. Dr. Ahmet Şevki Taşkıran, üniversitemizden.
Her konuşmacıya kısa bir alkış isteyin.""")

# 10 how we work
items = [
    icon("Clock", 48, V2) + H("Saatler", 30) + P("Bugün 09:00–16:30, yarın 09:00–15:00. Aralar programdaki saatlerde.", 26, BODY2, lh=1.38),
    icon("Fingerprint", 48, TT) + H("Katılımcı kodu", 30) + P("Testlerde adınız yerine kendi oluşturduğunuz kod yer alır. Ön ve son test böyle eşleşir.", 26, BODY2, lh=1.38),
    icon("MessageCircleQuestion", 48, PT) + H("Chatham House kuralı", 30) + P("Burada anlatılan kullanılabilir; kimin anlattığı dışarıya taşınmaz.", 26, BODY2, lh=1.38),
    icon("Award", 48, AMBERT) + H("Sertifika", 30) + P("İki günün tamamına katılım, son test ve geri bildirim formu.", 26, BODY2, lh=1.38),
]
content(D, "rules", "Çalışma düzeni", "Nasıl çalışacağız?",
        cards_row(items, top=320, height=420, pad="32px 32px")
        + callout(780, "Kendi laboratuvarınızdan örnek verin; ama parola, IP adresi ya da cihaz seri numarası paylaşmayın.", label="Tek kural", icon="ShieldAlert", build="rise 5 auto"),
        ill="checklist",
        notes="""Dört pratik bilgi. Saatler: bugün 16:30'a, yarın 15:00'e kadar. Katılımcı kodu: testlerde isim yok, birazdan nasıl oluşturacağınızı göstereceğim. Chatham House kuralı: söylenenler kullanılabilir, kim söylediği paylaşılmaz; bu, kendi laboratuvarınızdaki sorunları rahatça konuşabilmeniz için.
Sertifika: iki günün tamamına katılım, son test ve geri bildirim formu.
Tek kural: örnek verin ama parola, IP adresi ya da seri numarası paylaşmayın.""")


# 11 thanks to supporters
def support(i, n):
    s = progress(i, n, True) + bg_glow(11, V2, AMBER)
    s += eyebrow("Destek", 230)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:290px;width:1200px;font-family:{DISPLAY};font-size:72px;font-weight:800;letter-spacing:-2px;line-height:1.08;color:{CREAM}">Bu çalıştay, bir öğrenme yolculuğunun <span style="color:{AMBER}">devamı.</span></h2>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:480px;width:1150px;font-size:31px;line-height:1.45;color:{SKY}">Fikir, Eylül 2024’te Health Security Partners’ın “Securing Biotechnology from Cybertheft at Universities” çalıştayında doğdu. Bugün o öğrenmeyi kendi kurumumuzda kalıcı uygulamaya dönüştürüyoruz.</p>'
    org = [("Health Security Partners", "Hedefli Uygulama Hibesi", T2), ("University of Washington", "Program ortağı", V1), ("Sivas Cumhuriyet Üniversitesi", "Rektörlük ve ev sahipliği", AMBER)]
    for k, (a, b, c) in enumerate(org):
        s += (f'<div data-build-in="rise {k + 3} auto" style="position:absolute;left:{128 + k * 564}px;top:690px;width:536px;height:160px;display:flex;flex-direction:column;gap:8px;justify-content:center;padding:0px 34px;background:{INK2};border-radius:20px;border-top:6px solid {c}">'
              + H(a, 32, CREAM) + P(b, 26, SKY) + "</div>")
    s += kapsid_svg(220, 1560, 230, animate=True)
    s += footer(i + 1, True)
    return section("support", s, True, "fade", """Teşekkür. Bu çalıştay Eylül 2024'te HSP'nin "Securing Biotechnology from Cybertheft at Universities" çalıştayında başlayan bir öğrenmenin devamı.
Health Security Partners'a hibe desteği için, University of Washington'a program ortaklığı için, Rektörlüğümüze ev sahipliği ve idari destek için teşekkür ederim.""")


D.add("support", support)

# 12 participant code
CODE = [("AY", "Annenizin adının ilk iki harfi", V2), ("07", "Doğduğunuz gün (iki hane)", T3), ("42", "Telefonunuzun son iki hanesi", P2)]
body = ""
for k, (v, t, c) in enumerate(CODE):
    x = 128 + k * 420
    body += (f'<div data-build-in="pop {k + 1} auto" style="position:absolute;left:{x}px;top:330px;width:360px;display:flex;flex-direction:column;gap:16px;align-items:center">'
             f'<p style="width:300px;height:180px;border-radius:24px;background:{WHITE};border:4px solid {c};font-family:{MONO};font-size:110px;font-weight:600;color:{ {P2: PT, T3: TT}.get(c, c)};text-align:center;line-height:172px">{v}</p>'
             f'<p style="width:360px;font-size:26px;line-height:1.35;color:{BODY2};text-align:center">{t}</p></div>')
    if k < 2:
        body += f'<p style="position:absolute;left:{x + 368}px;top:380px;width:44px;font-family:{MONO};font-size:80px;color:{MUTE};text-align:center">-</p>'
body += (f'<div data-build-in="rise 4 auto" style="position:absolute;left:1420px;top:330px;width:372px;display:flex;flex-direction:column;gap:14px;padding:32px 34px;background:{INK};border-radius:22px">'
         f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{T2}">ÖRNEK KOD</p>'
         f'<p style="font-family:{MONO};font-size:54px;font-weight:600;white-space:nowrap;color:{CREAM}">AY-07-42</p>' + P("Son testte aynı kodu yazacaksınız.", 26, SKY) + "</div>")
body += callout(720, "Kod adınızı içermez; yalnız sizin bildiğiniz üç parçadan oluşur. Sonuçlar grup düzeyinde raporlanır.", label="Gizlilik", icon="Lock", build="rise 5 auto")
content(D, "code", "Ön test · 1. adım", "Katılımcı kodunuzu oluşturun", body, ill=None,
        notes="""Katılımcı kodu. Üç parça: annenizin adının ilk iki harfi, doğduğunuz gün ve telefonunuzun son iki hanesi. Örnek: AY-07-42.
Bu kod ön test ile son testi eşleştirmemizi sağlar; adınız hiçbir yerde geçmez. Sonuçlar HSP'ye grup düzeyinde raporlanacak.
Herkes kodunu kâğıdın ya da formun en üstüne yazsın.""")


# 13 pre-test with live countdown
def pretest(i, n):
    s = progress(i, n, True) + bg_glow(13, T3, V2)
    s += eyebrow("Ön test · 2. adım", 220)
    s += f'<h1 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:280px;width:1000px;font-family:{DISPLAY};font-size:130px;font-weight:800;letter-spacing:-4px;line-height:1;color:{CREAM}">Ön test</h1>'
    facts = [("ListChecks", "15 çoktan seçmeli soru", T2), ("Timer", "10 dakika", AMBER), ("UserRoundX", "İsim yok: yalnız katılımcı kodu", P1), ("Smile", "Puan sizi değil, eğitimi ölçer", V1)]
    for k, (ic, t, c) in enumerate(facts):
        s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{460 + k * 104}px;width:900px;display:flex;flex-direction:row;gap:22px;align-items:center">'
              f'<x-icon name="{ic}" style="width:44px;height:44px;color:{c}"></x-icon><p style="font-size:34px;color:{CREAM}">{t}</p></div>')
    s += emb("countdown", 1180, 230, 600, 600, PAL, min=10, cap="kalan süre", done="süre doldu")
    s += footer(i + 1, True)
    return section("pretest", s, True, "fade", """Ön test. 15 soru, 10 dakika. Sağdaki sayaç slayt açıldığı anda başlar; bu slayda testi dağıttıktan sonra geçin.
Vurgulayın: bu bir sınav değil. Puan sizi değil, eğitimi ölçüyor. Aynı soruları yarın kapanışta tekrar soracağız ve farkı göreceğiz.
Bilmediğiniz soruda tahmin yapmayın, "bilmiyorum" seçeneğini işaretleyin; bu, ölçümün doğruluğunu artırır.""")


D.add("pretest", pretest)

# 14 handover
statement(D, "next", [("Başlıyoruz.", None), ("09:30 · Siber biyogüvenliğin", T2), ("temelleri", T2)],
          """Testler toplandıktan sonra bu slayt. Prof. Dr. Ayşen Gargılı Keleş'i kürsüye davet edin.""",
          eyebrow_="Sıradaki oturum", sub="Prof. Dr. Ayşen Gargılı Keleş · Marmara Üniversitesi", size=92,
          right_html=kapsid_svg(300, 1490, 380, animate=True), width=1300)

SECTIONS = {"s1": {"description": "Hoş geldiniz", "start": "cover"}, "s2": {"description": "Program ve düzen", "start": "goals"},
            "s3": {"description": "Ön test", "start": "code"}}

if __name__ == "__main__":
    write_deck(sys.argv[1], "Açılış ve ön test · Sivas 2026", SECTIONS, D.render())
    print("ok", len(D.slides))
