import re;
import urllib.request;
import urllib.parse;
while True:
	mov=input('Type a Move Name Here --> ');
	if(len(mov)>0):
		break;
try:
	fuck={'q':mov};
	val=urllib.parse.urlencode(fuck);
	url='https://www.google.com/search?'+val;
	headers={};
	headers['User-Agent']='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36';
	req=urllib.request.Request(url,headers=headers);
	resp=urllib.request.urlopen(req);

except Exception as e:
	print(e);

mat=re.findall(r'Rating.*([0-9]\.[0-9]\/[0-9][0-9])\s',resp.read().decode());
if not mat:
	print('\nSorry can\'t find ratings of '+mov.upper());
else:
	print('\nRatings of "'+mov.title()+'" is '+mat[0]);
