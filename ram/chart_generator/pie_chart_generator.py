import matplotlib.pyplot as plt
import re

def generate_pie_chart(text):
    items = re.findall(r'(\b\w+\b)\s+(\d+)%', text)
    if not items:
        print("❌ No valid percentages found.")
        return

    labels, sizes = zip(*[(label, int(percent)) for label, percent in items])
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title("Pie Chart Representation")
    plt.show()

def main():
    paragraph = input("Enter a paragraph describing percentages (e.g., Product A 40%, B 30%, ...):\n")
    print("🛠 Generating Pie Chart...")
    generate_pie_chart(paragraph)

if __name__ == "__main__":
    main()
