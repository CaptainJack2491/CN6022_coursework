### 🧑‍🔬 Member 1: Jasmi (Focus: Star Types & Populations)
**Theme:** Classification & Unsupervised Learning (The H-R Diagram)

* **Model 1: The "Spectral Class" Predictor (Multi-class Classification)**
    * **The Goal:** Predict a star's spectral type (O, B, A, F, G, K, M) based on its properties.
    * **The "Label":** You don't have the text label, so you **create it** in Spark before training. Bin `teff_gspphot` (Temperature) into classes:
        * $> 7500K \to$ 'A/B/O' (Hot)
        * $5200K - 7500K \to$ 'G/F' (Sun-like)
        * $< 5200K \to$ 'K/M' (Cool)
    * **The Features:** `bp_rp` (Color), `absolute_magnitude` (Calculated), `phot_g_mean_mag`.
    * **The Algorithm:** **Random Forest Classifier** (Handles non-linear boundaries well).
    * **Coursework Checklist:** This lets you demonstrate **Label Indexing** and **Confusion Matrices**.

* **Model 2: The "Blind" Population Finder (Clustering)**
    * **The Goal:** Can an AI discover that Red Giants and White Dwarfs are different from normal stars *without* being told?
    * **The Features:** `bp_rp` and `absolute_magnitude`.
    * **The Algorithm:** **K-Means Clustering** ($k=3$ or $k=4$).
    * **Coursework Checklist:** This is **Unsupervised Learning**. You visualize the clusters on the H-R diagram to show they match the physics.

### 🔭 Member 2: Yogi (Focus: Structure & Data Quality)
**Theme:** Regression (Predicting Continuous Values)

* **Model 1: The "Photometric Parallax" Engine (Regression)**
    * **The Goal:** Predict the distance to a star (`parallax`) using only its color and brightness. This is a real technique astronomers use when parallax data is missing!
    * **The Label:** `parallax`.
    * **The Features:** `phot_g_mean_mag`, `bp_rp`, `teff_gspphot`.
    * **The Algorithm:** **Gradient Boosted Tree (GBT) Regressor**.
    * **Coursework Checklist:** Demonstrates **Feature Scaling** (StandardScaler) because Magnitude (1-20) and Temperature (3000-50000) have vastly different scales.

* **Model 2: The "Error Predictor" (Regression)**
    * **The Goal:** Predict how "bad" the data quality (`parallax_error`) will be based on the star's position and brightness.
    * **The Label:** `parallax_error`.
    * **The Features:** `phot_g_mean_mag` (dimmer stars should have more error), `dec` (stars low on horizon might have more error).
    * **The Algorithm:** **Linear Regression** (Simple baseline to compare against GBT).
    * **Coursework Checklist:** Good for **Model Evaluation** ($R^2$ and RMSE comparison).

### ✨ Member 3: Jayrup (Focus: Exotic Objects & Outliers)
**Theme:** Imbalanced Classification (The "Needle in a Haystack")

* **Model 1: The "Hypervelocity" Hunter (Binary Classification)**
    * **The Goal:** Predict if a star is a "High Velocity" outlier.
    * **The Label:** Create a binary column `is_fast`. Set to `1` if total motion > 99th percentile, else `0`.
    * **The Problem:** This creates a **99:1 Class Imbalance**.
    * **The Features:** `ra`, `dec` (Location), `parallax` (Distance).
    * **The Algorithm:** **Logistic Regression** (with weight balancing).
    * [cite_start]**Coursework Checklist:** This specifically hits the **"Class Imbalance"** requirement in the marking scheme[cite: 94]. You must show how you handled the imbalance (e.g., oversampling or `setWeightCol`).

* **Model 2: The "Galactic Cluster" Detector (Spatial Clustering)**
    * **The Goal:** Find physical clusters of stars in 3D space.
    * **The Features:** `ra`, `dec`, `parallax`.
    * **The Algorithm:** **Bisecting K-Means** or **Gaussian Mixture Model (GMM)**.
    * **Coursework Checklist:** Different from Jasmi's clustering because this is *spatial* (3D position), not *spectral* (light properties).

