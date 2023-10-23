"""
Prompt:
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that files media type if the files 
name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the files name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

"""

# Prompt user for input  --- strip + lower for easier match case comparison
file = input("File name: ").strip().lower()

# Seperate extension from file name --- rpartition will ensure that ext[2] will always be the portion of the file name after the FURTHEST RIGHT "."
ext = file.rpartition(".")

# Output media type dependant on suffix
match ext[2]:
    case "gif" | "jpg" | "jpeg" | "png":
        print(f"image/{ext[2]}")
    case "pdf" | "zip":
        print(f"application/{ext[2]}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")

"""
Alternative Solution 1) We could type out almost all of the use cases seperately. 

file = input("File name: ").strip().lower()
ext = file.rpartition(".")
match ext[2]:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


Alternative Solution 2) We could use if and elif statements along with .endswith to compare 

x = (input("File name: ")).lower().strip()
if x.endswith((".jpg", ".jpeg")):
    print("image/jpeg" )
elif x.endswith(".gif"):
    print ("image/gif")
elif x.endswith("png"):
    print ("image/png")
elif x.endswith(".pdf"):
    print ("application/pdf")
elif x.endswith(".zip"):
    print ("application/zip")
elif x.endswith(".txt"):
    print ("text/plain")
else:
    print("application/octet-stream")

"""