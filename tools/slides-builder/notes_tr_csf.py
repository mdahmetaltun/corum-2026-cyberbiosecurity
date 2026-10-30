# Word-for-word Turkish speaker scripts — D1 CSF 2.0 (v2-tr). "▸" = the next element appears on screen.
N = {
"cover": """Tekrar hoş geldiniz, öğleden sonra oturumuna hepiniz hoş geldiniz.

Bu sabah Prof. Gargılı, biyolojik laboratuvarların neden siber güvenliğe ihtiyaç duyduğunu çok güzel anlattı. Şimdi bu ihtiyaca bir yapı, bir iskelet kazandıracağız. Bu iskeletin adı NIST Siber Güvenlik Çerçevesi, sürüm 2.0. Kısaca CSF 2.0 diyeceğim.

Önümüzdeki bir saatte beş şey yapacağız. Önce neden bir çerçeveye ihtiyaç duyduğumuzu konuşacağız. Sonra 2.0 sürümünde nelerin değiştiğine bakacağız. Ardından altı fonksiyonu tek tek göreceğiz ve her biri için bir laboratuvar örneği vereceğim. Sonra Çekirdeğin nasıl kurulduğuna, kategori ve alt kategorilere ineceğiz. Ve en sonunda, yarın öğleden sonra sizin bizzat kullanacağınız kısma geleceğiz: Kademeler ve Profiller.

Sağda gördüğünüz çark, bu saatin haritası. Merkezde Yönetişim, çevresinde beş fonksiyon. Saatin sonunda bu çarkın her bir diliminin sizin laboratuvarınızda neye karşılık geldiğini söyleyebiliyor olmanızı istiyorum.

Kısa bir filmle başlayalım.""",

"film": """[Film yaklaşık on dört saniye; döngüde oynar. Film oynarken konuşmayın, başlık kartı gelince devam edin.]

Gördüğünüz gibi, beş fonksiyonlu eski çark açılıyor ve merkeze yeni bir fonksiyon yerleşiyor: Yönetişim. Bu bir saatlik oturumun tamamı aslında bu tek görüntünün hikâyesi.""",

"spafford": """Bir alıntıyla başlamak istiyorum.

▸ Purdue Üniversitesi’nden Gene Spafford, bilgisayar güvenliğinin öncülerinden biridir. Şöyle der:

▸ “Gerçekten güvenli tek sistem,
▸ kapatılmış, bir beton bloğa gömülmüş
▸ ve kurşun kaplı bir odada mühürlenmiş,
▸ başında silahlı nöbetçiler olan sistemdir.”

[Kısa bir ara verin.]

▸ Bizim laboratuvarlarımız ise açık.

Dizileme cihazlarımız açık. −80 dondurucularımız açık. Biyogüvenlik kabinlerimiz, inkübatörlerimiz, LIMS sistemimiz açık; üstelik çoğu bir ağa bağlı.

Dolayısıyla bizim için soru hiçbir zaman “nasıl yüzde yüz güvenli oluruz” değil. Böyle bir şey yok. Asıl soru şu: Riski, binadaki herkesin, yani biyogüvenlik sorumlusunun, BT ekibinin ve yönetimin aynı şekilde anlayacağı bir dille nasıl yöneteceğiz? Bu oturumun cevabı o ortak dil: CSF 2.0.""",

"oxford": """Bunun soyut bir mesele olmadığını gösteren gerçek bir vakaya bakalım.

Şubat 2021. Oxford Üniversitesi, Yapısal Biyoloji bölümü. Bu bölüm o dönemde COVID-19 araştırmaları yapıyordu.

▸ Saldırganlar, biyokimyasal numune hazırlayan cihazların kontrol arayüzlerine ulaştı. Pompalar ve basınç kontrolleri açıktaydı. Forbes’la paylaşılan ekran görüntüleri, bu cihaz arayüzlerine canlı erişim olduğunu gösteriyordu.

▸ Bağlam önemli: COVID-19 üzerinde çalışan bir laboratuvar. Zaman damgaları, erişimin en az 14 Şubat’a kadar sürdüğünü düşündürüyordu.

▸ Üniversite durumu sınırladı ve İngiltere’nin Ulusal Siber Güvenlik Merkezi’ne, NCSC’ye bildirdi. Klinik araştırmaların ya da hasta verilerinin etkilenmediğini açıkladı.

▸ Peki buradan çıkaracağımız ders ne? Raporlara göre saldırganlar çok becerikli kişiler değildi. Mesele saldırganların ustalığı değil. Mesele şu: Cihaz kontrolcüleri birer bilgi teknolojisi varlığıdır, ama hiçbir envanterde yer almıyorlardı. Envanterde olmayan bir şeyi de kimse korumaz.

Bu cümleyi aklınızda tutun; çünkü bu saatin geri kalanında “envanter” kelimesine sık sık döneceğiz.""",

"why": """Peki neden bir çerçeveye ihtiyacımız var? Çünkü biyogüvenlik sorumlusu, BT ekibi ve rektör aynı konuyu üç farklı dille konuşuyor. Çerçeve bize ortak bir dil veriyor.

CSF’yi açmadan önce onun hakkında bilmeniz gereken üç şey var.

▸ Birincisi: CSF size ne yapacağınızı değil, neye ulaşmanız gerektiğini söyler. Çekirdek bir çıktılar listesidir. Bu çıktılara ulaştıracak kontrolleri, ürünleri ve yöntemleri sizin laboratuvarınız seçer. Yani “şu marka güvenlik duvarını alın” demez; “ağınızı korunmuş hâle getirin” der.

▸ İkincisi: Sürüm 2.0 artık yalnızca enerji santralleri ya da bankalar gibi kritik altyapılar için değil, her ölçekteki kuruluş için yazılmıştır. Bir üniversitenin merkez laboratuvarı da bu kapsamın içindedir.

▸ Üçüncüsü: CSF gönüllüdür. Bir mevzuat değil, bir haritadır. 7545 sayılı Siber Güvenlik Kanunu’nun ve KVKK’nın yerini almaz; onların yanında durur ve bu yükümlülükleri nasıl karşılayacağınızı düzenli bir şekilde göstermenize yardımcı olur.""",

"timeline": """Kısa bir tarihçe vereyim, çünkü 2.0’ın neden böyle olduğunu anlamak için nereden geldiğini bilmek gerekiyor.

▸ Sürüm 1.0, 12 Şubat 2014’te yayımlandı. ABD’nin 13636 sayılı Başkanlık Kararnamesi’nden doğdu ve hedefi kritik altyapıydı: enerji, su, finans gibi sektörler.

▸ Dört yıl sonra, 16 Nisan 2018’de sürüm 1.1 geldi. Beş fonksiyonu korudu; tedarik zinciri riski, kimlik yönetimi ve öz değerlendirme konularını ekledi.

▸ Ve 26 Şubat 2024’te bugün anlattığımız sürüm, 2.0 yayımlandı. İki büyük değişiklik var. Birincisi, hedef kitle artık tüm kuruluşlar. İkincisi, altıncı bir fonksiyon eklendi ve bu fonksiyon çarkın tam merkezine yerleşti: Yönetişim.

Yani on yılda çerçeve, “kritik altyapıyı koruyalım” noktasından “her kuruluş siber riskini yönetsin ve bunu üst yönetim sahiplensin” noktasına geldi.""",

"k-six": """[Kelimeler tek tek ekrana gelir; her satırı ekranda gördüğünüzde okuyun.]

Tanımlama. Koruma.
Tespit. Müdahale.
Kurtarma.

On yıl boyunca çerçeve bu beş fonksiyondu.

Ve 2.0 ile birlikte bir altıncısı geldi: Yönetişim.""",

"fivesix": """▸ Bu, CSF 1.1’in çarkı. Beş dilim: Tanımlama, Koruma, Tespit, Müdahale, Kurtarma.

Merkeze dikkat edin. Boş ve sanki nabız gibi atıyor. Yıllarca bu çarkın ortası boştu. Yani teknik işler tanımlanmıştı, ama bu işlerin kimin sorumluluğunda olduğu, hangi stratejiyle yürütüleceği, ne kadar riskin kabul edilebilir olduğu çarkın içinde değildi.

▸ Beş fonksiyon, ▸ altı oldu.

▸ Eski çarkın boş merkezinde artık diğer beşini yönlendiren bir fonksiyon duruyor. Bir sonraki slaytta bu çarkın nasıl dönüştüğünü göreceğiz.""",

"six": """İşte CSF 2.0’ın Çekirdeği. Merkezde Yönetişim, çevresinde diğer beş fonksiyon. Her birini NIST’in kendi tek cümlelik tanımıyla okuyorum.

▸ Yönetişim: Kuruluşun siber güvenlik risk yönetimi stratejisi, beklentileri ve politikası belirlenir, duyurulur ve izlenir.

▸ Tanımlama: Kuruluşun mevcut siber güvenlik riskleri anlaşılır.

▸ Koruma: Bu riskleri yönetmek için önlemler kullanılır.

▸ Tespit: Olası saldırılar ve ihlaller bulunur ve analiz edilir.

▸ Müdahale: Tespit edilen bir olaya yönelik eylemler gerçekleştirilir.

▸ Kurtarma: Etkilenen varlıklar ve faaliyetler eski hâline getirilir.

Başlığa bir kez daha bakın: “Aynı anda çalışan altı fonksiyon.” Bu bir kontrol listesi değil; önce birini bitirip sonra diğerine geçmiyoruz. Altısı da her gün, eş zamanlı olarak çalışır. Şimdi her birine tek tek yakınlaşacağız; çarkı sağ üst köşede takip edebilirsiniz.""",

"f-GV": """Merkezden başlıyoruz: Yönetişim.

Tanımı: Siber güvenlik risk yönetimi stratejisi, beklentiler ve politika belirlenir, duyurulur ve izlenir. Bu fonksiyon 2.0’da yeni ve bence siber biyogüvenlik tam olarak burada başlıyor.

Altı kategorisi var.
▸ Kurumsal Bağlam: misyonumuzu, paydaşlarımızı ve yasal yükümlülüklerimizi biliyor muyuz?
▸ Risk Yönetimi Stratejisi: ne kadar riski kabul ediyoruz?
▸ Roller, Sorumluluklar ve Yetkiler. Burada biraz durmak istiyorum. Çoğu laboratuvarda, laboratuvar cihazlarının siber riski resmî olarak hiç kimseye verilmemiştir. Herkes bir başkasının ilgilendiğini düşünür.
▸ Politika.
▸ Gözetim.
▸ Ve Tedarik Zinciri Risk Yönetimi. Bunu kırmızıyla vurguladık, çünkü laboratuvarlar için çok kritik: uzaktan erişimi olan cihaz tedarikçileri, bulut LIMS sağlayıcıları ve merkez laboratuvarlar için numunelerini ve verilerini sakladığımız dış müşteriler.

▸ Laboratuvardan bir soru: Ağa bağlı −80 derecelik bir dondurucunun riski kimin? Laboratuvar sorumlusunun mu, biyogüvenlik sorumlusunun mu, yoksa BT’nin mi? Bu soruyu salonda sorsam büyük ihtimalle üç farklı cevap alırım. Yönetişim, birinin bu soruyu yazılı olarak cevaplamasını sağlar.""",

"f-ID": """İkinci fonksiyon: Tanımlama.

Tanımı: Kuruluşun mevcut siber güvenlik riskleri anlaşılır. Daha basit söylersek: neye sahip olduğumuzu ve neyin ters gidebileceğini bilmek.

Üç kategorisi var:
▸ Varlık Yönetimi,
▸ Risk Değerlendirmesi,
▸ ve İyileştirme.

Varlık yönetimi diğer her şeyin temelidir. Bilmediğiniz bir şeyi koruyamazsınız, izleyemezsiniz, kurtaramazsınız.

▸ Laboratuvardan örnekler: Desteği bitmiş bir işletim sisteminde çalışan dizileme bilgisayarı. Wi-Fi’a bağlı dondurucu alarmı. Herkesin kullandığı ortak analiz sunucusu. Bunlar envanterde yoksa, korunmuyorlar demektir. Oxford’da gördüğümüz tam olarak buydu.

Bugün saat 15:30’da Prof. Merey laboratuvar varlık haritalama alıştırmasını yürütecek. O alıştırma, şu an gördüğünüz ID.AM kategorisinin uygulamadaki hâli olacak.""",

"f-PR": """Üçüncü fonksiyon: Koruma.

Tanımı: Kuruluşun siber güvenlik risklerini yönetmek için önlemler kullanılır. Çoğu insanın “siber güvenlik” deyince aklına gelen kısım burası.

Beş kategorisi var:
▸ Kimlik, Doğrulama ve Erişim,
▸ Farkındalık ve Eğitim,
▸ Veri Güvenliği,
▸ Platform Güvenliği,
▸ ve Altyapı Dayanıklılığı.

Laboratuvarlarda zayıf noktalar genellikle iki tanedir. Birincisi kimlik ve erişim: cihaz bilgisayarlarında herkesin kullandığı ortak bir kullanıcı adı ve şifre. İkincisi insanlar. Sızmaların çoğu hâlâ birinin bir şeyi yapmaya ikna edilmesiyle başlıyor. O yüzden farkındalık eğitimi isteğe bağlı bir ek değil, bir Koruma çıktısıdır.

▸ Laboratuvarda bu ne demek? Cihaz bilgisayarlarında kişiye özel hesaplar. Her uzaktan bağlantıda çok faktörlü doğrulama. Laboratuvar cihazları için ayrı bir ağ. Ve telefonla arayıp kendini “tedarikçi firmanın mühendisi” olarak tanıtan birini tanıyabilen personel.""",

"f-DE": """Dördüncü fonksiyon: Tespit.

Tanımı: Olası siber saldırılar ve ihlaller bulunur ve analiz edilir.

İki kategorisi var:
▸ Sürekli İzleme, yani sinyalleri toplamak,
▸ ve Olumsuz Olay Analizi, yani bu sinyallerin ne anlama geldiğine karar vermek.

Bu ikisi arasındaki farkı çok önemsiyorum. Sinyal toplamak tek başına yetmez.

▸ Bir örnek vereyim: 2021’de İrlanda sağlık hizmeti, HSE, bir fidye yazılımı saldırısına uğradı. Antivirüs yazılımı saldırganı 31 Mart’ta tespit etti. Ama yazılım yalnızca izleme modundaydı; uyarıyı üretti ve kimse ona göre harekete geçmedi. Fidye yazılımı ancak haftalar sonra, Mayıs ortasında patladı.

Yani sinyal oradaydı. Analiz edilmeyen bir tespit, sadece bir kayıt satırıdır. Bu vakayı yarın saat 11:30’daki oturumda ayrıntılı olarak açacağız.""",

"f-RS": """Beşinci fonksiyon: Müdahale.

Tanımı: Tespit edilen bir siber güvenlik olayına yönelik eylemler gerçekleştirilir.

Dört kategorisi var:
▸ Olay Yönetimi,
▸ Olay Analizi,
▸ Raporlama ve İletişim,
▸ ve Olay Etkisinin Azaltılması.

Laboratuvara özgü incelik bu son kategoride. Çünkü bizde en hızlı sınırlama hamlesi, numuneleri yok edebilir ya da biyolojik muhafazayı bozabilir.

▸ Şöyle düşünün: Bir siber olay sırasında BT ekibi panikle bir odanın elektriğini keserse, o odadaki dondurucular da gider. O yüzden kural şu: Bir biyogüvenlik olayına yol açmadan sınırlayın. Dondurucunun elektriğini değil, cihaz ağını izole edin. Ve bu yüzden biyogüvenlik sorumlusunun yeri müdahale masasıdır; müdahale planları BT ve biyogüvenlik tarafından birlikte yazılmalıdır.

Bir de raporlama boyutu var: Türkiye’de 7545 sayılı Siber Güvenlik Kanunu, kapsamdaki kuruluşların tespit ettikleri olayları Siber Güvenlik Başkanlığı’na gecikmeksizin bildirmesini öngörüyor.""",

"f-RC": """Altıncı ve son fonksiyon: Kurtarma.

Tanımı: Bir siber güvenlik olayından etkilenen varlıklar ve faaliyetler eski hâline getirilir.

İki kategorisi var:
▸ Kurtarma Planının Uygulanması,
▸ ve Kurtarma İletişimi.

Burada altını çizmek istediğim şey şu: Kurtarma yalnızca sunucuları yeniden çalıştırmak değildir. Kurtarma, laboratuvarın sunduğu hizmeti geri getirmektir.

▸ Örnek: Haziran 2024’te Londra’daki patoloji hizmet sağlayıcısı Synnovis bir fidye yazılımı saldırısına uğradı. NHS England’ın Eylül 2024 ortasına kadarki rakamlarına göre 10.146 poliklinik randevusu ve 1.705 planlı işlem ertelendi.

Bu aynı zamanda bir tedarik zinciri hikâyesi: Tek bir patoloji yüklenicisi, iki büyük hastane grubunu aylarca aksattı. Bir merkez laboratuvar olarak bizim de başkalarının Synnovis’i olabileceğimizi aklımızda tutalım.""",

"anatomy": """Fonksiyonlardan yapıya geçelim. Çekirdek nasıl kurulmuş?

[Sayılar ekranda yükselir.]

▸ Altı fonksiyon.
▸ Yirmi iki kategori.
▸ Yüz altı alt kategori.

Yani her fonksiyon birkaç kategoriye, her kategori de birkaç alt kategoriye ayrılıyor. Alt kategori, artık tek bir somut çıktıdır; “şu yapılmış mı, yapılmamış mı” diye sorulabilecek düzeydedir.

▸ Ve her alt kategori iki şeyle ilişkilidir: Uygulama Örnekleri ve Bilgilendirici Referanslar. Uygulama örnekleri, “bu çıktıya nasıl ulaşılır”a dair NIST’in önerileridir. Bilgilendirici referanslar ise o alt kategorinin ISO 27001 gibi diğer standartlardaki karşılıklarıdır.

2.0’daki önemli bir değişiklik: Bunlar artık çerçeve belgesinin içinde değil, çevrimiçi yayımlanıyor. Böylece NIST, yeni bir çerçeve sürümü çıkarmadan bunları güncelleyebiliyor.

Bir sonraki slaytta bu yapının içinden tek bir hat çekeceğiz: bir fonksiyondan, laboratuvar tezgâhındaki somut bir göreve kadar.""",

"drill": """Çekirdeğin içinden tek bir hat izleyelim: bir fonksiyondan tezgâhtaki göreve.

▸ Fonksiyon: Tanımlama.
▸ Kategori: ID.AM, Varlık Yönetimi.
▸ Alt kategori: ID.AM-01.

▸ Alt kategorinin metni şu: “Kuruluşun yönettiği donanımların envanteri tutulur.” Tek cümle.

▸ NIST’in bunun için verdiği uygulama örneği: BT, IoT, OT ve mobil cihazlar dahil her tür donanımın envanterini tutun. Buradaki OT, operasyonel teknoloji demek; yani fiziksel süreçleri kontrol eden cihazlar.

▸ Peki bir biyoteknoloji laboratuvarında bunun anlamı ne? Tezgâh düzeyinde bir envanter. Cihaz kontrol bilgisayarları ve bunların işletim sistemi sürümleri. Dondurucu, inkübatör ve kabin kontrolcüleri. Veri kaydediciler, tabletler, hatta USB bellekler.

Deneyimlerime göre laboratuvarların çoğu ilk olarak bu tek satırda başarısız oluyor: OT ve IoT’yi de kapsayan güncel bir donanım envanteri. Ve bu, bu öğleden sonraki alıştırmanın da ilk adımı olacak.""",

"tiers": """Şimdi profillere geçmeden önce kademeleri konuşalım. Kademeler şu soruyu cevaplar: Uygulamalarımız ne kadar titiz?

Dört kademe var.
▸ Kademe 1, Kısmi: İşler duruma göre yönetiliyor, kuruluş genelinde farkındalık sınırlı.
▸ Kademe 2, Risk Bilgili: Uygulamalar yönetimce onaylanmış ama henüz kuruluş çapında bir politika hâline gelmemiş.
▸ Kademe 3, Tekrarlanabilir: Resmî olarak onaylanmış, politika olarak yazılmış ve düzenli güncelleniyor.
▸ Kademe 4, Uyarlanabilir: Kuruluş, alınan derslere ve öngörücü göstergelere göre kendini sürekli uyarlıyor.

▸ Ama lütfen üstteki cümleyi unutmayın: Kademeler en üste çıkarılacak bir puan değildir. Daha yüksek, otomatik olarak daha iyi demek değildir. Riskinizin gerektirdiği kademeyi seçersiniz. Bir eğitim laboratuvarıyla bir BSL-3 merkez laboratuvarının hedefleri aynı olamaz.

Turuncu çerçeveyle işaretlediğimiz Kademe 3, birçok araştırma birimi için makul bir hedeftir. Kademe 4 ise ciddi bütçe ve personel gerektirir.""",

"profiles": """Ve gelelim bu oturumun en uygulamalı kısmına: Profiller.

Profil, CSF’nin sizin laboratuvarınıza uygulanmış hâlidir.

▸ Önce şu soruyu sorarız: Neredeyiz? Bunun cevabı Mevcut Profil’dir; bugün hangi çıktılara ulaştığınızı gösterir.

▸ Sonra şunu sorarız: Nerede olmalıyız? Bunun cevabı Hedef Profil’dir; risklerinizi ve yükümlülüklerinizi göz önüne aldığınızda hangi çıktılara ihtiyaç duyduğunuzu gösterir.

▸ Bu ikisinin arasındaki fark, açığınızdır. Bu açık, çıktı çıktı tek tek görülür.

▸ Açığı kapatmak için bir eylem planı yaparsınız: sorumlular, bütçe ve tarihlerle önceliklendirilmiş işler.

▸ Ve döngü: Planı uygularsınız, sonra Mevcut Profili yeniden puanlarsınız ve tekrar edersiniz.

Yarın saat 14:30’da her grup tam olarak bunu yapacak: kurgusal bir laboratuvar için mevcut profil, hedef profil, açıklar ve üç maddelik bir eylem planı.""",

"radar": """Size bunun nasıl göründüğünü çözümlü bir örnekle göstereyim. Önemli bir uyarı: Bu temsilî bir profil; sayılar örnektir, gerçek bir birimin verisi değildir.

Dış sanayi müşterilerine hizmet veren bir üniversite merkez laboratuvarı düşünün. Radar grafikte her fonksiyon için 1’den 4’e kadar kademe var.

▸ Mavi alan bugünü, yani Mevcut Profili gösteriyor.
▸ Kesikli turuncu çizgi ise birimin yönetim kurulunun kararlaştırdığı hedefi.

İkisi arasındaki boşluklar açıklar. En büyük üç açığa bakalım:

▸ Birincisi tedarik zinciri: Müşteri numuneleri ve verileri dışarıdan geliyor ve tedarikçiler uzaktan bağlanıyor.
▸ İkincisi tespit: Cihaz bilgisayarlarından merkezi kayıt toplanmıyor.
▸ Üçüncüsü kurtarma: Yedekler var, ama bir geri yükleme hiç test edilmemiş.

Müşterilerinin numunelerini ve verilerini kabul eden bir birim için tedarik zinciri yönetişimi, yani GV.SC, genellikle en büyük ve bizim sektörümüze en özgü açıktır.""",

"kinds": """İki tür profil olduğunu da bilmeniz gerekiyor.

▸ Birincisi Kurumsal Profil: Sizin profiliniz. Tek bir kuruluş ya da birim için Mevcut ve Hedef profil. NIST bunun için bir Hızlı Başlangıç Kılavuzu ve doldurulabilir bir şablon yayımlıyor.

▸ İkincisi Topluluk Profili: Bir sektör ya da konu için ortak hazırlanmış profillerdir. Sıfırdan başlamak yerine bunlardan başlayabilirsiniz. Bu çalıştay için önemli iki tanesi var. Biri SP 800-61 Revizyon 3; Nisan 2025’te yayımlandı ve olay müdahalesini doğrudan CSF 2.0 fonksiyonlarına göre düzenliyor. Diğeri Siber Yapay Zekâ Profili, NIST IR 8596; Aralık 2025’te ön taslak olarak yayımlandı ve üç odak alanı var: Güvenceye al, Savun, Engelle.

▸ Bu ikincisi bizi doğrudan yarına bağlıyor: Yarın sabah saat 09:15’te NIST Yapay Zekâ Risk Yönetimi Çerçevesi ile, tam olarak bu Siber YZ Profili’nden başlayacağız.""",

"steps": """Peki bir profili pratikte nasıl çıkarırız? NIST’in Kurumsal Profiller için Hızlı Başlangıç Kılavuzu beş adım öneriyor.

▸ Bir: Kapsam. Hangi birim, hangi sistemler, hangi riskler?
▸ İki: Topla. Politikalarınızı, envanterlerinizi ve yasal yükümlülüklerinizi bir araya getirin.
▸ Üç: Oluştur. Mevcut durumu ve hedefi puanlayın.
▸ Dört: Analiz et. Açıkları bulun ve bunları önceliklendirilmiş bir eylem planına dönüştürün.
▸ Beş: Uygula. Harekete geçin, sonra profili güncelleyin.

▸ Yarın saat 14:30’daki alıştırmada, kurgusal bir biyoteknoloji laboratuvarı için birinci ile dördüncü adımları kırk beş dakikaya sığdıracağız. Beşinci adım ise sizin kendi laboratuvarınıza döndüğünüzde başlayacak.""",

"turkiye": """Şimdi konuyu kendimize, Türkiye’ye getirelim. Gönüllü bir çerçeve, ama bağlayıcı yükümlülükler.

▸ Birincisi 7545 sayılı Siber Güvenlik Kanunu. 19 Mart 2025’te Resmî Gazete’de yayımlandı. Kapsamdaki kuruluşlar, tespit ettikleri açıkları ve olayları Siber Güvenlik Başkanlığı’na gecikmeksizin bildirmek zorunda. CSF’deki karşılığı RS.CO, yani raporlama ve iletişim, ve GV.OC, yani kurumsal bağlam ve yasal gerekliliklerin anlaşılması.

▸ İkincisi 6698 sayılı Kişisel Verilerin Korunması Kanunu. Kişisel veri ihlalleri, Kurul’un 2019/10 sayılı kararına göre 72 saat içinde KVK Kurulu’na bildirilir. CSF’deki karşılığı yine RS.CO ve veri güvenliği, PR.DS.

▸ Uygulamada şunu bilmenizi istiyorum: CSF bu yükümlülüklerin yerini almaz. CSF, bu yükümlülükleri nasıl karşıladığınızı düzenli bir şekilde gösterdiğiniz yerdir. Hangi yükümlülüklerin kurumunuza uygulandığını ise mutlaka kurumunuzun hukuk birimiyle teyit edin.""",

"keep": """Toparlayalım. Bu oturumdan aklınızda kalmasını istediğim üç şey var.

▸ Bir: Önce yönetişim. Riskin bir sahibi olmalı; adı yazılı olarak belli olmalı.

▸ İki: Neyi çalıştırdığını bil. Envanter; ama OT ve IoT dahil, yani dondurucu kontrolcüsünden USB belleğe kadar.

▸ Üç: Önce profil, sonra eylem. Bulunduğunuz yeri olmanız gereken yerle karşılaştırın; satın almayı ondan sonra düşünün.

▸ Bu fikirler bugün ve yarın devam ediyor. Bugün saat 15:30’da Prof. Dr. Gökçe Merey’in laboratuvar varlık haritalama alıştırması var; yani ikinci maddenin uygulaması. Yarın saat 14:30’da ise kendi laboratuvarınızın profilini oluşturacaksınız; yani üçüncü maddenin uygulaması.""",

"refs": """Bu oturumda kullandığım kaynakların tamamı burada. Bu slayttaki her DOI Crossref üzerinden tek tek doğrulandı; kaynak başlıklarını özgün dillerinde bıraktım.

Özellikle iki tanesini okumanızı öneririm: CSF 2.0’ın kendisi, yani NIST CSWP 29, ve siber biyogüvenliği bir disiplin olarak tanımlayan Murch ve arkadaşlarının 2018 tarihli makalesi. Sunumu sizinle paylaşacağım, bu listeye oradan ulaşabilirsiniz.""",

"thanks": """Dinlediğiniz için çok teşekkür ederim.

Şimdi söz sizde. Çerçeve, fonksiyonlar ya da profiller hakkında sorularınızı alabilirim.

[Zaman kısıtlıysa:] Zamanımız sınırlı olduğu için bir iki soru alalım. Aklınıza takılan diğer soruları öğleden sonraki alıştırmada ya da arada konuşabiliriz. Teşekkürler.""",
}
