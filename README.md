JobScout: Graduate & Entry-Level Job Tracker

JobScout is a complete, lightweight application designed to help recent graduates find their next role. It scrapes entry-level and graduate-trainee job listings from Jobberman, stores them, and presents them in a clean, modern, filterable web interface.

**The Goal:** To make the job search process less overwhelming by aggregating relevant opportunities into one easily searchable and browsable dashboard.

✨ Key Features

-   **Automated Data Pipeline:** A Python script scrapes fresh job listings from Jobberman, storing them in a local database.
-   **JSON Export:** An included utility (`export_jobs.py`) exports the database contents to a `jobs.json` file, making the data accessible to the web frontend.
-   **Modern, Responsive UI:** A single-page application built with HTML, CSS, and JavaScript offers a user-friendly experience on both desktop and mobile devices.
-   **Real-time Search & Filter:**
    -   **Keyword Search:** Instantly filter jobs by title or company.
    -   **Location Filter:** Narrow down roles by city or region.
    -   **Type Filter:** Toggle between job types (e.g., Full Time, Internship, Contract).
-   **Detailed Job Modal:** Click on any job card to see a detailed view with full requirements, salary information, and a direct link to apply on Jobberman.
-   **Data Integrity:** The scraper and import process use `UNIQUE` constraints to prevent duplicate listings from being added to the database.

🛠️ Technology Stack

-   **Data Scraping:** Python with `BeautifulSoup` and `Requests`
-   **Data Storage:** `SQLite3`
-   **Backend Scripting:** Python
-   **Frontend:** HTML, CSS, JavaScript
-   **Dependencies:** `pandas` (primarily used in the Jupyter Notebook for data exploration)


 💾 Project Structure

-   `Intern_ship.ipynb`: The Jupyter Notebook containing the original scraping, data exploration, and database population code.
-   `export_jobs.py`: A standalone script to manually refresh the `jobs.json` file from the `scout.db` database.
-   `jobs.json`: The static data file read by the frontend.
-   `index.html`: The complete UI application.
-   `scout.db`: The local SQLite database (created after running the scraping process).


🚀 Getting Started

1.  **Clone the repository.**

2.  Set up a Python environment- and install the required packages (BeautifulSoup, Requests, Pandas).

3.  Run the Scraper: Open and run the cells in `Intern_ship.ipynb` to scrape new data and populate `scout.db`. You can also run the export script directly:
    python export_jobs.py

4.  Launch the UI: As the frontend requires `fetch` to load `jobs.json`, you need to serve the file via a local web server. For example, using Python:
    python -m http.server
    Then, open `http://localhost:8000` in your browser.

📖 How to Use

1.  **Search:** Use the main search bar to find roles by title or company.
2.  **Filter:**
    -   Use the "All locations" dropdown to view jobs in specific cities.
    -   Click the filter chips (e.g., "Full Time", "Internship") to see only those job types.
3.  **Explore:** Click any job card to open a detailed modal window.
4.  **Apply:** Click the "View and apply on Jobberman" button to be taken directly to the original listing.

🤝 Contributing

Contributions, suggestions, and feedback are welcome! Feel free to open an issue or submit a pull request to help improve the project.




#### 📜 License

This project is open source and available under the [MIT License](LICENSE).
