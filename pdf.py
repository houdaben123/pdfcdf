import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# عنوان التطبيق
st.title("اختبار الفرضيات حول الوسط الحسابي")

# اختيار نوع الاختبار
test_type = st.radio("اختر نوع اختبار t:", 
                     ["اختبار t لعينة واحدة", "اختبار t لعينتين مستقلتين", "اختبار t لعينتين مترابطتين"])

# اختيار طريقة إدخال البيانات
input_method = st.radio("اختر طريقة إدخال البيانات:", 
                        ["إدخال البيانات مباشرة", "إدخال الوسط الحسابي والتباين"])

# متغيرات عامة
alpha = st.number_input("مستوى الدلالة (α):", min_value=0.01, max_value=0.10, value=0.05, step=0.01)

if input_method == "إدخال البيانات مباشرة":
    # إدخال بيانات العينة (أو العينتين)
    sample_1 = st.text_area("أدخل بيانات العينة الأولى (مفصولة بمسافات أو فواصل):", "").strip()
    sample_1 = np.array([float(x) for x in sample_1.replace(",", " ").split() if x])

    if test_type != "اختبار t لعينة واحدة":
        sample_2 = st.text_area("أدخل بيانات العينة الثانية (مفصولة بمسافات أو فواصل):", "").strip()
        sample_2 = np.array([float(x) for x in sample_2.replace(",", " ").split() if x])

elif input_method == "إدخال الوسط الحسابي والتباين":
    mean_1 = st.number_input("أدخل الوسط الحسابي للعينة الأولى:", value=0.0)
    var_1 = st.number_input("أدخل التباين للعينة الأولى:", value=1.0)
    size_1 = st.number_input("أدخل حجم العينة الأولى:", value=10, step=1, min_value=1)

    if test_type != "اختبار t لعينة واحدة":
        mean_2 = st.number_input("أدخل الوسط الحسابي للعينة الثانية:", value=0.0)
        var_2 = st.number_input("أدخل التباين للعينة الثانية:", value=1.0)
        size_2 = st.number_input("أدخل حجم العينة الثانية:", value=10, step=1, min_value=1)

# زر لإجراء الاختبار
if st.button("إجراء الاختبار"):
    if input_method == "إدخال البيانات مباشرة" and len(sample_1) == 0:
        st.error("يرجى إدخال بيانات العينة.")
    else:
        if test_type == "اختبار t لعينة واحدة":
            mu0 = st.number_input("أدخل الوسط الحسابي المفترض تحت H0:", value=0.0)

            if input_method == "إدخال البيانات مباشرة":
                t_stat, p_value = stats.ttest_1samp(sample_1, mu0)
            else:
                se = np.sqrt(var_1 / size_1)
                t_stat = (mean_1 - mu0) / se
                df = size_1 - 1
                p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

        elif test_type == "اختبار t لعينتين مستقلتين":
            if input_method == "إدخال البيانات مباشرة":
                t_stat, p_value = stats.ttest_ind(sample_1, sample_2, equal_var=False)
            else:
                se = np.sqrt(var_1 / size_1 + var_2 / size_2)
                t_stat = (mean_1 - mean_2) / se
                df = ((var_1 / size_1 + var_2 / size_2) ** 2) / ((var_1 / size_1) ** 2 / (size_1 - 1) + (var_2 / size_2) ** 2 / (size_2 - 1))
                p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

        elif test_type == "اختبار t لعينتين مترابطتين":
            if input_method == "إدخال البيانات مباشرة":
                t_stat, p_value = stats.ttest_rel(sample_1, sample_2)
            else:
                st.error("لا يمكن استخدام هذه الطريقة لاختبار عينتين مترابطتين. أدخل البيانات مباشرة.")

        # عرض النتائج
        st.write(f"إحصائية t: {t_stat:.4f}")
        st.write(f"القيمة الاحتمالية (p-value): {p_value:.4f}")

        if p_value < alpha:
            st.success("نرفض الفرضية الصفرية (H0). يوجد فرق ذو دلالة إحصائية.")
        else:
            st.info("لا نرفض الفرضية الصفرية (H0). لا يوجد فرق ذو دلالة إحصائية.")

        # رسم التوزيع الطبيعي مع إحصائية t
        fig, ax = plt.subplots(figsize=(6, 4))
        x = np.linspace(-4, 4, 1000)
        y = stats.t.pdf(x, df if 'df' in locals() else len(sample_1) - 1)

        ax.plot(x, y, label="توزيع t", color="blue")
        ax.axvline(t_stat, color="red", linestyle="--", label=f"t-stat = {t_stat:.4f}")

        if p_value < alpha:
            ax.fill_between(x, y, where=(x > t_stat) | (x < -t_stat), color="red", alpha=0.3)
        else:
            ax.fill_between(x, y, where=(x > t_stat) | (x < -t_stat), color="gray", alpha=0.3)

        ax.set_title("التوزيع الاحتمالي واختبار t")
        ax.legend()
        st.pyplot(fig)
