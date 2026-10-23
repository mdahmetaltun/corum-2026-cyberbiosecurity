"""Deck S3 · Alıştırma 3: Çok faktörlü doğrulama ve donanım güvenlik anahtarları (2. Gün 13:00–14:30, 90 dk, uygulamalı)."""
import os, sys
from scommon import *

VID = (os.environ.get("S3_STILL", "/_blob/still"), os.environ.get("S3_CLIP", "/_blob/clip"))
D = Deck("Alıştırma 3 · MFA ve donanım anahtarları · Sivas 2026")


def dark(sid, notes, transition="fade", glow=(AMBER, V2)):
    def wrap(body):
        def f(i, n):
            inner = progress(i, n, True) + bg_glow(len(sid) * 5, *glow) + body(i, n) + footer(i + 1, True)
            return section(sid, inner, True, transition, notes)
        D.add(sid, f)
        return body
    return wrap


def steps(rows, top=300, left=128, width=1000, start=1, gap=112, h=96):
    out = ""
    for k, (t, sub) in enumerate(rows):
        out += (f'<div data-build-in="rise {start + k} auto" style="position:absolute;left:{left}px;top:{top + k * gap}px;width:{width}px;height:{h}px;display:flex;flex-direction:row;gap:24px;align-items:center;padding:0px 28px;background:{WHITE};border-radius:18px;box-shadow:0 8px 24px rgba(29,37,84,0.07)">'
                f'<p style="width:56px;height:56px;border-radius:28px;background:{AMBER};color:{INK};font-family:{DISPLAY};font-size:28px;font-weight:800;text-align:center;line-height:56px">{k + 1}</p>'
                f'<div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:28px;font-weight:600;line-height:1.25;color:{TEXT}">{t}</p>'
                + (f'<p style="font-size:24px;line-height:1.3;color:{MUTE}">{sub}</p>' if sub else "") + "</div></div>")
    return out


def station_tag(n, mins):
    return (f'<div style="position:absolute;left:1180px;top:136px;width:612px;display:flex;flex-direction:row;gap:14px;justify-content:flex-end;align-items:center">'
            f'<p style="font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:2px;color:{INK};background:{AMBER};padding:6px 16px;border-radius:20px">İSTASYON {n}</p>'
            f'<p style="font-family:{MONO};font-size:24px;font-weight:600;color:{MUTE}">{mins}</p></div>')


# 1 cover
cover(D, "cover", "2. Gün · Salı 17 Kasım 2026 · 13:00–14:30 · Alıştırma 3",
      [("Şifre yetmez.", None), ("MFA ve donanım", AMBER), ("anahtarı", AMBER)],
      "Uygulamalı: kendi hesabınızda çok faktörlü doğrulama, güvenlik anahtarı ve geçiş anahtarı",
      emb("keytap", 1130, 250, 700, 520, PAL, ink=INK, tap="DOKUN"),
      """Öğleden sonraya hoş geldiniz. Bu oturum 90 dakika ve neredeyse tamamı uygulama. Herkes telefonunu ve dizüstü bilgisayarını masaya koysun.
Sağdaki animasyon bugünün özeti: anahtara dokunuyorsunuz; gerçek giriş sayfasında anahtar imzalıyor, sahte sayfada reddediyor.""", size=96)

# 2 film
video(D, "film", VID[0], VID[1], "Açılış filmi: parola alanı doluyor, sızdırılmış parola uyarısı, ardından güvenlik anahtarına dokunuş",
      """Açılış filmi, yaklaşık 9 saniye. Bir parola yazılıyor, sızdırılmış listede çıkıyor; sonra "Şifre yetmez" ve donanım anahtarı. Başlıkta ilerleyin.""")


# 3 Change Healthcare
@dark("change", """Neden buradayız? Şubat 2024, ABD'de Change Healthcare. Saldırganlar çalınmış kimlik bilgileriyle, çok faktörlü doğrulaması olmayan bir uzaktan erişim portalından girdi. Bunu şirketin üst yöneticisi Mayıs 2024'te ABD Kongresi'ndeki ifadesinde doğruladı.
ABD Sağlık Bakanlığı Sivil Haklar Ofisi'nin Temmuz 2025 güncellemesine göre etkilenen kişi sayısı yaklaşık 192,7 milyon.
Tek bir eksik kontrol. Bugün kapatacağımız kapı tam olarak bu.""", glow=(P2, AMBER))
def _(i, n):
    s = eyebrow("Şubat 2024 · Change Healthcare, ABD", 210)
    s += emb("counter", 128, 270, 900, 240, PAL, to=192.7, dec=1, size=220, fg=CREAM)
    s += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:510px;width:1000px;font-family:{DISPLAY};font-size:44px;font-weight:700;color:{P1}">milyon kişinin verisi etkilendi</p>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:590px;width:1000px;font-size:31px;line-height:1.45;color:{SKY}">Giriş noktası: çalınmış kimlik bilgileri ve çok faktörlü doğrulaması olmayan bir uzaktan erişim portalı.</p>'
    s += (f'<div data-build-in="rise 3 auto" style="position:absolute;left:1220px;top:290px;width:572px;display:flex;flex-direction:column;gap:18px;padding:36px 40px;background:{INK2};border-radius:22px;border-top:6px solid {AMBER}">'
          f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{AMBER}">EKSİK OLAN</p>'
          + H("Tek bir kontrol: ikinci faktör.", 40, CREAM) + P("Parola çalınmıştı; ikinci faktör olsaydı tek başına yetmezdi.", 28, SKY, lh=1.4) + "</div>")
    s += src("Kaynaklar: ABD HHS Sivil Haklar Ofisi, Change Healthcare güncellemesi, 31 Temmuz 2025; şirket CEO’sunun ABD Senatosu ifadesi, 1 Mayıs 2024.", top=880, dark=True)
    return s


