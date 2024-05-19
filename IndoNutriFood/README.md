# Laporan Proyek Machine Learning - Imam Nurcakra

## Kesehatan

### Latar Belakang: Prediksi nutrisi berdasarkan kalori Makanan dan minuman di Indonesia

Dalam beberapa tahun terakhir, ada peningkatan penekanan pada pemahaman komposisi nutrisi dari berbagai jenis makanan dan minuman, didorong oleh kesadaran yang meningkat tentang dampak pola makan terhadap kesehatan dan kesejahteraan. Di Indonesia, negara yang terkenal dengan warisan kuliner yang kaya dan beragam, ada minat yang meningkat dalam mempelajari konten nutrisi dari makanan tradisional Indonesia.

Profil nutrisi dari item makanan dan minuman umumnya ditandai oleh beberapa parameter utama, termasuk kalori, protein, lemak, dan karbohidrat. Parameter-parameter ini memainkan peran penting dalam menentukan nilai nutrisi keseluruhan dari suatu produk makanan dan minuman serta dapat memberikan wawasan berharga tentang implikasi kesehatannya.

Dengan munculnya algoritma machine learning, telah menjadi mungkin untuk menganalisis dataset besar yang berisi informasi nutrisi dan menemukan pola dan wawasan yang berarti. Dengan memanfaatkan teknik-teknik machine learning, para peneliti dan ahli gizi dapat mengungkap hubungan tersembunyi antara atribut makanan dan minuman, mengidentifikasi tren dalam kebiasaan makanan dan minuman, dan bahkan memprediksi dampak nutrisi dari berbagai pilihan makanan dan minuman.

Dalam proyek ini bertujuan untuk mengembangkan model prediksi yang dapat memperkirakan kandungan kalori dari berbagai jenis makanan dan minuman yang ada di Indonesia. hal tersebut cocok menggunakan pendekatan machine learning untuk menganalisis dataset yang berisi informasi nutrisi dari berbagai makanan tradisional Indonesia. Dataset ini mencakup berbagai atribut, termasuk kalori, protein, lemak, karbohidrat, serta atribut kategoris seperti ID, nama, dan gambar makanan.

Model prediksi yang dikembangkan akan didasarkan pada berbagai fitur nutrisi yang tersedia dalam dataset. akan menggunakan teknik-teknik machine learning seperti regresi dan pengolahan bahasa alami untuk membangun model yang dapat memperkirakan kandungan kalori dari makanan berdasarkan atribut-atribut tersebut.

  **Kesehatan Masyarakat**
-  Dengan peningkatan kesadaran akan pentingnya pola makan yang sehat, informasi yang akurat tentang komposisi nutrisi dari makanan dan minuman menjadi sangat penting. Dengan memprediksi kandungan kalori dari berbagai jenis makanan, masyarakat dapat membuat pilihan makanan yang lebih sadar dan seha

  **Keanekaragaman Kuliner**
- Indonesia memiliki warisan kuliner yang kaya dan beragam, namun informasi nutrisi tentang makanan tradisional seringkali sulit ditemukan. Dengan mengembangkan model prediksi untuk makanan dan minuman Indonesia, memungkinkan dapat memberikan aksesibilitas yang lebih baik terhadap informasi nutrisi untuk masyarakat Indonesia.


## Business Understanding
### Problem Statements

**pernyataan masalah latar belakang:**

 **Pertanyaan 1 :**
Bagaimana cara meningkatkan aksesibilitas informasi tentang kandungan kalori, protein, lemak, dan karbohidrat dalam makanan dan minuman, terutama yang berasal dari Indonesia, bagi masyarakat?

**Pertanyaan 2 :**
Adakah inovasi teknologi yang dapat digunakan untuk memperbaiki aksesibilitas dan akurasi informasi nutrisi makanan dan minuman di Indonesia?

### Goals
**jawaban 1** 
Goals akhir dari projek ini secara umum di harapkan masyarakat indonesia dapat memiliki akses informasi yang informatif berdasarkan data prediktif yang di sugestikan oleh analisis machine learning models yang di paparkan dalam solution statements

