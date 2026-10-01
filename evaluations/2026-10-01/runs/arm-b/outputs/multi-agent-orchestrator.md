# Sıralı delivery plan
Concurrency bir, worker API yok: agents veya worktrees oluşturma. Bu görev yalnız plandır; merge/deploy yok. Olası workers aynı filesystem'i paylaşacağından spawning isolation sağlamaz.

1. Repo instructions, Git status/diff, README.md kullanıcı değişiklikleri, validator CLI ve mevcut test/CI commands incele; kullanıcı editlerini başlangıç evidence olarak kaydet.
2. Task B: validator checks ve tests için dar dosya sahipliğiyle ilerle; davranış/CLI contract'ı belirle, meaningful regression tests ve configured checks çalıştır. Report: changed paths, commands, exit status, unresolved issues.
3. Task A: README.md installation kısmını mevcut kullanıcı editlerine dokunmadan dar patch ile güncelle. B'nin finalized runtime/dependency/CLI bilgisini kullan; docs command'larını henüz doğrulanmış diye sunma.
4. Task C ancak A ve B tamamlandıktan sonra: README validation commands ile gerçek script CLI options, exit codes ve paths karşılaştır; disposable/local authorized input ile documented commands çalıştır ve tests ile birlikte integration doğrula.
5. Combined diff gözden geçir: kullanıcı edits korunuyor mu, installation instructions runtime ile uyumlu mu, docs/test/code aynı CLI contract'ı taşıyor mu? Actual checks ve blockers raporla; failing checks varsa tamamlandı deme.

A/B teorik bağımsızdır; worker olsaydı README ownership A, validator/tests ownership B, integration C olurdu ve C iki artifact'a bağımlı beklerdi. Burada native tracking/messaging yok; küçük sıralı checklist yeterli, distributed queue/state files gerekmez. Yeni kullanıcı yönlendirmesi obsolete adımları durdurmalı; yalnız owned geçici kaynaklar temizlenmeli.
