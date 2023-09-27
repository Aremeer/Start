#code that assigns media type based on a file extention
def main():
    #used this to find corret syntax for tring https://www.programiz.com/python-programming/string
    file_name = input("File name: ").strip().lower() 
    if ".jpeg" in file_name:
        print("image/jpeg")
    elif ".jpg" in file_name:
        print("image/jpeg")
    elif ".png" in file_name:
        print("image/png")
    elif ".gif" in file_name:
        print("image/gif")
    elif ".pdf" in file_name:
        print("application/pdf")
    elif ".txt" in file_name:
        print("text/plain")
    elif ".zip" in file_name:
        print("application/zip")
    else:
        print("application/octet-stream")
    
    
 
main()