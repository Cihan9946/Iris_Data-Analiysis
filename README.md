# Iris_Data-Analiysis
https://www.kaggle.com/code/mustafacihanncr/iris-csv-data-analiysis

Bu çalıimada Iris.csv veri seti incellendi. ANN modeli kullanılarak makine öğrenmesi yapıldı.
Veri setinde dengesizlikler vardı bu sebeple test size yüksek alındı bunun nedenleri ise aşşağıda açıkladığım gibi;

Test veri setinin büyük bir oranda seçilmesinin bazı nedenleri:

Veri Kısıtlılığı: Eğer başlangıçta veri setiniz çok küçükse (örneğin, yeterince veri yoksa), daha büyük bir test seti kullanmak, modelinizi daha güvenilir bir şekilde değerlendirmenize yardımcı olabilir. Küçük veri setleri, eğitim ve test işlemleri arasında daha fazla rasgelelik içerebilir ve bu da sonuçların değişkenliğini artırabilir. Daha büyük bir test seti, modelin gerçek performansını daha iyi tahmin etmenize yardımcı olabilir.

Hızlı İnceleme: Modelinizi hızlı bir şekilde incelemek istiyor olabilirsiniz. Özellikle büyük veri setlerinde modelin eğitimi daha uzun sürebilir. Bu nedenle, modelinizi hızlı bir şekilde değerlendirmek için daha küçük bir eğitim veri seti kullanmak ve daha büyük bir test veri seti kullanmak faydalı olabilir.

Veri Dengesizliği: Eğer veri setinizde sınıf dengesizliği varsa (bir sınıf diğerlerine göre çok daha fazla gözlem içeriyorsa), test veri setini büyük tutmak, nadir sınıfları daha iyi değerlendirmenize yardımcı olabilir. Bu, modelin nadir sınıfları yanlış pozitiflerden koruma yeteneğini ölçmenizi sağlar.

Ancak, test veri setini büyük tutmanın dezavantajları da vardır. Özellikle veri setiniz zaten küçükse, eğitim veri seti daha küçük olduğunda modelinizin eğitimi daha az bilgiyle gerçekleşebilir ve bu da modelin performansını olumsuz etkileyebilir. Bu nedenle, test veri seti boyutunu seçerken veri miktarı ve analiz hedeflerinizi dikkate almalısınız.

Sonuç olarak, test veri seti boyutunu seçerken, veri setinizin özelliklerini, analiz hedeflerinizi ve modelinizi güvenilir bir şekilde değerlendirmek istediğiniz zamanı dikkate almalısınız. Veri setinin yetersiz olması durumunda, çapraz doğrulama gibi diğer yöntemler de kullanılabilir.
