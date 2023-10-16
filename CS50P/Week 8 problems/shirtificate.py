import fpdf
from fpdf import FPDF



def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 44)
    pdf.cell(text="CS50 Shirtificate", align="C", center=True, h=50)
    pdf.image("shirtificate.png", x = "C", y = 55)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255,255,255)
    pdf.cell(text="Artem Davydov took CS50P", align="C", center=True, h=250)
    pdf.output("shirtificate.pdf")






if __name__ == "__main__":
    main()