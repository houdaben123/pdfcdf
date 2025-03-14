import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# إعداد الواجهة في Streamlit
st.title("اختبار t الإحصائي")

# اختيار نوع الاختبار
test_type = st.radio("اختر نوع الاختبار:", 
                     ["اختبار t لعينة واحدة", "اختبار t لعينتين مستقلتين", "اختبار t لعينتين مترابطتين"])

# إدخال البيانات
if test_type == "اختبار t لعينة واحدة":
    mu = st.number_input("أدخل القيمة الفرضية للمتوسط µ:", value=0.0)
    sample_size = st.number_input("عدد القيم في العينة:", min_value=2, value=10)
    sample = st.text_area("أدخل بيانات العينة (مفصولة بمسافات أو فواصل):", "10, 12, 9, 11, 8, 10, 13, 7, 12, 11")
    sample = np.array([float(x) for x in sample.replace(',', ' ').split()])
    
    if len(sample) > 1:
        t_stat, p_value = stats.ttest_1samp(sample, mu)
        st.write(f"**إحصائية t:** {t_stat:.4f}")
        st.write(f"**قيمة p:** {p_value:.4f}")
    
elif test_type == "اختبار t لعينتين مستقلتين":
    sample1 = st.text_area("أدخل بيانات العينة الأولى (مفصولة بمسافات أو فواصل):", "10, 12, 14, 11, 9, 13, 15")
    sample2 = st.text_area("أدخل بيانات العينة الثانية (مفصولة بمسافات أو فواصل):", "9, 8, 7, 10, 11, 9, 6")
    
    sample1 = np.array([float(x) for x in sample1.replace(',', ' ').split()])
    sample2 = np.array([float(x) for x in sample2.replace(',', ' ').split()])
    
    if len(sample1) > 1 and len(sample2) > 1:
        t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)
        st.write(f"**إحصائية t:** {t_stat:.4f}")
        st.write(f"**قيمة p:** {p_value:.4f}")

elif test_type == "اختبار t لعينتين مترابطتين":
    sample1 = st.text_area("أدخل بيانات المجموعة الأولى (مفصولة بمسافات أو فواصل):", "10, 12, 14, 11, 9, 13, 15")
    sample2 = st.text_area("أدخل بيانات المجموعة الثانية (مفصولة بمسافات أو فواصل):", "9, 11, 13, 10, 8, 12, 14")
    
    sample1 = np.array([float(x) for x in sample1.replace(',', ' ').split()])
    sample2 = np.array([float(x) for x in sample2.replace(',', ' ').split()])
    
    if len(sample1) == len(sample2) and len(sample1) > 1:
        t_stat, p_value = stats.ttest_rel(sample1, sample2)
        st.write(f"**إحصائية t:** {t_stat:.4f}")
        st.write(f"**قيمة p:** {p_value:.4f}")
    else:
        st.error("يجب أن تحتوي المجموعتان على نفس عدد القيم!")

# رسم التوزيع وإبراز t
fig, ax = plt.subplots()
x = np.linspace(-4, 4, 100)
y = stats.t.pdf(x, df=10)  # توزيع t بدرجات حرية 10
sns.lineplot(x=x, y=y, ax=ax, label="توزيع t")

ax.axvline(x=t_stat, color='red', linestyle='--', label="قيمة t المحسوبة")
ax.fill_between(x, 0, y, where=(x >= t_stat), color='red', alpha=0.3)
ax.legend()
st.pyplot(fig)
