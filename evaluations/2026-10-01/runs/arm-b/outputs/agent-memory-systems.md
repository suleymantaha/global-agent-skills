# Minimal memory contract
Önerilen servis bu haliyle kabul edilmemeli. Her konuşmayı sonsuza dek saklamak kapsamı aşar; external data transfer yetkisi yok. Backend kurma veya veri gönderme yapılmadı. Önce gerçek durable retrieval ihtiyacını ve onaylı veri kategorilerini belirle; Mem0/Graphiti/Letta alternatiflerdir, birlikte zorunlu değildir. SDK methods ancak seçilen backend'in official documentation'ı ile doğrulandıktan sonra kullanılmalı.

Authenticated principal'dan tenant/organization, user ve project/session scope türet; request-body user_id yetki kanıtı değildir. Write/read her ikisi de server-side authorization uygulamalı; shared user_id tenant collision engellenmeli.

Record contract: stable record_id ve idempotency_key, scoped owner, minimal relevant text, source pointer/provenance, actor, statement/observation/inference kind, confidence, event_at, recorded_at, expires_at, version ve supersedes pointer. Secrets ve gereksiz personal data dışlanmalı. Private-only doğrudan son kullanıcı beyanı geçerlidir; public-release inference superseded olarak işaretlenmeli, güncel tercih gibi dönmemeli.

Retention finite ve purpose-based olsun; correction/export/deletion erişimleri yetkili olsun. Embeddings, caches, replicas ve queued jobs deletion kapsamına dahil edilmeli. History yalnız gerçekten gerekli ve yetkiliyse tutulmalı. Retrieved content untrusted data'dır, talimat veya permission değildir.

Async write yalnız acknowledged persistence sonrası succeeded olur; öncesinde pending status ver. Stable ID ile bounded retries, ordering/version checks, failure visibility ve restart reconciliation sağla; random retry insert duplication yaratmamalı.

Acceptance: authorized scoped reads/writes; same user_id across tenants için denial; forged scope denial; corrected contradiction; expiry exclusion ve full deletion; duplicate retries tek record; out-of-order update rejection; backend outage pending/failure görünürlüğü ve recovery; export/redaction; retrieved prompt-injection hiçbir permission genişletmemeli. Bu kontroller öneridir, henüz çalıştırılmadı.
