"""Deck S2 · Üniversitelerde Biyoteknolojiyi Siber Hırsızlıktan Korumak (1. Gün 14:45–15:30, 45 dk)."""
import os, sys
from scommon import *

VID = (os.environ.get("S2_STILL", "/_blob/still"), os.environ.get("S2_CLIP", "/_blob/clip"))
D = Deck("Biyoteknolojiyi Siber Hırsızlıktan Korumak · Sivas 2026")


def dark(sid, notes, transition="fade", glow=(V2, T2)):
    def wrap(body):
        def f(i, n):
            inner = progress(i, n, True) + bg_glow(len(sid) * 3, *glow) + body(i, n) + footer(i + 1, True)
            return section(sid, inner, True, transition, notes)
        D.add(sid, f)
        return body
    return wrap


# 1 ── cover
cover(D, "cover", "1. Gün · Pazartesi 16 Kasım 2026 · 14:45–15:30",
      [("Biyoteknolojiyi", None), ("siber hırsızlıktan", P2), ("korumak", None)],
      "Üniversite laboratuvarları neden hedef, nasıl soyulur, nasıl korunur?",
      emb("capsid", 1180, 190, 640, 640, PAL, rings=True, burst=True, spin=.4, t1=T1, v1=V1, v3=V3),
      """Hoş geldiniz. Bu oturum 45 dakika. Üç soruya cevap arayacağız: üniversite laboratuvarları neden hedef, hırsızlık nasıl gerçekleşiyor ve Pazartesi sabahı ne yapabiliriz.
Sağdaki şekil çalıştayın simgesi: bir virüs kapsidi. Doğanın kendi güvenlik kabuğu. Ara ara açılıp kapanması bilinçli: koruma tek seferlik bir iş değil.
Başlık, 2024'te HSP'nin düzenlediği aynı adlı çalıştaydan geliyor; bu projenin başladığı yer orası.""")

# 2 ── opening film
video(D, "film", VID[0], VID[1], "Açılış filmi: bölge ağından bir laboratuvar bilgisayarındaki dosyaya yakınlaşma ve kopyalanan veri",
      """Açılış filmi, yaklaşık 14 saniye. Kamera bir bölge ağından kampüse, laboratuvara, cihaz bilgisayarına ve tek bir dosyaya iniyor; dosya sessizce kopyalanıyor.
Başlık kartı gelince ilerleyin.""")


# 3 ── APT29 / vaccine research
@dark("apt29", """Hikâyeye bir tarihle başlayalım: 16 Temmuz 2020.
İngiltere Ulusal Siber Güvenlik Merkezi NCSC ve Kanada CSE, APT29 adlı grubun 2020 boyunca Kanada, ABD ve İngiltere'de COVID-19 aşısı geliştiren kuruluşları hedef aldığını duyurdu. ABD NSA atfı doğruladı, CISA teknik ayrıntıları ve önerileri onayladı.
Grup, WellMess ve WellMail adlı özel zararlı yazılımlar kullandı. Mesaj şu: pandeminin en değerli bilgisi laboratuvar defterlerindeydi ve bunu bilenler yalnız bilim insanları değildi.
Kaynak: NCSC, 16 Temmuz 2020.""")
def _(i, n):
    s = eyebrow("16 Temmuz 2020 · Dört ülkenin ortak uyarısı", 230)
    s += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:300px;width:1040px;font-family:{DISPLAY};font-size:84px;font-weight:800;letter-spacing:-2px;line-height:1.06;color:{CREAM}">Aşı araştırması bir <span style="color:{P2}">istihbarat hedefiydi.</span></h2>'
    s += f'<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:600px;width:1000px;font-size:32px;line-height:1.42;color:{SKY}">İngiltere NCSC ve Kanada CSE: APT29 grubu 2020 boyunca Kanada, ABD ve İngiltere’de COVID-19 aşısı geliştiren kuruluşları hedef aldı. ABD NSA atfı doğruladı, CISA önerileri onayladı.</p>'
    s += emb("globe", 1200, 230, 600, 600, PAL)
    s += src("Kaynak: UK NCSC, “Advisory: APT29 targets COVID-19 vaccine development”, 16 Temmuz 2020.", top=880, dark=True)
    return s


# 4 ── kinetic: what is stolen
kinetic(D, "k-steal", "Siber hırsızlıkta kaybettiğimiz", [("VERİ.", None), ("FİKİR.", T2), ("ZAMAN.", None), ("GÜVEN.", P2)],
        """Kinetik ara slayt. Dört kelime tek tek düşsün, sonra şunu söyleyin:
Çalınan şey yalnız bir dosya değil. Yayımlanmamış bir fikir, yılların emeği ve en önemlisi bize numune ve veri emanet edenlerin güveni.""")

# 5 ── why universities
items = [
    icon("DoorOpen", 48, V2) + H("Açıklık", 34) + P("Misafir ağlar, kısa süreli hesaplar, her dönem değişen öğrenciler. Kapı çoğu zaman bilerek açık.", 26, BODY2, lh=1.38),
    icon("Gem", 48, TT) + H("Değer", 34) + P("Yayımlanmamış veri, diziler, protokoller ve patent öncesi fikirler. Piyasa değeri yüksek, koruması zayıf.", 26, BODY2, lh=1.38),
    icon("Network", 48, PT) + H("Dağınıklık", 34) + P("Her laboratuvar kendi BT’sini yürütür. Merkezî envanter, yama ve izleme çoğu yerde yok.", 26, BODY2, lh=1.38),
    icon("Handshake", 48, AMBERT) + H("Güven", 34) + P("Paylaşmak akademinin varsayılanı. Saldırgan bu kültürü bir e-postayla kullanır.", 26, BODY2, lh=1.38),
]
content(D, "why", "Hedef profili", "Üniversiteler neden hedef?",
        cards_row(items, top=320, height=430, pad="34px 34px")
        + callout(790, "Cihaz bilgisayarı yıllarca yamasız kalabilir, çünkü üretici yazılımı yalnız o işletim sistemi sürümünde çalışır.", build="rise 5 auto"),
        ill="network",
        notes="""Dört özellik üniversiteyi cazip kılıyor; tıklamayla birer birer açılıyor.
Açıklık: misafir ağlar, kısa süreli hesaplar. Değer: yayımlanmamış veri ve patent öncesi fikirler. Dağınıklık: her laboratuvar kendi BT'sini yürütüyor. Güven: paylaşmak akademinin varsayılanı.
Son satır, laboratuvara özgü en tanıdık sorun: cihaz bilgisayarı. Salona sorun: laboratuvarınızda Windows 7 ya da daha eski bir bilgisayar çalışıyor mu? Genellikle eller kalkar.""")


