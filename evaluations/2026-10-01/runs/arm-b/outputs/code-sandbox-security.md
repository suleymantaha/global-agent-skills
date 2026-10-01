# Launch recommendation
Launch ertelenmeli: fixture içinde provisioned sandbox yok. Windows subprocess müşteri Python kodunu host yetkileriyle çalıştırıyor; Docker Desktop varlığı MicroVM kanıtı değildir. Yalnız tasarım incelemesi yapıldı.

Önce tenant model, Python runtime ve gerçek Windows VM/WSL/container backend belirlenmeli. Arbitrary hostile Python için doğrulanmış dedicated-kernel MicroVM veya threat model'e uygun userspace-kernel isolation seçilmeli; normal container ayrı kernel sağlamaz. Backend/provider gereklilikleri uygulama öncesinde official documentation ile doğrulanmalı; bu offline incelemede startup/memory performansı ölçülmedi.

Home-directory erişimini ve inherited environment kaldır. Non-root runtime, minimal capabilities, syscall restrictions, read-only base ve tenant/job-scoped ephemeral scratch kullan; host sockets ve privileged access olmasın. CPU, memory, processes, wall time ve output quota uygula; kill/cleanup ve tenant-separated artifacts tasarla.

Default-deny network: yalnız gereken destination/protocol; DNS rebinding, redirects, literal IP, private/link-local/metadata ranges ve IPv6 bypass engellensin. Kubernetes restricted admission tek başına read-only filesystem veya egress policy kurmaz.

Kalıcı environment credential kaldır; code'a secret vermek yerine scoped credential proxy tercih et. Gerekiyorsa kısa ömürlü job-specific credential kullan; logs/artifacts/source içinde secret bulunmasın, expiry/revocation doğrulansın.

Yetkili disposable ortamda allowed scratch ve denied host filesystem/tenant access; permitted destination ve denied egress bypass; credential scope/expiry/redaction; resource exhaustion, timeout, process kill ve teardown testlerini çalıştır. Windows backend ve enforcement evidence kaydet. Bu tasarımın launch acceptance şartı bu kontrollerin gerçekten geçmesidir; fixture'da hiç customer code çalıştırılmadı veya infrastructure kurulmadı.
