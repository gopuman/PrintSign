from pathlib import Path

msg = input("Enter the message to be printed: \n")
if not msg:
    #Default message is Happy Birthday!
    msg = "Happy Birthday!"
s = "{}".format(msg).upper().strip()
s = s.replace(" ","")

fs = input("Enter Font size: \n")
if not fs:
    #Default font size is 800px
    fs = "800"

color = input("Specify the color or hex value for the letters: \n")
if not color:
    #Default color is black
    color = "black"

for i in s:
    path_to_file = "{}.html".format(i)
    path = Path(path_to_file)
    if path.is_file():
        continue
    file_handle = open(path_to_file, "w")
    html = "<style>@media print {  body { -webkit-print-color-adjust: exact; }}</style><div class=\"my-box\"><center><h1 style=\"color:"+color+";font-size:"+fs+"px;font-style:bold;padding-top:0px;\">"+i+"</h1><center></div>"
    file_handle.write(html)
    file_handle.close()