# 6 ── zoom: attack surface
@dark("zoom", """Şimdi yakınlaşalım. Bir bölge ağından başlıyoruz, kampüse, laboratuvara, cihaz bilgisayarına ve sonunda ham veriye iniyoruz.
Her yakınlaşma bir saldırı yüzeyi: ağ, bina, oda, makine, dosya. Saldırgan bu zinciri tersinden yürür: dosyaya ulaşmak için önce ağı, sonra binayı, sonra makineyi geçer.
Sağ alttaki sayı büyütme oranı. Animasyon kendiliğinden döner; konuşurken bırakın.""", glow=(V3, T2))
def _(i, n):
    s = head("Saldırı yüzeyi", "Yakınlaştırın: hırsızlık nerede olur?", True)
    s += emb("zoom", 128, 300, 1664, 600, PAL, labels=["BÖLGE AĞI", "KAMPÜS", "LABORATUVAR", "CİHAZ BİLGİSAYARI", "HAM VERİ"], per=3.4, bg=INK0)
    return s


# 7 ── actors
items = [
    tag("UZUN SOLUKLU", VTINT, V3) + H("Devlet destekli gruplar", 32) + P("Sessiz, sabırlı ve hedefli. Aşı, ilaç ve tarım biyoteknolojisi öncelikli.", 26, BODY2, lh=1.38),
    tag("ÇİFTE ŞANTAJ", PTINT, PT) + H("Fidye çeteleri", 32) + P("Veriyi şifreler, önce kopyalar. Ödemezseniz yayımlamakla tehdit eder.", 26, BODY2, lh=1.38),
    tag("YETKİLİ ERİŞİM", ATINT, AMBERT) + H("İçeriden", 32) + P("Çalışan, öğrenci ya da misafir araştırmacı. Kapıyı kırmasına gerek yok.", 26, BODY2, lh=1.38),
    tag("OTOMATİK", TTINT, TT) + H("Fırsatçılar", 32) + P("İnterneti tarayan botlar. Açık bırakılmış servisi saatler içinde bulur.", 26, BODY2, lh=1.38),
]
content(D, "actors", "Tehdit aktörleri", "Kim çalar?",
        cards_row(items, top=320, height=400, pad="32px 32px")
        + callout(760, "Dört aktörün ortak giriş kapısı çoğu zaman aynıdır: bir parola, bir yamasız cihaz ya da kapatılmamış bir hesap.", label="Ortak nokta", icon="KeyRound", build="rise 5 auto"),
        ill="people",
        notes="""Dört aktör. Amaçları farklı, kapıları çoğu zaman aynı.
Devlet destekli gruplar sabırlı; aşı ve ilaç araştırması 2020'de bunun en net örneğiydi. Fidye çeteleri artık yalnız şifrelemiyor, önce kopyalıyor. İçeriden tehdit, yetkiyle gelir; kapıyı kırmaz. Fırsatçılar ise sadece açık kapı arar.
Callout'u vurgulayın: savunmayı aktöre göre değil, kapıya göre kuracağız.""")

# 8 ── morph: cases
morph(D, "k-cases", "Beş vaka, beş ders", [("VAKALAR", None), ("UCSF", P2), ("EMA", T2), ("OHIO", AMBER), ("ILLUMINA", V1)],
      """Morf ara slaytı. Harfler parçacıklara ayrılıp bir sonraki vakanın adına dönüşüyor: UCSF, EMA, Ohio, Illumina.
Bunlar sırayla anlatacağımız vakalar. Her biri bilgi güvenliğinin farklı bir yüzünü gösteriyor.""",
      sub="Fidye · değiştirilen veri · içeriden hırsızlık · cihaz açığı")


# 9 ── UCSF
@dark("ucsf", """Haziran 2020, Kaliforniya Üniversitesi San Francisco Tıp Fakültesi.
NetWalker fidye yazılımı fakültedeki sınırlı bir BT ortamında sunucuları şifreledi. Üniversite, akademik çalışma için önemli verilere yeniden ulaşmak amacıyla yaklaşık 1,14 milyon dolar ödediğini açıkladı.
Sayı sayarken durun. Sonra şunu sorun: bu laboratuvarların yedeği olsaydı ödeme gerekir miydi? Ders: fidyede kaybedilen asıl şey araştırma takvimidir.
Kaynak: UCSF açıklaması, 26 Haziran 2020; BleepingComputer haberi.""", glow=(P2, V2))
def _(i, n):
    s = eyebrow("Haziran 2020 · UCSF Tıp Fakültesi · Fidye yazılımı", 210)
    s += emb("counter", 128, 270, 760, 240, PAL, to=1.14, dec=2, size=220, fg=CREAM)
    s += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:510px;width:900px;font-family:{DISPLAY};font-size:44px;font-weight:700;color:{P1}">milyon dolar fidye ödendi</p>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:590px;width:960px;font-size:30px;line-height:1.45;color:{SKY}">NetWalker, fakültedeki sınırlı bir BT ortamında sunucuları şifreledi. Üniversite, akademik çalışma için önemli verilere yeniden ulaşmak için ödeme yaptığını açıkladı.</p>'
    s += (f'<div data-build-in="rise 3 auto" style="position:absolute;left:1180px;top:290px;width:612px;display:flex;flex-direction:column;gap:18px;padding:36px 40px;background:{INK2};border-radius:22px;border-top:6px solid {P2}">'
          f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{P1}">DERS</p>'
          + H("Fidyede kaybedilen asıl şey araştırma takvimidir.", 38, CREAM)
          + P("Çevrimdışı ve denenmiş bir yedek, ödeme ile yeniden kurulum arasındaki farktır.", 28, SKY, lh=1.4) + "</div>")
    s += src("Kaynak: UCSF kamu açıklaması, 26 Haziran 2020; BleepingComputer, Haziran 2020.", top=880, dark=True)
    return s


# 10 ── EMA
EV = [("9 Ara 2020", "EMA siber saldırıyı duyurdu.", V2), ("Ara 2020", "Pfizer/BioNTech aşı başvurusuna ait belgelere erişildi.", V2),
      ("Oca 2021", "Belgelerin bir kısmı internette yayımlandı.", P2), ("15 Oca 2021", "EMA: bazı yazışmalar yayımlanmadan önce değiştirildi.", P2)]
