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

# 8 ── four cases, one glance (shortened)
TXC = {P2: PT, AMBER: AMBERT, T3: TT, T2: TT}
CASES = [("c-ucsf", "UCSF · 2020", "Fidye", "Tıp fakültesi sunucuları şifrelendi; veriye dönmek için yaklaşık 1,14 milyon dolar ödendi.", "Çevrimdışı ve denenmiş yedek.", P2),
         ("c-ema", "EMA · 2020", "Değiştirilen belge", "Aşı başvurusu belgeleri çalındı; bir kısmı değiştirilerek internette yayımlandı.", "İmzalı, sürümlü kayıt.", T3),
         ("c-ohio", "Ohio · 2008–2018", "İçeriden hırsızlık", "Bir hastane araştırmacısı exozom araştırmasına ait ticari sırları çaldı; 30 ay hapis.", "Ayrılışta erişim aynı gün kapanır.", V2),
         ("c-illu", "Illumina · 2023", "Cihaz açığı", "Dizileme cihazlarının kontrol yazılımında 10 üzerinden 10 önem puanlı açık.", "Cihaz bilgisayarı da yamalanır.", AMBER)]
body = ""
for k, (cid, when, t, d_, lesson, c) in enumerate(CASES):
    x = 128 + k * 422
    body += (f'<div id="{cid}" data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:300px;width:398px;height:470px;{card_style(c, pad="30px 30px", gap=14)}">'
             f'<p style="font-family:{MONO};font-size:24px;font-weight:600;color:{TXC.get(c, c)}">{when}</p>' + H(t, 32)
             + P(d_, 25, BODY2, lh=1.38) + '<div style="flex:1"></div>'
             + f'<div style="display:flex;flex-direction:row;gap:12px;align-items:center;padding-top:14px;border-top:2px solid {LINE}">'
             + f'<x-icon name="Verified" style="width:32px;height:32px;color:{TXC.get(c, c)}"></x-icon><p style="flex:1;font-size:24px;font-weight:600;line-height:1.3;color:{TEXT}">{lesson}</p></div></div>')
body += src("Kaynaklar: UCSF açıklaması, 26 Haziran 2020 · EMA açıklamaları, 9 Aralık 2020 ve 15 Ocak 2021 · ABD Ohio Güney Bölgesi Savcılığı, 1 Şubat 2021 · CISA ICSMA-23-117-01, 27 Nisan 2023.", top=830)
content(D, "cases", "Vakalar · kısa", "Dört vaka, dört ders", body, ill="layers",
        notes="""Vakaları kısa geçiyoruz; hepsi yurt dışından ama dersleri bizim laboratuvarlarımız için de geçerli. Kartlar tıkladıkça açılıyor; her birinde yalnız alttaki dersi vurgulayın.
UCSF, Haziran 2020: fidye yazılımı tıp fakültesi sunucularını şifreledi; üniversite yaklaşık 1,14 milyon dolar ödediğini açıkladı. Ders: çevrimdışı ve denenmiş yedek.
EMA, Aralık 2020: Avrupa İlaç Ajansı'ndan aşı başvurusu belgeleri çalındı; Ocak 2021'de EMA, bazı yazışmaların yayımlanmadan önce değiştirildiğini açıkladı. Ders: bütünlük; hangi sürümün gerçek olduğunu kanıtlayabilmek.
Ohio: Nationwide Children's Hospital araştırma enstitüsünde 2008–2018 arasında çalışan bir araştırmacı exozom araştırmasına ait ticari sırları çaldı; 1 Şubat 2021'de 30 ay hapis cezası aldı. Ders: ayrılış süreci.
Illumina, Nisan 2023: CISA, dizileme cihazlarının kontrol yazılımında önem puanı 10 olan bir açık duyurdu. Ders: cihaz bilgisayarı da bir sunucudur.
Bir sonraki slaytta bu dört vakayı üç değere yerleştireceğiz.""")

# 9 ── CIA triad (magic move from the four cards)


def chip(cid, text, c, x, y, w):
    return (f'<div id="{cid}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:96px;display:flex;flex-direction:row;align-items:center;gap:16px;padding:0px 26px;'
            f'background:{WHITE};border-radius:18px;border-left:8px solid {c};box-shadow:0 10px 30px rgba(29,37,84,0.09)">'
            f'<p style="font-family:{DISPLAY};font-size:28px;font-weight:700;letter-spacing:-0.5px;color:{INK}">{text}</p></div>')


