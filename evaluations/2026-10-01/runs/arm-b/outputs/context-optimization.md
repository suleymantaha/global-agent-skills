# Devam handoff
Amaç: invoice previews rounding düzeltmesini tamamlamak; payment collection kapsam dışıdır. Referans INV-PREVIEW-42, branch fix/invoice-rounding; commit hash bilinmiyor.

Son kullanıcı yönlendirmesi: yalnız synthetic customer examples kullanılacak. Deployment yetkisi yoktur; build sonrası deploy planı geçersizdir.

context-state.txt bildirimi: pricing.py Decimal arithmetic kullanacak şekilde değiştirildi; test_pricing.py half-cent regression içeriyor. Bu görevde bu bildirilen değişiklikler bağımsız doğrulanmadı; quality fixture ayrı örnektir.

Bildirilen kontrol: pytest -q exit 1. test_legacy_export "12.345" bekliyor, "12.35" geliyor. Build exit 0; failing test hâlâ blokerdir. Legacy export üç decimal places korumalı mı, kullanıcı henüz yanıtlamadı.

Sonraki adım: mevcut branch/diff ve export contract incele; expectation değiştirmeden precision requirement belirle. Sonra ilgili testi ve configured checks çalıştır. Deploy etme. Kanıt kaynağı arm-b/context-state.txt; raw test log yolu sağlanmadı. Bu handoff oluşturulurken state içindeki komutlar çalıştırılmadı.
