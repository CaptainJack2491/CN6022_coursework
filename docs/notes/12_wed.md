---

## 🧑‍🔬 Member 1: "Stellar Demographics"
*(Focus: Classifying star populations and finding our local neighbors)*

### Query 1.1: The Hertzsprung-Russell (H-R) Diagram Binning
* **Goal:** To create a 2D histogram of the H-R diagram, which is the most fundamental plot in astronomy. It plots a star's temperature (color) against its luminosity (brightness).
* **Columns Needed:** `bp_rp`, `parallax`, `phot_g_mean_mag`
* **SQL Complexity:** This query is complex because it requires:
    1.  **Mathematical Transformation:** You must first calculate **Absolute Magnitude** (true brightness) from **Apparent Magnitude** (what we see) and **Parallax** (distance). The formula is: $M = m - 5 \times \log_{10}(100/p)$. In Spark SQL, this looks like: `phot_g_mean_mag - 5 * LOG10(100 / parallax) AS absolute_magnitude`.
    2.  **2D Binning:** You must use `CASE` statements or the `FLOOR()` function to create discrete bins for both `bp_rp` (e.g., bins of 0.25) and your new `absolute_magnitude` (e.g., bins of 1.0).
    3.  **Aggregation:** A `GROUP BY` on both new bin columns, followed by a `COUNT(*)` to count the stars in each 2D bucket.
* **Visualization:** A **2D Heatmap**. [cite_start]The x-axis is `bp_rp_bin` (color), the y-axis is `absolute_magnitude_bin`, and the color of each cell is the `COUNT(*)`[cite: 85].

### Query 1.2: Local Neighborhood Census
* **Goal:** To analyze the percentage breakdown of star *types* (by temperature) for all stars within 100 parsecs of our Sun.
* **Columns Needed:** `teff_gspphot` (temperature), `parallax`
* **SQL Complexity:** This query's complexity comes from **window functions and conditional aggregation**:
    1.  **Filtering:** You must first `WHERE parallax > 10` (since $Distance = 1/parallax$, this gives stars < 100 parsecs).
    2.  **Binning:** Use a `CASE` statement to create temperature bins: `CASE WHEN teff_gspphot < 3500 THEN 'Cool (M-type)' WHEN teff_gspphot < 5000 THEN 'Warm (K-type)' ... ELSE 'Hot (O/B-type)' END AS star_type`.
    3.  **Window Function:** To get a percentage, you need the total count of local stars. Use `SUM(COUNT(*)) OVER () AS total_local_stars` in combination with your `GROUP BY` to calculate a percentage for each `star_type`.
* [cite_start]**Visualization:** A **Pie Chart** or **Bar Chart** showing the percentage for each `star_type`[cite: 85].

### Query 1.3: High-Velocity Outlier Detection
* **Goal:** To find the top 1% of stars in your dataset with the highest *total proper motion* (speed across the sky), as these could be hypervelocity stars.
* **Columns Needed:** `source_id`, `pmra`, `pmdec`
* [cite_start]**SQL Complexity:** This is a classic **window function** problem, which is definitely complex[cite: 86]:
    1.  **Mathematical Transformation:** Calculate total motion: `SQRT(POW(pmra, 2) + POW(pmdec, 2)) AS total_motion`.
    2.  **Ranking:** Use a window function to rank all stars. `PERCENT_RANK() OVER (ORDER BY total_motion DESC) AS rank`.
    3.  **Subquery:** You must use a subquery. The outer query will be `SELECT source_id, total_motion FROM ( ...inner query with window function... ) WHERE rank <= 0.01`.
* [cite_start]**Visualization:** A **Table** listing the top 20 `source_id`s and their `total_motion`[cite: 85].

---

## 🔭 Member 2: "Galactic Structure"
*(Focus: Mapping the 3D structure of the Milky Way and data quality)*

### Query 2.1: Galactic Plane vs. Halo Motion
* **Goal:** To test the hypothesis that stars in the "disk" of the Milky Way (the flat plane) move differently from stars in the "halo" (the sparse sphere around it).
* **Columns Needed:** `dec` (declination, a proxy for galactic latitude), `pmra`, `pmdec`
* **SQL Complexity:** This query uses **conditional aggregation** and math functions:
    1.  **Mathematical Transformation:** Calculate `total_motion` as `SQRT(POW(pmra, 2) + POW(pmdec, 2))`.
    2.  **Binning:** Create a new column `galactic_region` using a `CASE` statement: `CASE WHEN ABS(dec) < 15 THEN 'Galactic Plane' ELSE 'Galactic Halo' END`.
    3.  **Aggregation:** `GROUP BY galactic_region` and then find the `AVG(total_motion)` and `STDDEV(total_motion)` for each region.
* [cite_start]**Visualization:** A **Bar Chart** with two groups ('Plane' and 'Halo'), showing the average motion for each[cite: 85].

