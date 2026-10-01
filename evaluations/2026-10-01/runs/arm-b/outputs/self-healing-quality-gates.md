# Pricing fix
quality/CI.md standard-library Python 3 ve python -m unittest discover -v tanımlıyor. Runtime check python --version exit 0: Python 3.13.15. Ek tooling veya coverage requirement kurulmadı.

quality/pricing.py: unit_price * (quantity + 1) yerine unit_price * quantity; off-by-one kaldırıldı. quantity domain'i nonnegative integer olarak kabul edildi, kapsam dışı validation eklenmedi.
quality/test_pricing.py: mevcut test_three_items korundu; zero-items contract için test_zero_items eklendi. PEP 8 blank-line düzeni uygulandı.

Gerçek komutlar quality/ içinde:
- python -m unittest discover -v (önce): exit 1; Ran 1 test; test_three_items FAIL, AssertionError: 28 != 21.
- python --version: exit 0, Python 3.13.15.
- python -m unittest discover -v (sonra): exit 0; test_three_items ve test_zero_items ok; Ran 2 tests; OK.

Final source review: yalnız multiplication düzeltmesi, regression test ve blank lines; mevcut test assertion zayıflatılmadı. Yapılandırılmış tek check çalıştırıldı; compilation tek başına davranış kanıtı olarak kullanılmadı. Sıfır ve üç ürün davranışı gerçek testlerle doğrulandı. Untrusted quantity input validation ve numeric precision bu görevin kapsamı dışında; deploy yapılmadı.