# 4 evidence
@dark("evidence", """Kanıt. Microsoft araştırmacıları Meyer ve arkadaşları 2023'te kurumsal hesaplarda gerçek saldırı verisini inceledi.
Çok faktörlü doğrulama, hesabın ele geçirilme riskini genel olarak %99,22 azalttı. Parolası daha önce sızdırılmış hesaplarda bile azalma %98,56.
Dikkat: bu bir kurumun verisi ve doğrulayıcı türleri arasında fark var; birazdan merdiveni göreceğiz. Ama yön çok net.""", glow=(T2, V2))
def _(i, n):
    s = eyebrow("Kanıt · Microsoft kurumsal hesapları, 2023", 210)
    s += emb("counter", 128, 270, 900, 240, PAL, to=99.22, dec=2, size=220, fg=CREAM, pre="%")
    s += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:510px;width:1000px;font-family:{DISPLAY};font-size:44px;font-weight:700;color:{T2}">daha az hesap ele geçirme riski</p>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:590px;width:1000px;font-size:31px;line-height:1.45;color:{SKY}">Parolası daha önce sızdırılmış hesaplarda bile azalma %98,56.</p>'
    s += emb("shield", 1260, 230, 520, 560, PAL)
    s += src("Kaynak: Meyer LA ve ark. How effective is multifactor authentication at deterring cyberattacks? arXiv:2305.00945; 2023.", top=880, dark=True)
    return s


# 5 three factors
items = [
    icon("Brain", 52, V2) + H("Bildiğiniz", 34) + P("Parola, PIN, güvenlik sorusu.", 27, BODY2, lh=1.38) + tag("ÇALINABİLİR · TAHMİN EDİLEBİLİR", PTINT, PT),
    icon("KeyRound", 52, AMBERT) + H("Sahip olduğunuz", 34) + P("Telefon, doğrulayıcı uygulaması, güvenlik anahtarı.", 27, BODY2, lh=1.38) + tag("FİZİKSEL OLARAK SİZDE", ATINT, AMBERT),
    icon("Fingerprint", 52, TT) + H("Olduğunuz", 34) + P("Parmak izi, yüz tanıma; cihazın kilidini açar.", 27, BODY2, lh=1.38) + tag("CİHAZDA KALIR", TTINT, TT),
]
content(D, "factors", "Temel", "Üç faktör türü",
        cards_row(items, top=320, height=400, accents=[V2, AMBER, T2], pad="34px 36px")
        + callout(760, "Çok faktörlü doğrulama, farklı türden en az iki faktör ister. İki parola, iki faktör değildir.", label="Kural", icon="Layers", build="rise 4 auto"),
        ill="lock",
        notes="""Temel kavram: üç faktör türü. Bildiğiniz: parola. Sahip olduğunuz: telefon, uygulama, anahtar. Olduğunuz: biyometri, genellikle cihazın kilidini açmak için.
Kural: farklı türden iki faktör. Parola artı güvenlik sorusu iki faktör değildir; ikisi de "bildiğiniz".""")

# 6 ladder (magic source)
RUNGS = [("rung-sms", "SMS ile kod", "SIM değiştirme ve oltalamaya açık", "ZAYIF", P2, 140),
         ("rung-totp", "Uygulamada 6 haneli kod", "Kod sahte sayfaya yazdırılabilir", "ORTA", AMBER, 230),
         ("rung-push", "Bildirim + numara eşleştirme", "Bildirim yağmuruna karşı daha dirençli", "İYİ", V1, 320),
         ("rung-fido", "Güvenlik anahtarı · geçiş anahtarı", "Alan adına bağlı; sahte sayfada çalışmaz", "OLTALAMAYA DAYANIKLI", T3, 410)]


def ladder(active=None):
    out = ""
    for k, (rid, t, sub, lvl, c, hgt) in enumerate(RUNGS):
        x = 128 + k * 420
        y = 900 - hgt
        tc = {P2: PT, AMBER: AMBERT, T3: TT}.get(c, c)
        out += (f'<div id="{rid}" data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:{y - 150}px;width:396px;height:{hgt + 150}px;display:flex;flex-direction:column;gap:10px;padding:26px 28px;'
                f'background:{WHITE};border-radius:20px;border-top:8px solid {c};box-shadow:0 10px 30px rgba(29,37,84,0.08)">'
                f'<p style="font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:1px;color:{tc}">{lvl}</p>' + H(t, 30) + P(sub, 24, BODY2, lh=1.35) + "</div>")
    return out


