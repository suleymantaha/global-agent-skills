# Minimal memory contract
Mevcut tasarım kabul edilmemeli. Request body user_id yetkilendirme kaynağı değildir; authenticated principal üzerinden organization_id ve user_id türetilmeli. Tüm read/write/search/delete işlemleri bu birleşik scope ile sınırlandırılmalı; embedding search öncesinde veya güvenilir storage filtresinde isolation uygulanmalı.

Yalnızca açıkça gerekli ve yetkilendirilmiş karar/tercih kayıtlarını tut; tüm konuşmaları sonsuza kadar saklama. External transfer yetkisi gelmeden lokal tasarım/fixture ile kal. Tek backend için küçük adapter contract yeterli; Mem0/Graphiti/Letta birlikte kurulum gerekli değil.

Record contract: stable record_id, organization_id, user_id, text, source/reference, source_type (direct statement veya inference), observed_at/updated_at, confidence, retention_expires_at, revision ve deletion state; embedding aynı scope ve yaşam döngüsünü izler. En yeni doğrudan ifade 'private only' geçerlidir; 'public releases' inference bunu geçersiz kılamaz. Conflict provenance korunmalı; inference kullanıcı gerçeği diye sunulmamalı.

Writes acknowledged durable storage sonrası success vermeli; önce queued/pending gösterilebilir. Idempotency key ve unique constraint ile retry aynı kaydı güncellemeli; random ID ile duplicate insertion olmamalı. Delete text, embedding, caches ve bekleyen async jobs için uygulanmalı; silinen kayıt retry ile dirilmemeli. Retention sonlu ve kullanım amacıyla belirlenmeli.

Acceptance: iki organization aynı user_id kullandığında cross-tenant retrieval/write/delete sıfır; spoofed body ID reddi; latest direct statement inference üstünde; unknown source kayıtlarının gerçek diye sunulmaması; timeout/retry duplicate yaratmaması; storage failure success dönmemesi; expiry ve delete sonrası tüm retrieval yollarında yokluk; pending write deletion sonrası resurrection olmaması. Servise bağlanılmadı veya personal data persist edilmedi.
