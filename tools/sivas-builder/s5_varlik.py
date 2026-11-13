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
      "Küçük gruplarla: laboratuvarın varlıklarını haritalayın, riskleri yazın, ilk üçünü seçin.",
      emb("capsid", 1180, 190, 640, 640, PAL, rings=True, intro=True, spin=.35, t1=T1, v1=V1, v3=V3),
      """Öğle arasından dönüş. Katılımcılar salona girerken masalara yönlendirin: her masada dört ile altı kişi, aynı birimden gelenler farklı masalarda.
Bu oturumda ders yok; doksan dakikanın yetmiş beşi masalarda geçecek. Sunum yalnız yönergeleri ve sayaçları taşır.
Masalarda hazır olması gerekenler: senaryo kartları, dört form, beş renk yapışkan not, kalın kalemler ve bir pano kâğıdı.""", size=96)

# 2 kinetic
kinetic(D, "k-list", "Alıştırmanın tek cümlesi", [("LİSTEDE", None), ("YOKSA", None), ("KORUNMUYOR.", T2)],
        """Kinetik açılış. Bugünün tek cümlesi: listede olmayan varlık korunmuyor. Sabah Prof. Merey'in anlattığı risklerin hepsi bir varlığın üzerinde gerçekleşir; önce o varlıkları görmemiz gerekiyor.""",
        size=160)

# 3 outputs
OUT = [("01", "Varlık haritası", "Cihazlar, veriler, hesaplar, insanlar ve bağlantılar; her birinin bir sahibi.", V2),
       ("02", "Risk kaydı", "Her önemli varlık için “ne ters gidebilir?” sorusunun yazılı cevabı.", P2),
       ("03", "İlk üç risk", "Puanlanmış, sıralanmış ve her biri için bir ilk adım yazılmış.", AMBER)]
items = [numcard(a, t, d_, TX.get(c, c)) for a, t, d_, c in OUT]
content(D, "outputs", "Hedef", "90 dakikada üç çıktı",
        cards_row(items, top=320, height=380, accents=[c for *_, c in OUT], pad="32px 32px")
        + callout(740, "Gerçek kurum adı kullanmıyoruz. Bütün masalar aynı kurgusal laboratuvarı, HALMER’i çalışıyor.", label="Kural", icon="Trust", build="rise 5 auto"),
        ill="checklist",
        notes="""Doksan dakikanın sonunda her masanın elinde üç şey olacak: bir varlık haritası, bir risk kaydı ve puanlanmış ilk üç risk ile ilk adımları.
Kural: gerçek kurum adı yok. Herkes aynı kurgusal laboratuvarı çalışıyor; böylece kimse kendi biriminin açığını salonda anlatmak zorunda kalmıyor. Kendi laboratuvarınıza son beş dakikada döneceğiz.""")

# 4 flow
FL = [("10 dk", "Kurulum", "Roller ve senaryo", V1), ("25 dk", "Tur 1 · Harita", "Varlıklar ve veri akışı", V2), ("20 dk", "Tur 2 · Riskler", "Ne ters gidebilir?", P2),
      ("15 dk", "Tur 3 · Öncelik", "Puanla, ilk üçü seç", AMBER), ("15 dk", "Paylaşım", "Masa başına 2 dakika", T3), ("5 dk", "Kapanış", "Kendi laboratuvarınız", T2)]
mins = [10, 25, 20, 15, 15, 5]
bar = "".join(f'<div style="width:{round(1664 * m / 90) - 4}px;height:22px;border-radius:11px;background:{c}"></div>' for m, (*_, c) in zip(mins, FL))
body = f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:300px;width:1664px;height:22px;display:flex;flex-direction:row;gap:4px">{bar}</div>'
items = [f'<p style="font-family:{DISPLAY};font-size:44px;font-weight:800;letter-spacing:-1px;line-height:1;color:{TX.get(c, c)}">{m}</p>' + H(t, 27, lh=1.2) + P(d_, 24, BODY2, lh=1.32)
         for m, t, d_, c in FL]
