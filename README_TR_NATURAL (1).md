
# NFS Tarayıcı

Merhaba! Bu repo, NFS paylaşımlarını taramak isteyenler için hazırlanmış bir Python betiğini içeriyor. Birden fazla IP adresindeki NFS paylaşımlarını taramanız gerekiyorsa, bu araç tam size göre. Üstelik sadece paylaşımları bulmakla kalmıyor, aynı zamanda bu paylaşımların yazılabilir mi, okunabilir mi olduğunu da kontrol ediyor.

![NFS Tarayıcı](https://via.placeholder.com/1000x200.png?text=NFS+Tarayıcı+Scripti)

## 🚀 Özellikler

- **🔍 Otomatik Tarama**: Elinizdeki IP adreslerini hızlıca tarar ve NFS paylaşımlarını bulur.
- **🛡️ Yetki Kontrolü**: Paylaşımların üzerinde yazma ve okuma izinlerini kontrol eder.
- **📝 Detaylı Kayıt**: Bütün sonuçları ve karşılaşılan hataları bir dosyaya yazar, böylece hiçbir şey gözden kaçmaz.
- **📊 Okunaklı Çıktılar**: Sonuçlar, `tabulate` modülü kullanılarak düzenli ve anlaşılır bir şekilde sunulur.

## 🛠️ Nasıl Çalışır?

İşlem çok basit:

1. Betik, `ip_list.txt` dosyanızdan IP adreslerini okur.
2. Her IP adresi için, `showmount` komutuyla NFS paylaşımlarını bulmaya çalışır.
3. Eğer paylaşımlar varsa, betik bu paylaşımları bağlar ve okuma/yazma izinlerini kontrol eder.
4. Sonuçlar, paylaşımların içeriği de dahil olmak üzere, `nfs_scan_results.txt` dosyasına kaydedilir.

## 🧰 Gereksinimler

- Python 3.x
- `showmount` komutu (genellikle Linux'ta `nfs-common` paketiyle gelir)
- `tabulate` modülü (`pip install tabulate` komutuyla yükleyebilirsiniz)

## 🚀 Nasıl Kullanılır?

Adım adım şöyle yapabilirsiniz:

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/bahadirtmzr/nfs-scanner.git
   cd nfs-scanner
   ```

2. Tarama yapmak istediğiniz IP adreslerini `ip_list.txt` dosyasına, her satıra bir IP adresi olacak şekilde yazın.

3. Betiği çalıştırın:
   ```bash
   python3 nfs-tara.py
   ```

4. Sonuçları `nfs_scan_results.txt` dosyasında bulabilirsiniz.

## 📊 Örnek Çıktı

Sonuçların nasıl görüneceğine dair bir örnek:

![NFS Tarama Sonuçları](https://via.placeholder.com/800x400.png?text=Örnek+NFS+Tarama+Sonuçları)

Bu betik, bulduğu tüm NFS paylaşımlarını, onların okuma/yazma izinleriyle birlikte listeler ve dizin içeriklerini de gösterir.

## Katkıda Bulunma

Eğer projeye katkı sağlamak isterseniz, lütfen bir Pull Request gönderin. Her türlü katkı çok değerli!

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

