"""Deck S5 · Alıştırma 1: Laboratuvar varlık haritalama ve risk belirleme (1. Gün 13:00–14:30).
Küçük grup çalışması için yönlendirme sunumu: kurulum, üç sayaçlı tur, paylaşım, kapanış."""
import sys
import scommon
from scommon import *

scommon.SPEAKER = "Prof. Dr. Gökçe Merey · Prof. Dr. Ahmet Altun"
scommon.AFFIL = "Kolaylaştırıcılar · küçük grup çalışması"

TITLE = "Alıştırma 1 · Varlık haritası ve riskler · Sivas 2026"
D = Deck(TITLE)
TX = {P2: PT, AMBER: AMBERT, T3: TT, T2: TT}


def dark(sid, notes, transition="fade", glow=(T2, V2)):
    def wrap(body):
        def f(i, n):
            inner = progress(i, n, True) + bg_glow(len(sid) * 7, *glow) + body(i, n) + footer(i + 1, True)
            return section(sid, inner, True, transition, notes)
        D.add(sid, f)
        return body
    return wrap


def timed(sid, eyebrow_, title, facts, minutes, notes, glow=(T3, V2), title_size=104):
    """Dark task slide: big title, fact rows, live countdown."""
    def f(i, n):
        s = progress(i, n, True) + bg_glow(len(sid) * 3, *glow)
        s += eyebrow(eyebrow_, 220)
        s += f'<h1 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:280px;width:1020px;font-family:{DISPLAY};font-size:{title_size}px;font-weight:800;letter-spacing:-3px;line-height:1.02;color:{CREAM}">{title}</h1>'
        y0 = 280 + round(title_size * 1.1 * (title.count("<br>") + 1)) + 50
        for k, (ic, t, c) in enumerate(facts):
            s += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{y0 + k * 96}px;width:980px;display:flex;flex-direction:row;gap:22px;align-items:center">'
                  f'<x-icon name="{ic}" style="width:44px;height:44px;color:{c}"></x-icon><p style="flex:1;font-size:32px;line-height:1.3;color:{CREAM}">{t}</p></div>')
        s += emb("countdown", 1180, 230, 600, 600, PAL, min=minutes, cap="kalan süre", done="süre doldu")
        s += footer(i + 1, True)
        return section(sid, s, True, "fade", notes)
    D.add(sid, f)


# 1 cover
cover(D, "cover", "1. Gün · Pazartesi 16 Kasım 2026 · 13:00–14:30",
      [("Alıştırma 1", None), ("Varlık haritası", T2), ("ve riskler", None)],
      "Önce birlikte bir örnek çözüyoruz; sonra iki ekip kendi laboratuvarını haritalıyor.",
      emb("capsid", 1180, 190, 640, 640, PAL, rings=True, intro=True, spin=.35, t1=T1, v1=V1, v3=V3),
      """Öğle arasından dönüş. Oturum üç parça: on dakikalık giriş, kurgusal bir laboratuvar üzerinde birlikte çözeceğimiz bir örnek ve ardından iki ekibin kendi laboratuvarını haritalaması.
Salonda iki tahta ya da iki pano hazır olsun: biri CÜTAM, biri CÜTFAM ekibi için. Her tahtanın yanında kalın kalemler ve beş renk yapışkan not bulunsun.""", size=96)

# 2 kinetic
kinetic(D, "k-list", "Alıştırmanın tek cümlesi", [("LİSTEDE", None), ("YOKSA", None), ("KORUNMUYOR.", T2)],
        """Kinetik açılış. Bugünün tek cümlesi: listede olmayan varlık korunmuyor. Sabah Prof. Merey'in anlattığı risklerin hepsi bir varlığın üzerinde gerçekleşir; önce o varlıkları görmemiz gerekiyor.""",
        size=160)

# 3 what is an asset map
OUT = [("01", "Ne?", "Laboratuvarın çalışması için gereken her şeyin listesi: cihazlar, veriler, hesaplar, insanlar ve bağlantılar.", V2),
       ("02", "Neden?", "Risk değerlendirmesi buradan başlar. Neyimiz olduğunu bilmeden neyin tehlikede olduğunu söyleyemeyiz.", P2),
       ("03", "Çıktı", "Her satırında bir sahip olan bir liste, bir veri akışı ve işaretlenmiş en kritik üç varlık.", AMBER)]