body += cards_row(items, top=360, n=6, gap=20, height=300, accents=[c for *_, c in FL], pad="26px 24px", build_start=2)
body += callout(720, "Her turda perdede bir sayaç döner. Süre dolunca kalemler bırakılır; yarım kalan satır yarım kalır.", label="Zaman", icon="Clock", build="rise 9 auto")
content(D, "flow", "Akış", "Altı adım, doksan dakika", body, ill="timeline",
        notes="""Akış altı adım. On dakika kurulum, yirmi beş dakika varlık haritası, yirmi dakika riskler, on beş dakika önceliklendirme, on beş dakika paylaşım ve beş dakika kapanış.
Üstteki şerit sürelerin oranını gösteriyor: en uzun dilim haritaya ayrılmış, çünkü iyi bir harita olmadan risk yazılamaz.
Sayaç kuralını şimdi söyleyin: süre dolunca kalemler bırakılır.""")

# 5 roles
RL = [("Chat", "Moderatör", "Herkesin söz almasını sağlar; tartışma uzayınca kararı bağlar.", V2),
      ("Book", "Yazıcı", "Formları doldurur, yapışkan notları haritaya yerleştirir.", T3),
      ("Clock", "Zaman tutucu", "Sayacı izler; turun yarısında ve son üç dakikada uyarır.", AMBER),
      ("PaperPlane", "Sözcü", "Paylaşımda masanın bulgusunu iki dakikada anlatır.", P2)]
items = [icon(ic, 48, TX.get(c, c)) + H(t, 32) + P(d_, 26, BODY2, lh=1.38) for ic, t, d_, c in RL]
content(D, "roles", "Kurulum · 10 dakika", "Her masada dört rol",
        cards_row(items, top=320, height=360, accents=[c for *_, c in RL], pad="32px 32px")
        + callout(720, "4–6 kişilik masalar. Rolleri şimdi dağıtın; beşinci ve altıncı kişi “bunu kim kötüye kullanır?” diye soran kişidir.", label="Şimdi", icon="Users", build="rise 5 auto"),
        ill="people",
        notes="""Kurulum. Her masa dört rol dağıtsın: moderatör, yazıcı, zaman tutucu ve sözcü. Rolleri bir dakikada seçsinler; gönüllü çıkmazsa doğum günü en yakın olan moderatör olur.
Beş ya da altı kişilik masalarda kalan üyeler şeytanın avukatıdır: her varlık için "bunu kim, nasıl kötüye kullanır" diye sorar.
Roller dağılınca senaryo kartlarını açtırın.""")


# 6 scenario lab
@dark("lab", """Senaryo. HALMER, Halys Üniversitesi Merkezi Araştırma Laboratuvarı; tamamen kurgusal. Halys, Kızılırmak'ın antik adı.
On dört personel, dokuz lisansüstü öğrenci, beş birim. Yılda yaklaşık dört bin iki yüz numune; üçte biri dış müşterilerden. Raporlar e-postayla gidiyor, iki servis firması cihazlara uzaktan bağlanıyor ve son altı ayda üç olay yaşanmış.
Ayrıntıların hepsi masadaki kartta. Kartı okumaları için dört dakika verin; okurken varlıkların altını çizsinler. Kartta yirmi bulgu gizli; bunu söylemeyin.""", glow=(V2, P2))
def _(i, n):
    s = eyebrow("Senaryo · kurgusal laboratuvar", 190)
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
    s += src("Ayrıntılar masanızdaki senaryo kartında. HALMER kurgusaldır; gerçek bir kurumu anlatmaz.", top=880, dark=True)
    return s


# 7 morph: categories
morph(D, "k-cats", "Tur 1 · Varlık haritası", [("CİHAZ", T2), ("VERİ", P2), ("HESAP", AMBER), ("İNSAN", None), ("AĞ", T1), ("HARİTA", T2)],
      """Morf ara slaytı: cihaz, veri, hesap, insan, ağ ve hepsi bir arada harita. Varlık yalnız cihaz değildir; bugün en çok unutulan üç kategori veri, hesap ve insan olacak.""",
      size=230, sub="Beş kategori, tek harita.", per=2.6)

# 8 categories
CT = [("Settings", "Cihaz", "Analiz cihazları, cihaz bilgisayarları, dondurucular, depolama cihazları, USB bellekler.", V2),
      ("Database", "Veri", "Ham veri, raporlar, numune kayıtları, yöntem dosyaları, hasta kod anahtarı, sözleşmeler.", P2),
      ("Key", "Yazılım ve hesap", "Cihaz yazılımları, ortak hesaplar, e-posta, bulut hesapları, uzaktan erişim araçları.", AMBER),
      ("Users", "İnsan ve dış taraf", "Personel, öğrenciler, müşteriler, servis firmaları, temizlik firması, bilgi işlem.", T3),
      ("Globe", "Ağ ve alan", "Yerel ağ, misafir Wi-Fi, ortak sürücü, kapılar, cihaz odaları, dolaplar.", V1)]