CH = {"c-apt": ("APT29 · aşı araştırması", V2), "c-ohio": ("Ohio · ticari sır", V2), "c-ema": ("EMA · değiştirilen belge", T3),
      "c-ucsf": ("UCSF · fidye", P2), "c-illu": ("Illumina · cihaz açığı", AMBER)}
COLS = [("Gizlilik", "Bilgi yetkisiz kişilere geçti", V2, ["c-apt", "c-ohio"]), ("Bütünlük", "Bilgi fark ettirmeden değişti", T3, ["c-ema"]),
        ("Erişilebilirlik", "Bilgiye ulaşılamadı", P2, ["c-ucsf"])]
body = ""
for k, (t, sub, c, ids) in enumerate(COLS):
    x = 128 + k * 564
    body += (f'<div data-build-in="fade 1 auto" style="position:absolute;left:{x}px;top:300px;width:536px;display:flex;flex-direction:column;gap:8px">'
             f'<p style="font-family:{DISPLAY};font-size:44px;font-weight:800;letter-spacing:-1px;color:{c if c != P2 else PT}">{t}</p><p style="font-size:26px;color:{BODY2}">{sub}</p></div>')
    for j, cid in enumerate(ids):
        body += chip(cid, CH[cid][0], CH[cid][1], x, 430 + j * 120, 536)
body += chip("c-illu", CH["c-illu"][0], CH["c-illu"][1], 1256, 550, 536)
body += f'<p data-build-in="fade 2 auto" style="position:absolute;left:1256px;top:666px;width:536px;font-size:26px;line-height:1.38;color:{AMBERT};font-weight:600">Yamasız cihaz üçünü birden tehdit eder.</p>'
body += callout(760, "Gizlilik, bütünlük, erişilebilirlik: laboratuvar verisinin üç değeri. Her kontrolü, hangisini koruduğunu sorarak seçin.", label="Çerçeve", icon="Activity", build="rise 3 auto")
content(D, "triad", "Ara toplam", "Beş örnek, üç değer", body, ill="layers", transition="magic",
        notes="""Kartlar yerine oturdu: bilgi güvenliğinin üç temel değeri. Açılıştaki APT29 da burada.
Gizlilik: APT29 ve Ohio, bilgi yanlış ellere geçti. Bütünlük: EMA, bilgi değişti. Erişilebilirlik: UCSF, bilgiye ulaşılamadı. Illumina açığı üçünü birden tehdit ediyor.
Laboratuvar diliyle: veri sızmasın, değişmesin, kaybolmasın.
Şimdi asıl soruya geçiyoruz: saldırgan içeri nasıl giriyor? Cevabın çoğu zaman bir insan olduğunu göreceğiz.""")

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
Son cümle önemli: erken bir halkayı kırmak yeter. İkinci halka, ilk erişim, çoğu zaman bir insandan geçer; şimdi ona bakıyoruz.""")


# ═══ Sosyal mühendislik bölümü ═══
# SE-1 kinetic
kinetic(D, "k-social", "Sosyal mühendislik", [("TIKLA.", None), ("ONAYLA.", T2), ("SÖYLE.", None), ("GÖNDER.", P2)],
        """Kinetik ara slayt. Saldırı zincirinin ikinci halkası, ilk erişim, çoğu zaman bir yazılım açığından değil bir insandan geçer.