content(D, "ladder", "Doğrulayıcı türleri", "Her ikinci faktör eşit değil",
        ladder() + src("Kaynak: NIST SP 800-63B-4 (2025) doğrulayıcı gereksinimleri; Lang ve ark. (2017).", top=920),
        ill="stairs",
        notes="""Her ikinci faktör eşit değil. Soldan sağa yükseliyoruz.
SMS kodu en zayıfı: numara taşıma ve oltalamaya açık. Uygulamadaki altı haneli kod daha iyi ama sahte bir sayfaya yazdırılabilir. Numara eşleştirmeli bildirim, bildirim yağmuruna karşı dirençli.
En üstte güvenlik anahtarı ve geçiş anahtarı: alan adına bağlı oldukları için sahte sayfada hiç çalışmazlar. NIST bunlara oltalamaya dayanıklı doğrulayıcı diyor.
Tıklayın: en üst basamağa yakınlaşıyoruz.""")

# 7 zoom into top rung (magic target)
body = (f'<div id="rung-fido" style="position:absolute;left:128px;top:290px;width:860px;height:600px;display:flex;flex-direction:column;gap:18px;padding:40px 44px;'
        f'background:{WHITE};border-radius:24px;border-top:8px solid {T3};box-shadow:0 12px 34px rgba(29,37,84,0.09)">'
        f'<p style="font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:1px;color:{TT}">OLTALAMAYA DAYANIKLI</p>'
        + H("Güvenlik anahtarı · geçiş anahtarı", 44)
        + P("Anahtar, kayıt sırasında sitenin alan adını öğrenir. Giriş anında yalnız o alan adına imza atar.", 29, TEXT, lh=1.42)
        + P("Benzer görünen sahte bir sayfa, anahtardan hiçbir şey alamaz. Kullanıcı aldansa bile anahtar aldanmaz.", 29, BODY2, lh=1.42)
        + f'<div style="display:flex;flex-direction:row;gap:12px">{tag("FIDO2 · WebAuthn", TTINT, TT)}{tag("Gizli anahtar cihazdan çıkmaz", VTINT, V3)}</div></div>')
body += (f'<div data-build-in="fade 1 auto" style="position:absolute;left:1020px;top:290px;width:772px;height:600px;background:{INK};border-radius:24px"></div>'
         + emb("keytap", 1040, 330, 732, 520, PAL, ink=INK, build="fade 1 auto"))
content(D, "fido", "Yakın plan", "Anahtar neden aldanmaz?", body, ill=None, transition="magic",
        notes="""Yakınlaştık. Güvenlik anahtarı kayıt sırasında sitenin alan adını öğreniyor ve giriş anında yalnız o alan adı için imza atıyor.
Sağdaki animasyonu izleyin: gerçek alan adında anahtar imzalıyor; tek harfi farklı sahte alan adında reddediyor. Kullanıcı sayfanın sahte olduğunu fark etmese bile anahtar fark ediyor.
Lang ve arkadaşlarının 2017 çalışması, güvenlik anahtarlarının büyük bir kurumda günlük kullanımda pratik olarak işleyebildiğini gösterdi.""")


# 8 Uber MFA fatigue
@dark("fatigue", """İkinci faktörün de bir zayıflığı var: bildirim yorgunluğu. Eylül 2022'de Uber'de bir yüklenicinin parolası çalınmıştı.
Saldırgan tekrar tekrar giriş bildirimi gönderdi, sonra WhatsApp'tan kendini BT çalışanı gibi tanıtıp "bildirimler durmazsa onaylaman gerekiyor" dedi. Yüklenici onayladı; saldırgan içerideydi.
Ders: beklemediğiniz bir bildirimi asla onaylamayın. Reddedin ve bildirin. Numara eşleştirme de bu saldırıyı büyük ölçüde zorlaştırır.""", glow=(P2, V2))
def _(i, n):
    s = eyebrow("Eylül 2022 · Uber · Bildirim yorgunluğu saldırısı", 210)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:270px;width:1000px;font-family:{DISPLAY};font-size:76px;font-weight:800;letter-spacing:-2px;line-height:1.08;color:{CREAM}">Beklemediğiniz bildirimi <span style="color:{P2}">onaylamayın.</span></h2>'
    seq = [("Parola çalındı", "Yüklenicinin kurumsal parolası ele geçirilmişti."), ("Bildirim yağmuru", "Saldırgan art arda giriş onayı istedi."),
           ("Sahte BT mesajı", "WhatsApp’tan: “Durması için bir kez onayla.”"), ("Tek onay yetti", "Saldırgan iç ağa erişti.")]
    for k, (a, b) in enumerate(seq):
        s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{480 + k * 98}px;width:1000px;display:flex;flex-direction:row;gap:22px;align-items:center">'
              f'<p style="width:56px;height:56px;border-radius:28px;background:{P2 if k == 3 else INK3};color:#FFFFFF;font-family:{DISPLAY};font-size:26px;font-weight:800;text-align:center;line-height:56px">{k + 1}</p>'
              f'<p style="width:300px;font-size:30px;font-weight:600;color:{CREAM}">{a}</p><p style="flex:1;font-size:28px;color:{SKY}">{b}</p></div>')
    s += (f'<div data-build-in="rise 6 auto" style="position:absolute;left:1260px;top:300px;width:532px;display:flex;flex-direction:column;gap:16px;padding:36px 38px;background:{INK2};border-radius:22px;border-top:6px solid {T2}">'
          f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{T2}">KURAL</p>' + H("Reddet ve bildir.", 44, CREAM)
          + P("Numara eşleştirme açık olsun: ekrandaki sayıyı görmeden onay verilemez.", 28, SKY, lh=1.4) + "</div>")
    s += src("Kaynak: InfoQ, “Uber breach: MFA fatigue”, 24 Eylül 2022; Uber güvenlik güncellemesi, Eylül 2022.", top=900, dark=True)
    return s