items = [icon(ic, 46, TX.get(c, c)) + H(t, 29, lh=1.18) + P(d_, 24, BODY2, lh=1.36) for ic, t, d_, c in CT]
content(D, "cats", "Tur 1 · Varlık haritası", "Beş kategoride varlıklar",
        cards_row(items, top=320, n=5, gap=20, height=380, accents=[c for *_, c in CT], pad="28px 26px")
        + callout(740, "Her kategoriye bir yapışkan not rengi. Her notun altına bir sahip adı: sahibi olmayan varlık korunmaz.", label="Yöntem", icon="Lightbulb", build="rise 6 auto"),
        ill="network",
        notes="""Tur birin yöntemi. Beş kategori, beş renk yapışkan not: cihazlar, veriler, yazılım ve hesaplar, insanlar ve dış taraflar, ağ ve fiziksel alan.
Her nota bir varlık yazılır, altına sahibinin unvanı. Sahip yazamadıkları varlık zaten ilk riskleridir.
Sonra bir dış müşteri numunesini kabulden arşive kadar izleyip okları çizecekler: veri nerede duruyor, kim erişiyor, bir duraktan ötekine nasıl taşınıyor.""")

# 9 round 1
timed("tur1", "Tur 1 · 25 dakika", "Haritayı<br>kurun", [("Database", "Beş kategoride varlıkları yapışkan notlara yazın", T2),
                                                         ("Users", "Her varlığın altına bir sahip yazın", AMBER),
                                                         ("Link", "Numuneden rapora veri akışını oklarla çizin", P1),
                                                         ("CheckCircle", "Form 1 ve Form 2’yi doldurun", V1)], 25,
      """Tur bir, yirmi beş dakika. Sayaç slayt açılınca başlar; yönergeyi bir önceki slaytta bitirip bu slayda geçin.
Onuncu dakikada masaları dolaşıp sorun: haritanızda kaç insan ve kaç hesap var? Yalnız cihaz yazan masaya "bu cihazın ürettiği veri yarın nerede olacak" diye sorun.
Son beş dakikada veri akışına geçmeyen masaları uyarın: verinin laboratuvarın denetiminden çıktığı noktaları kırmızıyla işaretlesinler.""")

# 10 CIA
CIA = [("Lock", "Gizlilik", "Kim görmemeli?", "Müşteri raporunun rakibin eline geçmesi; hasta kod anahtarının açıkta durması.", V2),
       ("Verified", "Bütünlük", "Kim değiştirmemeli?", "Ham verinin ya da numune kaydının fark edilmeden değişmesi.", P2),
       ("Clock", "Erişilebilirlik", "Ne zaman lazım?", "Tek kopya verinin silinmesi; cihazın günlerce çalışmaması; alarmın kimseye ulaşmaması.", AMBER)]
items = [icon(ic, 48, TX.get(c, c)) + H(t, 34) + f'<p style="font-family:{MONO};font-size:24px;font-weight:600;color:{TX.get(c, c)}">{q}</p>' + P(d_, 26, BODY2, lh=1.38)
         for ic, t, q, d_, c in CIA]
content(D, "cia", "Tur 2 · Riskler", "Ne ters gidebilir?",
        cards_row(items, top=320, height=380, accents=[c for *_, c in CIA], pad="32px 32px")
        + callout(740, "“[Neden] yüzünden [varlık] üzerinde [olay] olursa [sonuç] doğar.” Her risk tek bir cümle.", label="Risk cümlesi", icon="Chat", build="rise 5 auto"),
        ill="shield",
        notes="""Tur ikinin yöntemi. Haritadaki her önemli varlık için üç soru: kim görmemeli, kim değiştirmemeli, ne zaman lazım. Bunlar sabah konuşulan gizlilik, bütünlük ve erişilebilirlik.
Risk tek cümleyle yazılır: neden, varlık, olay, sonuç. "Siber saldırı olabilir" bir risk cümlesi değildir; "ortak parola yüzünden cihaz bilgisayarındaki yöntem dosyası kim tarafından değiştirildiği bilinmeden değişirse sonuçlar geçersiz olur" bir risk cümlesidir.
Yalnız dış saldırganı düşünmesinler: en olası riskler sıradan hatalardır.""")

