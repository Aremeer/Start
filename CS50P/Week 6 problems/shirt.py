import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        exit(1)
    
    extentions = [".png", ".jpg", ".jpeg"]
    if any(extention in sys.argv[1] for extention in extentions) and any(extention in sys.argv[2] for extention in extentions):
        pass
    else:
        print("Invalid input")
        exit(1)
    
    if extentions_check():
        pass
    else: 
        print("Input and output have different extensions")
        exit(1)
    
    try:
        image1 = Image.open(sys.argv[1])
        image2 = Image.open("shirt.png")
    except FileNotFoundError:
        exit(1)
    
    image1 = ImageOps.fit(image1, (600, 600))
    image1.paste(image2, image2)
    image1.save(sys.argv[2])

def extentions_check():
    if ".png" in sys.argv[1] and ".png" in sys.argv[2]:
        return True
    else: pass
    
    if ".jpg" in sys.argv[1] and ".jpg" in sys.argv[2]:
        return True
    else: pass
    
    if ".jpeg" in sys.argv[1] and ".jpeg" in sys.argv[2]:
        return True
    else: exit(1)


if __name__ == "__main__":
    main()