items = [numcard(a, t, d_, TX.get(c, c)) for a, t, d_, c in OUT]
content(D, "outputs", "Giriş", "Varlık haritası nedir?",
        cards_row(items, top=320, height=380, accents=[c for *_, c in OUT], pad="32px 32px")
        + callout(740, "Varlık yalnız cihaz değildir. Bugün en çok unutulan üç şey veri, hesap ve insan olacak.", label="Dikkat", icon="Lightbulb", build="rise 5 auto"),
        ill="checklist",
        notes="""Varlık haritası, laboratuvarın çalışması için gereken her şeyin listesidir. Yalnız cihaz envanteri değildir; veriyi, hesapları, insanları ve bağlantıları da içerir.
Neden yapıyoruz: risk değerlendirmesinin ilk adımı budur. NIST Siber Güvenlik Çerçevesi'nde Tanımla işlevi tam olarak bununla başlar.
Bugünün çıktısı: her satırında bir sahip olan bir liste, bir veri akışı ve işaretlenmiş en kritik üç varlık.""")

# 4 flow
FL = [("10 dk", "Giriş", "Varlık haritası nedir?", V1), ("10 dk", "Örnek laboratuvar", "HALMER’i tanıyalım", V2), ("15 dk", "Örnek çözüm", "Haritalama nasıl yapılır?", P2),
      ("30 dk", "Ekip çalışması", "Kendi laboratuvarınız, tahtada", AMBER), ("20 dk", "Sunum", "Sözcüler anlatıyor", T3), ("5 dk", "Kapanış", "Sonraki adım", T2)]
mins = [10, 10, 15, 30, 20, 5]
bar = "".join(f'<div style="width:{round(1664 * m / 90) - 4}px;height:22px;border-radius:11px;background:{c}"></div>' for m, (*_, c) in zip(mins, FL))
body = f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:300px;width:1664px;height:22px;display:flex;flex-direction:row;gap:4px">{bar}</div>'
items = [f'<p style="font-family:{DISPLAY};font-size:44px;font-weight:800;letter-spacing:-1px;line-height:1;color:{TX.get(c, c)}">{m}</p>' + H(t, 27, lh=1.2) + P(d_, 24, BODY2, lh=1.32)
         for m, t, d_, c in FL]
body += cards_row(items, top=360, n=6, gap=20, height=300, accents=[c for *_, c in FL], pad="26px 24px", build_start=2)
body += callout(720, "İlk 35 dakika birlikte, sonraki 50 dakika sizde: iki ekip, iki tahta, iki sözcü.", label="Düzen", icon="Users", build="rise 9 auto")
content(D, "flow", "Akış", "Altı adım, doksan dakika", body, ill="timeline",
        notes="""Akış. İlk otuz beş dakika birlikte: giriş, kurgusal laboratuvarın tanıtımı ve o laboratuvar üzerinde örnek bir çözüm. Sonraki elli dakika ekiplerde: otuz dakika tahtada çalışma, yirmi dakika sözcülerin sunumu. Son beş dakika kapanış.
En uzun dilim ekip çalışmasına ayrılmış; örnek çözümü uzatmayın.""")

# 5 morph: categories
morph(D, "k-cats", "Beş kategori", [("CİHAZ", T2), ("VERİ", P2), ("HESAP", AMBER), ("İNSAN", None), ("AĞ", T1), ("HARİTA", T2)],
      """Morf ara slaytı: cihaz, veri, hesap, insan, ağ ve hepsi bir arada harita.""",
      size=230, sub="Beş kategori, tek harita.", per=2.6)

# 6 categories
CT = [("Settings", "Cihaz", "Analiz cihazları, cihaz bilgisayarları, dondurucular, depolama cihazları, USB bellekler.", V2),
      ("Database", "Veri", "Ham veri, raporlar, numune kayıtları, yöntem dosyaları, hasta kayıtları, sözleşmeler.", P2),
      ("Key", "Yazılım ve hesap", "Cihaz yazılımları, ortak hesaplar, e-posta, bulut hesapları, uzaktan erişim araçları.", AMBER),
      ("Users", "İnsan ve dış taraf", "Personel, öğrenciler, müşteriler, servis firmaları, temizlik firması, bilgi işlem.", T3),
      ("Globe", "Ağ ve alan", "Yerel ağ, misafir Wi-Fi, ortak sürücü, kapılar, cihaz odaları, dolaplar.", V1)]
