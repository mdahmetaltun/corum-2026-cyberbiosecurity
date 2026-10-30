# Word-for-word Turkish speaker scripts — D4 HelixLab exercise (v2-tr). "▸" = the next element appears on screen.
N = {
"cover": """Öğleden sonra oturumuna hoş geldiniz. Bu oturum, iki günün birleştiği yer.

Dün CSF 2.0’ı, fonksiyonları, kademeleri ve profilleri konuştuk. Bu sabah yapay zekâ riskini ve bir kurumun altyapısını nasıl kuracağımızı konuştuk. Şimdi sıra sizde. Başlığımız: Uygulama. Hayata geçirin.

Önümüzdeki kırk beş dakikada, gruplar hâlinde, kurgusal bir biyoteknoloji laboratuvarı için bir CSF 2.0 profili oluşturacaksınız. Her grup bu laboratuvarın siber biyogüvenlik çalışma grubu olacak; küçük bir Kurumsal Profil ve üç maddelik bir eylem planı üretecek. Saat 15:30’da da her grup sonuçlarını sunacak.

[Gruplar henüz oluşmadıysa:] Lütfen dört ila altı kişilik gruplar oluşturun. Mümkünse farklı kurumlardan ve farklı görevlerden kişiler aynı grupta olsun; tartışma o zaman çok daha verimli oluyor.

Kısa bir filmle başlayalım.""",

"film": """[Film yaklaşık on saniye. Film oynarken konuşmayın, başlık kartı gelince devam edin.]

Bir laboratuvar, altı fonksiyon, yirmi iki kategori ve kırk beş dakika. Bu oturumun bütün hikâyesi bu.""",

"mission": """Göreviniz şu. Lütfen dikkatle dinleyin.

▸ Siz HelixLab’in yeni ▸ siber biyogüvenlik çalışma grubusunuz.

Rektörlük sizi görevlendirdi ve sizden üç şey istiyor.

▸ Birinci çıktı: En değerli varlıklar ve kapsam. Bu laboratuvarda asla kaybedilmemesi, sızmaması ya da değiştirilmemesi gereken şeyler neler?

▸ İkinci çıktı: On iki kategori için Mevcut Profil ve Hedef Profil. Yani bugün neredesiniz, nerede olmalısınız?

▸ Üçüncü çıktı: Sorumlularıyla birlikte ilk üç eylem. Açıkları kapatmak için önce neyi yapacaksınız?

▸ Sunumlar saat 15:30’da yapılacak ve her grubun üç dakikası olacak.

Fark ettiyseniz bu üç çıktı, dün gördüğümüz NIST Hızlı Başlangıç Kılavuzu’nun ilk dört adımı: kapsamı belirle, topla, oluştur, analiz et ve planla. Yani dün teoride konuştuğumuzu şimdi kırk beş dakikada uygulayacaksınız.""",

"helix": """Şimdi laboratuvarınızı tanıyalım. Bu, HelixLab’in bilgi kartı. HelixLab kurgusal bir laboratuvar, ama buradaki her ayrıntı gerçek laboratuvarlarda gördüğüm şeylerden alındı.

Bir üniversite laboratuvarı, biyogüvenlik düzeyi 2.

▸ İnsanlar: Altı personel, on sekiz lisansüstü öğrenci ve kartlı girişi olan iki müşteri teknisyeni.

▸ Müşteriler: Üç biyoteknoloji şirketi laboratuvara numune gönderiyor ve karşılığında dizileme verisi alıyor.

▸ Ağ: Her şey için tek bir kampüs ağı var. Ve laboratuvarın Wi-Fi şifresi kapıda asılı.

Sistemlere bakalım.
▸ Bir yeni nesil dizileme cihazı. Windows 10 çalışan bir kontrol bilgisayarı var, veriler tedarikçinin bulutuna yükleniyor ve tedarikçinin uzaktan destek aracı kurulu.
▸ İki qPCR sistemi. Sonuçlar analiz bilgisayarına USB bellekle aktarılıyor.
▸ Dört adet −80 derece dondurucu. Wi-Fi’a bağlı bir alarm modülü var ve laboratuvar sorumlusuna SMS gönderiyor.
▸ LIMS bir bulut hizmeti ve tek bir ortak yönetici hesabı var.
▸ Analiz sunucusu Linux çalışıyor, on sekiz öğrenci hesabı var ve merkezi kayıt tutulmuyor.
▸ Ve yapay zekâ araçları: SOP taslakları için bir sohbet asistanı ve hücre sayımı için bir görüntü sınıflandırıcı.

Üç müşteri şirket size tedarik zinciri sorusunu hatırlatmalı; yapay zekâ araçları da bu sabahki oturumu.

Bu kartı grubunuzla birlikte okumanız için size iki dakika veriyorum.

[İki dakika bekleyin.]""",

"injects": """Laboratuvarınızı tanıdınız. Şimdi size bu ay HelixLab’de yaşanan üç şeyi anlatacağım.

▸ Cuma, saat 18:30. Laboratuvara “dizileme cihazı tedarikçisinden” geldiği görünen bir e-posta geliyor. E-posta, Pazartesiden önce bir indirme bağlantısıyla acil bir yazılım güncellemesi kurulmasını istiyor.

▸ Geçen hafta. Dondurucu alarmından gelen SMS’ler üç gün önce gelmez olmuş. Bir numune kontrolü yapılana kadar kimse bunu fark etmemiş.

▸ Dün. Bir öğrenci, proje kodlarını ve donör yaşlarını içeren bir müşteri numune listesini, yeniden biçimlendirmek için herkese açık bir yapay zekâ sohbet botuna yapıştırmış.

▸ Bu üç olayı, Mevcut Profili puanlarken kanıt olarak kullanın. ▸ Size bir ipucu vereyim: Her biri en az iki kategoriye işaret ediyor. Hangi kategoriler olduğunu şimdi söylemeyeceğim; sunumlardan sonra birlikte bakacağız.""",

"roles": """Gerçek bir çalışma grubunda herkes farklı bir yerden bakar. Bu yüzden her grupta altı rol var. Lütfen şimdi rolleri aranızda dağıtın.

▸ Laboratuvar sorumlusu: Toplantıya başkanlık eder ve son kararlar ondadır.
▸ Biyogüvenlik sorumlusu: Numunelerden, muhafazadan ve soğuk zincirden sorumludur.
▸ BT ve ağ sorumlusu: Sistemlerden, hesaplardan, kayıtlardan ve yedeklerden sorumludur.
▸ Veri sorumlusu: Müşteri verisinden, KVKK uyumundan ve yapay zekâ araçlarının kullanımından sorumludur.
▸ Tedarikçi yöneticisi: Sözleşmelerden, uzaktan erişimden ve satın almadan sorumludur.
▸ Raportör: Puanları kaydeder ve saat 15:30’da grubu adına sunar.

Grubunuz altı kişiden azsa, tedarikçi yöneticisi rolünü veri sorumlusuyla birleştirin.

Lütfen tartışırken kendi rolünüzün bakış açısından savunun. Özellikle BT sorumlusuyla biyogüvenlik sorumlusu arasında çıkacak tartışmalar, bu alıştırmanın en verimli kısmı olur.

[Rollerin dağıtılması için bir dakika bekleyin.]""",

"k-go": """[Kelimeler tek tek ekrana gelir; her birini görünce yüksek sesle okuyun.]

Bir laboratuvar.
Altı koltuk.
Kırk beş dakika.

Başlayın.

[Sayacı başlatın.]""",

"clock": """Kırk beş dakikayı beş aşamaya böldük. Sürelere lütfen uyun; sayacı burada ve etkileşimli araçta göreceksiniz.

▸ Birinci aşama, sekiz dakika: Kapsam ve en değerli varlıklar.
▸ İkinci aşama, on iki dakika: Mevcut Profili puanlayın.
▸ Üçüncü aşama, on dakika: Hedefi belirleyin ve açıkları bulun.
▸ Dördüncü aşama, on dakika: İlk üç eylemden oluşan eylem planı.
▸ Beşinci aşama, beş dakika: Üç dakikalık sunumunuzu hazırlayın.

Halkadaki dilimler her aşamaya düşen süre payını gösteriyor. Gördüğünüz gibi en uzun süre Mevcut Profili puanlamaya ayrıldı, çünkü asıl tartışma orada çıkacak.

Her aşamanın sonunda size haber vereceğim. Birinci aşamayla başlıyoruz.""",

"scope": """Birinci aşama, sekiz dakika. Kapsamı çizin ve en değerli varlıklarınızı seçin.

▸ Önce grup olarak şu üç soruyu birlikte yanıtlayın:
Hangi sistemler kapsamda? Hangileri kapsam dışında?
Hangi yasalar ve sözleşmeler geçerli? 7545 sayılı Kanun’u, KVKK’yı ve müşteri sözleşmelerini düşünün.
HelixLab iki hafta boyunca çalışamazsa kim zarar görür?

▸ Sonra en değerli üç varlığınızı seçin. Bunun için size üç soru öneriyorum.

▸ Kayıp: Asla ne kaybolmamalı? Bu, erişilebilirlik sorusudur.

▸ Sızıntı: Asla ne sızmamalı? Bu, gizlilik sorusudur.

▸ Tahrif: Kimse fark etmeden asla ne değişmemeli? Bu da bütünlük sorusudur.

Bu üçü, dün girişte konuştuğumuz bilgi güvenliğinin üç temel ilkesi: gizlilik, bütünlük ve erişilebilirlik.

Sekiz dakikanız başladı.

[Sekiz dakikanın sonunda:] Süre doldu. İkinci aşamaya geçiyoruz.""",

"rate": """İkinci ve üçüncü aşamalar. Şimdi on iki kategoriyi puanlayacaksınız. Her kategoriye 1’den 4’e bir puan vereceksiniz. Puanların anlamı şu:

▸ 1, Kısmi: Bu işin bir sahibi yok; biri hatırlarsa yapılıyor.
▸ 2, Risk bilgili: Önemli olduğu biliniyor ama yazılı bir politika değil.
▸ 3, Tekrarlanabilir: Yazılı, onaylı ve her seferinde aynı şekilde yapılıyor.
▸ 4, Uyarlanabilir: Ölçülüyor ve alınan derslerle sürekli iyileştiriliyor.

▸ Ekranın altındaki kodlar, bu laboratuvar için yirmi iki kategoriden seçtiğimiz on iki kategori. Bunları bilgi kartının ve az önceki üç olayın kanıt sunduğu kategoriler olarak seçtik.

İki önemli kural:

▸ Mevcut Profil için dürüst olun. Bilgi kartında ve olaylarda gördüğünüze göre puanlayın, umduğunuza göre değil.

▸ Hedef Profil için gerçekçi olun. Her yere 4 yazmayın. Bir eğitim ve araştırma laboratuvarı için hedeflerin çoğu 2 ya da 3’tür.

İkinci aşama, Mevcut Profili puanlama, on iki dakika. Ardından üçüncü aşama, hedefi belirleme ve açıkları bulma, on dakika. Süreniz başladı.""",

"worksheet": """Çalışma sayfanızın nasıl görünmesi gerektiğini göstermek için bu tamamlanmış bir örnek.

Her kategori için bir satır var. Solda kategori kodu ve adı. ▸ Ortada Mevcut puanınız, ▸ sağda Hedef puanınız. İki puan arasındaki fark, o kategorideki açığınızdır.

▸ Sağdaki radar grafik, bu puanların fonksiyon bazındaki ortalamasını gösteriyor. Yeşil alan bugün, turuncu çizgi hedef. Aradaki boşluk en büyük açıklarınızın nerede olduğunu bir bakışta gösterir.

Kâğıt üzerinde de çalışabilirsiniz, etkileşimli araçta da. Araçta her grubun kendi sekmesi var; kademelere tıkladığınızda radar ve en büyük üç açık kendiliğinden güncelleniyor.""",

"tool": """Etkileşimli araçtan kısaca bahsedeyim. Üç işe yarıyor: canlı puanlama, grupları karşılaştırma ve süreyi tutma.

▸ Aşama sayacı: Beş aşamanın her birini geriye sayıyor ve süre bitince kendiliğinden bir sonraki aşamaya geçiyor.

▸ Profil oluşturucu: Bir örnek sekmesi ve her grup için ayrı bir sekme var, Grup 1’den Grup 6’ya kadar. Kademelere tıkladığınızda radar grafik ve en büyük üç açık kendiliğinden güncelleniyor.

▸ Eylem planı: Üç satırlık bir form. Her satırda eylem, CSF kodu, sorumlu, tarih ve maliyet var.

▸ Bağlantı ekranda. Lütfen ikinci bir sekmede açın.

Bir uyarı: Puanlar, aracın açıldığı tarayıcıda saklanıyor. Bu yüzden her grup oturum boyunca tek bir dizüstü bilgisayar kullansın; raportörün bilgisayarı olursa en iyisi.""",

"plan": """Dördüncü aşama, on dakika: Eylem planı.

Üç eylem yazacaksınız ve her biri adı konmuş bir açığı kapatacak.

▸ Her eylem için beş sütun dolduracaksınız: Eylemin kendisi, kapattığı CSF kategorisi, sorumlusu, ne zamana kadar yapılacağı ve yaklaşık maliyeti.

▸ Size bir örnek vereyim. Eylem: Tedarikçilerin tüm uzaktan desteğini, çok faktörlü doğrulama ve talep kaydıyla, tek bir atlama sunucusundan geçir. CSF kategorisi: PR.AA ve GV.SC. Sorumlu: BT ve ağ sorumlusu. Süre: altı hafta. Maliyet: orta.

Sorumluyu bir kişinin adıyla değil, bir rolle yazın.

▸ Kolaylaştırıcı olarak gruplarınızın arasında dolaşacağım ve belirsiz eylemlere itiraz edeceğim. Örneğin biri “farkındalığı artır” yazarsa şunu soracağım: Neyin farkındalığı? Kimin için? Ne zamana kadar? Lütfen eylemlerinizi bu soruların cevabı belli olacak kadar somut yazın.

On dakikanız başladı.""",

"pitch": """Beşinci aşama, beş dakika: Sunumunuzu hazırlayın.

Saat 15:30’da her grubun üç dakikası, yani yüz seksen saniyesi olacak. Süreye kesinlikle uyacağız. Sunumunuz dört bölümden oluşsun.

▸ En değerli varlıklarınız: Neyi korumaya karar verdiniz?
▸ En büyük açığınız ve bunun kanıtı: Bilgi kartından ya da üç olaydan hangisi sizi bu sonuca götürdü?
▸ Üç eyleminiz ve sorumluları.
▸ Ve son olarak salona bir soru.

▸ Çubukların genişlikleri sürelerle orantılı. Gördüğünüz gibi en çok süre eylem planına ayrıldı.

Sondaki soru çok önemli. Deneyimime göre sunumların en iyi kısmı genellikle o soru oluyor; çünkü diğer grupların sizin göremediğiniz bir şeyi görmesini sağlıyor.

Beş dakikanız başladı.""",

"debrief": """[Bu slaytı grup sunumlarından sonra kullanın.]

Bütün gruplara teşekkür ediyorum. Şimdi birlikte bakalım: Üç olay aslında neye işaret ediyordu?

▸ Sahte tedarikçi e-postası. Bu olay tedarik zinciri risk yönetimine, yani GV.SC’ye; farkındalık ve eğitime, yani PR.AT’ye; ve kimlik ve erişim yönetimine, yani PR.AA’ya işaret ediyordu. Hangi gruplar bunu yakaladı?

▸ Susan dondurucu alarmı. Bu olay sürekli izlemeye, DE.CM’ye; varlık yönetimine, ID.AM’ye; ve olay yönetimine, RS.MA’ya işaret ediyordu. Üç gün boyunca kimsenin fark etmemesi, izlemenin bir sahibi olmadığını gösteriyor.

▸ Herkese açık sohbet botuna yapıştırılan müşteri verisi. Bu olay veri güvenliğine, PR.DS’ye; politikaya, GV.PO’ya; ve yine farkındalık ve eğitime, PR.AT’ye işaret ediyordu. Bu sabah konuştuğumuz yapay zekâ kullanım politikasının neden önemli olduğunu gösteriyor.

▸ Ve bir örüntü: Gruplarınızın çoğu en büyük açığı GV.SC’de ya da DE.CM’de buldu. Bu her çalıştayda gördüğüm bir örüntü. İkisinin de ortak özelliği şu: İkisi de büyük bir bütçe gerektirmiyor, ama ikisinin de bir sahibe ihtiyacı var. Yani en büyük açıklar esasen yönetişim işi. Bu da bizi iki günün başladığı yere, çarkın merkezindeki Yönetişim’e geri getiriyor.""",

"close": """Kapanıştan önce son bir söz.

▸ Bugün oluşturduğunuz profil bir taslak.

▸ Ama laboratuvarınız gerçek.

Sizden bir ricam var: Bu profili bir ay içinde kendi laboratuvarınız için tekrarlayın. Ve envanterden başlayın. Dondurucu kontrolcüsünden USB belleğe kadar, neye sahip olduğunuzu yazın. Gerisi oradan gelecek.

▸ Şimdi saat 15:30’daki grup sunumlarına ve tartışmaya geçiyoruz. ▸ Ardından kapanış, değerlendirme ve sertifika töreni ile çalıştayımızı tamamlayacağız.""",

"refs": """Bu oturumda kullandığımız kaynaklar burada. DOI’si olan her kaynak Crossref üzerinden doğrulandı.

Kendi laboratuvarınızda bu alıştırmayı tekrarlamak isterseniz iki belge çok işinize yarar: NIST’in Kurumsal Profiller için Hızlı Başlangıç Kılavuzu, yani SP 1301, ve NIST’in doldurulabilir Kurumsal Profil şablonu. Son bir not: HelixLab bu çalıştay için yazılmış kurgusal bir eğitim senaryosudur.""",

"thanks": """Bu iki gün boyunca gösterdiğiniz emek ve katılım için hepinize çok teşekkür ederim.

Şimdi grup sunumlarına geçiyoruz. İlk grubun raportörünü sahneye davet ediyorum. Lütfen üç dakikalık sürenize dikkat edin.""",
}