# 11 round 2
timed("tur2", "Tur 2 · 20 dakika", "Riskleri<br>yazın", [("Search", "Haritadaki her önemli varlık için: ne ters gidebilir?", T2),
                                                         ("Chat", "Her riski tek cümleyle Form 3’e yazın", AMBER),
                                                         ("Lock", "Gizlilik, bütünlük, erişilebilirlik: her birinden en az iki", P1),
                                                         ("Warning", "Karttaki üç olaya dönün: neden yaşandı?", V1)], 20,
      """Tur iki, yirmi dakika. Hedef en az sekiz risk cümlesi.
Masaları dolaşırken dengeye bakın: çoğu masa yalnız gizlilik riski yazar. Erişilebilirlik için "bu veri yarın sabah yok olsa ne olur", bütünlük için "biri bu kaydı değiştirse kim fark eder" diye sorun.
On ikinci dakikada karttaki üç olayı hatırlatın: her biri haritadaki bir zayıflığın sonucu.""", glow=(P2, V2))

# 12 matrix
LIK = ["1 · Seyrek", "2 · Yılda bir", "3 · Sık"]
IMP = [("3 · Ağır", 3), ("2 · Orta", 2), ("1 · Hafif", 1)]


def cell_col(v):
    return (P2, "#FFFFFF") if v >= 6 else ((AMBER, INK) if v >= 3 else (T2, INK))


body = f'<p style="position:absolute;left:128px;top:292px;width:190px;font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:2px;color:{MUTE}">ETKİ</p>'
k = 0
for r, (lab, iv) in enumerate(IMP):
    y = 336 + r * 132
    body += f'<p style="position:absolute;left:128px;top:{y + 42}px;width:190px;font-size:26px;font-weight:600;color:{TEXT}">{lab}</p>'
    for c_ in range(3):
        v = iv * (c_ + 1)
        bg, fg = cell_col(v)
        k += 1
        body += (f'<p data-build-in="pop {k} auto" style="position:absolute;left:{330 + c_ * 232}px;top:{y}px;width:220px;height:120px;border-radius:18px;background:{bg};color:{fg};'
                 f'font-family:{DISPLAY};font-size:52px;font-weight:800;text-align:center;line-height:120px">{v}</p>')
for c_, lab in enumerate(LIK):
    body += f'<p style="position:absolute;left:{330 + c_ * 232}px;top:740px;width:220px;font-size:26px;font-weight:600;text-align:center;color:{TEXT}">{lab}</p>'
body += f'<p style="position:absolute;left:330px;top:782px;width:684px;font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:2px;text-align:center;color:{MUTE}">OLASILIK</p>'
DEC = [("6–9", "Hemen", "Bu ay içinde bir ilk adım.", P2), ("3–4", "Planla", "Bu dönem; sahibi ve tarihi belli.", AMBER), ("1–2", "İzle", "Yılda bir gözden geçir.", T2)]
for j, (rng, t, d_, c) in enumerate(DEC):
    body += (f'<div data-build-in="rise {10 + j} auto" style="position:absolute;left:1090px;top:{336 + j * 132}px;width:702px;height:120px;display:flex;flex-direction:row;gap:24px;align-items:center;padding:0px 30px;background:{WHITE};border-radius:18px;border-left:8px solid {c};box-shadow:0 8px 24px rgba(29,37,84,0.07)">'
             f'<p style="width:110px;font-family:{DISPLAY};font-size:40px;font-weight:800;color:{TX.get(c, c)}">{rng}</p><p style="width:150px;font-size:30px;font-weight:700;color:{TEXT}">{t}</p><p style="flex:1;font-size:26px;line-height:1.3;color:{BODY2}">{d_}</p></div>')
body += callout(826, "Puan = olasılık × etki. Tartışma uzarsa yüksek olanı yazın ve devam edin.", label="Kural", icon="Lightning", build="rise 13 auto")
content(D, "matrix", "Tur 3 · Öncelik", "Olasılık × etki = öncelik", body, ill="gauge",
        notes="""Tur üçün yöntemi. Her riske iki puan: olasılık bir ile üç, etki bir ile üç. Çarpım öncelik puanıdır.
Altı ile dokuz arası hemen ele alınır, üç ile dört planlanır, bir ile iki izlenir. Ölçek bu alıştırma için sadeleştirilmiş üç basamaklı bir ölçektir; puanların tanımı Form 3'ün altında yazıyor.
Kural: bir puan üzerinde bir dakikadan fazla tartışmasınlar; yüksek olanı yazıp devam etsinler. Amaç kusursuz puan değil, sıralama.""")