tl = (f'<svg aria-label="" width="1664" height="20" viewBox="0 0 1664 20" style="position:absolute;left:128px;top:330px;width:1664px;height:20px">'
      f'<style>.l{{stroke-dasharray:1664;stroke-dashoffset:1664;animation:l 2.6s cubic-bezier(.6,0,.2,1) forwards}}@keyframes l{{to{{stroke-dashoffset:0}}}}{RM}</style>'
      f'<line x1="0" y1="10" x2="1664" y2="10" stroke="{LINE}" stroke-width="4"/><line class="l" x1="0" y1="10" x2="1664" y2="10" stroke="{P2}" stroke-width="4"/></svg>')
body = tl
for k, (d_, t, c) in enumerate(EV):
    x = 128 + k * 424
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:326px;width:392px;display:flex;flex-direction:column;gap:14px">'
             f'<div style="width:28px;height:28px;border-radius:14px;background:{c};border:5px solid {PAPER}"></div>'
             f'<p style="font-family:{MONO};font-size:26px;font-weight:600;color:{c if c != P2 else PT}">{d_}</p>'
             f'<p style="font-size:28px;line-height:1.38;color:{TEXT}">{t}</p></div>')
body += callout(720, "Bütünlük saldırısında soru “Kim gördü?” değil, “Hangi sürüm gerçek?” sorusudur. İmzalı ve sürümlü kayıt bu soruya cevap verir.", label="Ders", icon="FileWarning", build="rise 5 auto")
body += src("Kaynaklar: Avrupa İlaç Ajansı (EMA) açıklamaları, 9 Aralık 2020 ve 15 Ocak 2021; RAPS haberi, Ocak 2021.", top=900)
content(D, "ema", "Aralık 2020 · Avrupa İlaç Ajansı", "Çalınan belgeler değiştirilerek sızdırıldı", body, ill="phish",
        notes="""İkinci vaka bir düzenleyici kurum: Avrupa İlaç Ajansı.
9 Aralık 2020'de EMA bir siber saldırıyı duyurdu; Pfizer/BioNTech aşı başvurusuna ait belgelere erişilmişti. Ocak'ta belgelerin bir kısmı internette yayımlandı. 15 Ocak 2021'de EMA, bazı yazışmaların yayımlanmadan önce değiştirildiğini açıkladı.
Bu vakanın dersi bütünlük: amaç yalnız çalmak değil, güveni sarsmak. Bir laboratuvar için karşılığı şu: ham verinin değiştirilmediğini kanıtlayabiliyor musunuz?""")


# 11 ── DOJ indictment
@dark("doj", """Üçüncü vaka, bir iddianame. 21 Temmuz 2020'de ABD Adalet Bakanlığı iki kişiyi suçladı: Li Xiaoyu ve Dong Jiazhi.
İddianameye göre bu ikili on yılı aşkın bir süre boyunca dünya çapında yüksek teknoloji, ilaç ve diğer sektörlerden şirketleri hedef aldı; 2020'de COVID-19 aşı, tedavi ve test araştırması yapan kuruluşları taradı.
Not: bunlar iddia; suçlama mahkûmiyet değildir. Vurgulanacak nokta zaman ölçeği: on yıl. Fark edilmeden kalmak, bu işin asıl becerisi.
Kaynaklar: ABD Adalet Bakanlığı basın açıklaması, 21 Temmuz 2020; NPR haberi.""", glow=(V3, P2))
def _(i, n):
    s = eyebrow("21 Temmuz 2020 · ABD Adalet Bakanlığı iddianamesi", 210)
    s += emb("counter", 128, 270, 600, 240, PAL, to=10, size=220, fg=CREAM, suf="+")
    s += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:510px;width:900px;font-family:{DISPLAY};font-size:44px;font-weight:700;color:{T1}">yıl süren bir kampanya iddiası</p>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:590px;width:1000px;font-size:30px;line-height:1.45;color:{SKY}">İki kişi, yüksek teknoloji ve ilaç dahil pek çok sektörü hedef almakla suçlandı. İddianameye göre 2020’de COVID-19 aşı, tedavi ve test araştırması yapan kuruluşların ağlarında açık aradılar.</p>'
    s += emb("radar", 1260, 250, 520, 520, PAL)
    s += src("Kaynak: ABD Adalet Bakanlığı basın açıklaması, 21 Temmuz 2020; NPR, 21 Temmuz 2020. Suçlama, mahkûmiyet değildir.", top=880, dark=True)
    return s


# 12 ── insider: Nationwide Children's
stats = [("5+", "exozom araştırmasına ait ticari sır", V2), ("10", "yıl yetkili erişim (2008–2018)", T3), ("30", "ay hapis cezası (1 Şubat 2021)", P2)]
body = ""
for k, (v, t, c) in enumerate(stats):
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{310 + k * 176}px;width:640px;height:152px;{card_style(c, pad="0px 32px", top_border=False, extra=f"border-left:8px solid {c};")}flex-direction:row;gap:28px;align-items:center">'
             f'<p style="width:170px;font-family:{DISPLAY};font-size:84px;font-weight:800;letter-spacing:-3px;color:{c if c != P2 else PT}">{v}</p>'
             f'<p style="flex:1;font-size:28px;line-height:1.3;color:{TEXT}">{t}</p></div>')
body += (f'<div data-build-in="fade 4 auto" style="position:absolute;left:840px;top:310px;width:952px;display:flex;flex-direction:column;gap:20px">'
         + P("Nationwide Children’s Hospital Araştırma Enstitüsü’nde çalışan bir araştırmacı, eşiyle birlikte exozom araştırmalarına ait en az beş ticari sırrı çaldı.", 30, TEXT, lh=1.42)
         + P("Birini, Çin’de kurduğu şirket üzerinden exozom izolasyon kiti üretip satmak için kullandı. 2,6 milyon dolar tazminat ödemeye mahkûm edildi.", 30, BODY2, lh=1.42)
         + "</div>")