# 9 kinetic
kinetic(D, "k-go", "Uygulama", [("4 İSTASYON.", None), ("90 DAKİKA.", T2), ("KENDİ", None), ("HESABINIZ.", AMBER)],
        """Kinetik ara slayt. Konuşma bitti, uygulama başlıyor. Dört istasyon, kendi hesaplarınızda.""", size=140)

# 10 agenda
AG = [("13:10", "Hazırlık", "Telefon, uygulama mağazası, dizüstü", INK3), ("13:15", "İstasyon 1", "Doğrulayıcı uygulaması", V2),
      ("13:30", "İstasyon 2", "Hesapta MFA’yı açma, kurtarma kodları", T3), ("13:50", "İstasyon 3", "Güvenlik anahtarı ve geçiş anahtarı", AMBER),
      ("14:10", "İstasyon 4", "Reddet ve bildir tatbikatı", P2), ("14:20", "Doğrulama", "Kolaylaştırıcı kontrol listesi", V1)]
body = (f'<svg aria-label="" width="1664" height="16" viewBox="0 0 1664 16" style="position:absolute;left:128px;top:346px;width:1664px;height:16px"><style>.l{{stroke-dasharray:1664;stroke-dashoffset:1664;animation:l 3s cubic-bezier(.6,0,.2,1) forwards}}@keyframes l{{to{{stroke-dashoffset:0}}}}{RM}</style>'
        f'<line x1="0" y1="8" x2="1664" y2="8" stroke="{LINE}" stroke-width="4"/><line class="l" x1="0" y1="8" x2="1664" y2="8" stroke="{AMBER}" stroke-width="4"/></svg>')
for k, (tm, t, sub, c) in enumerate(AG):
    x = 128 + k * 282
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:320px;width:262px;display:flex;flex-direction:column;gap:14px">'
             f'<p style="width:68px;height:68px;border-radius:34px;background:{c};border:6px solid {PAPER}"></p>'
             f'<p style="font-family:{MONO};font-size:28px;font-weight:600;color:{TEXT}">{tm}</p>' + H(t, 30) + P(sub, 25, BODY2, lh=1.35) + "</div>")
body += callout(720, "Takıldığınız yerde elinizi kaldırın. Ekranınızı göstermeniz yeter; parolanızı kimseye söylemeyin, kolaylaştırıcıya da.", label="Destek", icon="Hand", build="rise 7 auto")
content(D, "agenda", "Akış", "Altı adımda 80 dakika", body, ill="clock",
        notes="""Akış. 13:10 hazırlık; 13:15 birinci istasyon, doğrulayıcı uygulaması; 13:30 ikinci istasyon, hesapta MFA ve kurtarma kodları; 13:50 üçüncü istasyon, güvenlik anahtarı ve geçiş anahtarı; 14:10 dördüncü istasyon, reddet ve bildir tatbikatı; 14:20 doğrulama.
Önemli kural: kolaylaştırıcılar ekranınıza bakabilir ama parolanızı hiç kimse istemez, siz de söylemezsiniz. Bu da bugünün dersinin bir parçası.""")

# 11 prep
items = [icon("BatteryCharging", 48, V2) + H("Telefon", 30) + P("Şarjı en az %30. Uygulama mağazasında oturum açık.", 26, BODY2, lh=1.38),
         icon("Laptop", 48, TT) + H("Dizüstü", 30) + P("Güncel bir tarayıcı: Chrome, Edge, Firefox ya da Safari.", 26, BODY2, lh=1.38),
         icon("AtSign", 48, PT) + H("Hesap", 30) + P("Kurumsal hesabınızın parolasını bildiğinizden emin olun.", 26, BODY2, lh=1.38),
         icon("Wifi", 48, AMBERT) + H("Bağlantı", 30) + P("Salon ağına bağlanın; ağ bilgisi masanızdaki kartta.", 26, BODY2, lh=1.38)]
content(D, "prep", "Hazırlık · 13:10", "Masanızda dört şey olsun",
        cards_row(items, top=320, height=360, pad="32px 32px")
        + callout(720, "Parolanızı hatırlamıyorsanız şimdi söyleyin; sıfırlama birkaç dakika sürer ve alıştırmanın geri kalanını bekletmez.", label="Şimdi", icon="Clock", build="rise 5 auto"),
        ill="checklist",
        notes="""Hazırlık. Telefonun şarjı ve uygulama mağazasında oturum; dizüstünde güncel tarayıcı; kurumsal hesap parolası; ağ bağlantısı.
Parolasını hatırlamayan varsa şimdi ayırın; BT sorumlusuyla sıfırlama yapılsın.""")