items = [icon(ic, 46, TX.get(c, c)) + H(t, 29, lh=1.18) + P(d_, 24, BODY2, lh=1.36) for ic, t, d_, c in CT]
content(D, "cats", "Giriş", "Beş kategoride varlıklar",
        cards_row(items, top=320, n=5, gap=20, height=380, accents=[c for *_, c in CT], pad="28px 26px")
        + callout(740, "Bir şey kaybolduğunda, bozulduğunda ya da başkasının eline geçtiğinde işiniz aksıyorsa o bir varlıktır.", label="Ölçüt", icon="Search", build="rise 6 auto"),
        ill="network",
        notes="""Beş kategori. Cihazlar; veriler; yazılım ve hesaplar; insanlar ve dış taraflar; ağ ve fiziksel alan.
Varlık ölçütü basit: kaybolduğunda, bozulduğunda ya da başkasının eline geçtiğinde işiniz aksıyorsa o bir varlıktır. Bir parola da, bir servis firması da, bir Excel dosyası da bu ölçüte girer.""")


# 7 scenario lab
@dark("lab", """Örnek laboratuvar. HALMER, Halys Üniversitesi Merkezi Araştırma Laboratuvarı; tamamen kurgusal. Halys, Kızılırmak'ın antik adı.
On dört personel, dokuz lisansüstü öğrenci, beş birim. Yılda yaklaşık dört bin iki yüz numune; üçte biri dış müşterilerden. Raporlar e-postayla gidiyor, iki servis firması cihazlara uzaktan bağlanıyor ve son altı ayda üç olay yaşanmış.
Senaryo kartını dağıtın ve okumaları için dört dakika verin. Okurken varlıkların altını çizsinler; birazdan birlikte listeleyeceğiz.""", glow=(V2, P2))
def _(i, n):
    s = eyebrow("Örnek laboratuvar · kurgusal", 190)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:246px;width:1664px;font-family:{DISPLAY};font-size:120px;font-weight:800;letter-spacing:-4px;line-height:1;color:{CREAM}">HAL<span style="color:{T2}">MER</span></h2>'
    s += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:384px;width:1500px;font-size:34px;line-height:1.3;color:{SKY}">Halys Üniversitesi Merkezi Araştırma Laboratuvarı</p>'
    facts = [("Users", "14 personel", "ve 9 lisansüstü öğrenci", T2), ("Activity", "5 birim", "kabul, LC-MS/MS, genomik, biyobanka, mikroskopi", V1),
             ("Database", "4.200 numune", "yılda; üçte biri dış müşteriden", AMBER), ("PaperPlane", "E-postayla rapor", "sonuçlar PDF olarak gider", P1),
             ("Link", "Uzaktan servis", "iki firma cihazlara bağlanır", T1), ("Warning", "3 olay", "son altı ayda yaşandı", P2)]
    for k, (ic, a, b, c) in enumerate(facts):
        r, col = divmod(k, 3)
        s += (f'<div data-build-in="pop {k + 3} auto" style="position:absolute;left:{128 + col * 563}px;top:{480 + r * 190}px;width:538px;height:166px;display:flex;flex-direction:row;gap:24px;align-items:center;padding:0px 30px;background:{INK2};border-radius:22px;border-left:8px solid {c}">'
              f'<x-icon name="{ic}" style="width:52px;height:52px;color:{c}"></x-icon><div style="flex:1;display:flex;flex-direction:column;gap:4px">'
              f'<p style="font-family:{DISPLAY};font-size:36px;font-weight:800;letter-spacing:-0.5px;color:{CREAM}">{a}</p><p style="font-size:24px;line-height:1.3;color:{SKY}">{b}</p></div></div>')
    s += src("Ayrıntılar elinizdeki senaryo kartında. HALMER kurgusaldır; gerçek bir kurumu anlatmaz.", top=880, dark=True)
    return s


# 8 method in five steps
ST = [("1", "Listele", "Beş kategoride aklınıza gelen her varlığı yazın.", V2), ("2", "Sahip ata", "Her satıra bir görev ya da kişi adı.", T3),
      ("3", "Akışı izle", "Bir numunenin verisi nereden nereye gidiyor?", P2), ("4", "Kritikliği işaretle", "Düşük, orta ya da yüksek.", AMBER),
      ("5", "Risk yaz", "En kritik üç varlığa birer risk cümlesi.", V1)]