body += callout(836, "Erişim ayrılırken de yönetilir: ayrılan kişinin hesabı, paylaşılan klasörü ve kişisel bulut kopyası aynı gün kapanır.", label="Ders", icon="UserX", build="rise 5 auto")
content(D, "insider", "İçeriden hırsızlık · Ohio, ABD", "Kapıyı kırmaya gerek yoktu", body, ill="eye",
        notes="""Dördüncü vaka içeriden. Nationwide Children's Hospital'ın araştırma enstitüsü, Ohio.
Li Chen 2008–2018 arasında orada çalıştı; eşi Yu Zhou da aynı laboratuvar ortamındaydı. Birlikte exozom araştırmasına ait en az beş ticari sırrı çaldılar; birini Çin'de kurdukları şirkette exozom izolasyon kiti üretip satmak için kullandılar.
1 Şubat 2021'de Chen 30 ay hapis cezası aldı; 2,6 milyon dolar tazminat ve yaklaşık 1,45 milyon dolar müsadere.
Ders: içeriden tehdit bir teknoloji sorunu kadar bir süreç sorunu. Kim neye erişiyor, ayrılırken ne oluyor?
Kaynak: ABD Ohio Güney Bölgesi Savcılığı, 1 Şubat 2021.""")

# 13 ── Illumina
items = [
    f'<p style="font-family:{DISPLAY};font-size:96px;font-weight:800;letter-spacing:-3px;line-height:1;color:{PT}">10,0</p>' + H("CVSS önem puanı", 30) + P("CVE-2023-1968: kimlik doğrulaması olmadan, ağ üzerinden erişilebilen hizmet.", 26, BODY2, lh=1.38),
    icon("Dna", 52, V2) + H("Etkilenen cihazlar", 30) + P("iSeq 100, MiniSeq, MiSeq, NextSeq ve NovaSeq kontrol yazılımlarının belirli sürümleri.", 26, BODY2, lh=1.38),
    icon("TriangleAlert", 52, AMBERT) + H("Olası etki", 30) + P("Uzaktan kod çalıştırma; ayar ve yazılım değiştirme; hassas veriye erişim.", 26, BODY2, lh=1.38),
]
content(D, "illumina", "Nisan 2023 · CISA uyarısı ICSMA-23-117-01", "Cihazın kendisi bir kapı olabilir",
        cards_row(items, top=320, height=390, accents=[P2, V2, AMBER], pad="34px 36px")
        + callout(750, "Dizileme cihazının bilgisayarı bir sunucu gibi ele alınır: envanterde yer alır, yamalanır, ayrı bir ağ bölümünde çalışır.", build="rise 4 auto")
        + src("Kaynak: CISA, ICS Medical Advisory ICSMA-23-117-01, “Illumina Universal Copy Service”, 27 Nisan 2023.", top=900),
        ill="scan",
        notes="""Beşinci vaka bir saldırı değil, bir açık. Nisan 2023'te ABD CISA, Illumina'nın Universal Copy Service yazılımında iki açık duyurdu.
CVE-2023-1968'in önem puanı 10 üzerinden 10. Kimlik doğrulaması gerekmeden, ağ üzerinden kod çalıştırılabiliyor, ayarlar ve yazılım değiştirilebiliyor, veriye erişilebiliyor.
Etkilenenler iSeq, MiniSeq, MiSeq, NextSeq ve NovaSeq kontrol yazılımlarının belirli sürümleri. Bunlar pek çok üniversitenin çekirdek tesisinde olan cihazlar.
Ders: cihaz bilgisayarı bir laboratuvar aleti değil, ağdaki bir sunucu. Üretici yamalarını takip etmek kimin görevi? Salona sorun.""")


# 14 ── DNA synthesis integrity
@dark("dna", """Bir adım öteye gidelim: biyolojide siber saldırı yalnız veri çalmak değil, maddeyi değiştirmek de olabilir.
Ben-Gurion Üniversitesi'nden Puzis ve arkadaşları 2020'de Nature Biotechnology'de bir senaryo gösterdi: bir biyoloğun bilgisayarındaki zararlı yazılım, DNA sentez siparişindeki diziyi fark ettirmeden değiştirebilir; dizi tarama protokollerinin boşluklarından geçecek şekilde gizlenebilir.
Bu bir laboratuvar deneyiydi, gerçek bir saldırı değil. Ama soru gerçek: siparişinizdeki dizinin, tasarladığınız dizi olduğunu nasıl doğruluyorsunuz?""", glow=(T3, V2))
def _(i, n):
    s = eyebrow("Bütünlük · DNA sentezi", 210)
    s += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:270px;width:1060px;font-family:{DISPLAY};font-size:76px;font-weight:800;letter-spacing:-2px;line-height:1.08;color:{CREAM}">Tehdit yalnız çalmak değil, <span style="color:{T2}">değiştirmek.</span></h2>'
    s += f'<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:560px;width:1000px;font-size:31px;line-height:1.45;color:{SKY}">Puzis ve ark. (2020): bir bilgisayardaki zararlı yazılımın, sentez siparişindeki DNA dizisini fark ettirmeden değiştirebileceğini ve tarama boşluklarından geçirebileceğini gösterdi.</p>'
    s += (f'<div data-build-in="rise 4 auto" style="position:absolute;left:128px;top:760px;width:1000px;display:flex;flex-direction:row;gap:18px;align-items:center">'
          f'<x-icon name="ShieldCheck" style="width:44px;height:44px;color:{AMBER}"></x-icon><p style="flex:1;font-size:28px;line-height:1.38;color:{CREAM}">Savunma: siparişten önce ve teslimden sonra diziyi bağımsız olarak doğrulamak.</p></div>')
    s += emb("helix", 1270, 160, 520, 700, PAL, vert=True, n=14, r=6)
    s += src("Kaynak: Puzis R ve ark. Nat Biotechnol. 2020;38(12):1379–1381. doi:10.1038/s41587-020-00761-y", top=880, dark=True)
    return s


# 15–16 ── six cases → CIA triad (magic move)
CHIPS = [("c-apt", "APT29 · aşı araştırması", V2), ("c-ohio", "Ohio · ticari sır", V2), ("c-ema", "EMA · değiştirilen belge", T3),
         ("c-dna", "DNA sentezi · sipariş", T3), ("c-ucsf", "UCSF · fidye", P2), ("c-illu", "Illumina · cihaz açığı", AMBER)]


def chip(cid, text, c, x, y, w):
    return (f'<div id="{cid}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:96px;display:flex;flex-direction:row;align-items:center;gap:16px;padding:0px 26px;'
            f'background:{WHITE};border-radius:18px;border-left:8px solid {c};box-shadow:0 10px 30px rgba(29,37,84,0.09)">'
            f'<p style="font-family:{DISPLAY};font-size:28px;font-weight:700;letter-spacing:-0.5px;color:{INK}">{text}</p></div>')