# 12 station 1: authenticator
body = station_tag(1, "13:15–13:30") + steps([
    ("Uygulama mağazasından bir doğrulayıcı uygulaması kurun.", "Microsoft Authenticator, Google Authenticator ya da Yubico Authenticator."),
    ("Uygulamayı açın; bildirim izni verin.", "Numara eşleştirmeli onay için bildirimler gerekir."),
    ("Telefonunuzun ekran kilidinin açık olduğunu kontrol edin.", "Kilitsiz telefon, ikinci faktörü herkese verir."),
    ("Bulut yedeklemeyi, hesabınız korunuyorsa açın.", "Telefon değişirse kodlar kaybolmaz."),
], top=300, width=1040)
body += f'<div style="position:absolute;left:1220px;top:300px;width:572px;height:560px;background:{INK};border-radius:24px"></div>'
body += emb("otp", 1220, 300, 572, 560, PAL, ink=INK, acc="kullanici@kurum.edu.tr", cap="Kod her 30 saniyede değişir", per=8)
content(D, "s1", "İstasyon 1", "Doğrulayıcı uygulamasını kurun", body, ill=None,
        notes="""İstasyon 1, on beş dakika. Bir doğrulayıcı uygulaması kurun. Hangisi olduğu çok önemli değil; kurumunuzun MFA platformu hangisini öneriyorsa onu seçin.
Ekran kilidi şart: kilitsiz telefon ikinci faktörü herkese verir.
Sağdaki animasyon bir kod ekranı: altı hane, otuz saniyede bir değişir. Burada hızlandırılmış gösteriliyor.""")

# 13 station 2: enable MFA
body = station_tag(2, "13:30–13:50") + steps([
    ("Dizüstünde hesabınızın güvenlik ayarlarını açın.", "Genellikle Hesap › Güvenlik › İki adımlı doğrulama."),
    ("“Doğrulayıcı uygulaması ekle” seçeneğini seçin.", "Ekranda bir QR kod belirir."),
    ("Telefondaki uygulamayla QR kodu tarayın.", "Hesap adı uygulamada listelenir."),
    ("Uygulamadaki 6 haneli kodu dizüstüne yazın.", "Kod süresi dolarsa bir sonrakini bekleyin."),
    ("Çıkış yapıp tekrar girin: ikinci faktör istenmeli.", "Bu, kurulumun çalıştığının kanıtıdır."),
], top=300, width=1664, gap=110, h=94)
content(D, "s2", "İstasyon 2", "Hesabınızda MFA’yı açın", body, ill=None,
        notes="""İstasyon 2, yirmi dakika. Önce kurumsal hesabınızda, zaman kalırsa kişisel e-postanızda.
Beş adım: güvenlik ayarları, doğrulayıcı ekle, QR'ı tara, kodu yaz, çıkış yapıp tekrar gir. Son adım önemli: ikinci faktör sorulmazsa kurulum tamamlanmamıştır.
Menü adları platforma göre değişir; masa aralarında dolaşarak ekranları birlikte bulalım.""")

# 14 recovery codes
items = [icon("Printer", 48, V2) + H("Kâğıda yazın ya da yazdırın", 30) + P("Kilitli bir çekmecede ya da kasada saklayın.", 26, BODY2, lh=1.38),
         icon("Ban", 48, PT) + H("Bunları yapmayın", 30) + P("E-postanıza göndermeyin, fotoğrafını çekmeyin, masaüstüne kaydetmeyin.", 26, BODY2, lh=1.38),
         icon("RefreshCw", 48, TT) + H("Kullandıkça yenileyin", 30) + P("Her kod bir kez çalışır. Azaldığında yeni set oluşturun.", 26, BODY2, lh=1.38)]
content(D, "recovery", "İstasyon 2 · son adım", "Kurtarma kodları: telefonunuz kaybolursa",
        cards_row(items, top=320, height=360, pad="32px 34px")
        + callout(720, "İkinci bir yöntem de ekleyin: güvenlik anahtarı ya da ikinci bir cihaz. Tek faktöre bağlı kalan hesap, telefonla birlikte kaybolur.", label="Yedek", icon="Copy", build="rise 4 auto"),
        ill="backup",
        notes="""Kurtarma kodları. Çoğu platform MFA'yı açarken bir set kod verir. Bunlar telefonunuz kaybolduğunda hesaba girmenin yolu.
Kâğıda yazın, kilitli yerde saklayın. E-postaya, fotoğrafa, masaüstüne değil; çünkü saldırgan oralara zaten bakar.
İkinci bir yöntem ekleyin. Telefon kaybı, MFA'dan vazgeçmenin değil, yedeğin nedenidir.""")

