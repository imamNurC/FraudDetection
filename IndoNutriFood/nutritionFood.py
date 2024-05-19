# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import string
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import warnings

# %% [markdown]
# ## Load dataset

# %%
# from google.colab import drive
# drive.mount('/content/drive/', force_remount=True)

# %%
# data = pd.read_csv('/content/drive/MyDrive/IndoNutrition/nutrition.csv')
data = pd.read_csv('nutrition.csv')

# %%
data.head()

# %% [markdown]
# ### Hapus kolom id dan image
# dalam menemukan insight yang sesuai kolom id dan image tidak diperlukan dalam kebutuhan analisis ini

# %%
data = data.drop(['id','image'], axis=1)

# %% [markdown]
# ### Descriptive Statistics

# %%
data.describe()


# %%
data.info()


# %% [markdown]
# ### cek tidak ada kolom kosong?

# %%
data.isna().sum()

# %% [markdown]
# ### cek ada baris yg duplikat?

# %%
data.duplicated().sum()

# %% [markdown]
# ### backup data

# %%
df = data.copy()

# %% [markdown]
# # Exploratory Data Analysis
# ## Univariate Analysis
# 

# %%
numerical_features = ['calories', 'proteins', 'fat', 'carbohydrate']


fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(18, 4))
for i, col in enumerate(numerical_features):
    plt.subplot(1, 4, i+1)


    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')


    warnings.filterwarnings("ignore", category=FutureWarning)


# plt.show()
plt.tight_layout()

# %% [markdown]
# #### opsional
# menemukan keyword 

# %%
text = " ".join(df['name'].astype(str))


wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='white', colormap='rainbow', collocations=False, stopwords=STOPWORDS).generate(text)

# Plot
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# %% [markdown]
# ## Bivariate Analysis

# %%
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))

for i, feat in enumerate(numerical_features[1:]):
    plt.subplot(1, 3, i+1)
    sns.scatterplot(x=feat, y='calories', data=df)
    plt.title(f' {feat.capitalize()} vs. Calories')


plt.tight_layout()
plt.show()

# %% [markdown]
# ## Multivariate Analysis

# %%

sns.pairplot(df[['calories', 'proteins', 'fat', 'carbohydrate']],plot_kws={"s": 3})
plt.suptitle('Nutritional Content', y=1.02)
# plt.show()

# %% [markdown]
# #### numerical outliers boxplot

# %%

# import seaborn as sns


plt.figure(figsize=(20, 3))

for i, feature in enumerate(numerical_features):
    plt.subplot(1, 4, i+1)

    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot {feature}')


    warnings.filterwarnings("ignore", category=FutureWarning)

plt.show()


# %%
# # df[numerical_features] = df[numerical_features].apply(pd.to_numeric, errors='coerce')

Q1 = df[numerical_features].quantile(0.25)
Q3 = df[numerical_features].quantile(0.75)
IQR=Q3-Q1
df=df[~((df[numerical_features]<(Q1-1.5*IQR))|(df[numerical_features] >(Q3+1.5*IQR))).any(axis=1)]

# Cek ukuran dataset setelah kita drop outliers
df.shape

# %% [markdown]
# #### After Removing the outliers

# %%
plt.figure(figsize=(20, 3))

for i, feature in enumerate(numerical_features):
    plt.subplot(1, 4, i+1)

    sns.boxplot(x=df[feature],color='green')
    plt.title(f'Boxplot {feature}')


    warnings.filterwarnings("ignore", category=FutureWarning)

plt.show()

# %% [markdown]
# # Data Preparation
#  Label Encoding berujuan untuk kolom tipe kategorikal dan menskalakan nilai kolom numerik agar dapat mendapati insight fitur korelasi antar variable

# %%
catcol = []
numcol = []

for col in df.columns:
    if df[col].dtype == 'object':
        catcol.append(col)
    else:
        numcol.append(col)

print("Categorical Columns:",catcol)
print("Numerical Columns:", numcol)

encoder = LabelEncoder()

for col in catcol:  # Corrected here
    df[col] = encoder.fit_transform(df[col])

scale = MinMaxScaler()

for col in numcol:
    df[[col]] = scale.fit_transform(df[[col]])

df.head()


# %% [markdown]
# ### Korelasi antara fitur tiap variable
# 
# tujuannya mengetahui keterhubungan kuat antar variaable, pada hasil ini ternyata kalori mempunyi keterikatan kuat dengan variable variable lainnya, sehingga memutuskan bahwa variable calories cocok untuk menjadi target prediksi untuk mewakili keseluruhan nutrisi yang terkandung dari suatu makanan

# %%
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

plt.figure(figsize=(15, 12))

cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

plt.title('Correlation Heatmap')
plt.show()

# %% [markdown]
# ## train-test splitting dan Scalling

# %%
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Ridge
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.svm import scR
# from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# %%
data_ml = df.copy()

