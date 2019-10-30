import re;
import urllib.request;
while 1:
	try:
		res=input('Search The Meaning Of: ');
		if res=='':
			continue;
		else:
			if res.lower()=='q':
				break;
			else:
				urs=urllib.request.urlopen('https://en.oxforddictionaries.com/definition/'+res).read();
				deco=urs.decode('utf-8');
				sear=re.search('class="ind".*?<',deco);
				rk=deco[sear.start():sear.end()];
				val=re.search('>.*?\.',rk);
				result=rk[val.start()+1:val.end()];
				print("\n"+result);
				break;
	except:
		print('\nOops! did\'t get that.. Try again with a proper word ^,^\n');
