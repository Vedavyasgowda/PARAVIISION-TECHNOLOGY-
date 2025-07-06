from flowchart_generator import generate_flowchart
from pie_chart_generator import generate_pie_chart

def main():
    paragraph = input("Enter your paragraph:\n")
    
    print("\nChoose chart type:")
    print("1. Flowchart")
    print("2. Pie Chart")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        print("🛠 Generating Flowchart...") 
        generate_flowchart(paragraph)
    elif choice == '2':
        print("🛠 Generating Pie Chart...")
        generate_pie_chart(paragraph)
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