Dört fiil: bir bağlantıya tıkla, bir bildirimi onayla, bir kodu söyle, bir dosyayı gönder. Sosyal mühendislik bu dört fiilden birini yaptırma sanatıdır.
Salona sorun: son bir ayda şüpheli bir e-posta, SMS ya da WhatsApp mesajı alan elini kaldırsın. Genellikle salonun çoğu kaldırır.""", size=160)


# SE-2 numbers
@dark("se-stat", """İki sayı. Verizon'un her yıl yayımladığı Veri İhlali Soruşturmaları Raporu'nun 2025 baskısına göre ihlallerin yaklaşık yüzde 60'ında insan unsuru var: biri tıklıyor, biri onaylıyor, biri yanlış kişiye gönderiyor ya da kandırılıyor.
FBI'ın İnternet Suçları Şikâyet Merkezi'nin 2024 raporuna göre yalnız iş e-postası dolandırıcılığından, yani yönetici ya da tedarikçi taklidiyle ödeme yaptırmaktan bildirilen kayıp yaklaşık 2,8 milyar dolar.
Mesaj: en pahalı açık, bir insanın iyi niyeti. Bu yüzden savunmanın da bir kısmı insanda.""", glow=(P2, V2))
def _(i, n):
    s = eyebrow("Sosyal mühendislik · neden önemli?", 200)
    s += emb("counter", 128, 260, 640, 240, PAL, to=60, size=220, fg=CREAM, pre="~%")
    s += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:500px;width:740px;font-family:{DISPLAY};font-size:40px;font-weight:700;line-height:1.15;color:{P1}">ihlalde insan unsuru var</p>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:610px;width:740px;font-size:28px;line-height:1.42;color:{SKY}">Biri tıklıyor, biri onaylıyor, biri yanlış kişiye gönderiyor ya da kandırılıyor.</p>'
    s += (f'<div data-build-in="rise 3 auto" style="position:absolute;left:1000px;top:290px;width:792px;display:flex;flex-direction:column;gap:16px;padding:40px 44px;background:{INK2};border-radius:22px;border-top:6px solid {AMBER}">'
          f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{AMBER}">İŞ E-POSTASI DOLANDIRICILIĞI · 2024</p>'
          f'<p style="font-family:{DISPLAY};font-size:96px;font-weight:800;letter-spacing:-3px;line-height:1;color:{CREAM}">2,8 <span style="font-size:48px;color:{AMBER}">milyar $</span></p>'
          + P("Yönetici ya da tedarikçi taklidiyle yaptırılan ödemelerden FBI’a bildirilen kayıp.", 28, SKY, lh=1.4) + "</div>")
    s += src("Kaynaklar: Verizon, 2025 Data Breach Investigations Report (Nisan 2025) · FBI IC3, 2024 Internet Crime Report (Nisan 2025).", top=880, dark=True)
    return s


# SE-3 levers
LV = [("Warning", "Aciliyet", "“24 saat içinde doğrulamazsanız hesabınız kapatılacak.”", P2),
      ("GraduationCap", "Otorite", "“Rektörlük adına yazıyorum, toplantıdayım.”", V2),
      ("Lock", "Korku", "“Hesabınızdan şüpheli giriş tespit edildi.”", AMBER),
      ("Search", "Merak", "“2026_maas_tablosu.xlsx ektedir.”", T3),
      ("Users", "Yardımseverlik", "“Hocam acil bir işim var, müsait misiniz?”", V1),
      ("Trust", "Tanıdıklık", "Bildik bir logo, bir meslektaşın adı, bir kongre.", T2)]
items = [f'<div style="display:flex;flex-direction:row;gap:16px;align-items:center">{icon(ic, 40, TXC.get(c, c))}{H(t, 32, lh=1.15, extra="flex:1;")}</div>'
         + P(q, 27, BODY2, lh=1.38, extra="font-style:italic;") for ic, t, q, c in LV]
content(D, "se-levers", "Sosyal mühendislik · psikoloji", "Altı psikolojik kaldıraç",
        cards_row(items, top=320, n=3, height=200, row_gap=22, gap=22, accents=[c for *_, c in LV], pad="26px 30px", kind="pop")
        + callout(780, "Bir mesaj sizi acele ettiriyorsa, durmak için en iyi andır.", label="Kural", icon="Clock", build="rise 8 auto"),
        ill="phish",
        notes="""Sosyal mühendislik teknik değil, psikolojik bir saldırı. Altı kaldıraç kullanır; kartlar tıkladıkça açılıyor.
