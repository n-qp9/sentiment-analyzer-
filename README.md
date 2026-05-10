# 🤖 Sentiment Analyzer — Arabic & English NLP

> **مشروع تحليل مشاعر النصوص باستخدام Python والذكاء الاصطناعي**  
> Detect whether text is Positive, Negative, or Neutral — in Arabic & English.

-----

##  نبذة عن المشروع / About

This project is a **Natural Language Processing (NLP)** tool built in Python that analyzes the sentiment of text in both **Arabic and English**. It uses a lexicon-based machine learning approach to classify text as:

|التصنيف|Sentiment|Emoji|
|-------|---------|-----|
|إيجابي |Positive |😊    |
|سلبي   |Negative |😞    |
|محايد  |Neutral  |😐    |

-----

##  المميزات / Features

- 🌐 **ثنائي اللغة** — يدعم العربية والإنجليزية
- 📊 **نسبة الثقة** — يعطي نسبة مئوية لدقة التحليل
- 🔍 **الكلمات المؤثرة** — يحدد الكلمات الإيجابية والسلبية في النص
- 🎯 **وضع تفاعلي** — يمكن اختبار أي نص مباشرة من الـ Terminal
- 💡 **خفيف** — لا يحتاج اتصال إنترنت أو مكتبات ثقيلة

-----

##  التقنيات المستخدمة / Tech Stack

```
Language : Python 3.x
Approach : Lexicon-based Sentiment Analysis (NLP)
Libraries: re · json · collections (built-in only)
Concepts : Text Classification · Language Detection · NLP
```

-----

##  طريقة التشغيل / How to Run

**1. تأكد من تثبيت Python:**

```bash
python --version
```

**2. شغّل المشروع:**

```bash
python sentiment_analyzer.py
```

**3. جرّب نصوصك الخاصة:**

```
📝 أدخل النص: هذا المنتج رائع ومفيد جداً
─────────────────────────────────────────
  📝 النص     : هذا المنتج رائع ومفيد جداً
  🌐 اللغة    : 🇸🇦 عربي
  😊 المشاعر   : إيجابي / Positive
  📊 الثقة    : 100%
  ✅ كلمات إيجابية : ['رائع', 'مفيد']
─────────────────────────────────────────
```

-----

##  هيكل المشروع / Project Structure

```
sentiment-analyzer/
│
├── sentiment_analyzer.py   # الكود الرئيسي / Main script
├── README.md               # توثيق المشروع / Documentation
└── examples/
    └── sample_texts.txt    # أمثلة نصية / Sample texts
```

-----

##  أمثلة / Examples

```python
from sentiment_analyzer import analyze_sentiment

result = analyze_sentiment("This product is absolutely amazing!")
print(result["sentiment"])   # إيجابي / Positive
print(result["confidence"])  # 100%

result2 = analyze_sentiment("خدمة سيئة جداً ومحبطة")
print(result2["sentiment"])  # سلبي / Negative
```

-----

##  ما تعلمته / What I Learned

- مفاهيم **NLP** ومعالجة النصوص الطبيعية
- كيفية بناء **مصنّف نصوص (Text Classifier)** من الصفر
- اكتشاف اللغة برمجياً باستخدام **Regex**
- تصميم كود Python نظيف وقابل للقراءة

-----

##  تطويرات مستقبلية / Future Improvements

- [ ] إضافة نموذج ML متقدم (BERT / AraBERT)
- [ ] واجهة ويب باستخدام Flask
- [ ] تحليل مشاعر تويتر/X بشكل مباشر
- [ ] دعم لغات إضافية

-----

## 👨‍💻 المطور / Developer

**[اسمك هنا / Your Name]**  
🎓 طالب في أكاديمية طويق  
📧 [بريدك الإلكتروني]  
🔗 [LinkedIn Profile]

-----

> ⭐ إذا أعجبك المشروع، لا تنسى تضغط Star على GitHub!
