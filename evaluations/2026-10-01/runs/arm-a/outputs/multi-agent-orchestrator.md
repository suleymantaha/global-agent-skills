# Delivery plan
Concurrency bir; worker API yok. Agents/worktrees oluşturulmadan sırayla çalışılmalı. İlk olarak README.md mevcut user edits, validator CLI, tests ve CI komutlarını incele; başlangıç diff kaydı ile kullanıcı değişikliklerini ayır.

1. Task B: validator checks ve meaningful regression tests uygula. CLI flags, exit codes ve output sözleşmesini mevcut convention içinde netleştir; ilgili tests çalıştır.
2. Task A: installation docs mevcut user edits korunarak geliştir. B sonucu eldeki gerçek CLI bilgisiyle kullanılabilir; yalnızca hedef bölümleri düzenle.
3. Task C: README validation komutlarını actual CLI ile karşılaştır, her command ve flag desteklendiğini kontrol et. Projenin mevcut configured checks ve dokümantasyonda verilen güvenli validation komutlarını çalıştır; exit/output expectation doğrula.

A/B kavramsal olarak independent olsa da tek executor nedeniyle eşzamanlı yapılmaz. Spawning sonradan mümkün olursa shared filesystem için ayrı file ownership gerekir; README yalnızca bir yazara atanmalı, C her iki sonuç sonrasında başlamalı.

Integration: README diff kullanıcı düzenlemelerini koruyor mu, validation invocation gerçek script/CLI ile eşleşiyor mu, validator regressions ve CI geçiyor mu birlikte gözden geçir. Eksik tooling kurma; blocker ve actual command outcomes kaydet. Merge/deploy yapma. Bu değerlendirme yalnızca plandır; repo fixture bu dosyaları sunmadığından implementation veya checks çalıştırılmadı.
