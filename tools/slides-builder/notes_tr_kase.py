# Word-for-word Turkish speaker scripts — D3 Institutional Infrastructure (v2-tr). "▸" = the next element appears on screen.
N = {
"cover": """Hoş geldiniz. Bu sabahki üçüncü oturumumuz ve bu oturum diğerlerinden biraz farklı: Uygulamalı bir vaka çalışması.

Dün CSF 2.0’ın fonksiyonlarını, bu sabah da yapay zekâ riskini konuştuk. Şimdi bu çerçeveleri bir kurumun gerçek altyapısına indireceğiz. Başlığımız: Kurumsal Siber Güvenlik Altyapısı.

Oturumu iki parçada yürüteceğim. Önce büyük ve gerçek bir olayı ele alacağız; bir kurumun altyapısının nasıl çöktüğünü adım adım göreceğiz. Sonra birleşik bir vakayı inceleyeceğiz: dış sanayi müşterilerine de hizmet veren bir üniversite merkez araştırma laboratuvarı. Bu laboratuvarı iki aşamada önce değerlendireceğiz, sonra yeniden kuracağız.

Göreceğiniz her şey dün konuştuğumuz CSF fonksiyonlarına bağlanıyor. Bu yüzden öğleden sonraki alıştırma size çok tanıdık gelecek.

Önce bir filmle başlayalım.""",

"film": """[Film yaklaşık on beş saniye; döngüde oynar. Film oynarken konuşmayın, başlık kartı gelince devam edin.]

Az önce gördüğünüz zaman çizelgesi gerçek. İrlanda’nın ulusal sağlık hizmeti, 2021. İlk e-postadan fidye yazılımının patlamasına kadar yaklaşık sekiz hafta. Şimdi bu sekiz haftayı birlikte açalım.""",

"hse": """İrlanda Sağlık Hizmeti, kısaca HSE, 2021. İlk e-postadan fidye yazılımına sekiz hafta.

Bu ayrıntıların tamamı, Aralık 2021’de yayımlanan bağımsız PwC olay sonrası inceleme raporundan.

▸ 16 Mart 2021: Kötü amaçlı bir e-posta bir iş istasyonuna ulaşıyor.

▸ 18 Mart: E-posta açılıyor. Ekteki Excel dosyası iniyor ve saldırgan sisteme tutunuyor.

▸ 31 Mart: Antivirüs yazılımı şüpheli etkinliği tespit ediyor. Ama yazılım yalnızca izleme modunda; yani uyarıyı kaydediyor, engellemiyor. Ve kimse o uyarıya göre harekete geçmiyor.

▸ 7 ile 13 Mayıs arası: Güvenlik hizmet sağlayıcısı, on altıdan fazla sistemde ele alınmamış tehdit olduğunu bildiriyor. Yine yeterli bir müdahale olmuyor.

▸ 14 Mayıs, sabah saat dört: Conti fidye yazılımı devreye giriyor. Ülkenin sağlık BT sistemleri ülke çapında kapatılmak zorunda kalıyor.

Turuncu noktalar, kurumun harekete geçebileceği anlar.

▸ Saldırganın içeride kalma süresi: yaklaşık sekiz hafta. ▸ İlk müdahalenin maliyeti, HSE’nin İrlanda parlamentosunun Kamu Hesapları Komitesi’ne bildirdiği rakamla, yaklaşık 53 milyon avro.

▸ Ve PwC’nin kök bulgusu: Saldırıya dayanacak şekilde hiç tasarlanmamış, parçalı ve eski bir BT altyapısı ve siber riskin tek bir sahibinin olmaması. Dikkat edin: Kök bulgu teknik değil, bir yönetişim bulgusu.""",

"lesson": """Bu vakadan çıkaracağımız tek bir ders varsa o da şu:

▸ Sinyaller oradaydı.

▸ Onlara göre harekete geçecek yapı yoktu.

[Kısa bir ara verin.]

Teknoloji sızmayı tespit etti. Antivirüs gördü, güvenlik sağlayıcısı uyardı. Ama kurum yanıt vermedi; çünkü kimin karar vereceği, kimin müdahale edeceği belli değildi.

▸ O yüzden bu oturum boyunca “altyapı” derken yalnızca donanımı kastetmiyorum. Altyapı; riskin sahibinin, izleyenin ve karar verebilecek olanın kim olduğudur. Dün Yönetişim’i çarkın tam merkezine koymamızın nedeni de buydu.""",

"layers": """Bir kurumun altyapısına bakarken üç katman düşünüyorum. Bu, sosyal mühendislik eğitimlerinde kullandığımız modelin aynısı.

▸ Birincisi teknik katman: ağlar, cihaz bilgisayarları, kullanıcı hesapları, kayıtlar ve yedekler.

▸ İkincisi insan katmanı: personel, öğrenciler, müşteri teknisyenleri ve tedarikçi mühendisleri.

▸ Üçüncüsü fiziksel katman: kapılar, dondurucular, kabinler, numune depoları ve USB portları.

▸ Unutmamamız gereken şey şu: Herhangi bir katmandaki zayıflık diğer ikisini de açar. Kilitsiz bir kapı, bir bilgisayara erişim demektir; bir bilgisayara erişim, bir dondurucunun alarm ayarlarına erişim demektir. Ve saldırmanın en ucuz yolu genellikle insan katmanıdır. Birazdan vakamızdaki her bulgunun bu üç katmandan birine ait olduğunu göreceksiniz.""",

"facility": """Şimdi vakamıza gelelim. Önemli bir not: Bu tek bir gerçek kurum değil; tipik merkez laboratuvarlardan derlenmiş birleşik bir örnek ve sayılar temsilî.

Sanayiye de hizmet veren bir merkez laboratuvar düşünün.

▸ Kırktan fazla cihaz var ve bunların çoğunun kendine ait bir kontrol bilgisayarı var.

▸ Altmış kullanıcı var: personel, öğrenciler ve ziyarete gelen müşteri teknisyenleri.

▸ On iki dış sanayi müşterisi, bu laboratuvara numune ve veri gönderiyor.

▸ Ve sekiz tedarikçinin bir şekilde uzaktan destek erişimi var.

▸ Bu laboratuvarı özel kılan şey dış müşteriler. Yalnızca kendi araştırmacılarına hizmet veren bir laboratuvarın riski içseldir. Ama on iki şirketin numunelerini ve verilerini tutan bir laboratuvar, o şirketlerin tedarik zincirinin bir parçasıdır. Buradaki bir ihlal, on iki şirket için bir ihlal demektir. CSF diliyle bu vakanın ağırlık merkezi GV.SC, yani tedarik zinciri risk yönetimi.

Bu yapı bana çok tanıdık; Sivas Cumhuriyet Üniversitesi’nde merkezi araştırma laboratuvarımızla ilgili proje tasarımımızı da tam olarak bu dış müşteri boyutu şekillendirmişti.""",

"phases": """Böyle bir laboratuvarı nasıl ele alırız? İki aşamada, toplam on haftada.

▸ Birinci aşama, ilk dört hafta: Değerlendir. Envanter çıkarılır, ağ haritası çizilir, personelle görüşmeler yapılır ve Mevcut Profil oluşturulur.

▸ İkinci aşama, beşinci ile onuncu haftalar arası: Kur ve eğit. Ağ bölümlenir, kimlik yönetimi düzenlenir, merkezi kayıt kurulur, yedekler gözden geçirilir, planlar yazılır ve insanlar eğitilir.

▸ Sıra çok önemli: Önce değerlendirme, sonra hedefli yatırım. Benim gördüğüm en yaygın ve en pahalı hata, envanter çıkarmadan araç satın almak. Envanteriniz ve Mevcut Profiliniz olmadan, hangi yatırımın hangi açığı kapatacağını bilemezsiniz.""",

"jewels": """Birinci aşamaya şu soruyla başlıyoruz: Asla kaybedilmemesi gereken nedir?

Ekrandaki halkaları dıştan içe doğru açacağım. Bunlar saldırı yüzeyinin katmanları.

▸ En dışta çevre: internet, e-posta, tedarikçiler ve bulut LIMS.

▸ Sonra uç noktalar ve hesaplar: bilgisayarlar, dizüstüler ve ortak kullanılan oturumlar.

▸ Sonra laboratuvar cihazları ve operasyonel teknoloji: cihaz bilgisayarları, dondurucu ve oda izleyicileri.

Listeyi göstermeden önce size sormak istiyorum: Sizin laboratuvarınızda en değerli varlıklar neler? Kaybederseniz telafisi olmayan şeyler?

[Birkaç cevap alın.]

▸ Bu vakada en değerli varlıklar şunlar: Müşteri numuneleri, sonuçları ve sözleşmeleri. Cihaz kontrol ve kalibrasyon verileri. Soğuk zincir, yani −80 derece depolama ve onun alarmları. Ve yayımlanmamış araştırma verileri ile fikrî mülkiyet.

Soğuk zincir genellikle unutulan kalemdir. Ama Wi-Fi’a bağlı bir dondurucu alarmı, sonucu biyogüvenliğe dokunan bir siber varlıktır.""",

"findings": """Birinci aşamanın sonunda tipik olarak ne buluruz? Ortak araştırma birimlerinin hemen her değerlendirmesinde çıkan sekiz bulgu. Tekrar söyleyeyim, bunlar temsilî; tek bir denetimden alınmadı.

▸ Cihaz bilgisayarları desteği bitmiş Windows sürümlerinde çalışıyor ve yama yapılamıyor. Yüksek risk.

▸ Tek, düz bir ağ var: ofis bilgisayarları, Wi-Fi ve cihazlar aynı segmentte. Yüksek risk.

▸ Cihaz bilgisayarlarında ortak oturumlar var; müşteri teknisyenleri personel hesaplarını kullanıyor. Yüksek risk.

▸ Tedarikçilerin uzaktan destek araçları kurulu ve sürekli açık. Yüksek risk.

▸ Sonuçlar cihazlar ile analiz bilgisayarları arasında USB bellekle taşınıyor. Orta risk.

▸ Merkezi kayıt yok ve cihaz bilgisayarlarının saatleri dakikalarca kayıyor. Orta risk.

▸ Yedekler var, ama kimse bir geri yüklemeyi hiç test etmemiş. Yüksek risk.

▸ Ve hiçbir olay planında biyogüvenlik sorumlusunun adı geçmiyor. Orta risk.

Her bulgunun yanında bir CSF kodu var. Bu eşleştirme çok önemli: Bir şikâyet listesini, bir Mevcut Profile dönüştüren şey bu eşleştirmedir.

Size bir soru: Bu sekiz bulgudan kaçı sizin binanız için de doğru?""",

"schneier": """Bulgulardan birkaçı insanlarla ilgiliydi. İnsan katmanına biraz daha yakından bakalım. Her eğitimde kullandığım bir söz var.

▸ Bruce Schneier der ki: “Amatör sistemi hackler,
▸ profesyonel insanı.”

Neden? Çünkü teknik kontroller sistemlere saldırmanın maliyetini artırır. Güvenlik duvarları, yamalar, şifreleme bir saldırganın işini zorlaştırır. Bu yüzden deneyimli saldırganlar bu kontrollerin etrafından dolaşır. Ve en kolay yol, insanlardan geçer.""",

"se": """Sosyal mühendisliğin bu vakada nasıl işleyeceğini görelim. Üç aşama var ve dikkat ederseniz hepsi göz önünde.

▸ Birinci aşama, araştır. Saldırgan laboratuvarın web sitesinden personel adlarını öğrenir. Kamu ihale belgelerinden hangi firmadan hangi cihazın alındığını öğrenir. Yayımlanmış makalelerin yöntem bölümlerinden cihaz modellerini öğrenir. Bunların hiçbiri gizli değil; hepsi kamuya açık.

▸ İkinci aşama, geliştir. Telefon çalar. Arayan kişi kendini dizileme cihazı tedarikçisinin servis mühendisi olarak tanıtır. Cihazın modelini biliyor, laboratuvar sorumlusunun adını biliyor. Çok samimi ve yardımsever.

▸ Üçüncü aşama, istismar et. “Pazartesi günkü yazılım güncellemesinden önce, lütfen şu uzaktan destek aracını kurar mısınız?”

▸ Peki savunma ne? Savunma bir ürün değil, bir süreç. Tedarikçi erişimi yalnızca atlama sunucusundan yapılır. Erişim bir talep kaydıyla istenir. Ve arayan kişi, telefonu kapatıp, sizin elinizde zaten olan, bilinen bir numaradan geri aranarak doğrulanır.""",

"pressures": """Saldırganlar bu tür aramalarda üç temel baskı kullanır. Bunları tanımak, personelimizi korumanın en etkili yolu.

▸ Ego: “Bu sistemi gerçekten anlayan tek kişi sizsiniz.” Kendinizi önemli hissettirerek yardım etmenizi sağlar.

▸ Sempati: “Bu bugün düzelmezse işimi kaybedeceğim.” Vicdanınıza seslenir.

▸ Yıldırma: “Rektörlükten arıyoruz” ya da “Denetim kurumundan arıyoruz. Hemen yapın ve kimseye söylemeyin.” Otoriteyle korkutur.

▸ Bu üçünün ortak imzası şu: Aciliyet artı gizlilik. Bir istek hem acil hem de gizli tutulması gereken bir şey olarak geliyorsa, durun. Personelinize bu iki işarette durmayı öğretin. Ve bildirimi kolay ve suçlamasız kılın; çünkü yanıldığını fark eden birinin bunu korkmadan söyleyebilmesi gerekir.""",

"k-build": """[Kelimeler tek tek ekrana gelir; her birini görünce okuyun.]

Birinci aşama bitti. Değerlendirdik.

Şimdi ikinci aşama:
Kur.
Eğit.
Ve prova et.""",

"arch": """İkinci aşamaya hedef mimariyle başlıyoruz. Dört kelimede özetleyebilirim: Bölümle, kapıla, izle, kopya tut. Mimariyi dört adımda kuracağım.

▸ Birinci adım bölgeler. İnternetten gelen her şey önce güvenlik duvarından geçiyor. Arkasında üç ayrı bölge var. Kampüs BT bölgesi: e-posta, ofis bilgisayarları, Wi-Fi ve öğrenciler. Laboratuvar OT bölgesi: kendi ayrı sanal ağında, yani VLAN’ında; cihaz bilgisayarları ve dondurucu izleyicileri burada, varsayılan olarak internete kapalı ve herkes kişisel hesabıyla giriyor. Ve müşteri verisi bölmesi: her müşterinin verisi ayrı tutuluyor ve erişim sözleşmeye göre veriliyor.

▸ İkinci adım atlama sunucusu. Tedarikçilerin laboratuvara uzaktan girebileceği tek kapı. Çok faktörlü doğrulama zorunlu, her oturum kaydediliyor ve her erişim bir talep kaydıyla açılıyor.

▸ Üçüncü adım merkezi kayıt. Bütün bölgelerden gelen kayıtlar tek bir yerde toplanıyor; tüm saatler NTP ile eşzamanlı ve saklama süresi önceden tanımlı.

▸ Dördüncü adım çevrim dışı yedek. Değiştirilemez bir kopya ve en önemlisi: geri yüklemesi test edilmiş.

Bu dört öğenin her biri, birkaç slayt önce gördüğümüz bulgulardan birini kapatıyor.""",

"change": """Atlama sunucusunda çok faktörlü doğrulamada neden bu kadar ısrar ettiğimi bir vakayla göstereyim.

Change Healthcare, Şubat 2024. ABD’de sağlık sektörünün ödeme ve veri altyapısını işleten bir şirket.

[Sayaç yükselir.]

▸ 192,7 milyon kişi. Bu, ABD Sağlık Bakanlığı’nın Sivil Haklar Ofisi’ne Temmuz 2025’te bildirilen rakam. ABD’de kayıtlara geçmiş en büyük sağlık verisi ihlali.

▸ Peki saldırganlar nasıl girdi? Bir uzaktan erişim portalından. ▸ Ve o portal çok faktörlü doğrulama istemiyordu. Yalnızca bir kullanıcı adı ve şifre.

▸ Buradan çıkan kural çok net: Her uzak erişim yolunda çok faktörlü doğrulama. Ve önceliği tedarikçi yollarına verin. Bizim birimimiz için bu; atlama sunucusu, her VPN bağlantısı ve her uzak masaüstü yolu demek. CSF’deki karşılığı PR.AA: kimlik, doğrulama ve erişim.""",

"synnovis": """Şimdi tedarik zinciri konusuna dönelim, ama bu kez ters taraftan bakalım: Laboratuvar tedarikçi olduğunda ne olur?

▸ Synnovis, Haziran 2024. Londra’da King’s College Hospital ile Guy’s and St Thomas’ hastanelerine patoloji hizmeti veren bir laboratuvar hizmeti sağlayıcısı. Tek bir laboratuvar hizmeti sağlayıcısı, iki hastane grubu ve aylarca süren bir aksama.

▸ NHS England’ın Eylül 2024 ortasına kadarki rakamlarına göre 10.146 poliklinik randevusu ertelendi. ▸ 1.705 planlı işlem ertelendi.

▸ Ve Haziran 2025’te King’s College Hospital, saldırının bir hastanın ölümüne katkıda bulunan etkenlerden biri olduğunu doğruladı. Yani bir siber olay, bir laboratuvar üzerinden bir insanın hayatına dokundu.

▸ Şimdi tersinden bakın: Bizim merkez laboratuvarımız da on iki müşterisi için bir Synnovis. Bu yüzden bir birim olarak şunlara ihtiyacımız var: Güvenlik ve bildirim maddeleri içeren müşteri sözleşmeleri, müşteri bazında veri ayrımı ve bir olay anında her müşteriye saatler içinde haber verecek bir plan. GV.SC iki yönde de geçerlidir.""",

"telemetry": """HSE vakasına geri dönelim: Sinyaller oradaydı ama kimse görmedi. Göremediğinizle savaşamazsınız. Bu, CSF’de DE.CM, sürekli izleme.

Bir merkez laboratuvar için altı kayıt kaynağı öneriyorum.

▸ Güvenlik duvarı. ▸ Kimlik ve dizin hizmeti, yani kim ne zaman oturum açtı. ▸ Atlama sunucusu oturumları. ▸ Cihaz bilgisayarlarındaki olaylar. ▸ LIMS denetim izi. ▸ Ve dondurucu ile oda alarmları.

Bu sonuncuyu bilerek turuncuya boyadık. Çünkü dondurucu alarmı hem bir güvenlik sinyali hem de bir biyogüvenlik sinyalidir.

Ve üç kural:

▸ Bir: Her saati eşzamanlayın. NTP olmadan, farklı cihazlardan gelen kayıtlarla bir olayın zaman çizelgesini yeniden kuramazsınız.

▸ İki: Kayıtları merkezde toplayın. Çünkü ele geçirilen bir makinedeki kayıtlar, saldırganın ilk sildiği şeydir.

▸ Üç: Saklama süresine önceden karar verin. HSE saldırganı sekiz hafta içerideydi. İki haftalık kayıt tutuyorsanız, sekiz haftalık bir sızma sizin için görünmezdir. En az o kadar saklayın.

Sağdaki terminal, böyle bir sistemin sabah saat dörtte nasıl göründüğünü canlandırıyor: Saatler eşzamanlı, tedarikçi girişi çok faktörlü doğrulamayla yapılmış ve üçüncü dondurucu bir alarm veriyor.""",

"taxonomy": """Bir sinyal geldiğinde ilk yapmanız gereken, müdahale etmeden önce onun düzeyini adlandırmaktır. Dört düzey var.

▸ Olgu: Gözlemlenebilir herhangi bir oluş. Örneğin LIMS’te başarısız bir oturum açma denemesi.

▸ Olay: Politikayı ihlal eden ya da faaliyetleri tehdit eden bir durum. Örneğin bir cihaz bilgisayarında zararlı yazılım bulunması.

▸ İhlal: Doğrulanmış bir veri kaybı. Örneğin müşteri sonuçlarının dışarı kopyalandığının anlaşılması.

▸ Kriz: Güvenliği ya da kurumun kendisini tehdit eden durum. Örneğin dondurucuların ya da muhafazanın etkilenmesi.

Neden bu ayrım bu kadar önemli? Çünkü uyarıların çoğu olgudur. Her olguya kriz derseniz ekibinizi tüketirsiniz. Bir krize olgu derseniz müdahaleyi geciktirirsiniz. O yüzden bu eşikleri, ihtiyaç duymadan önce yazılı olarak belirleyin.

Ve laboratuvar için özel bir kural: Muhafazaya ya da numune canlılığına dokunan her şey, doğrudan en üst düzeye, krize çıkar.""",

"raci": """Bir olay ilan edildiğinde kim ne yapacak? Bunun için bir komuta yapısına ihtiyacımız var. Kim karar verir, kim yapar, kim bilir?

Bu tablo bir RACI matrisi; olay müdahalesi eğitimlerimden uyarladım. Sütunlarda roller var: olay sorumlusu, BT ve ağ, biyogüvenlik sorumlusu, laboratuvar sorumlusu, hukuk ve veri koruma sorumlusu, iletişim.

[Satırlar tek tek gelir.]

▸ Olay ilan etmek: Hesap veren olay sorumlusu, uygulayan BT.
▸ Laboratuvar ağını izole etmek: Yine hesap veren olay sorumlusu, uygulayan BT.
▸ Numuneler ve muhafaza hakkında karar vermek: İşte laboratuvarlar için yaptığım tek değişiklik burada. Bu satırda hesap veren biyogüvenlik sorumlusu, uygulayan laboratuvar sorumlusu. Yani BT, bir dondurucu odasının elektriğini kendi yetkisiyle kesemez.
▸ 7545 sayılı Kanun ve KVKK kapsamında bildirim yapmak: Hesap veren olay sorumlusu, uygulayan hukuk birimi.
▸ Müşterileri ve kamuoyunu bilgilendirmek: Hesap veren olay sorumlusu, uygulayan iletişim birimi.

▸ Harflerin anlamı: R uygulayan, A hesap veren, C danışılan, I bilgilendirilen. Tek bir kural var: Her satırda yalnızca bir A olur. Bir işin iki hesap vereni varsa, aslında hiç hesap vereni yok demektir.""",

"golden": """Bir olay sırasında öncelikler mutlaka çatışır. O an tartışmaya vaktiniz olmaz. O yüzden sıralamayı önceden belirlemek gerekir. Olay müdahalesindeki altın kural şu:

▸ Bir: İnsan güvenliği.
▸ İki: Hizmet sürekliliği.
▸ Üç: Veri bütünlüğü.
▸ Dört: İtibar.

Laboratuvarda insan güvenliği biyogüvenliği de kapsar. Yani muhafaza, dizileme cihazını yeniden çalıştırmaktan önce gelir.

▸ Ve son satır bir denge ekliyor: Baskı altında bile zaman damgalarını ve delil zincirini koruyun. Bir yanda olayı hızla sınırlamak, öbür yanda adli incelemeye kanıt bırakmak. Hızlı hareket edin, ama kanıtı yok etmeyin.""",

"backup": """Kurtarmaya gelelim. Burada bilinmesi gereken temel kural 3-2-1 kuralı.

▸ Verinizin üç kopyası olsun.
▸ Bu kopyalar iki farklı ortamda tutulsun.
▸ Ve en az bir kopya çevrim dışı ya da değiştirilemez olsun.

Bu sonuncusu neden bu kadar önemli? Çünkü fidye yazılımı grupları bir sisteme girdiklerinde ilk olarak yedekleri arar ve onları şifreler ya da siler. Sizi kurtaracak olan, onların ulaşamadığı kopyadır.

▸ Ve bu slaytın asıl cümlesi şu: Yedek bir hipotezdir. Test edilmiş bir geri yükleme ise kanıttır.

Hepimiz bilim insanıyız; hipotezle kanıt arasındaki farkı biliriz. Size bir soru: Grubunuz en son ne zaman, bilerek, yedekten bir şeyi geri yükledi?""",

"maturity": """Aynı olayın farklı kurumlarda nasıl farklı sonuçlanabileceğini görelim. Bunu bir olgunluk merdiveni olarak düşünüyorum.

Senaryo şu: ▸ Bir cihaz bilgisayarında, dışarıya bağlantı kuran şüpheli bir PowerShell komutu çalışıyor.

▸ Düzey 1, temel: Antivirüs uyarı veriyor, biri gidip bilgisayarı elle ağdan ayırmaya çalışıyor ve elde yalnızca seyrek yerel kayıtlar var. Sonuç: panik ve gecikme.

▸ Düzey 2, orta: Uç nokta tespit ve müdahale yazılımı, yani EDR, uyarı veriyor. Ekip benzer göstergeleri diğer makinelerde hızla tarıyor ve merkezi kayıtlara bakıyor. Sonuç: kontrollü sınırlama.

▸ Düzey 3, ileri: Sınırlama otomatik gerçekleşiyor, ekip aktif olarak tehdit avcılığı yapıyor ve ağ zaten bölümlenmiş. Sonuç: tehdit dakikalar içinde etkisiz.

▸ Şimdi size soruyorum: Kurumunuz bugün bu merdivenin neresinde?

[Birkaç cevap alın.]

Çoğu birim için Düzey 2 gerçekçi bir bir yıllık hedef. Ve Düzey 2, büyük bir güvenlik ekibi gerektirmiyor; merkezi kayıtlar ve prova edilmiş bir müdahale kılavuzu yeterli.""",

"sprint": """Bütün bunlar kulağa büyük bir proje gibi gelebilir. O yüzden size yarın başlayabileceğiniz, otuz günlük bir sprint öneriyorum. Dört hafta, dört çıktı.

▸ Birinci hafta: Envanter ve roller. Varlık listesi, en değerli varlıklar, bir olay sorumlusu ve onun yedekleri.

▸ İkinci hafta: Başlangıç seti. Bir ana plan ve üç müdahale kılavuzu: fidye yazılımı, tedarikçi ihlali ve veri sızıntısı.

▸ Üçüncü hafta: Telemetri denetimi. Saatler eşzamanlı mı, kayıt kaynakları bağlı mı, saklama süresi belirli mi?

▸ Dördüncü hafta: Masa başı tatbikat. BT, biyogüvenlik, laboratuvar sorumluları ve hukuk birimiyle altmış dakikalık bir senaryo çalışması.

▸ Karmaşıklık uygulamanın düşmanıdır. ▸ Temel olandan başlayın, ama başlayın.

Bu sprint bilerek mütevazı tutuldu. Burada temsil edilen her kurumun bunu yıl sonundan önce yapabileceğine inanıyorum.""",

"metrics": """Son olarak, ölçmediğinizi yönetemezsiniz. Bir birimin gerçekten toplayabileceği altı ölçüt öneriyorum.

▸ MTTD: Ortalama tespit süresi. Bir olayı fark etmemiz ne kadar sürüyor?
▸ MTTR: Ortalama müdahale süresi. Fark ettikten sonra sınırlamamız ne kadar sürüyor?
▸ MFA yüzdesi: Uzak erişim yollarının yüzde kaçında çok faktörlü doğrulama var?
▸ Varlık yüzdesi: Cihazlarımızın yüzde kaçı envanterde?
▸ Kurtarma: En son ne zaman başarılı bir geri yükleme testi yaptık?
▸ Bildirimler: Personel kaç oltalama girişimini bize bildirdi?

Bu sonuncusu hakkında bir not: Oltalama bildirimlerinin artması kötü değil, iyi haberdir. İnsanların fark ettiğini gösterir.

▸ Bu ölçütleri her çeyrekte yönetime raporlayın. Ölçütler, güvenliği bir maliyetten bir bütçe kalemine dönüştürür. İkinci aşamanın bütçesini gerekçelendirmenin yolu da bu sayılardır.""",

"takeaways": """Toparlayalım. Bu oturumdan aklınızda kalmasını istediğim üç şey var.

▸ Bir: Yatırımdan önce envanter. Neye sahip olduğunuzu bilmeden bir şey satın almayın.

▸ İki: Her uzak erişim yolunda çok faktörlü doğrulama. Change Healthcare’i hatırlayın.

▸ Üç: Biyogüvenlikle birlikte prova edin. Müdahale planı BT’nin tek başına yazacağı bir belge değildir.

▸ Öğleden sonra bu konular devam ediyor. Saat 13:30’da Prof. Dr. Gökçe Merey laboratuvar siber biyogüvenlik politikalarını ve SOP’leri anlatacak; bu sabah gördüğümüz RACI tablosunun ve müdahale kılavuzlarının doğrudan devamı olacak. ▸ Saat 14:30’da ise uygulamalı oturumda CSF 2.0’ı kendiniz uygulayacaksınız.""",

"refs": """Bu oturumda kullandığım kaynakların tamamı burada. DOI’si olan her kaynak Crossref üzerinden doğrulandı. DOI’si olmayan raporların ve haberlerin yayın tarihlerini ve kurumlarını açıkça yazdım; kaynak başlıklarını özgün dillerinde bıraktım.

HSE vakasıyla ilgilenenlere PwC’nin olay sonrası inceleme raporunu özellikle öneririm. Bir kurumun nasıl çöktüğünü bu kadar açık anlatan çok az belge var. Sunumu sizinle paylaşacağım.""",

"thanks": """Dinlediğiniz için çok teşekkür ederim.

Altyapının kurulması üzerine sorularınızı alabilirim.

[Soru-cevaptan sonra:] Şimdi öğle arasına çıkıyoruz. Saat 14:30’daki alıştırmada bu oturumda gördüğümüz her şeyi kullanacağız: envanter, en değerli varlıklar, tedarikçi erişimi ve müdahale rolleri. Afiyet olsun.""",
}