# 15 station 3a: security key
body = station_tag(3, "13:50–14:10") + steps([
    ("Yubico Authenticator ile anahtara bir FIDO2 PIN’i belirleyin.", "En az 6 karakter. PIN anahtarda kalır, sunucuya gitmez."),
    ("Hesap güvenlik ayarlarında “Güvenlik anahtarı ekle”yi seçin.", "Bazı platformlar “Geçiş anahtarı ekle” der."),
    ("Anahtarı USB’ye takın ya da telefonun arkasına dokundurun (NFC).", "Tarayıcı istediğinde PIN’i girin."),
    ("Altın diske dokunun; anahtarı adlandırın.", "Örnek: “Anahtar 1 · ofis”."),
    ("Çıkış yapıp anahtarla tekrar girin.", "Sonra ikinci yöntemin de kayıtlı olduğunu kontrol edin."),
], top=300, width=1100, gap=110, h=94)
body += (f'<div data-build-in="fade 6 auto" style="position:absolute;left:1260px;top:300px;width:532px;display:flex;flex-direction:column;gap:16px;padding:32px 36px;background:{INK};border-radius:22px;border-top:6px solid {AMBER}">'
         f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{AMBER}">KİMLER İÇİN?</p>'
         + H("En yüksek erişime sahip beş kullanıcı", 34, CREAM)
         + P("YubiKey 5 NFC anahtarlar bu kişiler için yapılandırılır. Diğer katılımcılar adımları izler ve geçiş anahtarını telefonlarında dener.", 27, SKY, lh=1.42) + "</div>")
content(D, "s3a", "İstasyon 3a", "Güvenlik anahtarını kaydedin", body, ill=None,
        notes="""İstasyon 3, yirmi dakika. İki grup var.
En yüksek erişime sahip beş kullanıcı YubiKey 5 NFC anahtarını kendi hesabına kaydediyor: önce Yubico Authenticator ile FIDO2 PIN'i, sonra hesapta "güvenlik anahtarı ekle", tak ya da dokundur, altın diske dokun, adlandır, çıkış yapıp anahtarla tekrar gir.
PIN anahtarda kalır, sunucuya gitmez; bu yüzden PIN kısa olsa bile güvenli. Diğer katılımcılar bir sonraki slayttaki geçiş anahtarını dener.""")

# 16 station 3b: passkey
items = [icon("Smartphone", 48, V2) + H("Telefonunuz anahtar olur", 30) + P("Geçiş anahtarı telefonun güvenli bölgesinde saklanır; yüz ya da parmak iziyle açılır.", 26, BODY2, lh=1.38),
         icon("QrCode", 48, TT) + H("Dizüstünde QR ile", 30) + P("Dizüstü tarayıcısı bir QR gösterir; telefonla tarayıp onaylarsınız. Bluetooth yakınlığı da kontrol edilir.", 26, BODY2, lh=1.38),
         icon("Globe", 48, PT) + H("Alan adına bağlı", 30) + P("Güvenlik anahtarı gibi, yalnız kaydedildiği sitede çalışır.", 26, BODY2, lh=1.38)]
content(D, "s3b", "İstasyon 3b", "Geçiş anahtarı: telefonunuz anahtar olur",
        cards_row(items, top=320, height=380, pad="32px 34px")
        + callout(740, "Platformunuz geçiş anahtarını destekliyorsa, kişisel e-postanızda da deneyin. Evde de aynı alışkanlık.", label="Ev ödevi", icon="House", build="rise 4 auto"),
        ill="lock",
        notes="""Geçiş anahtarı, yani passkey. Telefonunuz bir güvenlik anahtarı gibi davranır; gizli anahtar telefonun güvenli bölgesinde kalır ve yüz ya da parmak izinizle açılır.
Dizüstünde giriş yaparken tarayıcı bir QR gösterir; telefonla tarayıp onaylarsınız. Güvenlik anahtarı gibi alan adına bağlıdır, sahte sitede çalışmaz.""")

# 17 station 4: drill
SC = [("Gece 02:10", "Telefonunuza bir giriş onayı bildirimi geliyor. O saatte bilgisayar başında değilsiniz.", "Reddet · parolayı değiştir · BT’ye bildir", V2),
      ("Telefon", "“BT’den arıyoruz, hesabınızı doğrulamak için ekrandaki kodu okur musunuz?”", "Kodu söyleme · kapat · bilinen numaradan geri ara", P2),
      ("E-posta", "“giris-kurum.edu-tr.com” adresine yönlendiren bir “şifre süresi doldu” mesajı.", "Bağlantıya tıklama · anahtar zaten imzalamaz · bildir", AMBER)]
items = [tag(a, {V2: VTINT, P2: PTINT, AMBER: ATINT}[c], {V2: V3, P2: PT, AMBER: AMBERT}[c]) + P(b, 27, TEXT, lh=1.4)
         + f'<div style="height:2px;background:{LINE}"></div>' + f'<p style="font-family:{MONO};font-size:24px;font-weight:600;line-height:1.4;color:{TT}">{r}</p>' for a, b, r, c in SC]