# %%
data_ml = data_ml.drop(['name'], axis=1)

# %% [markdown]
# Split data 0.2 untuk tes, 0.8 untuk training dan melakukan transformasi scalling

# %%
X = data_ml.drop('calories', axis=1)
y = data_ml['calories']

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# %% [markdown]
# # Modeling
# 
# modelling yang akan di lakukan menggunakan 4 buah tipe :
# 
# LinearRegression()
# 
# RandomForestRegression(max_depth=16, n_estimators=30, n_jobs=-1, random_state=4)
# 
# AdaBoostRegression(learning_rate=0.05, random_state=42)
# 
# KNeigborsRegression(n_neighbors=10)

# %%
LR = LinearRegression()
RFR = RandomForestRegressor(n_estimators=30, max_depth=16, random_state=42, n_jobs=-1) #parameter
ABR = AdaBoostRegressor(learning_rate=0.05, random_state=42)
KNR = KNeighborsRegressor(n_neighbors=10)


LR.fit(X_train_scaled, y_train)


# %%

RFR.fit(X_train_scaled, y_train)

# %%

ABR.fit(X_train_scaled, y_train)

# %%
KNR.fit(X_train_scaled, y_train)

# %% [markdown]
# # Evaluation
# 
# fungi ini untuk mengevaluasi tiap tipe model dengan data yang sudah di split dalam 0.8 train 0.2 test dan pula menghitung R square sebagai kecocokan kalori prediksi dengan kalorri sebenarnya pada data set train dan tes

# %%
def evaluate_model(model, X_train, y_train, X_test, y_test):
    # Predictions on the training set
    y_train_pred = model.predict(X_train)
    # Predictions on the test set
    y_test_pred = model.predict(X_test)

    # Calculate MSE for train and test sets
    mse_train = mean_squared_error(y_train, y_train_pred)
    mse_test = mean_squared_error(y_test, y_test_pred)

    # Calculate R2 for train and test sets
    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)

    # Plot actual vs predicted values for test set
    plt.scatter(y_test, y_test_pred)
    plt.xlabel('Actual Calories')
    plt.ylabel('Predicted Calories')
    plt.title(f'Actual vs Predicted Calories - {type(model).__name__}')
    plt.show()

    return mse_train, mse_test, r2_train, r2_test

# %% [markdown]
# benchmark model berdasarkan MSE terurut dari performa train dan tes yang terbaik sampai performa nya terjelek, semakin rata rata error menunjukkan angka yang kecil maka error semakin minimal dan pula sebaliknya
# dan tampak terlihat MSE train dan tes model yang terminimum yaitu  linear regression

# %%
# Evaluate model
results = {}
models = {'lr':LR,'rfr':RFR,'abr':ABR,'knr':KNR}

for model_name, model in models.items():
    mse_train, mse_test, r2_train, r2_test = evaluate_model(model, X_train_scaled, y_train, X_test_scaled, y_test) # yang sudah di skalakan
    results[model_name] = {'MSE_train': mse_train, 'MSE_test': mse_test, 'R2_train': r2_train, 'R2_test': r2_test}

# Convert results to DataFrame
results_df = pd.DataFrame(results).T.reset_index().rename(columns={'index': 'Model'})

# Sort DataFrame by test set MSE
mse_sorted = results_df.sort_values(by='MSE_test', ascending=False)

# Create a horizontal bar plot
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size if needed
mse_sorted.plot(kind='barh', x='Model', y=['MSE_train', 'MSE_test'], ax=ax, zorder=3)

# Add grid lines
ax.grid(zorder=0)

# Set labels and title
plt.xlabel('Mean Squared Error (MSE)')
plt.ylabel('Model')
plt.title('Mean Squared Error (MSE) Comparison between Train and Test Sets')

# Add legend
plt.legend(['Train Set', 'Test Set'])

# Show the plot
plt.show()


# %% [markdown]
# ## summary model
# 
# linear regression dengan parameter kosong sebagai best model

# %%
# Find the best model based on the minimum test MSE
best_model = min(results, key=lambda x: results[x]['MSE_test'])

# Extract MSE and R-squared values for the best model
best_metrics = results[best_model]

for model_name, metrics in results.items():
    print(f'Model: {model_name}')
    print(f'Mean Squared Error (Train): {metrics["MSE_train"]}')
    print(f'Mean Squared Error (Test): {metrics["MSE_test"]}')
    print(f'R-squared (Train): {metrics["R2_train"]}')
    print(f'R-squared (Test): {metrics["R2_test"]}')
    print()


print('=============================================')

# Print the best model and its evaluation metrics
print(f'Best Model: {best_model}')
print(f'Mean Squared Error (Train): {best_metrics["MSE_train"]}')
print(f'Mean Squared Error (Test): {best_metrics["MSE_test"]}')
print(f'R-squared (Train): {best_metrics["R2_train"]}')
print(f'R-squared (Test): {best_metrics["R2_test"]}')