items = [f'<p style="width:72px;height:72px;border-radius:36px;background:{c};color:{"#FFFFFF" if c in (V2, T3, V1) else INK};font-family:{DISPLAY};font-size:36px;font-weight:800;text-align:center;line-height:72px">{a}</p>'
         + H(t, 29, lh=1.18) + P(d_, 24, BODY2, lh=1.36) for a, t, d_, c in ST]
content(D, "steps", "Örnek çözüm · HALMER", "Haritalama beş adımda",
        cards_row(items, top=320, n=5, gap=20, height=360, accents=[c for *_, c in ST], pad="28px 26px")
        + callout(720, "Şimdi bu beş adımı HALMER üzerinde birlikte yapacağız; sonra aynısını kendi laboratuvarınızda siz yapacaksınız.", label="Yöntem", icon="Play", build="rise 6 auto"),
        ill="stairs",
        notes="""Yöntem beş adım: listele, sahip ata, veri akışını izle, kritikliği işaretle ve en kritik üç varlığa birer risk cümlesi yaz.
Sonraki üç slaytta bu adımları HALMER üzerinde gösteriyoruz. İsterseniz slaytları açmadan önce salona sorun: karttan hangi varlıkların altını çizdiniz? Gelen cevapları tahtaya yazıp sonra slaytla karşılaştırın.""")

# 9 worked example: the list
ROWS = [("LC-MS/MS bilgisayarı", "Cihaz", "Kromatografi uzmanı", "Müşteri ham verisi, yöntemler", "Yüksek"),
        ("Dizileme ham verisi (NAS)", "Veri", "Genomik uzmanı", "Proje ve müşteri dizileri", "Yüksek"),
        ("Numune takip dosyası", "Veri", "Numune kabul sorumlusu", "Müşteri adları, numune kayıtları", "Yüksek"),
        ("“lcms” ortak hesabı", "Hesap", "Sahibi yok", "Cihaz bilgisayarına tam erişim", "Yüksek"),
        ("Servis firması", "Dış taraf", "Müdür yardımcısı", "Cihazlara uzaktan erişim", "Orta"),
        ("Misafir Wi-Fi", "Ağ", "Bilgi işlem", "Cihazlarla aynı ağda", "Orta")]
CW = [430, 180, 340, 470, 150]
HD = ["Varlık", "Kategori", "Sahibi", "Tuttuğu veri ya da erişim", "Kritiklik"]
body = (f'<div style="position:absolute;left:128px;top:296px;width:1664px;display:flex;flex-direction:row;gap:18px;padding:0px 28px">'
        + "".join(f'<p style="width:{w}px;font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:1px;color:{MUTE}">{tr_upper(h)}</p>' for w, h in zip(CW, HD)) + "</div>")
for k, r in enumerate(ROWS):
    none = r[2] == "Sahibi yok"
    cells = ""
    for j, (w, v) in enumerate(zip(CW, r)):
        col = PT if (none and j == 2) else (PT if (j == 4 and v == "Yüksek") else (AMBERT if j == 4 else (TEXT if j == 0 else BODY2)))
        wt = 700 if (j in (0, 4) or (none and j == 2)) else 400
        cells += f'<p style="width:{w}px;font-size:26px;line-height:1.2;font-weight:{wt};color:{col}">{v}</p>'
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:128px;top:{340 + k * 78}px;width:1664px;height:68px;display:flex;flex-direction:row;gap:18px;align-items:center;padding:0px 28px;'
             f'background:{PTINT if none else WHITE};border-radius:14px;border-left:8px solid {P2 if none else LINE};box-shadow:0 6px 18px rgba(29,37,84,0.06)">{cells}</div>')
body += callout(820, "“Sahibi yok” yazdığınız her satır bir bulgudur. Silmeyin, işaretleyin.", label="Adım 1–2–4", icon="Warning", build="rise 8 auto")
content(D, "demo-list", "Örnek çözüm · HALMER", "Liste böyle görünür", body, ill="layers",
        notes="""Adım bir, iki ve dört bir arada: liste, sahip ve kritiklik. Satırlar tıkladıkça açılıyor; her satırda karttaki ilgili cümleyi hatırlatın.
Dördüncü satıra dikkat çekin: "lcms" ortak hesabının sahibi yok. Hesap da bir varlıktır ve sahibi olmayan varlık korunmaz. Bu tür satırları silmeyin; onlar ilk bulgularınızdır.
Bu altı satır örnek; HALMER'in tam listesi otuzun üzerinde varlık içerir. Ekiplerden kendi laboratuvarları için en az on beş satır bekliyoruz.""")