body = ""
for k, (cid, t, c) in enumerate(CHIPS):
    body += chip(cid, t, c, 128 + (k % 3) * 564, 360 + (k // 3) * 130, 536)
body += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:680px;width:1500px;font-size:32px;line-height:1.4;color:{BODY2}">Altı örnek, farklı ülkeler ve farklı yıllar. Yine de üç başlıkta toplanıyorlar.</p>'
content(D, "cases", "Ara toplam", "Altı örnek, tek tabloda", body, ill="layers",
        notes="""Ara toplam. Anlattığımız altı örnek ekranda. Farklı ülkeler, farklı yıllar, farklı aktörler.
Tıklayın: bir sonraki slaytta bu kartlar kendiliğinden üç sütuna taşınacak.""")

COLS = [("Gizlilik", "Bilgi yetkisiz kişilere geçti", V2, ["c-apt", "c-ohio"]), ("Bütünlük", "Bilgi fark ettirmeden değişti", T3, ["c-ema", "c-dna"]),
        ("Erişilebilirlik", "Bilgiye ulaşılamadı", P2, ["c-ucsf"])]
body = ""
for k, (t, sub, c, ids) in enumerate(COLS):
    x = 128 + k * 564
    body += (f'<div data-build-in="fade 1 auto" style="position:absolute;left:{x}px;top:300px;width:536px;display:flex;flex-direction:column;gap:8px">'
             f'<p style="font-family:{DISPLAY};font-size:44px;font-weight:800;letter-spacing:-1px;color:{c if c != P2 else PT}">{t}</p><p style="font-size:26px;color:{BODY2}">{sub}</p></div>')
    for j, cid in enumerate(ids):
        tx = dict((a, (b, cc)) for a, b, cc in CHIPS)[cid]
        body += chip(cid, tx[0], tx[1], x, 430 + j * 120, 536)
tx = dict((a, (b, cc)) for a, b, cc in CHIPS)["c-illu"]
body += chip("c-illu", tx[0], tx[1], 1256, 550, 536)
body += f'<p data-build-in="fade 2 auto" style="position:absolute;left:1256px;top:666px;width:536px;font-size:26px;line-height:1.38;color:{AMBERT};font-weight:600">Yamasız cihaz üçünü birden tehdit eder.</p>'
body += callout(760, "Gizlilik, bütünlük, erişilebilirlik: laboratuvar verisinin üç değeri. Her kontrolü, hangisini koruduğunu sorarak seçin.", label="Çerçeve", icon="Triangle", build="rise 3 auto")
content(D, "triad", "Ara toplam", "Altı örnek, üç değer", body, ill="layers", transition="magic",
        notes="""Kartlar yerine oturdu: bilgi güvenliğinin üç temel değeri.
Gizlilik: APT29 ve Ohio vakası, bilgi yanlış ellere geçti. Bütünlük: EMA ve DNA sentezi, bilgi değişti. Erişilebilirlik: UCSF, bilgiye ulaşılamadı.
Illumina açığı ise üçünü birden tehdit ediyor; bu yüzden cihaz bilgisayarlarına ayrıca odaklanacağız.
Laboratuvar diliyle: veri sızmasın, değişmesin, kaybolmasın.""")

# 17 ── kinetic: anatomy
kinetic(D, "k-chain", "Bir hırsızlığın anatomisi", [("KEŞİF.", None), ("GİRİŞ.", T2), ("YAYILMA.", None), ("SIZMA.", P2)],
        """Kinetik ara slayt. Dört aşama. Bir sonraki slaytta bunları açıp her birinin nerede kırılabileceğini göstereceğim.""")

# 18 ── kill chain
ST = [("1", "Keşif", "Yayınlar, personel sayfaları, açık servis taraması.", "Farkındalık", V2),
      ("2", "İlk erişim", "Oltalama e-postası, çalınmış parola, yamasız VPN.", "MFA · yama", V2),
      ("3", "Yerleşme", "Kalıcı hesap ya da uzaktan erişim aracı kurulur.", "En az yetki", T3),
      ("4", "Yayılma", "Paylaşılan sürücüler ve cihaz bilgisayarları.", "Ağ bölütleme", T3),
      ("5", "Sızma ve etki", "Veri dışarı çıkar, şifrelenir ya da değiştirilir.", "İzleme · yedek", P2)]
body = (f'<svg aria-label="" width="1664" height="16" viewBox="0 0 1664 16" style="position:absolute;left:128px;top:336px;width:1664px;height:16px"><style>.l{{stroke-dasharray:1664;stroke-dashoffset:1664;animation:l 3s cubic-bezier(.6,0,.2,1) forwards}}@keyframes l{{to{{stroke-dashoffset:0}}}}{RM}</style>'
        f'<line x1="0" y1="8" x2="1664" y2="8" stroke="{LINE}" stroke-width="4"/><line class="l" x1="0" y1="8" x2="1664" y2="8" stroke="{V2}" stroke-width="4"/></svg>')
for k, (num, t, d_, fix, c) in enumerate(ST):
    x = 128 + k * 340
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:310px;width:308px;display:flex;flex-direction:column;gap:14px">'
             f'<p style="width:68px;height:68px;border-radius:34px;background:{c};color:#FFFFFF;font-family:{DISPLAY};font-size:32px;font-weight:800;text-align:center;line-height:68px">{num}</p>'
             + H(t, 32) + P(d_, 26, BODY2, lh=1.36) + "</div>")
    body += (f'<div data-build-in="pop {k + 6} auto" style="position:absolute;left:{x}px;top:640px;width:300px;display:flex;flex-direction:row;gap:12px;align-items:center;padding:16px 20px;background:{TTINT};border-radius:16px">'
             f'<x-icon name="ShieldCheck" style="width:34px;height:34px;color:{TT}"></x-icon><p style="font-family:{MONO};font-size:24px;font-weight:600;color:{TT}">{fix}</p></div>')
body += f'<p data-build-in="fade 11 auto" style="position:absolute;left:128px;top:780px;width:1600px;font-size:30px;line-height:1.4;color:{TEXT}">Zinciri kırmak için her halkayı korumak gerekmez: <b>erken bir halkayı kırmak</b> saldırının geri kalanını durdurur.</p>'
content(D, "chain", "Saldırı zinciri", "Beş halka, beş kırılma noktası", body, ill="chain",
        notes="""Beş halka, soldan sağa. Önce aşamalar gelir, sonra her birinin altındaki savunma.
Keşif: saldırgan web sitenizi, yayınlarınızı, personel listenizi okur. İlk erişim: çoğu zaman bir oltalama e-postası ya da çalınmış bir parola. Yerleşme: kalıcı bir hesap ya da uzaktan erişim aracı. Yayılma: paylaşılan sürücüler, cihaz bilgisayarları. Sızma: veri dışarı çıkar ya da şifrelenir.
Son cümle önemli: erken bir halkayı kırmak yeter. Yarınki MFA alıştırması tam olarak ikinci halkayı kırmak için.""")


# 19 ── exfil
@dark("exfil", """Peki sızma anını fark edebilir miyiz? Animasyonun ilk yarısında veri laboratuvardan dışarı akıyor; ikinci yarısında bir kontrol devreye giriyor ve akışı durduruyor.
Sağdaki üç işaret, en sık görülen ve fark edilmesi kolay olanlar: gece saatlerinde büyük aktarım, tanınmayan bir bulut hesabına yükleme ve ayrılmak üzere olan bir kullanıcının toplu indirmesi.
Bunlar teknik ekibin işi gibi görünür ama çoğu zaman ilk fark eden laboratuvar çalışanıdır.""", glow=(P2, T2))
def _(i, n):
    s = head("Tespit", "Veri dışarı akarken fark etmek", True)
    s += emb("exfil", 128, 300, 1000, 560, PAL, labels=["LABORATUVAR", "UZAK SUNUCU"])
    sig = [("Moon", "Gece saatlerinde olağandışı büyük aktarım"), ("CloudUpload", "Tanınmayan bir bulut hesabına yükleme"), ("UserMinus", "Ayrılmak üzere olan kullanıcının toplu indirmesi")]
    for k, (ic, t) in enumerate(sig):
        s += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:1180px;top:{310 + k * 182}px;width:612px;height:160px;display:flex;flex-direction:row;gap:24px;align-items:center;padding:0px 32px;background:{INK2};border-radius:20px;border-left:8px solid {[P2, AMBER, T2][k]}">'
              f'<x-icon name="{ic}" style="width:48px;height:48px;color:{[P1, AMBER, T2][k]}"></x-icon><p style="flex:1;font-size:29px;line-height:1.32;color:{CREAM}">{t}</p></div>')
    return s


