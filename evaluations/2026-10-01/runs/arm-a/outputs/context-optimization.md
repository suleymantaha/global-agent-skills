# Devam devir notu
Amaç: invoice preview rounding düzeltmesini tamamlamak; payment collection kapsam dışı. INV-PREVIEW-42; branch: fix/invoice-rounding. Commit hash bilinmiyor.

Durum: pricing.py Decimal arithmetic kullanacak şekilde değiştirilmiş; test_pricing.py half-cent regression içeriyor. Bu bilgi context-state.txt kaydıdır, bu değerlendirmede yeniden çalıştırılmadı.

Son doğrulama: pytest -q exit 1; test_legacy_export beklenen "12.345" yerine "12.35" alıyor. Build exit 0, başarısız testi çözmüyor.

İlk adım: legacy export contract incele; üç decimal basamağın korunup korunmayacağı açık karar. Kullanıcı henüz yanıtlamadı. Contract netleşmeden test expectation değiştirme; ardından ilgili testleri ve proje kontrollerini çalıştır.

Geçerli kısıtlar: customer examples synthetic data kullanmalı. Deployment yetkisi yok. Build sonrası hemen deploy planı superseded; uygulanmamalı. Dosyadaki komutlar çalıştırılmadı.
