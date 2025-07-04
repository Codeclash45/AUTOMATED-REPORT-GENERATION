import csv
from statistics import mean, median
from fpdf import FPDF

# Load data from a CSV file and return a list of student records
def load_data(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            try:
                student_id = row["StudentID"]
                grade = row["GradeClass"]
                gpa = float(row["GPA"])
                data.append({
                    "StudentID": student_id,
                    "GradeClass": grade,
                    "GPA": gpa
                })
            except (ValueError, KeyError):
                continue  # skip rows with missing or bad data
        return data

# Analyze the student data and compute summary statistics
def analyze_data(data):
    gpas = [item["GPA"] for item in data]
    return {
        "Average GPA": mean(gpas),
        "Median GPA": median(gpas),
        "Highest GPA": max(gpas),
        "Lowest GPA": min(gpas),
        "Total Students": len(gpas)
    }

# PDF report class using FPDF
class PDFReport(FPDF):
    # Add a header to each page
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student GPA Report", ln=True, align="C")

    # Add a footer to each page
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    # Add summary statistics to the PDF
    def add_summary(self, summary):
        self.set_font("Arial", "", 12)
        self.ln(10)
        self.cell(0, 10, "Summary Statistics", ln=True)
        for key, value in summary.items():
            self.cell(0, 10, f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}", ln=True)

    # Add a table of student data to the PDF
    def add_table(self, data):
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(40, 10, "StudentID", 1)
        self.cell(40, 10, "GradeClass", 1)
        self.cell(40, 10, "GPA", 1)
        self.ln()
        self.set_font("Arial", "", 12)
        for row in data:
            self.cell(40, 10, str(row["StudentID"]), 1)
            self.cell(40, 10, row["GradeClass"], 1)
            self.cell(40, 10, f'{row["GPA"]:.2f}', 1)
            self.ln()

# Main function to generate the PDF report
def generate_pdf_report(input_file, output_pdf):
    data = load_data(input_file)           # Load student data from CSV
    summary = analyze_data(data)           # Compute summary statistics

    pdf = PDFReport()                      # Create PDF report object
    pdf.add_page()                         # Add a new page
    pdf.add_summary(summary)               # Add summary section
    pdf.add_table(data)                    # Add student data table
    pdf.output(output_pdf)                 # Save PDF to file
    print(f"PDF report saved as {output_pdf}")

# Entry point for script execution
if __name__ == "__main__":
    generate_pdf_report("data.csv", "student_gpa_report.pdf")