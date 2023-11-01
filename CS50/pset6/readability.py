def main():
    text = input("Text: ").lower()
    characters = 0
    for i in text:
        if i.isalpha():
            characters += 1
    words = text.count(" ") + 1
    sentences = text.count(".") + text.count("?") + text.count("!")
    grade = 0.0588 * (characters / words * 100) - 0.296 * (sentences / words * 100) - 15.8
    if grade < 1:
        print("Before grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade", round(grade))

if __name__ == "__main__":
    main()