Aciliyet: düşünme süresini elinizden alır. Otorite: itiraz etmeyi zorlaştırır; "Rektörlük adına", "Dekan Bey toplantıda". Korku: hesabınız, maaşınız, itibarınız. Merak: maaş tablosu, sınav sonuçları, "sizin hakkınızda bir şikâyet". Yardımseverlik: akademide çok güçlü; meslektaşa yardım etmek refleks. Tanıdıklık: bildik logo, bildik ad.
Tek kural: bir mesaj sizi acele ettiriyorsa, durmak için en iyi an odur. Salona sorun: size en çok hangisi işler?""")

# SE-4 channels
CHN = [("PaperPlane", "E-posta", "Sahte BT duyurusu, kargo, fatura, paylaşılan belge bildirimi.", V2),
       ("Chat", "SMS ve WhatsApp", "Kargo, banka ya da kurum taklidi; yöneticiden “acil” mesaj.", P2),
       ("Users", "Telefon", "“Bilgi işlemden arıyorum, telefonunuza gelen kodu okur musunuz?”", AMBER),
       ("Key", "MFA yorgunluğu", "Gece arka arkaya gelen giriş onayları; bıkıp “onayla”ya basılması beklenir.", T3),
       ("Search", "QR kod", "Afiş ya da e-postadaki karekod sizi sahte giriş sayfasına götürür.", V1),
       ("Home", "Fiziksel", "Kapıda arkanızdan giren “servis elemanı”, koridorda bulunan USB bellek.", T2)]
items = [f'<div style="display:flex;flex-direction:row;gap:16px;align-items:center">{icon(ic, 40, TXC.get(c, c))}{H(t, 30, lh=1.15, extra="flex:1;")}</div>'
         + P(d_, 25, BODY2, lh=1.38) for ic, t, d_, c in CHN]
content(D, "se-channels", "Sosyal mühendislik · kanallar", "Yalnız e-posta değil",
        cards_row(items, top=320, n=3, height=210, row_gap=22, gap=22, accents=[c for *_, c in CHN], pad="26px 30px", kind="pop")
        + callout(790, "Kanal değişir, istek aynıdır: bir parola, bir kod, bir onay, bir ödeme ya da bir dosya.", label="Ortak nokta", icon="Lightbulb", build="rise 8 auto"),
        ill="network",
        notes="""Altı kanal. E-posta hâlâ en yaygını ama tek değil.
SMS ve WhatsApp: kargo, banka ya da kurum taklidi; bir yöneticinin adıyla gelen "acil" mesaj. Telefon: sesli dolandırıcılık; "bilgi işlemden arıyorum" ya da "cihaz servisinden arıyorum".
MFA yorgunluğu: parolanızı ele geçiren saldırgan gece arka arkaya giriş onayı gönderir, birinde "onayla"ya basmanızı bekler. Beklemediğiniz bir onayı asla onaylamayın.
QR kod: e-posta filtrelerini atlattığı için giderek yaygın. Fiziksel: kapıda arkanızdan giren biri, koridorda "bulunan" bir USB bellek.
Ortak nokta: istenen şey hep aynı beş şeyden biri.""")


# SE-5 spot the phish: e-mail
def flag(k, x, y, w, t, sub, c=P2):
    return (f'<div data-build-in="pop {k + 1} auto" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;display:flex;flex-direction:row;gap:18px;align-items:center">'
            f'<p style="width:52px;height:52px;border-radius:26px;background:{c};color:#FFFFFF;font-family:{DISPLAY};font-size:26px;font-weight:800;text-align:center;line-height:52px">{k + 1}</p>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:27px;font-weight:700;color:{TEXT}">{t}</p><p style="font-size:24px;line-height:1.3;color:{BODY2}">{sub}</p></div></div>')


def pin_dot(k, x, y):
    return f'<p data-build-in="pop {k + 1} auto" style="position:absolute;left:{x}px;top:{y}px;width:44px;height:44px;border-radius:22px;background:{P2};color:#FFFFFF;font-family:{DISPLAY};font-size:24px;font-weight:800;text-align:center;line-height:44px">{k + 1}</p>'


mail = (f'<div style="position:absolute;left:128px;top:290px;width:960px;height:600px;display:flex;flex-direction:column;background:{WHITE};border-radius:22px;box-shadow:0 18px 50px rgba(29,37,84,0.14);overflow:hidden">'
        f'<div style="display:flex;flex-direction:row;gap:12px;align-items:center;padding:18px 28px;background:{PAPER2}">'
        + "".join(f'<div style="width:16px;height:16px;border-radius:8px;background:{c}"></div>' for c in (P1, AMBER, T2))
        + f'<p style="flex:1;font-family:{MONO};font-size:24px;color:{MUTE};text-align:center">Gelen kutusu</p></div>'
        f'<div style="display:flex;flex-direction:column;gap:10px;padding:26px 36px;border-bottom:2px solid {LINE}">'
        f'<p style="font-size:26px;color:{TEXT}"><b>Bilgi İşlem Daire Başkanlığı</b> <span style="color:{MUTE}">&lt;destek@posta-guvenlik.net&gt;</span></p>'
        f'<p style="font-family:{DISPLAY};font-size:32px;font-weight:700;color:{INK}">[ACİL] E-posta hesabınız 24 saat içinde kapatılacak</p></div>'
        f'<div style="display:flex;flex-direction:column;gap:20px;padding:28px 36px">'
        f'<p style="font-size:26px;line-height:1.45;color:{TEXT}">Sayın kullanıcı,</p>'
        f'<p style="font-size:26px;line-height:1.45;color:{TEXT}">Posta kutunuz kapasite sınırını aştı. Hesabınızın kapatılmaması için 24 saat içinde kullanıcı adı ve şifrenizle doğrulama yapınız.</p>'
        f'<p style="width:330px;padding:16px 26px;border-radius:12px;background:{V2};color:#FFFFFF;font-size:26px;font-weight:700;text-align:center">Hesabımı doğrula</p>'
        f'<p style="font-family:{MONO};font-size:24px;color:{MUTE}">hesap-dogrula.posta-guvenlik.net/giris</p></div></div>')
body = mail
FL = [("Gönderen adresi", "Ad kurum adı, adres kurumun alan adı değil."), ("Aciliyet ve tehdit", "“24 saat içinde”, “kapatılacak”."),
      ("Adınız yok", "“Sayın kullanıcı”: toplu gönderim."), ("Şifre isteniyor", "Bilgi işlem şifrenizi e-postayla istemez."),
      ("Bağlantı başka yere gidiyor", "Üzerine gelin, tıklamayın: adres kurumunuz değil.")]
for k, (t, sub) in enumerate(FL):
    body += flag(k, 1140, 296 + k * 118, 652, t, sub)
for k, (x, y) in enumerate([(1050, 360), (1050, 420), (1050, 520), (1050, 600), (1050, 790)]):
    body += pin_dot(k, x, y)
content(D, "se-mail", "Gerçek mi, oltalama mı? · 1", "Beş işaret, tek e-posta", body, ill=None,
        notes="""Etkileşimli slayt. Önce yalnız e-postayı gösterin ve salona sorun: bu e-postada kaç uyarı işareti var? Birkaç cevap alın, sonra tıklayarak işaretleri tek tek açın.
