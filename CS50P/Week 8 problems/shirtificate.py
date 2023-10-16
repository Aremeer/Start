from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 44)
    pdf.cell(text="CS50 Shirtificate", align="C", center=True, h=50)
    pdf.image("shirtificate.png", x = "C", y = 55)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255,255,255)
    pdf.cell(text=f"{name}", align="C", center=True, h=230)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()