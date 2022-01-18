import re
x = '.stitched {\
   padding: 20px;\
   margin: 10px; \
   background: #ff0030; \
   color: #fff; \
   font-size: 21px; \
   font-weight: bold; \
   line-height: 1.3em; \
   border: 2px dashed #fff; \
   border-radius: 10px; \
   box-shadow: 0 0 0 4px #ff0030, 2px 1px 6px 4px rgba(10, 10, 0, 0.5); \
   text-shadow: -1px -1px #aa3030; \
   font-weight: normal; \
}'
y = '\
.custom-file-input::-webkit-file-upload-button { \
  visibility: hidden;\
}\
.custom-file-input::before { \
  content: ''Select some files'';\
  display: inline-block;\
  background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);\
  border: 1px solid #999;\
  border-radius: 3px;\
  padding: 5px 8px;\
  outline: none;\
  white-space: nowrap;\
  -webkit-user-select: none;\
  cursor: pointer;\
  text-shadow: 1px 1px #fff;\
  font-weight: 700;\
  font-size: 10pt; \
} \
.custom-file-input:hover::before {\
  border-color: black;\
} \
.custom-file-input:active::before {\
  background: -webkit-linear-gradient(top, #e3e3e3, #f9f9f9);'

lst = re.findall('#+[a-fA-F0-9]+[;,)]',y)
for i in lst:
    print(i.replace(';','').replace(',','').replace(')',''))