# 10 worked example: data flow
@dark("demo-flow", """Adım üç: veri akışı. Bir dış müşteri numunesini kabulden müşteriye kadar izliyoruz. Her durakta iki soru: veri nerede duruyor ve bir sonraki durağa nasıl gidiyor?
Kırmızı etiketler verinin laboratuvarın denetiminden çıktığı ya da korumasız kaldığı noktalar: etikette açık müşteri adı, ortak hesap, tek kopya ham veri, kişisel bulut ve yapay zekâ aracı, kişisel e-posta.
Liste size neyiniz olduğunu söyler; akış ise nerede kaybedebileceğinizi gösterir. Ekipler de tahtada tek bir numunenin ya da veri setinin yolunu çizecek.""", glow=(P2, V2))
def _(i, n):
    s = eyebrow("Örnek çözüm · HALMER · adım 3", 190)
    s += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:246px;width:1500px;font-family:{DISPLAY};font-size:68px;font-weight:800;letter-spacing:-2px;line-height:1.05;color:{CREAM}">Bir numunenin yolculuğu</h2>'
    s += f'<div style="position:absolute;left:180px;top:468px;width:1560px;height:6px;border-radius:3px;background:{INK3}"></div>'
    ND = [("Numune kabul", "Excel dosyası, ortak sürücü", "Etikette müşteri adı açık", P2), ("Cihaz", "LC-MS/MS, dizileme", "Ortak hesapla çalışılır", P2),
          ("Ham veri", "Cihaz bilgisayarı, NAS", "Tek kopya", P2), ("Analiz", "Uzmanın bilgisayarı", "Kişisel bulut, yapay zekâ aracı", P2),
          ("Rapor", "PDF, ortak sürücü", "Herkes değiştirebilir", AMBER), ("Müşteri", "E-posta", "Kişisel e-posta adresi", P2)]
    for k, (t, w, chip, c) in enumerate(ND):
        x = 128 + k * 283
        s += (f'<div data-build-in="pop {k + 2} auto" style="position:absolute;left:{x}px;top:390px;width:250px;height:164px;display:flex;flex-direction:column;gap:8px;justify-content:center;padding:0px 22px;background:{INK2};border-radius:20px;border-top:6px solid {T2}">'
              f'<p style="font-family:{DISPLAY};font-size:28px;font-weight:700;color:{CREAM}">{t}</p><p style="font-size:24px;line-height:1.25;color:{SKY}">{w}</p></div>')
        s += (f'<p data-build-in="rise {k + 8} auto" style="position:absolute;left:{x}px;top:580px;width:250px;height:112px;padding:14px 18px;border-radius:16px;background:{c};color:{"#FFFFFF" if c == P2 else INK};font-size:24px;font-weight:600;line-height:1.25">{chip}</p>')
    s += f'<p data-build-in="fade 14 auto" style="position:absolute;left:128px;top:740px;width:1500px;font-size:30px;line-height:1.4;color:{CREAM}">Liste neyiniz olduğunu söyler. Akış, onu nerede kaybedebileceğinizi gösterir.</p>'
    s += src("Renkli etiketler: verinin laboratuvarın denetiminden çıktığı ya da korumasız kaldığı noktalar.", top=880, dark=True)
    return s


# 11 worked example: top three and risks
RK = [("LC-MS/MS bilgisayarı", "Bütünlük", "Ortak hesap ve yazılı parola yüzünden yöntem dosyası, kimin değiştirdiği bilinmeden değişirse sonuçlar savunulamaz.", P2),
      ("Dizileme ham verisi", "Erişilebilirlik", "Tek kopya cihazla aynı odada durduğu için disk arızasında ham veri geri getirilemez.", AMBER),
      ("Hasta kod anahtarı", "Gizlilik", "Anahtar sonuçlarla aynı klasörde durduğu için klasöre erişen herkes hastaları tanımlayabilir.", V2)]
items = [f'<div style="display:flex;flex-direction:row;gap:14px;align-items:center">{icon("Star", 40, TX.get(c, c))}<p style="font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:1px;color:{TX.get(c, c)}">{tr_upper(v)}</p></div>'
         + H(t, 32) + P(d_, 26, BODY2, lh=1.4) for t, v, d_, c in RK]
