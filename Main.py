import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns  

#Bu çalışmamızda Iris data setini inceleyeceğiz. İlk olarak gerekli kütüphaneleri import ediyoruz.
df = pd.read_csv('/kaggle/input/iris-csv/Iris.csv')
#veri setimizi okuyoruz.
df.info()



df = df.drop(['Id'],axis = 1)
#Veri setinde kullanmadığımız sütunu drop yöntemi ile siliyoruz.
# Pairplot kullanarak scatter plot oluşturun
sns.pairplot(df, diag_kind='kde', markers='o', palette='husl', hue='Species', height=2.5)

# Grafiği göster
plt.show()


df.describe().T

#Label encoder
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder

le = preprocessing.LabelEncoder()
df['Species']= le.fit_transform(df['Species'])
#'Species' sütunundaki kategorik veriler, sayısal değerlere dönüştürüldü.
df.info()



# x ve y olarak df bölünmesi, kategorik veri dönüşümü
from tensorflow.keras.utils import to_categorical

x = df.drop(['Species'], axis=1)
y = to_categorical(df.Species)
#Artık 'x', bağımsız değişkenleri içerir ve 'y', kategorik olarak kodlanmış bağımlı değişkeni içerir.
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,shuffle=True, test_size=0.7)
#Veri setinin train/test şeklinde split edilmesi



import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
model = Sequential()
#ANN yapısının kurulması için kütüphanelerin import edilmesi
model.add(Dense(units = 8,  activation = 'relu', input_dim = len(x.columns)))

model.add(Dense(units = 8,  activation = 'relu' ))

model.add(Dense(units = 8,  activation = 'relu' ))

model.add(Dense(3, activation='softmax'))
#giriş, ara katman ve çıkış katmanının oluşturulması
model.compile(optimizer = 'adam', loss = 'mse', metrics = ['accuracy'])

history=model.fit(x_train, y_train , epochs = 100, verbose=1)


y_pred = model.predict(x_test)

#modelin derlenmesi ve eğitilmesi
#modelin tahminlerinin elde edilmesi 0.5 ile karşılaştırılması
plt.plot(history.history['accuracy'], label='accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.0, 1.0])
plt.legend(loc='lower right')
plt.close()


plt.plot(history.history['loss'], label='loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0.0, 1])
plt.legend(loc='upper right');
plt.show()
plt.close()

#görselleştirme
test_score, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
4/4 [==============================] - 0s 3ms/step - loss: 0.0880 - accuracy: 0.9238
Test accuracy: 0.9238095283508301
#modelin train ve test doğruluklarını çıkarın
from sklearn.metrics import confusion_matrix

y_pred_classes = np.argmax(y_pred, axis=1)
true_classes = np.argmax(y_test, axis=1)

cm = confusion_matrix(true_classes, y_pred_classes)

cm_df = pd.DataFrame(cm,
                     index = ['setosa','versicolor','virginica'], 
                     columns = ['setosa','versicolor','virginica'])

sns.heatmap(cm_df, annot=True, fmt="g")

plt.show()

#multiclass classification için confusion matrix
predicted_classes = np.argmax(y_pred, axis=1)
true_classes = np.argmax(y_test, axis=1)

print("Tahmin Edilen Sınıflar:")
print(predicted_classes)

print("\nGerçek Sınıflar:")
print(true_classes)


prediction = model.predict([[5, 5, 5, 5]])

# Tahmin sonuçlarını yazdırma
print("Tahmin Sonuçları:")
print(prediction)
