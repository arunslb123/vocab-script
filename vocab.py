import webbrowser
# The following lines of code will open the vocab file and store the vocab words in an array.

text_file = open("/Users/arunprakash/Desktop/engvid/vocab.txt", "r")
lines = text_file.read().split(',')
text_file.close()


# code to read the start value

infile = open("/Users/arunprakash/Desktop/engvid/demo.txt", "r+")
content = infile.readline()
print(content)
total = int(content)+10
content1=content.replace(content,str(total))
infile.close()
infile = open("/Users/arunprakash/Desktop/engvid/demo.txt", "w")
infile.write(content1)
infile.close()

# The following lines of code opens 10 vocabulary in a browser

website_name = "https://www.vocabulary.com/dictionary/"
start_range= total-10

for i in range(start_range,start_range+11):
    print (lines[i])
    open_website = website_name+lines[i]
    webbrowser.open(open_website)






