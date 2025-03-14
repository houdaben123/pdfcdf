import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import streamlit as st

# إعداد واجهة Streamlit
st.title("🎲 رسم دالة الكثافة الاحتمالية (PDF) ودالة التوزيع التراكمي (CDF)")

# قائمة التوزيعات المتاحة
distributions = {
    "التوزيع الطبيعي": ("norm", {"loc": 0, "scale": 1}),
    "التوزيع الطبيعي المعياري": ("norm", {"loc": 0, "scale": 1}),
    "توزيع ستودنت": ("t", {"df": 10}),
    "توزيع كاي مربع": ("chi2", {"df": 5}),
    "توزيع فيشر": ("f", {"dfn": 5, "dfd": 2}),
    "التوزيع الأسي": ("expon", {"scale": 1}),
    "توزيع غاما": ("gamma", {"a": 2}),
    "توزيع بيتا": ("beta", {"a": 2, "b": 5})
}

# اختيار التوزيع من القائمة
dist_name = st.selectbox("🔍 اختر التوزيع:", list(distributions.keys()))

# إعداد نطاق القيم بناءً على التوزيع المختار
dist_key, params = distributions[dist_name]
dist = getattr(stats, dist_key)  # استدعاء التوزيع من scipy.stats
x = np.linspace(dist.ppf(0.01, **params), dist.ppf(0.99, **params), 100)

# حساب PDF و CDF
pdf = dist.pdf(x, **params)
cdf = dist.cdf(x, **params)

# رسم التوزيعات
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# رسم دالة الكثافة الاحتمالية PDF
ax[0].plot(x, pdf, 'b-', lw=2, label="PDF")
ax[0].set_title(f"دالة الكثافة الاحتمالية ({dist_name})")
ax[0].legend()
ax[0].grid()

# رسم دالة التوزيع التراكمي CDF
ax[1].plot(x, cdf, 'r-', lw=2, label="CDF")
ax[1].set_title(f"دالة التوزيع التراكمي ({dist_name})")
ax[1].legend()
ax[1].grid()

# عرض الرسومات
st.pyplot(fig)