content(D, "demo-risk", "Örnek çözüm · HALMER · adım 5", "En kritik üç ve riskleri",
        cards_row(items, top=320, height=390, accents=[c for *_, c in RK], pad="32px 32px")
        + callout(750, "“[Neden] yüzünden [varlık] üzerinde [olay] olursa [sonuç] doğar.” Her risk tek bir cümle.", label="Risk cümlesi", icon="Chat", build="rise 5 auto"),
        ill="shield",
        notes="""Adım beş: en kritik üç varlık ve her biri için bir risk cümlesi. Üç soru yardımcı olur: kim görmemeli, kim değiştirmemeli, ne zaman lazım. Yani gizlilik, bütünlük ve erişilebilirlik.
Risk tek cümleyle yazılır: neden, varlık, olay, sonuç. "Siber saldırı olabilir" bir risk cümlesi değildir.
Örnek çözüm burada bitiyor. Soru varsa şimdi alın; sonra ekiplere ayrılıyoruz.""")

# 12 two teams
TM = [("CÜTAM", "Araştırma merkezi ekibi", T3), ("CÜTFAM", "Tıp Fakültesi laboratuvarı ekibi", P2)]
items = [f'<p style="font-family:{DISPLAY};font-size:88px;font-weight:800;letter-spacing:-3px;line-height:1;color:{TX.get(c, c)}">{t}</p>' + H(d_, 32)
         + P("Kendi laboratuvarınızı, kendi tahtanızda haritalayın.", 28, BODY2, lh=1.4) for t, d_, c in TM]
RL3 = [("Book", "Yazıcı", "tahtaya yazar"), ("Clock", "Zaman tutucu", "süreyi izler"), ("PaperPlane", "Sözcü", "sonucu anlatır")]
roles = "".join(f'<div style="flex:1;display:flex;flex-direction:row;gap:16px;align-items:center">{icon(ic, 40, AMBER)}<p style="font-size:28px;color:{CREAM}"><b>{a}</b> {b}</p></div>' for ic, a, b in RL3)
content(D, "teams", "Ekip çalışması", "İki ekip, iki laboratuvar",
        cards_row(items, top=320, n=2, height=330, accents=[c for *_, c in TM], pad="40px 44px", gap=32, kind="pop")
        + f'<div data-build-in="rise 3 auto" style="position:absolute;left:128px;top:700px;width:1664px;display:flex;flex-direction:row;gap:28px;align-items:center;padding:28px 40px;background:{INK};border-radius:22px">{roles}</div>',
        ill="people",
        notes="""Şimdi iki ekibe ayrılıyoruz: CÜTAM ekibi ve CÜTFAM ekibi. Her ekip kendi laboratuvarını kendi tahtasında haritalayacak.
Her ekip üç kişi seçsin: tahtaya yazacak bir yazıcı, süreyi izleyecek bir zaman tutucu ve sonucu anlatacak bir sözcü. Diğer herkes varlık söyler.
Ekipte farklı görevlerden insanlar var: cihaz kullanıcısı, numune kabul, yönetim. Herkes kendi gördüğü varlıkları söylesin; en iyi liste böyle çıkar.""")

# 13 board template
BH = [("Varlık", 300), ("Kategori", 170), ("Sahibi", 210), ("Veri", 190), ("Kritiklik", 150)]
board = "".join(f'<p style="width:{w}px;font-family:{MONO};font-size:24px;font-weight:600;color:{V3}">{tr_upper(h)}</p>' for h, w in BH)
lines = "".join(f'<div style="height:3px;border-radius:2px;background:{LINE}"></div>' for _ in range(5))
body = (f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:300px;width:1090px;height:510px;display:flex;flex-direction:column;gap:56px;padding:36px 40px;background:{WHITE};border-radius:22px;border:4px solid {INK};box-shadow:0 12px 34px rgba(29,37,84,0.09)">'
        f'<div style="display:flex;flex-direction:row;gap:0px">{board}</div>{lines}'
        f'<p style="font-size:26px;font-weight:600;color:{PT}">★ = en kritik üç varlık; yanına bir risk cümlesi</p></div>')
CK = [("En az 15 satır", V2), ("Her kategoriden en az iki varlık", T3), ("Her satırda bir sahip; yoksa “sahibi yok”", P2), ("Bir numunenin ya da veri setinin yolu", AMBER), ("En kritik üçe yıldız ve risk cümlesi", V1)]
for k, (t, c) in enumerate(CK):
    body += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:1260px;top:{300 + k * 104}px;width:532px;height:88px;display:flex;flex-direction:row;gap:18px;align-items:center;padding:0px 24px;background:{WHITE};border-radius:16px;border-left:8px solid {c};box-shadow:0 6px 18px rgba(29,37,84,0.06)">'
             f'{icon("CheckCircle", 36, TX.get(c, c))}<p style="flex:1;font-size:26px;line-height:1.25;font-weight:600;color:{TEXT}">{t}</p></div>')
