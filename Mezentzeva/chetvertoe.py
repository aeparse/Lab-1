#Вариант 7
#Задание 4
import  xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize

elements = dom.getElementsByTagName('Valute')
charCode_dict = []

for node in  elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Nominal':
                nominal = child.firstChild.data
            if child.tagName == 'CharCode':
                CharCode = child.firstChild.data
                #print(CharCode)
    if nominal == '10' or nominal== '100':
        charCode_dict.append(CharCode)

print(charCode_dict)

xml_file.close()