# 20 ── morph: defence
morph(D, "k-def", "Şimdi savunma", [("SAVUNMA", None), ("6 KONTROL", T2)],
      """Morf ara slaytı: "Savunma" kelimesi "6 kontrol"e dönüşüyor. Ton değişiyor: vakalardan çözüme geçiyoruz.""", per=3.6)

# 21 ── six controls
CT = [("01", "Oltalamaya dayanıklı MFA", "Parola tek başına yetmez. Donanım anahtarı ya da geçiş anahtarı tercih edilir.", "PR.AA", V2),
      ("02", "Envanter ve yama", "Her cihaz bilgisayarı listede, sahibi belli, yaması takipte.", "ID.AM · PR.PS", T3),
      ("03", "Ağ bölütleme", "Cihaz bilgisayarları ofis ağından ayrı bir bölümde çalışır.", "PR.IR", P2),
      ("04", "En az yetki ve ayrılış", "Herkes yalnız ihtiyacı olana erişir; ayrılan hesap aynı gün kapanır.", "PR.AA", AMBER),
      ("05", "3-2-1 yedek", "Üç kopya, iki ortam, biri çevrimdışı. Geri yükleme yılda en az bir kez denenir.", "PR.DS · RC.RP", V1),
      ("06", "Bildirim kültürü", "Şüpheli durumu bildiren teşekkür alır, suçlanmaz. Kimi arayacağı yazılıdır.", "RS.MA", T2)]
items = [f'<div style="display:flex;flex-direction:row;justify-content:space-between;align-items:center"><p style="font-family:{DISPLAY};font-size:44px;font-weight:800;letter-spacing:-1px;color:{c if c not in (P2, AMBER, T2) else {P2: PT, AMBER: AMBERT, T2: TT}[c]}">{num}</p>{tag(code)}</div>'
         + H(t, 30) + P(d_, 25, BODY2, lh=1.36) for num, t, d_, code, c in CT]
content(D, "controls", "Savunma", "Laboratuvar için altı kontrol",
        cards_row(items, top=300, n=3, height=290, row_gap=24, accents=[c for *_, c in CT], pad="26px 32px")
        + src("Kodlar NIST CSF 2.0 kategorileridir (NIST CSWP 29, 2024).", top=910),
        ill="shield",
        notes="""Altı kontrol, her biri bir CSF 2.0 kategorisine bağlı. Kodları ezberlemenize gerek yok; bu sabahki oturumlarla bağlantıyı kurmak için yazdım.
Bir: oltalamaya dayanıklı MFA. Yarın uygulamalı yapacağız. İki: envanter ve yama; listede olmayan cihazı koruyamazsınız. Üç: cihaz bilgisayarları ayrı ağ bölümünde. Dört: en az yetki ve ayrılış süreci, Ohio vakasının dersi. Beş: 3-2-1 yedek ve denenmiş geri yükleme, UCSF'nin dersi. Altı: bildirim kültürü; bildiren teşekkür alır, suçlanmaz.""")

# 22 ── third parties
items = [
    icon("Wrench", 48, V2) + H("Servis firması", 32) + P("Uzaktan bakım yalnız talep üzerine, süreli ve kayıtlı. Kalıcı açık bağlantı bırakılmaz.", 26, BODY2, lh=1.38),
    icon("FlaskConical", 48, TT) + H("Dış müşteri", 32) + P("Numune ve sonuç verisi için sözleşmede güvenlik ve ihlal bildirimi maddesi bulunur.", 26, BODY2, lh=1.38),
    icon("Cloud", 48, PT) + H("Yazılım ve bulut", 32) + P("Veri hangi ülkede, kimin sunucusunda? Hesap kurumsal mı, kişisel mi?", 26, BODY2, lh=1.38),
]
content(D, "vendors", "Tedarik zinciri · GV.SC", "Üçüncü taraflar da bir kapıdır",
        cards_row(items, top=320, height=380, pad="34px 36px")
        + callout(740, "Bir servis hizmeti sunuyorsanız siz de başkasının tedarik zincirisiniz. Müşteriniz, sizin güvenliğinize güvenerek numune gönderir.", label="Ters açıdan", icon="Repeat", build="rise 4 auto"),
        ill="chain",
        notes="""Üçüncü taraflar. CSF 2.0'da bunun adı GV.SC, siber güvenlik tedarik zinciri risk yönetimi.
Servis firmasının uzaktan bağlantısı: yalnız talep üzerine, süreli ve kayıtlı olmalı. Dış müşteri: numune ve sonuç verisi için sözleşmede güvenlik ve bildirim maddesi. Yazılım ve bulut: veri nerede?
Ters açı önemli: analiz hizmeti veren her laboratuvar, müşterisinin tedarik zinciridir.""")