Bir: gönderenin adı kurumsal, adresi değil. İki: aciliyet ve tehdit, 24 saat, kapatılacak. Üç: adınız yok, "Sayın kullanıcı". Dört: şifre isteniyor; bilgi işlem şifrenizi asla e-postayla istemez. Beş: bağlantının gittiği adres kurumunuz değil; fareyle üzerine gelip adresi okuyun, tıklamayın.
Bu e-posta ve adresleri eğitim için uydurulmuştur.""")


# SE-6 spot the phish: chat + call + MFA (dark)
@dark("se-chat", """İkinci örnek: e-posta dışındaki kanallar. Üç sahne, üç kurgusal örnek.
Sol: tanımadığınız bir numaradan, profil fotoğrafı ve adıyla bir yöneticiniz gibi görünen WhatsApp mesajı. Önce "müsait misiniz", sonra acil bir ödeme ya da hediye kartı. Bu, iş e-postası dolandırıcılığının mesajlaşma sürümü. Doğrulama: yöneticinizi bildiğiniz numaradan arayın.
Orta: cihaz servisinden aradığını söyleyen biri, telefonunuza gelen doğrulama kodunu istiyor. O kod, birinin şu anda sizin hesabınıza girmeye çalıştığının kanıtıdır. Kod kimseyle paylaşılmaz.
Sağ: gece 02:14'ten itibaren arka arkaya gelen giriş onayları. Siz giriş yapmıyorsanız, biri parolanızı biliyor demektir. Reddedin, parolanızı değiştirin, bilgi işleme bildirin.""", glow=(P2, T2))
def _(i, n):
    s = eyebrow("Gerçek mi, oltalama mı? · 2", 190)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:236px;width:1600px;font-family:{DISPLAY};font-size:60px;font-weight:800;letter-spacing:-1.5px;line-height:1.05;color:{CREAM}">Üç kanal, aynı oyun</h2>'

    def panel(x, title, c, inner, k):
        return (f'<div data-build-in="rise {k} auto" style="position:absolute;left:{x}px;top:340px;width:530px;height:560px;display:flex;flex-direction:column;gap:16px;padding:28px 28px;background:{INK2};border-radius:24px;border-top:6px solid {c}">'
                f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{c}">{tr_upper(title)}</p>{inner}</div>')

    def bubble(t, mine=False):
        bg, fg = (T3, "#FFFFFF") if mine else ("#F2F4FF", INK)
        al = "flex-end" if mine else "flex-start"
        return f'<p style="align-self:{al};width:400px;padding:14px 18px;border-radius:18px;background:{bg};color:{fg};font-size:24px;line-height:1.32">{t}</p>'

    wa = (f'<div style="display:flex;flex-direction:row;gap:14px;align-items:center"><div style="width:52px;height:52px;border-radius:26px;background:{V1}"></div>'
          f'<div style="display:flex;flex-direction:column"><p style="font-size:26px;font-weight:700;color:{CREAM}">Bölüm Başkanı</p><p style="font-size:24px;color:{SKY}">+90 5•• ••• •• •• · kayıtlı değil</p></div></div>'
          + bubble("Merhaba hocam, toplantıdayım, konuşamıyorum. Müsait misiniz?")
          + bubble("Bugün yetişmesi gereken bir ödeme var. 5 adet hediye kartı alıp kodlarını buraya yazar mısınız? Yarın öderim."))
    call = (f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px;padding:14px 0px">'
            f'<div style="width:96px;height:96px;border-radius:48px;background:{AMBER}"></div>'
            f'<p style="font-size:30px;font-weight:700;color:{CREAM}">Gelen arama</p><p style="font-size:24px;color:{SKY}">“Cihaz servisinden arıyorum”</p></div>'
            + bubble("Uzaktan bağlanmam için telefonunuza gelen 6 haneli kodu okur musunuz? Bir dakikalık iş."))
    mfa = "".join(f'<div style="display:flex;flex-direction:row;gap:14px;align-items:center;padding:14px 18px;border-radius:16px;background:#F2F4FF">'
                  f'<x-icon name="Key" style="width:32px;height:32px;color:{V2}"></x-icon><p style="flex:1;font-size:24px;color:{INK}"><b>02:{14 + j:02d}</b> Girişi onaylıyor musunuz?</p></div>' for j in range(4))
    s += panel(128, "WhatsApp", P1, wa, 2) + panel(695, "Telefon", AMBER, call, 3) + panel(1262, "MFA bildirimi", T2, mfa, 4)
    s += src("Mesajlar eğitim amaçlı kurgudur. Doğrulama her zaman ikinci, bildiğiniz bir kanaldan yapılır.", top=930, dark=True)
    return s


# SE-7 academia-specific bait
AC = [("Book", "Sahte dergi ve kongre", "Davet, hızlı yayın, “makale yükleme” sayfasında kurum şifresi.", V2),
      ("Star", "Hakem ve editör daveti", "Tanınmış bir dergi adıyla gelen bağlantı, sahte giriş sayfasına gider.", P2),
      ("Users", "“Ortak çalışalım”", "İlgili görünen bir araştırmacı yayımlanmamış veriyi, protokolü, numuneyi ister.", AMBER),
      ("Globe", "Profesyonel ağlar", "Sahte profil önce sohbet eder, sonra danışmanlık ya da gezi teklif eder.", T3)]
items = [icon(ic, 46, TXC.get(c, c)) + H(t, 30, lh=1.18) + P(d_, 25, BODY2, lh=1.38) for ic, t, d_, c in AC]
content(D, "se-academic", "Sosyal mühendislik · akademi", "Akademisyene özel yemler",
        cards_row(items, top=320, height=360, accents=[c for *_, c in AC], pad="30px 30px")
        + callout(720, "İngiltere’de MI5, bir yılda profesyonel ağlarda 10.000’i aşkın gizlenmiş yaklaşım gördüğünü açıkladı (CPNI, Mayıs 2022).", label="Ölçek", icon="Search", build="rise 5 auto"),
        ill="eye",
        notes="""Akademisyene özel yemler. Saldırgan bizim günlük işimizi bilir ve onu taklit eder.
Sahte dergi ve kongre davetleri: çoğu yalnız para ister, bazıları "makale yükleme" sayfasında kurum şifrenizi ister. Hakem ve editör davetleri: tanınmış bir dergi adı, sahte bir giriş sayfası.
"Ortak çalışalım": ilgili görünen bir araştırmacı, iş birliği bahanesiyle yayımlanmamış veri, protokol ya da numune ister. Bu, sabahki araştırma güvenliği konusuyla doğrudan bağlantılı.
Profesyonel ağlar: İngiltere'nin altyapı güvenliği kurumu CPNI, 2022'de "Think Before You Link" kampanyasını duyururken MI5'ın bir yılda bu ağlarda 10.000'i aşkın gizlenmiş yaklaşım gördüğünü açıkladı. Sahte profil önce sohbet eder, sonra danışmanlık, rapor ya da gezi teklif eder.""")


# SE-8 defence: stop · think · verify
SD = [("01", "Dur", "Aciliyet, tehdit ya da beklenmedik bir istek: yavaşlama işaretidir.", P2),
      ("02", "Doğrula", "Bildiğiniz numaradan arayın ya da kurum sayfasına kendiniz girin. Mesajdaki bağlantı ve numarayı kullanmayın.", V2),
      ("03", "Paylaşma", "Parola, doğrulama kodu ve beklenmedik bir onay hiçbir kanaldan verilmez.", AMBER),
      ("04", "Bildir", "Tıkladıysanız da bildirin. Erken bildirim zararı küçültür; bildiren suçlanmaz.", T3)]
items = [numcard(a, t, d_, TXC.get(c, c)) for a, t, d_, c in SD]
content(D, "se-defence", "Sosyal mühendislik · savunma", "Dur, doğrula, paylaşma, bildir",
        cards_row(items, top=320, height=380, accents=[c for *_, c in SD], pad="30px 30px")
        + callout(740, "Oltalamaya dayanıklı MFA, kandırılan bir anın bedelini küçültür: parola çalınsa da hesap açılmaz.", label="Teknik destek", icon="Key", build="rise 5 auto"),
        ill="shield",
        notes="""Savunma dört kelime. Dur: acele ettiren her mesaj yavaşlama işaretidir. Doğrula: bildiğiniz numarayı arayın, kurum sayfasına kendiniz girin; mesajdaki bağlantıyı ve numarayı kullanmayın. Paylaşma: parola, kod ve beklenmedik onay hiçbir kanaldan verilmez. Bildir: tıkladıysanız bile bildirin.
Son nokta en önemlisi: bildiren suçlanmaz. Utandığı için susan kişi, saldırgana saatler kazandırır.
Teknik destek de var: oltalamaya dayanıklı MFA, kandırıldığınız anda bile hesabınızı korur. Altı kontrolün ilki bu.""")


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
Bir: oltalamaya dayanıklı MFA; mümkünse donanım anahtarı ya da geçiş anahtarı. İki: envanter ve yama; listede olmayan cihazı koruyamazsınız. Üç: cihaz bilgisayarları ayrı ağ bölümünde. Dört: en az yetki ve ayrılış süreci, Ohio vakasının dersi. Beş: 3-2-1 yedek ve denenmiş geri yükleme, UCSF'nin dersi. Altı: bildirim kültürü; bildiren teşekkür alır, suçlanmaz.""")

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
Ana mesaj: 72 saat kısa. Kim karar veriyor, kim arıyor, hangi bilgi toplanıyor? Bunu yarın sabahki politikalar ve SOP oturumundaki masa başı tatbikatta deneyeceğiz.""")

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
@dark("takeaways", """Üç çıkarım. Bir: üniversite laboratuvarları değerli olduğu için hedef; açıklık bir zayıflık değil ama yönetilmesi gereken bir risk. İki: kapıların çoğu insandan geçiyor: bir tıklama, bir onay, bir kod. Üç: erken halkayı kırmak yeter.
Günün akışı: 15:30'da Doç. Dr. Taşkıran ile araştırma güvenliği. Yarın 10:30'da Prof. Merey ile laboratuvar politikaları, SOP'ler ve bir olay müdahalesi masa başı tatbikatı.""", glow=(V2, P2))
def _(i, n):
    s = eyebrow("Üç çıkarım", 210)
    TK = [("Değer hedef çeker.", "Açıklık bir zayıflık değil; yönetilmesi gereken bir risk.", T2),
          ("Kapı çoğu zaman insandır.", "Dur, doğrula, paylaşma, bildir.", P1),
          ("Erken halkayı kırın.", "MFA, envanter ve yedek zincirin başında durur.", AMBER)]
    for k, (a, b, c) in enumerate(TK):
        s += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{280 + k * 150}px;width:1100px;display:flex;flex-direction:column;gap:8px">'
              f'<p style="font-family:{DISPLAY};font-size:54px;font-weight:800;letter-spacing:-1.5px;color:{c}">{a}</p><p style="font-size:30px;color:{SKY}">{b}</p></div>')
    nx = [("BUGÜN · 15:30", "Araştırma güvenliği", "Doç. Dr. Ahmet Şevki Taşkıran"), ("YARIN · 10:30", "Politikalar, SOP’ler ve masa başı tatbikat", "Prof. Dr. Gökçe Merey")]
    for k, (a, b, c) in enumerate(nx):
        s += (f'<div data-build-in="fade {k + 4} auto" style="position:absolute;left:1300px;top:{290 + k * 250}px;width:492px;display:flex;flex-direction:column;gap:10px;padding:30px 34px;background:{INK2};border-radius:22px;border-left:8px solid {[T2, AMBER][k]}">'
              f'<p style="font-family:{MONO};font-size:24px;letter-spacing:2px;font-weight:600;color:{[T2, AMBER][k]}">{a}</p>' + H(b, 32, CREAM) + P(c, 26, SKY) + "</div>")
    return s


