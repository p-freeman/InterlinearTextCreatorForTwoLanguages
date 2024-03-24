# Aralıklı Metin Oluşturucu

Bu Python betiği, İsviçre Almancası öğrenmek isteyenler için Türkçe metinleri öğrenmelerine yardımcı olacak aralıklı metin HTML dosyaları oluşturmanıza olanak tanır.

## Özellikler

- Almanca ve Türkçe çevirileri olan aralıklı metin HTML dosyaları oluşturun.
- YouTube videolarını HTML dosyalarına gömün.
- Ses dosyalarını HTML dosyalarına gömün.
- Kolay giriş ve proje yönetimi için GUI.

## Kullanım

1. Betiği çalıştırın ve GUI penceresi açılacaktır.
2. Gerekli alanları doldurun:
   - **Başlık**: Aralıklı metnin başlığı.
   - **Dosya Adı/Klasör Adı**: Oluşturulacak klasör ve HTML dosyasının adı.
   - **İsviçre Almancası Kelimeler**: Sol metin kutusuna İsviçre Almancası metni girin.
   - **Türkçe Kelimeler**: Sağ metin kutusuna karşılık gelen Türkçe çevirileri girin.
   - **Dikey Mesafe (px)**: Piksel cinsinden kelime çiftleri arasındaki dikey mesafe.
   - **Yazı Tipi Boyutu**: Piksel cinsinden metin yazı tipi boyutu.
   - **Video Bağlantısı (URL) *isteğe bağlı**: Bir YouTube videosunun URL'sini girin (isteğe bağlı).
   - **Ses Dosyası Mevcut *isteğe bağlı**: Bir ses dosyası mevcutsa bu kutuyu işaretleyin.
3. HTML dosyasını oluşturmak için **Aralıklı Metin Oluştur** düğmesine tıklayın.
4. İsteğe bağlı olarak, bir projeyi düzenlemek için **Mevcut Projeyi Aç** düğmesine tıklayın.

## Video Gömme

Bir YouTube video URL'si girdiğinizde, betik videoyu üst kısıma gömülü olan ikinci bir HTML dosyası oluşturacaktır.

## Ses Gömme

"Ses Dosyası Mevcut" onay kutusunu işaretlerseniz, betik gömülü bir ses çalar içeren üçüncü bir HTML dosyası oluşturur.

## Gereksinimler

- Python 3.x
- tkinter (çoğu Python kurulumunda bulunması gerekir)
- Temel işlevsellik için internet bağlantısı gerekmez. Ancak gömülü YouTube videolarını izlemek için etkin bir internet bağlantısına ihtiyaç vardır. Gömülü HTML dosyalarını çevrimdışı görüntülemek, oynatılamayan videolara neden olur.

## Notlar

- Hataları önlemek için geçerli girişler sağladığınızdan emin olun.
- Betik, ses dosyasının oluşturulan HTML dosyalarıyla aynı klasörde olduğunu varsayar.
- Oluşturulan HTML dosyaları, belirtilen dosya adıyla bir klasöre kaydedilir.
