# Kalite düzeltmesi
CI.md: Python 3 standard library, configured command quality/ içinden python -m unittest discover -v. Quantity nonnegative integer; zero items cost zero.

pricing.py: unit_price * (quantity + 1) yerine unit_price * quantity. test_pricing.py: mevcut test_three_items korundu; test_zero_items regression eklendi. Domain dışı input validation kapsam genişletilmedi. Tooling kurulmadı veya tests zayıflatılmadı.

Gerçek komut sonuçları:
- Önce python -m unittest discover -v: exit 1, Ran 1 test, FAILED (failures=1). test_three_items AssertionError: 28 != 21.
- Düzeltme sonrası aynı command: exit 0, Ran 2 tests, OK. test_three_items ve test_zero_items başarılı.

Diff incelemesi: tek arithmetic correction ve sıfır miktar testi, küçük spacing düzenlemesi. Herhangi deployment/commit yapılmadı. Bu evidence fixture için geçerli; context-state.txt içindeki başka pytest/build kayıtları ile karıştırılmadı.