# 13 round 3
timed("tur3", "Tur 3 · 15 dakika", "İlk üçü<br>seçin", [("Chart", "Her riske olasılık ve etki puanı verin", T2),
                                                        ("Star", "En yüksek puanlı üç riski Form 4’e yazın", AMBER),
                                                        ("Play", "Her biri için bir ilk adım, bir sahip, bir tarih", P1),
                                                        ("ThumbsUp", "İlk adım pazartesi sabahı yapılabilir olsun", V1)], 15,
      """Tur üç, on beş dakika. İlk yedi dakika puanlama, kalan sekiz dakika ilk üç risk ve ilk adımlar.
İlk adımı sınayın: küçük, somut ve tek bir kişinin yapabileceği bir iş mi? "Farkındalık artırılacak" ya da "yeni sistem alınacak" ilk adım değildir. "Parolanın yazılı olduğu kâğıt kaldırılacak, parola değiştirilecek" bir ilk adımdır.
Sözcüler son iki dakikada tek cümlelerini hazırlasın.""", glow=(AMBER, V2))

# 14 share
timed("share", "Paylaşım · 15 dakika", "Masa başına<br>iki dakika", [("Warning", "En büyük riskiniz hangisi?", P1),
                                                                   ("Search", "Neden o? Hangi varlık, hangi sonuç?", T2),
                                                                   ("Play", "İlk adımınız ne, kim yapacak?", AMBER)], 15,
      """Paylaşım. Her sözcü iki dakika: en büyük risk, neden o, ilk adım. Sayaç toplam süreyi gösterir; masa sayısına göre sözcü başına süreyi ayarlayın.
Tekrar eden bulguları panoya çetele ile işaretleyin. Bir masa başka masanın söylediğini tekrar edecekse ikinci riskini anlatsın.
Yorum yapmayın, yalnız not alın; ortak bulguları bir sonraki slaytta toplayacağız.""", glow=(T3, P2), title_size=96)

# 15 common findings
FD = [("Key", "Ortak hesap, yazılı parola", "Kimin ne yaptığı bilinmez.", V2), ("Wrench", "Yamasız cihaz bilgisayarı", "Eski işletim sistemi, kapalı antivirüs, açık internet.", P2),
      ("Link", "Kalıcı uzaktan erişim", "Servis bağlantısı yıllardır aynı parolayla açık.", AMBER), ("Database", "Tek kopya ham veri", "Yedek düzensiz; geri yükleme hiç denenmemiş.", T3),
      ("Cloud", "Denetim dışına çıkan veri", "Kişisel e-posta, kişisel bulut, herkese açık yapay zekâ aracı.", V1), ("Users", "Kapatılmayan hesaplar", "Ayrılan öğrenci ve personelin erişimi sürüyor.", T2)]
items = [f'<div style="display:flex;flex-direction:row;gap:16px;align-items:center">{icon(ic, 40, TX.get(c, c))}{H(t, 28, lh=1.2, extra="flex:1;")}</div>' + P(d_, 25, BODY2, lh=1.36) for ic, t, d_, c in FD]
content(D, "findings", "Ortak bulgular", "Masalar genellikle bunları bulur",
        cards_row(items, top=310, n=3, height=200, row_gap=22, accents=[c for *_, c in FD], pad="26px 30px", gap=22, kind="pop")
        + callout(770, "Altısının da ilk adımı para istemez: bir karar, bir liste ya da bir deneme yeterlidir.", label="Dikkat", icon="Lightbulb", build="rise 8 auto"),
        ill="scan",
        notes="""Ortak bulgular. Kartları tek tek açın ve her birinde salona sorun: kaç masa bunu yazdı? Panodaki çeteleyle karşılaştırın.
Altı bulgu: ortak hesap ve yazılı parola; yamasız cihaz bilgisayarı; kalıcı uzaktan erişim; tek kopya ham veri; denetim dışına çıkan veri; kapatılmayan hesaplar.
Vurgulayın: altısının da ilk adımı bütçe gerektirmez. Senaryo kartında toplam yirmi bulgu vardı; hiçbir masanın hepsini bulması beklenmez.
Üçüncü olayın, yani rakibin sonuçları bilmesinin tek bir cevabı yok; bu belirsizlik gerçek hayattaki durumun kendisidir.""")