content(D, "board", "Ekip çalışması", "Tahtanız böyle görünsün", body, ill="checklist",
        notes="""Tahtanın düzeni. Beş sütun: varlık, kategori, sahibi, tuttuğu veri ve kritiklik. Sütun başlıklarını şimdi tahtaya yazdırın.
Beş hedef: en az on beş satır; her kategoriden en az iki varlık; her satırda bir sahip, yoksa açıkça "sahibi yok"; tahtanın altına bir numunenin ya da veri setinin yolu; ve en kritik üç varlığa yıldız ile birer risk cümlesi.
Yapışkan not kullanmak isteyen ekip her kategoriye bir renk versin.""")

# 14 team work
timed("work", "Ekip çalışması · 30 dakika", "Kendi<br>laboratuvarınız", [("Database", "Varlıkları beş kategoride tahtaya yazın", T2),
                                                                      ("Users", "Her satıra bir sahip yazın", AMBER),
                                                                      ("Link", "Bir numunenin yolunu izleyin: veri nereden çıkıyor?", P1),
                                                                      ("Star", "En kritik üçe yıldız ve birer risk cümlesi", V1)], 30,
      """Ekip çalışması, otuz dakika. Sayaç slayt açılınca başlar.
İlk on beş dakika yalnız liste. On beşinci dakikada iki tahtayı da dolaşın ve sorun: tahtada kaç insan, kaç hesap, kaç dış firma var? Çoğu ekip yalnız cihaz yazar.
Yirminci dakikada veri akışına ve kritikliğe geçsinler. Son beş dakika en kritik üç varlık ve risk cümleleri; sözcü bu sırada anlatacağını hazırlasın.
Takılan ekibe sorulacak soru: bu cihazın ürettiği veri yarın nerede olacak ve ona kim erişebilecek?""")

# 15 spokespeople
timed("share", "Sunum · 20 dakika", "Sözcüler<br>anlatıyor", [("Chart", "Kaç varlık yazdınız? Hangi kategori zayıf kaldı?", T2),
                                                             ("Search", "Sizi en çok şaşırtan satır hangisiydi?", AMBER),
                                                             ("Star", "En kritik üç varlığınız ve riskleri", P1),
                                                             ("Warning", "Sahibi olmayan satırlar", V1)], 20,
      """Sunum, yirmi dakika: her sözcü sekiz dakika anlatır, iki dakika soru alır. Sayaç toplam süreyi gösterir; onuncu dakikada ikinci ekibe geçin.
Sözcü dört şeyi anlatsın: kaç varlık yazdılar ve hangi kategori zayıf kaldı; en çok şaşırtan satır; en kritik üç varlık ve riskleri; sahibi olmayan satırlar.
Diğer ekip dinlerken kendi tahtasında eksik kalanı not etsin: karşı tahtada olup bizde olmayan ne var?""", glow=(T3, P2), title_size=96)

# 16 compare
CMP = [("Users", "Ortak olan ne?", "İki tahtada da bulunan varlıklar: ağ, e-posta, bilgi işlem, servis firmaları.", V2),
       ("Search", "Kimde ne eksik?", "Karşı tahtada olup sizde olmayan kategori ya da satır.", T3),
       ("Warning", "Kaç satır sahipsiz?", "“Sahibi yok” yazan her satır için bir aday belirleyin.", P2),
       ("Link", "Veri nereden çıkıyor?", "E-posta, USB bellek, bulut, uzaktan erişim: laboratuvarın dışına açılan kapılar.", AMBER)]