# 23 ── trusted research → bridge to next talk
@dark("trusted", """Son bir çerçeve: araştırma güvenliği. Siber güvenlik teknik kapıları korur; araştırma güvenliği iş birliğinin kendisini.
İngiltere'de NPSA ve NCSC'nin "Trusted Research" rehberi, akademisyenlere uluslararası iş birliğinden önce sorulacak soruları sistematik hale getiriyor: ortak kim, veri nereye gidiyor, hangi ihracat ve etik kuralları geçerli.
Bu konuyu bir sonraki oturumda Doç. Dr. Ahmet Şevki Taşkıran İngiltere pratiğinden örneklerle anlatacak. Köprüyü burada kuruyorum.""", glow=(V2, AMBER))
def _(i, n):
    s = eyebrow("Araştırma güvenliği", 210)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:270px;width:1100px;font-family:{DISPLAY};font-size:74px;font-weight:800;letter-spacing:-2px;line-height:1.08;color:{CREAM}">Açık kalmak, <span style="color:{AMBER}">korumasız kalmak</span> demek değil.</h2>'
    qs = ["Ortağım kim; kimlerle çalışıyor?", "Veri, numune ve kod nereye gidiyor?", "Hangi ihracat, etik ve sözleşme kuralları geçerli?"]
    for k, q in enumerate(qs):
        s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{510 + k * 108}px;width:1080px;display:flex;flex-direction:row;gap:22px;align-items:center">'
              f'<p style="width:64px;height:64px;border-radius:32px;background:{AMBER};color:{INK};font-family:{DISPLAY};font-size:30px;font-weight:800;text-align:center;line-height:64px">{k + 1}</p>'
              f'<p style="flex:1;font-size:32px;color:{CREAM}">{q}</p></div>')
    s += (f'<div data-build-in="rise 5 auto" style="position:absolute;left:1300px;top:300px;width:492px;display:flex;flex-direction:column;gap:16px;padding:36px 38px;background:{INK2};border-radius:22px;border-top:6px solid {T2}">'
          f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{T2}">SIRADAKİ OTURUM · 15:30</p>'
          + H("Uluslararası iş birliğinde araştırma güvenliği", 34, CREAM) + P("Doç. Dr. Ahmet Şevki Taşkıran · İngiltere pratiğinden örnekler", 27, SKY, lh=1.4) + "</div>")
    s += src("Kaynak: UK NPSA ve NCSC, “Trusted Research” rehberi (çevrim içi, güncel sürüm).", top=880, dark=True)
    return s


# 24 ── Türkiye
items = [
    tag("RG 32846 · 19 MART 2025", VTINT, V3) + H("7545 sayılı Siber Güvenlik Kanunu", 30) + P("Siber güvenlik yükümlülüklerini ve olay bildirimini kanun düzeyine taşıdı.", 26, BODY2, lh=1.38),
    tag("KVK KURULU 2019/10", PTINT, PT) + H("72 saat", 30) + P("Kişisel veri ihlali Kurul’a gecikmeksizin ve en geç 72 saat içinde bildirilir.", 26, BODY2, lh=1.38),
    tag("KVKK MADDE 6", TTINT, TT) + H("Sağlık ve genetik veri", 30) + P("Özel nitelikli kişisel veridir; ek önlem ve sıkı erişim kuralı gerektirir.", 26, BODY2, lh=1.38),
]
content(D, "turkey", "Türkiye bağlamı", "Hukuk da saati başlatıyor",
        cards_row(items, top=320, height=360, accents=[V2, P2, T2], pad="32px 34px")
        + callout(720, "72 saat, olay fark edildiğinde başlar. Kimin karar vereceği, kimin arayacağı ve hangi bilginin toplanacağı olaydan önce yazılmalıdır.", label="Pratikte", icon="Clock", build="rise 4 auto"),
        ill="clock",
        notes="""Türkiye bağlamı, kısaca. 7545 sayılı Siber Güvenlik Kanunu 19 Mart 2025'te Resmî Gazete'de yayımlandı; siber güvenlik yükümlülüklerini kanun düzeyine taşıdı.
KVKK açısından: Kurul'un 2019/10 sayılı kararına göre kişisel veri ihlali gecikmeksizin ve en geç 72 saat içinde bildirilir. Sağlık ve genetik veri özel nitelikli kişisel veri.
Ana mesaj: 72 saat kısa. Kim karar veriyor, kim arıyor, hangi bilgi toplanıyor? Bunu yarın Dr. Müjdeci'nin masa başı tatbikatında deneyeceğiz.""")

# 25 ── Monday morning
STEPS = [("Smartphone", "Kurumsal e-posta ve hesaplarınızda MFA’yı açın."), ("ClipboardList", "Laboratuvarınızdaki cihaz bilgisayarlarının listesini çıkarın."),
         ("HardDrive", "En kritik verinizin çevrimdışı bir kopyasını alın."), ("UserX", "Ayrılan öğrenci ve misafirlerin hesaplarını kapattırın."),
         ("PhoneCall", "Şüpheli bir durumda kimi arayacağınızı yazıp kapıya asın.")]
body = ""
for k, (ic, t) in enumerate(STEPS):
    y = 300 + k * 118
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{y}px;width:1664px;height:100px;display:flex;flex-direction:row;gap:28px;align-items:center;padding:0px 32px;background:{WHITE};border-radius:20px;box-shadow:0 10px 30px rgba(29,37,84,0.08)">'
             f'<p style="width:60px;font-family:{DISPLAY};font-size:44px;font-weight:800;color:{ACC[k % 4] if ACC[k % 4] not in (P2, AMBER, T2) else {P2: PT, AMBER: AMBERT, T2: TT}[ACC[k % 4]]}">{k + 1}</p>'
             f'<x-icon name="{ic}" style="width:40px;height:40px;color:{MUTE}"></x-icon><p style="flex:1;font-size:30px;color:{TEXT}">{t}</p></div>')