# 16 take home
HM = [("01", "İlk on varlık", "Kendi laboratuvarınızın ilk on varlığını yazın; en az ikisi veri, ikisi hesap olsun.", V2),
      ("02", "Her birine bir sahip", "Yanına bir ad yazamadığınız satır, ilk riskinizdir.", P2),
      ("03", "En değerli veri", "Kaç kopyası var, kopyalar nerede duruyor, en son ne zaman geri yüklendi?", AMBER)]
items = [numcard(a, t, d_, TX.get(c, c)) for a, t, d_, c in HM]
content(D, "home", "Kapanış · 5 dakika", "Kendi laboratuvarınızda ilk adım",
        cards_row(items, top=320, height=380, accents=[c for *_, c in HM], pad="32px 32px")
        + callout(740, "Form 4’ü masadan çıkmadan teslim edin. Haritanızın fotoğrafını çekin; kontrol listesi sayfası sizde kalır.", label="Çıkarken", icon="CheckCircle", build="rise 5 auto"),
        ill="flag",
        notes="""Kapanış, beş dakika. HALMER'den kendi laboratuvarınıza dönüyoruz. Üç iş: ilk on varlığı yazmak, her birine bir sahip atamak ve en değerli verinin kopyalarını saymak.
Bunu salonda yüksek sesle paylaşmalarını istemeyin; herkes kendi kâğıdına yazsın. Kontrol listesi sayfası katılımcıda kalıyor.
Form 4'leri toplayın: masa bazındaki bulgular eğitim raporunda kullanılacak.""")

# 17 refs
refs(D, "refs", [
    "National Institute of Standards and Technology. The NIST Cybersecurity Framework (CSF) 2.0. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Joint Task Force Transformation Initiative. Guide for Conducting Risk Assessments. NIST SP 800-30 Rev. 1; 2012. doi:10.6028/NIST.SP.800-30r1",
    "Murch RS, So WK, Buchholz WG, Raman S, Peccoud J. Cyberbiosecurity: An Emerging New Discipline to Help Safeguard the Bioeconomy. Front Bioeng Biotechnol. 2018;6:39. doi:10.3389/fbioe.2018.00039",
    "HALMER senaryosu ve üç basamaklı puan ölçeği bu çalıştay için hazırlanmıştır; senaryo kurgusaldır.",
], notes="""Kaynaklar. Varlık yönetimi ve risk değerlendirme başlıkları NIST Siber Güvenlik Çerçevesi 2.0'ın Tanımla işlevinden; olasılık ve etki yaklaşımı NIST SP 800-30'dan. Üç DOI Crossref'te doğrulandı.
Üç basamaklı puan ölçeği bu alıştırma için sadeleştirildi; kaynaklarda bu biçimde yer almaz.""", size=26)

# 18 close
statement(D, "close", [("Harita hazır.", None), ("Sıra korumada.", T2)],
          """Kahve arası, on beş dakika. Dönüşte Prof. Dr. Ahmet Altun ile biyoteknolojiyi siber hırsızlıktan korumak oturumu var; bugün haritaya yazdığınız varlıkların nasıl çalındığını gerçek vakalarla göreceğiz.""",
          eyebrow_="Kahve arası · 14:30–14:45", sub="14:45’te devam: Üniversitelerde biyoteknolojiyi siber hırsızlıktan korumak.",
          right_html=emb("capsid", 1240, 240, 560, 560, PAL, rings=True, burst=True, spin=.3, t1=T1, v1=V1, v3=V3), size=104, width=1080)

SECTIONS = {"s1": {"description": "Kurulum", "start": "cover"}, "s2": {"description": "Tur 1 · Varlık haritası", "start": "k-cats"},
            "s3": {"description": "Tur 2 · Riskler", "start": "cia"}, "s4": {"description": "Tur 3 · Öncelik", "start": "matrix"},
            "s5": {"description": "Paylaşım ve kapanış", "start": "share"}}

if __name__ == "__main__":
    write_deck(sys.argv[1], TITLE, SECTIONS, D.render())
    print("ok", len(D.slides))
