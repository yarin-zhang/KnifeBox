import sys
import pangu

def main(input_text):
    spaced_text = pangu.spacing_text(input_text)
    print(spaced_text)

if __name__ == "__main__":
    input_text = sys.argv[1]
    main(input_text)
