# 📊 User Retention & Funnel Analysis

## 📌 Overview

This project analyzes user behavior across key stages of the product lifecycle using funnel analysis, cohort retention, and event distribution.

---

## 🎯 Objectives

* Analyze user drop-off across funnel stages
* Measure cohort-based retention trends
* Understand user engagement patterns

---

## 📊 Dataset

* **Users Data** → user_id, signup_date, acquisition channel
* **Events Data** → user actions with timestamps
* **Funnel Data** → stage-wise user counts

---

## 🔍 Funnel Analysis

* Tracks user journey from signup → upgrade
* Identifies drop-offs at each stage
* Visualized using funnel chart

### Key Insight

Significant drop-off observed before the upgrade stage.

---

## 🔁 Retention Analysis

* Cohort-based retention grouped by signup week
* Users bucketed into time intervals:

  * Day 0
  * Day 1–3
  * Day 4–7
  * Day 8–30

### Key Insight

Retention declines after Day 3, highlighting importance of early engagement.

---

## 📊 Event Distribution

* Analyzes frequency of user actions

### Key Insight

Core actions like login and project creation dominate usage, while upgrade events are lower.

---

## 🚀 Business Impact

* Improve onboarding experience
* Increase early-stage engagement
* Optimize funnel conversion
* Enhance user retention strategies

---

## 🛠️ Tech Stack

* Python
* Pandas
* Seaborn
* Matplotlib
* Plotly

---

## 📁 Project Structure

```
retention_funnel_projects/
│
├── 1_dashboards/
├── 2_data/
├── 3_notebooks/
├── 4_scripts/
├── 5_sql/
```

---

## 📌 Conclusion

This project demonstrates how funnel and retention analysis can uncover key user behavior patterns and drive data-informed product decisions.