items = [icon(ic, 46, TX.get(c, c)) + H(t, 30, lh=1.18) + P(d_, 25, BODY2, lh=1.38) for ic, t, d_, c in CMP]
content(D, "compare", "Kapanış · 5 dakika", "İki tahtaya birlikte bakalım",
        cards_row(items, top=320, height=360, accents=[c for *_, c in CMP], pad="30px 30px")
        + callout(720, "Tahtaların fotoğrafını çekin ve kurum içinde tutun: bu liste bir saldırgan için de haritadır.", label="Çıkarken", icon="Lock", build="rise 5 auto"),
        ill="scan",
        notes="""Kapanış, beş dakika. İki tahtayı yan yana değerlendirin: ortak olan ne, kimde ne eksik, kaç satır sahipsiz ve veri laboratuvardan hangi kapılardan çıkıyor.
Tahtaların fotoğrafını çektirin. Uyarı: bu liste gerçek laboratuvarlarınızı anlatıyor; fotoğraflar kurum içinde kalsın, sosyal medyada ya da dış yazışmada paylaşılmasın.
Bu listeler tamamlanmış envanter değil, başlangıçtır.""")

# 17 next step
HM = [("01", "Listeyi tamamlayın", "Tahtadaki listeyi bir hafta içinde yazıya geçirin; salonda aklınıza gelmeyenleri ekleyin.", V2),
      ("02", "Sahipleri onaylatın", "Her satırdaki sahip, o varlıktan sorumlu olduğunu bilsin. “Sahibi yok” satırı kalmasın.", P2),
      ("03", "Yılda bir güncelleyin", "Yeni cihaz, yeni yazılım, ayrılan personel: liste yaşayan bir belgedir.", AMBER)]
items = [numcard(a, t, d_, TX.get(c, c)) for a, t, d_, c in HM]
content(D, "home", "Sonraki adım", "Tahtadan envantere",
        cards_row(items, top=320, height=380, accents=[c for *_, c in HM], pad="32px 32px")
        + callout(740, "Bir olay olduğunda ilk bakılan belge varlık listesidir; yarınki masa başı tatbikatta bunu göreceksiniz.", label="Yarın", icon="Play", build="rise 5 auto"),
        ill="flag",
        notes="""Sonraki adım. Tahtadaki liste bir başlangıç: bir hafta içinde yazıya geçirin, her sahibin sorumluluğunu bildiğinden emin olun ve listeyi yılda bir güncelleyin.
Mevcut bir envanteriniz varsa bugünkü listeyle karşılaştırın; fark, envanterin eksiğidir.
Yarın olay müdahalesi tatbikatında varlık listesinin neden ilk bakılan belge olduğunu göreceğiz.""")

# 18 refs
refs(D, "refs", [
    "National Institute of Standards and Technology. The NIST Cybersecurity Framework (CSF) 2.0. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Joint Task Force Transformation Initiative. Guide for Conducting Risk Assessments. NIST SP 800-30 Rev. 1; 2012. doi:10.6028/NIST.SP.800-30r1",
    "Murch RS, So WK, Buchholz WG, Raman S, Peccoud J. Cyberbiosecurity: An Emerging New Discipline to Help Safeguard the Bioeconomy. Front Bioeng Biotechnol. 2018;6:39. doi:10.3389/fbioe.2018.00039",
    "HALMER senaryosu bu çalıştay için hazırlanmıştır ve kurgusaldır.",
], notes="""Kaynaklar. Varlık yönetimi ve risk değerlendirme başlıkları NIST Siber Güvenlik Çerçevesi 2.0'ın Tanımla işlevinden; risk cümlesi yaklaşımı NIST SP 800-30'dan. Üç DOI Crossref'te doğrulandı.""", size=26)

# 19 close
statement(D, "close", [("Harita hazır.", None), ("Sıra korumada.", T2)],
          """Kahve arası, on beş dakika. Dönüşte Prof. Dr. Ahmet Altun ile biyoteknolojiyi siber hırsızlıktan korumak oturumu var; bugün haritaya yazdığınız varlıkların nasıl çalındığını gerçek vakalarla göreceğiz.""",
          eyebrow_="Kahve arası · 14:30–14:45", sub="14:45’te devam: Üniversitelerde biyoteknolojiyi siber hırsızlıktan korumak.",
          right_html=emb("capsid", 1240, 240, 560, 560, PAL, rings=True, burst=True, spin=.3, t1=T1, v1=V1, v3=V3), size=104, width=1080)

SECTIONS = {"s1": {"description": "Giriş", "start": "cover"}, "s2": {"description": "Örnek laboratuvar ve örnek çözüm", "start": "lab"},
            "s3": {"description": "Ekip çalışması", "start": "teams"}, "s4": {"description": "Sunum ve kapanış", "start": "share"}}

if __name__ == "__main__":
    write_deck(sys.argv[1], TITLE, SECTIONS, D.render())
    print("ok", len(D.slides))