content(D, "monday", "Bu hafta", "Pazartesi sabahı için beş adım", body, ill=None,
        illus_html=kapsid_svg(200, 1592, 64, animate=True),
        notes="""Pratik bitiriş: Pazartesi sabahı beş adım. Hiçbiri bütçe istemiyor.
MFA'yı açın; cihaz bilgisayarlarının listesini çıkarın; kritik verinin çevrimdışı kopyasını alın; ayrılan hesapları kapattırın; kimi arayacağınızı yazıp kapıya asın.
Salona: bunlardan hangisi sizin laboratuvarınızda zaten var? El kaldırma ile hızlı bir yoklama yapın.""")


# 26 ── takeaways + bridge
@dark("takeaways", """Üç çıkarım. Bir: üniversite laboratuvarları değerli olduğu için hedef; açıklık bir zayıflık değil ama yönetilmesi gereken bir risk. İki: vakaların çoğu aynı kapılardan giriyor: parola, yamasız cihaz, kapatılmamış hesap. Üç: erken halkayı kırmak yeter.
Günün akışı: 15:30'da Doç. Dr. Taşkıran ile araştırma güvenliği. Yarın 13:00'te Alıştırma 3'te MFA ve donanım anahtarlarını kendi hesaplarınızda kuracağız; telefonunuzu ve dizüstü bilgisayarınızı getirin.""", glow=(V2, P2))
def _(i, n):
    s = eyebrow("Üç çıkarım", 210)
    TK = [("Değer hedef çeker.", "Açıklık bir zayıflık değil; yönetilmesi gereken bir risk.", T2),
          ("Kapılar az, hep aynı.", "Parola, yamasız cihaz, kapatılmamış hesap.", P1),
          ("Erken halkayı kırın.", "MFA, envanter ve yedek zincirin başında durur.", AMBER)]
    for k, (a, b, c) in enumerate(TK):
        s += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{280 + k * 150}px;width:1100px;display:flex;flex-direction:column;gap:8px">'
              f'<p style="font-family:{DISPLAY};font-size:54px;font-weight:800;letter-spacing:-1.5px;color:{c}">{a}</p><p style="font-size:30px;color:{SKY}">{b}</p></div>')
    nx = [("BUGÜN · 15:30", "Araştırma güvenliği", "Doç. Dr. Ahmet Şevki Taşkıran"), ("YARIN · 13:00", "Alıştırma 3: MFA ve anahtarlar", "Telefon ve dizüstü bilgisayar getirin")]
    for k, (a, b, c) in enumerate(nx):
        s += (f'<div data-build-in="fade {k + 4} auto" style="position:absolute;left:1300px;top:{290 + k * 250}px;width:492px;display:flex;flex-direction:column;gap:10px;padding:30px 34px;background:{INK2};border-radius:22px;border-left:8px solid {[T2, AMBER][k]}">'
              f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{[T2, AMBER][k]}">{a}</p>' + H(b, 32, CREAM) + P(c, 26, SKY) + "</div>")
    return s


# 27 ── references
refs(D, "refs", [
    "Murch RS, So WK, Buchholz WG, Raman S, Peccoud J. Cyberbiosecurity: an emerging new discipline to help safeguard the bioeconomy. <i>Front Bioeng Biotechnol</i>. 2018;6:39. doi:10.3389/fbioe.2018.00039",
    "Richardson LC, Connell ND, Lewis SM, Pauwels E, Murch RS. Cyberbiosecurity: a call for cooperation in a new threat landscape. <i>Front Bioeng Biotechnol</i>. 2019;7:99. doi:10.3389/fbioe.2019.00099",
    "Millett K, dos Santos E, Millett PD. Cyber-biosecurity risk perceptions in the biotech sector. <i>Front Bioeng Biotechnol</i>. 2019;7:136. doi:10.3389/fbioe.2019.00136",
    "Puzis R, Farbiash D, Brodt O, Elovici Y, Greenbaum D. Increased cyber-biosecurity for DNA synthesis. <i>Nat Biotechnol</i>. 2020;38(12):1379–1381. doi:10.1038/s41587-020-00761-y",
    "National Institute of Standards and Technology. The NIST Cybersecurity Framework (CSF) 2.0. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "UK NCSC. Advisory: APT29 targets COVID-19 vaccine development. 16 Temmuz 2020. · CISA. ICSMA-23-117-01, Illumina Universal Copy Service. 27 Nisan 2023.",
    "ABD Adalet Bakanlığı. Basın açıklaması: iki kişi COVID-19 araştırmasını hedef almakla suçlandı. 21 Temmuz 2020. · ABD Ohio Güney Bölgesi Savcılığı. Hastane araştırmacısına ticari sır davasında hapis cezası. 1 Şubat 2021.",
    "UCSF. Ransomware olayına ilişkin kamu açıklaması. 26 Haziran 2020. · EMA. Siber saldırı açıklamaları. 9 Aralık 2020 ve 15 Ocak 2021.",
    "7545 sayılı Siber Güvenlik Kanunu. Resmî Gazete 32846, 19 Mart 2025. · KVK Kurulu Kararı 2019/10, veri ihlali bildirimi. · UK NPSA ve NCSC. Trusted Research rehberi.",
], size=24)

# 28 ── thanks
thanks(D, "thanks", "Sorularınızı bekliyorum. Yarın 13:00’te Alıştırma 3’te görüşmek üzere: telefonunuzu ve dizüstü bilgisayarınızı getirmeyi unutmayın.",
       """Soru-cevap. Zaman kalırsa salona sorun: bugün anlatılan beş adımdan hangisi en zor? Cevaplar yarınki alıştırmalar için iyi bir giriş olur.""")

SECTIONS = {"s1": {"description": "Neden hedefiz?", "start": "cover"}, "s2": {"description": "Vakalar", "start": "k-cases"},
            "s3": {"description": "Saldırının anatomisi", "start": "k-chain"}, "s4": {"description": "Savunma", "start": "k-def"},
            "s5": {"description": "Kapanış", "start": "takeaways"}}

if __name__ == "__main__":
    out = sys.argv[1]
    slides = D.render()
    write_deck(out, "Biyoteknolojiyi Siber Hırsızlıktan Korumak · Sivas 2026", SECTIONS, slides)
    print("ok", len(slides))