**jawaban 2**
Innovasi yang diajukan yaitu membangun model machine learning prediktif analysis dengan improvisasi akurasi yang ditingkatkan sehingga, dengan data makanan dan minuman khas indonesia yang akan selalu update terus, di harapkan model dapat menyesuaikan masalah nutrisi makanan di indonesia 

jadi secara keseluruhan project ini bertujuan untuk menyediakan solusi yang inovatif dan efektif untuk menanggapi masalah aksesibilitas dan keakuratan informasi nutrisi pangan serta meningkatkan transparansi dalam industri makanan dan minuman Indonesia.
dengan evaluasi metrik yang digunakan yakni MSE(Mean squared Error) dan R-Squarred yang di lakukan beberapa tipe algoritma regresi dengan target terukur yakni :
- Linear regression = Target acc(R-squarred) test > 80%; target MSE tes< 0.1
- AdaBoost regression = Target acc(R-squarred) test > 80%; target MSE tes< 0.1
- Random forest regression = Target acc(R-squarred) test > 80%; target MSE tes< 0.1
- KNeighbors regression = Target acc(R-squarred) test > 80%; target MSE tes < 0.1

goals yang akan di gunakan adalah yang R-Squarred nya tertinggi dan MSE nya ter rendah diantara ke empat pilihan model benchmarking, hal itu yang di jadikan kelayakkan untuk menyelesaikan permasalahan project ini 

#### **Solution statements**
 - **Solusi pernyataan masalah 1 :**
Untuk mengatasi kurangnya aksesibilitas dan keakuratan informasi nutrisi makanan dan minuman, pendekatan terbaik adalah mengembangkan model prediksi nutrisi berdasarkan kandungan kalori makanan dan minuman. Model ini fokusnya akan digunakan oleh masyarakat di Indonesia baik individu maupun untuk kelompok/ahli. Standar acuan akan diterapkan untuk memberikan pemahaman yang jelas tentang nutrisi dari makanan/minuman khas Indonesia, dengan fokus pada kandungan kalori. Metrik evaluasi utama projek ini adalah akurasi prediksi kalori, yang ditetapkan pada 80% untuk data(tes) makanan dan minuman Indonesia yang belum pernah dikenali oleh model. Jika akurasi berada di bawah standar tersebut, maka proyek ini akan memerlukan pengembangan lebih lanjut.
  
 - **Solusi pernyataan masalah 2 :**
Menggunakan algoritma machine learning predictive analysis untuk memprediksi jumlah kalori tiap makanan dan minuman dapat meningkatkan akurasi prediksi nutrisi dan menyediakan informasi yang lebih relevan bagi pengguna. Hal ini dilakukan melalui visualisasi data yang menarik untuk membantu pengguna memahami informasi makanan berdasarkan kalori dengan lebih baik, terutama pada platform yang umum digunakan di ponsel masyarakat. Keberhasilan proyek ini cukup ditetapkan dengan mencapai tingkat keakuratan prediksi pada data tes di atas 80%.



## Data Understanding
Dalam konteks analisis data nutrisi, kalori seringkali dijadikan target karena merupakan ukuran penting dari nilai energi yang diberikan oleh makanan atau minuman. Protein, lemak, dan karbohidrat adalah komponen utama dari makanan yang berkontribusi terhadap total kalori.

Data ini memungkinkan dapat memberikan wawasan dalam mengukur jumlah nutrisi yang masuk ke dalam tubuh saat mengonsumsi makanan dan minuman khas Indonesia.

memahami hubungan antara berbagai nutrisi dan total kalori dapat membantu untuk memahami bagaimana makanan dan minuman memberikan energi. Misalnya, makanan dengan kandungan lemak tinggi akan memiliki kalori yang lebih tinggi dibandingkan dengan makanan dengan jumlah protein atau karbohidrat yang sama. Demikian pula, makanan dengan karbohidrat tinggi akan memiliki kalori yang lebih tinggi dibandingkan dengan makanan dengan jumlah protein yang sama tetapi lebih rendah lemak.

