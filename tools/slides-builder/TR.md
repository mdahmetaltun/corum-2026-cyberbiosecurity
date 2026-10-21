# Türkçe yerelleştirme (v2-tr)

`tr.py` v2 slaytlarını yerleşim, animasyon, 3B gömüler ve geçişlere dokunmadan Türkçeye çevirir:
yalnızca metin düğümleri, aria/alt etiketleri, kinetik kelimeler, konuşmacı notları ve deck.json başlık/bölüm açıklamaları değişir.
Sayaçlar `tr-TR` biçimine geçer (40.000; 192,7) ve her `<section>` `lang="tr"` alır (büyük harfte İ/ı doğru çıksın diye).

```bash
python3 tr.py extract <v2>/project csf.en.json      # çevrilecek metinler
python3 tr.py apply <v2>/project <v2-tr>/project tr_csf.py
python3 trcheck.py <v2> <v2-tr>                      # EN/TR taşma karşılaştırması
```

`tr_<deste>.py`: `T` sözlüğü (EN → TR) ve gerekirse slayta özel `OV` düzeltmeleri.
Kaynakça başlıkları özgün dilinde bırakılır. Açılış filmleri: `tools/remotion-openers-v2-tr/`.
