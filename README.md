# Student Academic Report Generator

This project is a Python-based tool that reads student academic data from a CSV file, analyzes performance metrics such as GPA, and generates a structured PDF report using the FPDF library. The report includes summary statistics and a tabular overview of each student's performance.

---

## 📌 Project Overview

This tool automates the generation of academic performance reports from student data. It is ideal for educators, school administrators, and data analysts who need quick, clean, and readable reports without manual formatting.

---

## 🔍 Features

- ✅ Reads structured data from a CSV file
- 📈 Analyzes key academic performance metrics:
    - Average GPA
    - Median GPA
    - Highest and Lowest GPA
    - Total Number of Students
- 🧾 Displays individual student details in a clean table format
- 📄 Exports a well-structured PDF report using FPDF
- 💡 Simple and customizable for school or college data use cases

---

## 📂 Dataset Information

- **Dataset Name:** student-performance-data  
- **Author:** Muhammad Azam  
- **Source:** Kaggle  
- **Description:** Analytical dataset exploring academic performance factors among students.

**Key fields used:**
- `StudentID`
- `GPA` (Grade Point Average)
- `GradeClass` (e.g., A, B, C, D, etc.)

---

## 🛠 How It Works

1. **Load the Data**  
     Reads from a CSV file (`data.csv`) using Python's `csv` module, extracting each student's ID, GPA, and grade classification.

2. **Analyze Data**  
     Uses Python's `statistics` module to compute:
     - Mean GPA
     - Median GPA
     - Minimum and Maximum GPA
     - Total number of students

3. **Generate PDF**  
     Uses the `fpdf` library to create a PDF report with:
     - Title and header
     - Summary statistics
     - Tabular list of student records

---

## 📦 Requirements

Install the required Python library:

```bash
pip install fpdf
```

---

## 🚀 How to Use

1. Download the `data.csv` file (ensure it matches the required column structure).
2. Place it in the same directory as the Python script.
3. Run the script:

     ```bash
     python index.py
     ```

4. The PDF report (`student_gpa_report.pdf`) will be generated in the current folder.

---

## 📁 File Structure

```
├── index.py                # Main script
├── data.csv                # Input dataset file
├── student_gpa_report.pdf  # Output PDF (generated)
├── README.md               # Project documentation
```

## 🙏 Acknowledgments

- Dataset by Muhammad Azam on Kaggle
- Thanks to the open-source community for tools like FPDF that simplify report generation