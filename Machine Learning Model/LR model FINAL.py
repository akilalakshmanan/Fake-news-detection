from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import re
import string

df_fake = pd.read_csv("fake.csv")
df_true = pd.read_csv("true.csv")

# print(df_fake.head(10))
# print(df_true.head(10))

df_fake["class"] = 1
df_true["class"] = 0
#print(df_fake.shape, df_true.shape)

df_merge = pd.concat([df_fake, df_true], axis=0)
# print(df_merge.head(10))

df = df_merge.drop(["text"], axis=1)
# print(df.head(10))

df = df.sample(frac=1)
# print(df.head(10))

df.isnull().sum()


def word_drop(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text


df["title"] = df["title"].apply(word_drop)
# print(df.head(10))

x = df["title"]
y = df["class"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

# Logistic Regression

LR = LogisticRegression()
LR.fit(xv_train, y_train)

LR_score = LR.score(xv_test, y_test)
print(LR_score)

# making prediction on test data
pred_LR = LR.predict(xv_test)
print(classification_report(y_test, pred_LR))

# confusion matrix
# actual value of testing set (y_test) and prediction of testing set (pred_LR) is passed
cm = confusion_matrix(y_test, pred_LR)
print(cm)


# Manual Testing


def output_label(n):
    if(n == 0):
        return "Not a Fake news"
    elif(n == 1):
        return "Fake news"


def manual_testing(news):
    testing_news = {"title": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["title"] = new_def_test["title"].apply(word_drop)
    new_x_test = new_def_test["title"]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    #pred_DT = DT.predict(new_xv_test)

    return print("\nLR prediction: {} ".format(output_label(pred_LR)))


i = 0
while(i <= 10):
    print("Enter news content: ")  # from manual_testing.csv
    news = str(input())
    i = i+1
    manual_testing(news)
