import PyPDF2
a=input("Enter adress:")
pdfFileObject = open(r"{}".format(a),'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
print(" No. Of Pages :", pdfReader.numPages)
pageObject = pdfReader.getPage(0)
print(pageObject.extractText())
b=pageObject.extractText()
with open('sample.txt', 'w') as f:
    f.write('{}\n'.format(b))
f = open("sample.txt", "r")
Lines = f.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "{}".format(line.strip())
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 
    f=open('sample.txt', 'a+')
    f.write('{}\n'.format(j))

pdfFileObject.close()