# 27 ── references
refs(D, "refs", [
    "Murch RS, So WK, Buchholz WG, Raman S, Peccoud J. Cyberbiosecurity: an emerging new discipline to help safeguard the bioeconomy. <i>Front Bioeng Biotechnol</i>. 2018;6:39. doi:10.3389/fbioe.2018.00039",
    "Salahdine F, Kaabouch N. Social engineering attacks: a survey. <i>Future Internet</i>. 2019;11(4):89. doi:10.3390/fi11040089",
    "National Institute of Standards and Technology. The NIST Cybersecurity Framework (CSF) 2.0. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Verizon. 2025 Data Breach Investigations Report. Nisan 2025. · FBI Internet Crime Complaint Center. 2024 Internet Crime Report. Nisan 2025.",
    "UK Cabinet Office ve CPNI. New app to counter malicious approaches online (Think Before You Link). 17 Mayıs 2022.",
    "UK NCSC. Advisory: APT29 targets COVID-19 vaccine development. 16 Temmuz 2020. · CISA. ICSMA-23-117-01, Illumina Universal Copy Service. 27 Nisan 2023.",
    "UCSF. Ransomware olayına ilişkin kamu açıklaması. 26 Haziran 2020. · EMA. Siber saldırı açıklamaları. 9 Aralık 2020 ve 15 Ocak 2021. · ABD Ohio Güney Bölgesi Savcılığı. 1 Şubat 2021.",
    "7545 sayılı Siber Güvenlik Kanunu. Resmî Gazete 32846, 19 Mart 2025. · KVK Kurulu Kararı 2019/10, veri ihlali bildirimi. · UK NPSA ve NCSC. Trusted Research rehberi.",
], size=24)

# 28 ── thanks
thanks(D, "thanks", "Sorularınızı bekliyorum. Bu akşam ilk adım olarak kurumsal hesabınızda çok faktörlü doğrulamayı açın.",
       """Soru-cevap. Zaman kalırsa salona sorun: bugün anlatılan beş adımdan hangisi en zor? Cevaplar yarınki masa başı tatbikat için iyi bir giriş olur.""")

SECTIONS = {"s1": {"description": "Neden hedefiz?", "start": "cover"}, "s2": {"description": "Vakalar", "start": "cases"},
            "s3": {"description": "Saldırının anatomisi", "start": "k-chain"}, "s6": {"description": "Sosyal mühendislik", "start": "k-social"},
            "s4": {"description": "Savunma", "start": "exfil"},
            "s5": {"description": "Kapanış", "start": "takeaways"}}

if __name__ == "__main__":
    out = sys.argv[1]
    slides = D.render()
    write_deck(out, "Biyoteknolojiyi Siber Hırsızlıktan Korumak · Sivas 2026", SECTIONS, slides)
    print("ok", len(slides))
