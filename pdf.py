import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# إعداد التوزيعات والمعالم الخاصة بها
distributions = {
    "Normal": [(0, 1), (0, 2), (-2, 1), (2, 0.5), (1, 1.5)],  # (mean, std)
    "Standard Normal": [(0, 1)],
    "Student's t": [1, 2, 5, 10, 30],  # درجات الحرية
    "Chi-Square": [1, 2, 5, 10, 30],  # درجات الحرية
    "F-Distribution": [(5, 2), (10, 5), (20, 10), (30, 15), (40, 20)],  # (df1, df2)
    "Exponential": [0.5, 1, 2, 3, 5],  # معدل λ
    "Gamma": [(1, 2), (2, 2), (3, 1), (5, 1), (7, 0.5)],  # (shape, scale)
    "Beta": [(0.5, 0.5), (1, 2), (2, 2), (2, 5), (5, 1)]  # (alpha, beta)
}

# إعداد الأشكال
fig, axes = plt.subplots(len(distributions), 2, figsize=(12, 20))
x = np.linspace(-5, 5, 1000)  # نطاق القيم

# رسم التوزيعات
for i, (dist, params) in enumerate(distributions.items()):
    ax_pdf = axes[i, 0]
    ax_cdf = axes[i, 1]
    
    for param in params:
        if dist == "Normal":
            pdf = stats.norm.pdf(x, loc=param[0], scale=param[1])
            cdf = stats.norm.cdf(x, loc=param[0], scale=param[1])
            label = f"μ={param[0]}, σ={param[1]}"
        elif dist == "Standard Normal":
            pdf = stats.norm.pdf(x)
            cdf = stats.norm.cdf(x)
            label = "μ=0, σ=1"
        elif dist == "Student's t":
            pdf = stats.t.pdf(x, df=param)
            cdf = stats.t.cdf(x, df=param)
            label = f"df={param}"
        elif dist == "Chi-Square":
            x = np.linspace(0, 10, 1000)
            pdf = stats.chi2.pdf(x, df=param)
            cdf = stats.chi2.cdf(x, df=param)
            label = f"df={param}"
        elif dist == "F-Distribution":
            x = np.linspace(0, 5, 1000)
            pdf = stats.f.pdf(x, dfn=param[0], dfd=param[1])
            cdf = stats.f.cdf(x, dfn=param[0], dfd=param[1])
            label = f"df1={param[0]}, df2={param[1]}"
        elif dist == "Exponential":
            x = np.linspace(0, 5, 1000)
            pdf = stats.expon.pdf(x, scale=1/param)
            cdf = stats.expon.cdf(x, scale=1/param)
            label = f"λ={param}"
        elif dist == "Gamma":
            x = np.linspace(0, 10, 1000)
            pdf = stats.gamma.pdf(x, a=param[0], scale=param[1])
            cdf = stats.gamma.cdf(x, a=param[0], scale=param[1])
            label = f"shape={param[0]}, scale={param[1]}"
        elif dist == "Beta":
            x = np.linspace(0, 1, 1000)
            pdf = stats.beta.pdf(x, a=param[0], b=param[1])
            cdf = stats.beta.cdf(x, a=param[0], b=param[1])
            label = f"α={param[0]}, β={param[1]}"

        # رسم المنحنيات
        ax_pdf.plot(x, pdf, label=label)
        ax_cdf.plot(x, cdf, label=label)

    # تنسيق الرسومات
    ax_pdf.set_title(f"{dist} PDF")
    ax_cdf.set_title(f"{dist} CDF")
    ax_pdf.legend()
    ax_cdf.legend()
    ax_pdf.grid()
    ax_cdf.grid()

# عرض الأشكال
plt.tight_layout()
plt.show()