dataset ini di peroleh dari Tabel Komposisi Pangan Indonesia (Indonesian Food Composition Table) data ini di publikasi oleh kementrian republik Indonesia 

- [panganku](www.panganku.org)  
- [Indonesian Food and Drink Nutrition Dataset](https://www.kaggle.com/datasets/anasfikrihanif/indonesian-food-and-drink-nutrition-dataset/data) 

#### Dataset Contain
tahap awal untuk membaca isi kandungan dataset yang akan di gunakan 

<sub>Tabel 1,dataset sebelum di lakukan manipulasi apapun</sub>

| id | calories | proteins | fat  | carbohydrate | name         | image |
|----|----------|----------|------|--------------|--------------|-------|
| 1  | 280.0    | 9.2      | 28.4 | 0.0          | Abon         | -     |
| 2  | 513.0    | 23.7     | 37.0 | 21.3         | Abon haruwan | -     |
| 3  | 0.0      | 0.0      | 0.2  | 0.0          | Agar-agar    | -     |
| 4  | 45.0     | 1.1      | 0.4  | 10.8         | Akar tanjong | -     |
| 5  | 37.0     | 4.4      | 0.5  | 3.8          | Aletoge segar| -     |
| ... | ...    | ...   |     ...      | ...            | ...          | ...   |


**Variabel-variabel pada Indonesian food and drink nutrition dataset adalah sebagai berikut:**
- id: nomor baris
- calories: jumlah kalori (dalam cal) per 100 grams of food/drink
- proteins: banyaknya protein (dalam gram) per 100 gram of food/drink
- fat: banyaknya lemak (dalam gram) per 100 gram of food/drink
- carbohydrate: jumlah karbohidrat (dalam grams) per 100 gram of food/drink
- name: nama dari food/drink
- image: tautan gambar food/drink



#### Distribusi/Sebaran (Univariate analysis) data menggunakan Histogram

![datasethead](https://raw.githubusercontent.com/imamNurC/Notebook-Research/main/IndoNutriFood/img/univariate.png)

<sub>gambar 1 :Univariate Analysis</sub>

pada gambar 1, distribusi dari keempat variable menunjukkan bahwa sebagian besar nilai di semua variable berada di bawah 200 kalori untuk calories, 20 gram untuk protein, 25 gram untuk fat, dan 150 gram untu carbohydrate

#### Bivariate Analysis

![datasethead](https://raw.githubusercontent.com/imamNurC/Notebook-Research/main/IndoNutriFood/img/bivariate.png)

<sub>gambar 2: Bivariate Analysis</sub><br>

<sub> pada gambar 2, menunjukkan korelasi titik data antara kalori dengan protein, lemak dan karbohidrat </sub>

Karena calories mempunyai sebaran yang paling signifikan, Analisis selanjutnya melakukakn bivariate analysis yang dapat membantu menentukan sejauh mana kemudahan untuk mengetahui dan memprediksi suatu keterhubungan antar nilai dari dua  variabel

- ##### Protein vs. Kalori: 
   Terdapat korelasi positif antara protein dan kalori. Ini menunjukkan bahwa semakin tinggi kandungan protein, semakin tinggi pula kandungan kalori.
- ##### Lemak vs. Kalori:
   Korelasi positif juga terlihat antara lemak dan kalori. Hal ini menandakan bahwa peningkatan kandungan lemak berkaitan dengan peningkatan kalori.
- ##### Karbohidrat vs. Kalori: 
  Sama seperti dua variabel sebelumnya, terdapat korelasi positif antara karbohidrat dan kalori, yang berarti bahwa semakin banyak karbohidrat, semakin tinggi pula kalori.


#### Statistics Descriptive
dari banyak kalori, protein, lemak dan karbohirat di lakukan untuk menggambarkan ringkasan dataset secara statistik 
<br><sub>Tabel 2, Ringkasan dataset secara statistik</sub>

|    | calories | proteins | fat  | carbohydrate |
|----|----------|----------|------|--------------|
| Count | 1346.0   |1346.0      | 1346.0        |1346.0  |
| mean  | 203.217385   | 10.001189      | 7.584027   | 25.390193 |
| std   | 163.075430   | 11.847980      | 13.733063  | 32.193054  |
| min   | 0.0   | 0.0     | 0.0        |0.0    | 
| 25% | 75.0   | 1.8      | 0.5        |4.52    |
| 50% | 146.0   | 5.0     | 2.0        | 13.3    |
| 75% | 333.75   | 15.0      | 8.275        | 37.575   |
| max | 940.0   | 83.0      | 100.0        | 647.0   |


##### calories :
Rata-rata kalori per porsi makanan adalah sekitar 203, dengan deviasi standar yang cukup tinggi (163). Hal ini menunjukkan bahwa ada variasi besar dalam jumlah kalori antar item makanan. Nilai minimum yang nol mungkin menunjukkan adanya item makanan dengan kalori sangat rendah atau bahkan nol kalori, yang mungkin mengindikasikan adanya item makanan yang tidak berkontribusi banyak terhadap asupan kalori.

##### proteins :
Rata-rata protein per porsi makanan adalah sekitar 10 gram, dengan deviasi standar yang cukup tinggi (11.85). Ini menunjukkan variasi yang signifikan dalam kandungan protein antar item makanan. Nilai minimum yang nol mungkin menunjukkan adanya item makanan yang tidak mengandung protein atau mengandung hanya sedikit protein.

##### fat :
Rata-rata lemak per porsi makanan adalah sekitar 7.58 gram, dengan deviasi standar yang tinggi (13.73). Ini menunjukkan variasi yang signifikan dalam kandungan lemak antar item makanan. Nilai minimum yang nol mungkin menunjukkan adanya item makanan yang tidak mengandung lemak atau mengandung hanya sedikit lemak.

##### carbohydrate :
Rata-rata karbohidrat per porsi makanan adalah sekitar 25.39 gram, dengan standar deviasi sebesar 32.19 gram. Standar deviasi yang tinggi menunjukkan variasi yang cukup besar dalam kandungan karbohidrat antar item makanan. Nilai minimum yang nol mungkin menunjukkan adanya item makanan yang tidak mengandung karbohidrat atau mengandung hanya sedikit karbohidrat. Sedangkan nilai maksimum yang cukup tinggi (647.0) menunjukkan adanya item makanan dengan kandungan karbohidrat yang sangat tinggi.

Secara Keseluruhan untuk data understanding memberikan deskripsi tentang data yang digunakan untuk analisis hingga menemukan temuan temuan yang berpengaruh untuk goals dan tujuan project ini

## Data Preparation


##### 1. Cek duplikat data
Saat persiapan sebelum ketahap berikutnya telah dilakukan pengecekkan duplikasi data. hasilnya tidak ada baris yang sama dengan kata lain dataset tidak memiliki duplikasi data di tiap barisnya

##### 2. deteksi missing value Outliers menggunakan boxplot


pada umumnya dataset yang digunakan mengandung outliers, Outliers adalah nilai-nilai dalam dataset yang jauh berbeda dari nilai-nilai lainnya. Mereka bisa muncul karena berbagai alasan, seperti kesalahan pengukuran atau variasi alami.

 
![outlier](https://raw.githubusercontent.com/imamNurC/Notebook-Research/main/IndoNutriFood/img/outlier.png)

<sub>gambar3, boxplot Sebelum menghapus outlier </sub>


![remOutlier](https://raw.githubusercontent.com/imamNurC/Notebook-Research/main/IndoNutriFood/img/removeOutlier.png)

<sub>gambar4, boxplot Setelah menghapus outlier </sub>

Berikut beberapa informasi penting yang bisa diambil dari visualisasi kedua boxplot diatas sebelum dan setelah penghapusan outliers:

Sebelum Penghapusan Outliers: Visualisasi data sebelum penghapusan outliers memberikan gambaran tentang seluruh data, termasuk nilai-nilai ekstrem. Dalam konteks dataset ini, boxplot menunjukkan beberapa outliers dalam kalori, protein, lemak, dan karbohidrat. Outliers ini mungkin menunjukkan adanya item makanan dengan kandungan nutrisi yang sangat tinggi atau rendah. Namun, keberadaan outliers bisa mempengaruhi statistik deskriptif seperti mean dan standar deviasi, dan bisa mengganggu interpretasi data.

Setelah Penghapusan Outliers: Setelah outliers dihapus, visualisasi data biasanya menjadi lebih “bersih” dan lebih mudah untuk diinterpretasikan. Dalam boxplot tersebut setelah penghapusan outliers,bisa dilihat bahwa rentang data untuk kalori, protein, lemak, dan karbohidrat menjadi lebih kecil. Ini bisa membantu lebih memahami distribusi “normal” data dan membuat analisis lebih lanjut (seperti pemodelan statistik atau machine learning) menjadi lebih akurat.


##### 3. Persiapan data


**Teknik encoding**

Teknik encoding adalah suatu proses mengkonversi nilai dari fitur bertipe categorcal/text ke dalam format yang dapat di mengerti algoritma machine learning biasanya numerik tujuannya karena algorima machine learning adalah komputasi suatu bilangan numerik

 - **teknik encoding pada project ini adalah :**
 untuk kategorikal kolom dilakukan fungsi LabelEncoder() dan fit_transform untuk konversi text ke numerikal dari value value di kolom tersebut untuk di skalakan
   

**Correlation heatmap**

Sebelum menormalisasikan data, datanya perlu dipastikan lagi target yang akan menjadi prediksi dengan memvisualisasikan keterhubungan antar variable terkuat 

- **Corellation heatmap pada project ini adalah :**
    Teknik yang sudah diterapkan yakni menggunakan confussion matrix ternyata dari semua keterhubungan yang paling banyak berkorelasi yaitu variable calories sehingga ini menjadi trust score pertimbangan prediksi nutrisi berdasarkan jumlah kalorinya 

**Teknik Train-tes split**

Teknik ini merupakan prosedur validasi model yang mengungkapkan bagaimana kinerja model  pada data baru metode ini yakni memisahkan kumpulan set data yang akan di train/latih dan set data yang akan di tes dari hasil pelatihan

 - **teknik Train-tes split pada project ini adalah :**
     metode menggunakan perbandingan 80:20 untuk split (membagi) data, dimana 80% dari data digunakan untuk melatih model dan 20% sisanya digunakan untuk pengujian
    

**Normalisasi/scalling**

tahap ini merupakan langkah yang umum digunakan dalam tahap setelah data di split, sehingga memastikan bahwa skala nilai dari berbagai fitur numerik seimbang dan tidak mendominasi proses pemodelan. untuk setiap data latih(train) dan data uji(tes)

- **teknik normalisasi pada project ini adalah :**
    scickitlearn StandardScaler() untuk data yang telah di split, pada data train menggunakan method fit_transform() dan untuk data tes transform

## Modeling

  Pada tahap ini, menggunakan empat algoritma machine learning untuk menyelesaikan permasalahan prediksi kandungan nutrisi berdasarkan kalori dari makanan di Indonesia. dilakukan eksperimen dengan masing-masing algoritma dan memilih model terbaik berdasarkan evaluasi kinerja.
  
  
  ### Algoritma parameter yang Digunakan dalam pemodelan
  - #### Linear Regression (LR):
    **Parameter:**
    - Tidak ada parameter yang perlu dituning secara khusus, karena LR adalah model linier sederhana.


  - #### RandomForestRegressor(RFR):
       **Parameter:**
    - n_estimators=30: jumlah pohon sekitar 30 sudah cukup untuk mendapatkan hasil yang baik tanpa terlalu banyak mengorbankan kecepatan pelatihan.
    - max_depth=16: kedalaman maksimum setiap pohon, Nilai 16 dipilih setelah beberapa percobaan dan penilaian terhadap kinerja model pada data validasi. Ini  memberikan keseimbangan antara kinerja dan kecenderungan overfitting.
    - random_state = 42 : untuk menentukan rangkaian pelatihan dan pengujian yang sama pada eksekusi yang berbeda
    - n_jobs = -1 : Nilai -1 menunjukkan bahwa semua core CPU yang tersedia akan digunakan. Ini dapat mempercepat proses pelatihan.
  
  - #### AdaBoostRegression(ABR boosting algorithm):
     **Parameter:**
    - learning_rate = 0.05: tingkat pembelajaran, Sebuah nilai yang lebih rendah menunjukkan kontribusi yang lebih kecil dari setiap model keputusan. Ini dapat membantu menghindari overfitting.
    - random_state = 42 : untuk menentukan rangkaian pelatihan dan pengujian yang sama pada eksekusi yang berbeda 
  
 
  - #### KNeighborsRegressor(KNR):
    **Parameter:**
    - n_neighbors=10 : jumlah tetangga yang dipertimbangkan untuk memprediksi nilai,diatur ke 10, yang berarti model akan menggunakan 10 tetangga terdekat untuk membuat prediksi.

  ### Kelebihan dan Kekurangan Algoritma Machine Learning yang digunakan prediktif analisis nutrisi
  
  #### Linear Regression :
  - **Kelebihan:**
    - Sederhana dan mudah diinterpretasi.
    - Berjalan cepat dan cocok untuk data dengan fitur yang linier.
  
  - **Kekurangan:**
    - Tidak bisa menangani hubungan yang kompleks antara fitur dan target.
  
  #### AdaBoost:
  - **Kelebihan:**
    - Mampu meningkatkan kinerja dengan menggabungkan beberapa model lemah.
    - Tahan terhadap overfitting.
  - **Kekurangan:**
    - Rentan terhadap noise dan outliers dalam data.
  
#### RandomForestRegressor :
**Kelebihan:**
- Mampu menangani dataset dengan fitur yang banyak dan kompleks.
- Tidak memerlukan banyak tuning parameter

**Kekurangan:**
- Cenderung lambat dalam proses training untuk dataset besar.
  
#### KNeighborsRegressor:
**Kelebihan:**
- Sederhana dan mudah diimplementasikan.
- Tidak mengasumsikan distribusi data tertentu.

**Kekurangan:**
- Sensitif terhadap skala dan dimensi data.
- Memerlukan penyimpanan yang besar untuk menyimpan semua data pelatihan.

### Tahapan yang digunakan dalam proses pemodelan
  Secara umum proses pemodelan dalam project ini, dimulai dari :
 - Menentukan model prediktif analisis 
 - semua model diperuntukkan dari data yang sudah di split ke dalam 80% train saja
 - lakukan fit data latih dengan data yang sudah di skalakan(masing masing dari keempat model hal serupa)
 - Proses pelatihan di eksekusi berdasarkan parameter yang sudah di tentukan untuk menambah performa dari data yang sudah dilatih



**Menggunakan ke empat model tersebut karena :**

LinearRegression() :
algoritma yang menentukan hubungan antara fitur dan target secara linier seperti dalam kasus prediksi jumlah kalori berdasarkan atribut makanan atau minuman. ini adalah indikator yang kuat pada dataset Cocok untuk masalah regresi sederhana di mana hubungan antara variabel dependen dan independen linier


Boosting algorithm :
Algoritma yang menggunakan teknik boosting bekerja dengan membangun model dari data latih. Kemudian ia membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan. alasannya karena Dapat meningkatkan performa model dengan cara memperhatikan sampel yang salah diklasifikasikan pada iterasi sebelumnya.

RFR :
Algoritma RFR atau random forest adalah salah satu algoritma supervised learning. dapat digunakan untuk menyelesaikan masalah regresi dan juga klasifikasi. Random forest juga merupakan algoritma yang sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni. Random forest merupakan salah satu model machine learning yang termasuk ke dalam kategori ensemble (group) learning. yang berarti, model prediksi yang terdiri dari beberapa model dan bekerja secara bersama-sama untuk menyelesaikan masalah. Sehingga, tingkat keberhasilan akan lebih tinggi dibanding model yang bekerja sendirian. jadi pada dataset yang digunakan di kasus regresi sangat cocok karena memungkinkan model membuat data point yang bervariasi untuk nilai nilai nutrisi, prediksi akhir adalah rata-rata prediksi seluruh pohon dalam model ensemble. 

KNR : 
KNR atau KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif). algoritma yang relatif sederhana dibandingkan dengan algoritma lain. Algoritma KNN menggunakan ‘kesamaan fitur’ untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan. jadi dalam karakteristik dataset nutrisi sangat lah cocok digunakan karena banyak karakteristik data yang cocok dengan algoritma ini seperti kemiripan suatu makanan/minuman tentunya hampir mirip juga kandungan nutrisinya



## Evaluation
Metrik evaluasi yang digunakan adalah Mean Squared Error (MSE), yang mengukur jumlah selisih kuadrat rata-rata antara nilai sebenarnya dan nilai prediksi. Proses scalling dilakukan pada data latih untuk menghindari kebocoran data. Sementara itu, R-squared memberikan pemahaman tentang seberapa baik model cocok dengan data. Semakin mendekati nilai 1, R-squared menunjukkan bahwa model memahami data dengan baik dalam memprediksi, sedangkan nilai yang rendah menandakan sebaliknya.

Dalam kasus prediksi keakuratan nutrisi terhadap kalori menggunakan regresi dengan metrics **MSE(Mean Squared Error) dan  R-Squared**
- berdasarkan, metrik evaluasi yang di dapat dalam menentukan kalori dalam suatu makanan dan minuman diungguli oleh model dari linearRegression() dengan MSE test = 0.0058 artinya rata rata nilai prediksi yang error dari nilai asli dan R squarred Test = 0.8371 besarnya akurasi model yang dapat membaca seberapa cocok kalori prediksi dengan kalori yang sebenarnya

#### Evaluation Metrices
Mengkomparasikan performa dari kesalahan Error rata rata ter minimum (MSEs) pada dataset train dan tes
![datasethead](https://raw.githubusercontent.com/imamNurC/Notebook-Research/main/IndoNutriFood/img/bestmse.png)

<sub> gambar 5, MSE train vs MSE test </sub>
<sub>pada gambar 5, menunjukkan kesalahan error rata rata pada data tes dan train di ungguli oleh linear regression </sub>

### Result Models
tahap akhir besaran nilai evaluasi model

<sub> tabel 3, Evaluasi MSE dan juga R Squrred pada train dan tes secara numerik </sub>
| Model Name                | Mean Squared Error (Train) | Mean Squared Error (Test) | R-squared (Train) | R-squared (Test) |
|---------------------------|----------------------------|---------------------------|-------------------|------------------|
| Linear Regression         | 0.00250096263850438        | 0.0058361287734854305     | 0.929461663244967 | 0.8371216163780317 |
| Adaboost Regression       | 0.00421951658269911        | 0.008744347598192917      | 0.838529561193212 | 0.7559640141887368 |
| Random Forest             | 0.00039188476267620995     | 0.0066212268782707335     | 0.9894780686351566| 0.8152157596256422 |
| K Nearest Neighbors  | 0.0021843873819942158      | 0.006294557284124444      | 0.933777451866915 | 0.8243324073263159  |


Berdasarkan metrics diatas tampaknya semua model cukup dilatih dengan baik dari data Train dan tes pada konteks project ini berhasil / tidak bisa dikatakan project ini "Berhasil" karena terbilang cukup berhasil mendekati tujuan dan pertanyaan dalam goals yang diinginkan, serta target dipilihnya model yakni R-Squarred tes > 80% dan MSE tes < 0.1 artinya ada model yang sudah mampu mencapai goals dan yang terbaik yaitu linearRegression() dengan akurasi tes sekitar 84% dan kesalahan error rata rata sekitar 0.005

namun untuk saat ini belum sampai mampu menyelesaikan problem yang diangkat tetapi sudah menuju kearah situ, karena pengguna umum pastinya tidak terlalu paham apa yang dimaksudkan dari visualisasi yang di sajikan 

Diharapkan Model ini dapat digunakan sebagaimana solusi jawaban dari permasalahan pada bisnis, dan akan menjadi pengembangan lebih lanjut untuk meningkatkan performa dan skalabilitas pada data nya  serta dapat berjalan baik pada proses produksi di dunia nyata 



