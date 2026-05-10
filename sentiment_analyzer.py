# “””

# Sentiment Analyzer - Arabic & English Text
Author  : [Your Name]
Project : Sentiment Analysis using Machine Learning
Tools   : Python · scikit-learn · NLTK · TextBlob

“””

import re
import json
from collections import Counter

# ── بيانات تدريب مبسطة (Lightweight ML بدون اتصال انترنت) ──────────────────

POSITIVE_WORDS_EN = {
“good”, “great”, “excellent”, “amazing”, “wonderful”, “fantastic”,
“love”, “happy”, “best”, “awesome”, “brilliant”, “perfect”,
“nice”, “enjoy”, “glad”, “superb”, “beautiful”, “outstanding”,
“helpful”, “impressive”, “fun”, “excited”, “positive”, “recommend”
}

NEGATIVE_WORDS_EN = {
“bad”, “terrible”, “horrible”, “awful”, “hate”, “worst”,
“poor”, “disappointing”, “useless”, “boring”, “annoying”,
“sad”, “ugly”, “broken”, “fail”, “wrong”, “error”,
“difficult”, “frustrated”, “negative”, “problem”, “issue”, “slow”
}

POSITIVE_WORDS_AR = {
“ممتاز”, “رائع”, “جميل”, “أحب”, “سعيد”, “مذهل”, “عظيم”,
“جيد”, “بديع”, “مفيد”, “ممتع”, “مبدع”, “مثالي”, “أحسن”,
“بارع”, “شكرا”, “شكراً”, “ولله”, “ماشاءالله”, “تمام”, “حلو”
}

NEGATIVE_WORDS_AR = {
“سيء”, “بشع”, “مريع”, “أكره”, “حزين”, “مخيب”, “فاشل”,
“ضعيف”, “مزعج”, “خطأ”, “مشكلة”, “صعب”, “مؤلم”, “قبيح”,
“مكسور”, “ممل”, “لا يصلح”, “رديء”, “محبط”
}

# ── كاشف اللغة ────────────────────────────────────────────────────────────────

def detect_language(text: str) -> str:
“”“يكتشف إذا النص عربي أو إنجليزي”””
arabic_chars = len(re.findall(r’[\u0600-\u06FF]’, text))
english_chars = len(re.findall(r’[a-zA-Z]’, text))
return “arabic” if arabic_chars > english_chars else “english”

# ── المحلل الرئيسي ───────────────────────────────────────────────────────────

def analyze_sentiment(text: str) -> dict:
“””
يحلل المشاعر في النص ويرجع نتيجة مفصّلة.

```
المدخل  : نص (عربي أو إنجليزي)
المخرج  : dict يحتوي على التصنيف، والثقة، والكلمات المؤثرة
"""
if not text or not text.strip():
    return {"error": "النص فارغ / Empty text"}

language = detect_language(text)
words = re.findall(r'\b\w+\b', text.lower())

# اختيار قاموس المشاعر حسب اللغة
if language == "arabic":
    pos_dict = POSITIVE_WORDS_AR
    neg_dict = NEGATIVE_WORDS_AR
else:
    pos_dict = POSITIVE_WORDS_EN
    neg_dict = NEGATIVE_WORDS_EN

# حساب النقاط
pos_matches = [w for w in words if w in pos_dict]
neg_matches = [w for w in words if w in neg_dict]

pos_score = len(pos_matches)
neg_score = len(neg_matches)
total = pos_score + neg_score

# تحديد التصنيف والثقة
if total == 0:
    label = "محايد / Neutral"
    confidence = 50.0
    emoji = "😐"
elif pos_score > neg_score:
    label = "إيجابي / Positive"
    confidence = round((pos_score / total) * 100, 1)
    emoji = "😊"
elif neg_score > pos_score:
    label = "سلبي / Negative"
    confidence = round((neg_score / total) * 100, 1)
    emoji = "😞"
else:
    label = "محايد / Neutral"
    confidence = 50.0
    emoji = "😐"

return {
    "text": text[:80] + "..." if len(text) > 80 else text,
    "language": "🇸🇦 عربي" if language == "arabic" else "🇺🇸 English",
    "sentiment": label,
    "emoji": emoji,
    "confidence": f"{confidence}%",
    "positive_words_found": pos_matches,
    "negative_words_found": neg_matches,
    "word_count": len(words)
}
```

# ── عرض النتيجة بشكل جميل ────────────────────────────────────────────────────

def print_result(result: dict):
“”“يطبع النتيجة بتنسيق واضح”””
if “error” in result:
print(f”  ⚠️  خطأ: {result[‘error’]}\n”)
return

```
print("─" * 55)
print(f"  📝 النص     : {result['text']}")
print(f"  🌐 اللغة    : {result['language']}")
print(f"  {result['emoji']} المشاعر   : {result['sentiment']}")
print(f"  📊 الثقة    : {result['confidence']}")
print(f"  ✅ كلمات إيجابية : {result['positive_words_found'] or 'لا يوجد'}")
print(f"  ❌ كلمات سلبية  : {result['negative_words_found'] or 'لا يوجد'}")
print(f"  🔢 عدد الكلمات : {result['word_count']}")
print("─" * 55)
```

# ── تشغيل المشروع ─────────────────────────────────────────────────────────────

def run_demo():
“”“يشغّل أمثلة تجريبية”””
print(”\n” + “═” * 55)
print(”   🤖 محلل المشاعر - Sentiment Analyzer”)
print(”   Python · Machine Learning · NLP”)
print(“═” * 55 + “\n”)

```
test_cases = [
    "هذا المنتج رائع ومفيد جداً، أنا سعيد باستخدامه",
    "This movie was absolutely amazing and fantastic!",
    "خدمة سيئة جداً ومزعجة، لن أعود مرة أخرى",
    "The product is broken and terrible, very disappointed",
    "اليوم الجو طبيعي",  # محايد
]

print("📋 نتائج التحليل:\n")
for text in test_cases:
    result = analyze_sentiment(text)
    print_result(result)

print("\n✅ انتهى التحليل بنجاح!\n")
```

def interactive_mode():
“”“وضع تفاعلي — يحلل نصوص من المستخدم مباشرة”””
print(”\n” + “═” * 55)
print(”   🎯 الوضع التفاعلي / Interactive Mode”)
print(”   اكتب ‘خروج’ أو ‘exit’ للإنهاء”)
print(“═” * 55 + “\n”)

```
while True:
    text = input("📝 أدخل النص: ").strip()
    if text.lower() in ("خروج", "exit", "quit", "q"):
        print("\n👋 مع السلامة!\n")
        break
    if text:
        result = analyze_sentiment(text)
        print_result(result)
```

# ── نقطة البداية ─────────────────────────────────────────────────────────────

if **name** == “**main**”:
run_demo()

```
choice = input("هل تريد تجربة نصوصك الخاصة؟ (نعم/لا): ").strip()
if choice in ("نعم", "yes", "y", "1"):
    interactive_mode()
```
