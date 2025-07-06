import matplotlib.pyplot as plt
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

# Download required tokenizer
nltk.download('punkt', quiet=True)

# Create sentence tokenizer
punkt_param = PunktParameters()
tokenizer = PunktSentenceTokenizer(punkt_param)

def generate_flowchart(text):
    sentences = tokenizer.tokenize(text)
    steps = [s.strip() for s in sentences if len(s) > 10]

    num_steps = len(steps)
    fig, ax = plt.subplots(figsize=(8, num_steps * 1.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    spacing = 1 / (num_steps + 1)

    for i, step in enumerate(steps):
        y = 1 - (i + 1) * spacing
        ax.text(0.5, y, f"{i + 1}. {step}", ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue"))
        if i < num_steps - 1:
            ax.annotate("",
                        xy=(0.5, y - spacing + 0.02),
                        xytext=(0.5, y - 0.02),
                        arrowprops=dict(arrowstyle="->", lw=1.5))

    plt.title("Flowchart Representation", fontsize=14)
    plt.tight_layout()
    plt.show()

def main():
    paragraph = input("Enter a step-by-step paragraph to generate a flowchart:\n")
    print("🛠 Generating Flowchart...")
    generate_flowchart(paragraph)

if __name__ == "__main__":
    main()
