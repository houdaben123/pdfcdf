import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import streamlit as st  # إضافة مكتبة Streamlit

# إنشاء الرسومات
def plot_distribution(distribution_name, x_values, distributions):
    fig, ax = plt.subplots(figsize=(6, 4))

    for params, label in distributions:
        pdf_values = params.pdf(x_values)
        ax.plot(x_values, pdf_values, label=label)

    ax.set_title(f'PDF of {distribution_name}')
    ax.legend()
    
    # عرض الشكل في Streamlit
    st.pyplot(fig)

# إعداد الصفحة في Streamlit
st.title("Visualization of Probability Distributions")

# التوزيع الطبيعي
x = np.linspace(-4, 4, 1000)
distributions = [(stats.norm(loc=mu, scale=sigma), f'μ={mu}, σ={sigma}') for mu, sigma in [(-1, 1), (0, 1), (1, 1), (0, 0.5), (0, 2)]]
plot_distribution("Normal Distribution", x, distributions)

# التوزيع الطبيعي المعياري
x = np.linspace(-4, 4, 1000)
distributions = [(stats.norm(), 'Standard Normal')]
plot_distribution("Standard Normal Distribution", x, distributions)

# توزيع ستودنت
x = np.linspace(-4, 4, 1000)
distributions = [(stats.t(df=df), f'df={df}') for df in [1, 5, 10, 30, 50]]
plot_distribution("Student's t-Distribution", x, distributions)

# توزيع كاي مربع
x = np.linspace(0, 10, 1000)
distributions = [(stats.chi2(df=df), f'df={df}') for df in [1, 2, 3, 5, 10]]
plot_distribution("Chi-Square Distribution", x, distributions)

# توزيع فيشر
x = np.linspace(0, 5, 1000)
distributions = [(stats.f(df1=d1, df2=d2), f'df1={d1}, df2={d2}') for d1, d2 in [(1, 2), (2, 5), (5, 10), (10, 20), (20, 30)]]
plot_distribution("F-Distribution", x, distributions)

# التوزيع الأسي
x = np.linspace(0, 5, 1000)
distributions = [(stats.expon(scale=scale), f'λ={1/scale:.2f}') for scale in [0.5, 1, 2, 3, 4]]
plot_distribution("Exponential Distribution", x, distributions)

# توزيع غاما
x = np.linspace(0, 10, 1000)
distributions = [(stats.gamma(a=shape), f'k={shape}') for shape in [1, 2, 3, 5, 7]]
plot_distribution("Gamma Distribution", x, distributions)

# توزيع بيتا
x = np.linspace(0, 1, 1000)
distributions = [(stats.beta(a=a, b=b), f'α={a}, β={b}') for a, b in [(0.5, 0.5), (2, 2), (2, 5), (5, 1), (5, 5)]]
plot_distribution("Beta Distribution", x, distributions)