content(D, "s4", "İstasyon 4 · 14:10–14:20", "Reddet ve bildir: üç senaryo",
        cards_row(items, top=300, height=470, accents=[c for *_, c in SC], pad="32px 34px", kind="rise")
        + src("Her senaryoda önce masanızda 1 dakika tartışın; sonra doğru davranış kartın altında açılır.", top=820),
        ill="phish",
        notes="""İstasyon 4, on dakika. Üç senaryo. Her biri için masada bir dakika tartışın, ne yapardınız?
Bir: gece ikide gelen beklenmedik onay isteği. Reddet, parolayı değiştir, bildir. Parolanız zaten çalınmış demektir.
İki: "BT'den arıyoruz, kodu okur musunuz?" Kodu kimse istemez. Kapatın, bilinen numaradan geri arayın.
Üç: benzer alan adıyla gelen şifre yenileme e-postası. Tıklamayın; tıklasanız bile güvenlik anahtarı bu alan adı için imza atmaz.
Not: kartlarda doğru cevap görünüyor; isterseniz tartışma bitene kadar slaydı bir önceki ekranda tutun.""")

# 18 troubleshooting
TR = [("Clock", "Kod kabul edilmiyor", "Telefonun saati otomatik ayarda mı? Kodlar zamana bağlıdır."),
      ("Nfc", "Anahtar okunmuyor", "Telefonun arkasında NFC alanını bulun; anahtarı 2–3 saniye sabit tutun."),
      ("AppWindow", "Tarayıcı anahtarı görmüyor", "Güncel bir tarayıcı deneyin; gizli pencerede eklentisiz açın."),
      ("SmartphoneNfc", "Telefon kayboldu", "Kurtarma koduyla girin, eski cihazı hesaptan kaldırın, BT’ye bildirin.")]
items = [icon(ic, 46, [V2, TT, PT, AMBERT][k]) + H(a, 30) + P(b, 26, BODY2, lh=1.38) for k, (ic, a, b) in enumerate(TR)]
content(D, "trouble", "Sorun giderme", "En sık dört takılma",
        cards_row(items, top=320, n=2, height=250, row_gap=24, pad="30px 34px"),
        ill="gauge",
        notes="""En sık takılmalar. Kod kabul edilmiyorsa çoğu zaman telefonun saati elle ayarlanmıştır; otomatik saate alın. Anahtar okunmuyorsa telefonun NFC alanını bulun, iki üç saniye sabit tutun. Tarayıcı anahtarı görmüyorsa güncel bir tarayıcı deneyin.
Telefon kaybında: kurtarma koduyla girin, eski cihazı hesaptan kaldırın, BT'ye bildirin.""")

# 19 policy
items = [icon("Siren", 48, PT) + H("Kaybolursa hemen bildirin", 30) + P("Anahtar aynı gün hesaptan kaldırılır. Bildirmek ceza değil, korumadır.", 26, BODY2, lh=1.38),
         icon("KeySquare", 48, V2) + H("İkinci anahtar ya da yöntem", 30) + P("Kritik hesaplarda iki kayıtlı anahtar ya da anahtar + uygulama.", 26, BODY2, lh=1.38),
         icon("HandMetal", 48, TT) + H("Paylaşılmaz", 30) + P("Anahtar kişiye özeldir. Laboratuvarda “ortak anahtar” olmaz.", 26, BODY2, lh=1.38)]
content(D, "policy", "Kural", "Anahtarın yaşam döngüsü",
        cards_row(items, top=320, height=360, accents=[P2, V2, T2], pad="32px 34px")
        + callout(720, "Bu üç kural, laboratuvarın taslak olay müdahale protokolüne ve eğitim el kitabına eklenecek.", label="Yazılı hale", icon="FileCheck", build="rise 4 auto"),
        ill="lock",
        notes="""Anahtarın yaşam döngüsü üç kurala bağlı. Kaybolursa hemen bildir; anahtar aynı gün kaldırılır. Kritik hesaplarda ikinci anahtar ya da ikinci yöntem. Anahtar kişiye özeldir, paylaşılmaz.
Bunları el kitabına ve olay müdahale protokolüne ekliyoruz.""")

# 20 verification
CK = [("MFA açık", "Hesap ayarlarında ikinci faktör listeleniyor."), ("Test girişi", "Çıkış yapıp girildiğinde ikinci faktör isteniyor."),
      ("Kurtarma", "Kurtarma kodları güvenli bir yerde, çevrim dışı."), ("Anahtar", "Yüksek erişimli kullanıcılar anahtarla giriş yapabiliyor."),
      ("Davranış", "Beklenmedik bildirim senaryosunda doğru cevap: reddet ve bildir.")]
body = ""
for k, (a, b) in enumerate(CK):
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{300 + k * 112}px;width:1240px;height:96px;display:flex;flex-direction:row;gap:24px;align-items:center;padding:0px 28px;background:{WHITE};border-radius:18px;box-shadow:0 8px 24px rgba(29,37,84,0.07)">'
             f'<x-icon name="SquareCheckBig" style="width:44px;height:44px;color:{TT}"></x-icon><p style="width:220px;font-size:29px;font-weight:700;color:{TEXT}">{a}</p><p style="flex:1;font-size:27px;color:{BODY2}">{b}</p></div>')