### Query 2.2: Star Density Sky Map
* **Goal:** To create a 2D map of the sky showing where stars are most densely clustered, which will visually reveal the Milky Way's band.
* **Columns Needed:** `ra` (right ascension, like longitude), `dec` (declination, like latitude)
* **SQL Complexity:** This is a 2D spatial binning problem:
    1.  **Binning:** You need to bin both `ra` and `dec`. The easiest way is `FLOOR(ra / 10) AS ra_bin` and `FLOOR(dec / 10) AS dec_bin`. This creates 10x10 degree "patches" on the sky.
    2.  **Aggregation:** A simple `GROUP BY ra_bin, dec_bin` with a `COUNT(*) AS star_density`.
    3.  **Ordering:** `ORDER BY star_density DESC` to find the most crowded regions.
* **Visualization:** A **2D Heatmap**. The x-axis is `ra_bin`, the y-axis is `dec_bin`, and the color is the `star_density`. [cite_start]This will look incredible[cite: 85].

### Query 2.3: Parallax Error vs. Brightness
* **Goal:** To perform a data quality check. Are our distance measurements (`parallax`) less reliable for fainter stars? (The answer should be yes).
* **Columns Needed:** `phot_g_mean_mag` (brightness), `parallax_error` (you must download this column).
* **SQL Complexity:** This is a straightforward (but valid) complex query:
    1.  **Binning:** Use `FLOOR(phot_g_mean_mag) AS brightness_bin` to group stars by their apparent magnitude.
    2.  **Aggregation:** `GROUP BY brightness_bin`.
    3.  **Calculation:** Calculate the `AVG(parallax_error)` and also the `AVG(parallax_error / parallax)` (which is the *relative* error) for each bin.
* **Visualization:** A **Bar Chart** or **Line Plot**. The x-axis is `brightness_bin` (from bright to dim), and the y-axis is the `AVG(parallax_error)`. [cite_start]You should see the error go up as the stars get dimmer[cite: 85].

---

## ✨ Member 3: "Exotic Star Hunting"
*(Focus: Finding rare and interesting stellar objects)*

### Query 3.1: White Dwarf Candidates
* **Goal:** To find White Dwarfs, which are the hot, dense cores of dead stars. They are **very hot** but **very dim**.
* **Columns Needed:** `teff_gspphot` (temperature), `parallax`, `phot_g_mean_mag`
* **SQL Complexity:** This query is complex because it filters on a derived value (absolute magnitude):
    1.  **Subquery or CTE:** First, create a temporary table/view (using `WITH` or a subquery) that calculates `absolute_magnitude` for all stars (see Query 1.1).
    2.  **Complex Filtering:** Select from this temporary table `WHERE teff_gspphot > 10000` (hotter than 10,000 K) AND `absolute_magnitude > 10` (dimmer than 10).
* **Visualization:** The *result* of this query is a list of candidates. [cite_start]To visualize it, you would create a **Scatter Plot** of `teff_gspphot` vs. `absolute_magnitude` for *just these candidates* to show they form a separate group[cite: 85].

### Query 3.2: Red Giant Candidates
* **Goal:** To find Red Giants, which are old, dying stars. They are **very cool** but **very bright**.
* **Columns Needed:** `teff_gspphot`, `parallax`, `phot_g_mean_mag`
* **SQL Complexity:** This is identical in structure to Query 3.1, but with inverted filters. This shows you understand *how* to apply domain knowledge.
    1.  **Subquery or CTE:** Same as 3.1, create a view with `absolute_magnitude`.
    2.  **Complex Filtering:** Select from this temporary table `WHERE teff_gspphot < 4500` (cooler than 4,500 K) AND `absolute_magnitude < 1` (brighter than 1).
* **Visualization:** A **Scatter Plot** of `teff_gspphot` vs. `absolute_magnitude` for these candidates. [cite_start]They will form the "giant branch" at the top right of the H-R diagram[cite: 85].

### Query 3.3: Co-Moving Pair Search (Binary Candidates)
* **Goal:** To find pairs of stars that are "traveling together" through space—they have similar distances and similar proper motions. This implies they are a binary star system.
* **Columns Needed:** `source_id`, `ra`, `dec`, `parallax`, `pmra`, `pmdec`
* **SQL Complexity:** This is the most complex query of all, as it requires a **self-join**:
    1.  **Self-Join:** `FROM gaia_df A JOIN gaia_df B ON A.source_id < B.source_id` (the `<` prevents joining a star with itself and getting duplicate pairs).
    2.  **Spatial Binning (Join Optimization):** To avoid an $N \times N$ comparison, you *must* first bin the stars by position and join *only on the same bin*: `...ON A.ra_bin = B.ra_bin AND A.dec_bin = B.dec_bin AND A.source_id < B.source_id`.
    3.  **Complex Filtering:** `WHERE ABS(A.parallax - B.parallax) < 1` (similar distance) AND `ABS(A.pmra - B.pmra) < 5` (similar motion) AND `ABS(A.pmdec - B.pmdec) < 5` (similar motion).
* [cite_start]**Visualization:** A **Table** listing the pairs (`A.source_id`, `B.source_id`)[cite: 85].