body += (f'<div data-build-in="fade 6 auto" style="position:absolute;left:1420px;top:300px;width:372px;display:flex;flex-direction:column;gap:14px;padding:32px 34px;background:{INK};border-radius:22px;border-top:6px solid {T2}">'
         f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{T2}">KAYIT</p>' + H("Kolaylaştırıcı katılımcı koduyla işaretler.", 30, CREAM)
         + P("Sonuç, yeterlik kontrolünün MFA bölümüne girer.", 26, SKY, lh=1.4) + "</div>")
content(D, "verify", "Doğrulama · 14:20", "Beş maddelik kontrol", body, ill=None,
        notes="""Doğrulama. Kolaylaştırıcılar masaları dolaşıp beş maddeyi işaretliyor: MFA açık, test girişi çalışıyor, kurtarma kodları güvenli yerde, yüksek erişimli kullanıcılar anahtarla girebiliyor ve beklenmedik bildirim senaryosunda doğru cevap.
İşaretleme katılımcı koduyla yapılır; bu, kapanıştaki yeterlik kontrolünün MFA bölümü.""")


# 21 takeaways
@dark("takeaways", """Üç çıkarım. Bir: parola tek başına yetmez; ikinci faktör hesap ele geçirmenin büyük kısmını durdurur. İki: her ikinci faktör eşit değil; mümkün olan her yerde oltalamaya dayanıklı yöntem. Üç: beklemediğiniz bildirimi onaylamayın.
Sıradaki: 14:45'te Doç. Dr. Taşkıran ile veri bütünlüğü, ardından 15:45'te yeterlik kontrolü ve kapanış.""", glow=(AMBER, T2))
def _(i, n):
    s = eyebrow("Üç çıkarım", 210)
    TK = [("Parola tek başına yetmez.", "İkinci faktör, ele geçirmenin büyük kısmını durdurur.", T2),
          ("Oltalamaya dayanıklı olanı seçin.", "Güvenlik anahtarı ve geçiş anahtarı aldanmaz.", AMBER),
          ("Beklemediğiniz onayı vermeyin.", "Reddet ve bildir.", P1)]
    for k, (a, b, c) in enumerate(TK):
        s += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{280 + k * 150}px;width:1120px;display:flex;flex-direction:column;gap:8px">'
              f'<p style="font-family:{DISPLAY};font-size:52px;font-weight:800;letter-spacing:-1.5px;color:{c}">{a}</p><p style="font-size:30px;color:{SKY}">{b}</p></div>')
    nx = [("14:45", "Deneysel laboratuvarlarda veri bütünlüğü", "Doç. Dr. Ahmet Şevki Taşkıran"), ("15:45", "Yeterlik kontrolü ve kapanış", "Katılımcı kodunuzu hazır tutun")]
    for k, (a, b, c) in enumerate(nx):
        s += (f'<div data-build-in="fade {k + 4} auto" style="position:absolute;left:1320px;top:{290 + k * 250}px;width:472px;display:flex;flex-direction:column;gap:10px;padding:30px 34px;background:{INK2};border-radius:22px;border-left:8px solid {[T2, P2][k]}">'
              f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{[T2, P1][k]}">{a}</p>' + H(b, 30, CREAM) + P(c, 26, SKY) + "</div>")
    return s


# 22 references
refs(D, "refs", [
    "Temoshok D, Fenton JL, Choong YY, Lefkovitz N, Regenscheid A, Galluzzo R, Richer JP. Digital Identity Guidelines: Authentication and Authenticator Management. NIST SP 800-63B-4; 2025. doi:10.6028/NIST.SP.800-63B-4",
    "Lang J, Czeskis A, Balfanz D, Schilder M, Srinivas S. Security keys: practical cryptographic second factors for the modern web. In: Financial Cryptography and Data Security (FC 2016). LNCS 9603. Springer; 2017:422–440. doi:10.1007/978-3-662-54970-4_25",
    "Meyer LA, Romero S, Bertoli G, Burt T, Weinert A, Lavista Ferres J. How effective is multifactor authentication at deterring cyberattacks? arXiv:2305.00945; 2023 (DataCite DOI 10.48550/arXiv.2305.00945).",
    "National Institute of Standards and Technology. The NIST Cybersecurity Framework (CSF) 2.0. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "ABD HHS Sivil Haklar Ofisi. Change Healthcare siber güvenlik olayı güncellemesi. 31 Temmuz 2025. · Change Healthcare CEO’su, ABD Senatosu Maliye Komitesi ifadesi. 1 Mayıs 2024.",
    "InfoQ. Uber breach: MFA fatigue. 24 Eylül 2022.",
    "FIDO Alliance ve W3C. Web Authentication (WebAuthn) Level 2 önerisi ve FIDO2 belirtimleri (çevrim içi).",
])

SECTIONS = {"s1": {"description": "Neden?", "start": "cover"}, "s2": {"description": "Doğrulayıcılar", "start": "factors"},
            "s3": {"description": "Uygulama", "start": "k-go"}, "s4": {"description": "Doğrulama ve kapanış", "start": "trouble"}}

if __name__ == "__main__":
    write_deck(sys.argv[1], "Alıştırma 3 · MFA ve donanım anahtarları · Sivas 2026", SECTIONS, D.render())
    print("ok", len(D.slides))
