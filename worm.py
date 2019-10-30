import os;
import sys;
import random;
import re;
from colorama import Fore;

print(Fore.YELLOW+"""\nCaution!! You Are About To Change The File And The Folders.
Do This For The Practical Purpose only On A Testing Folders Only!!\n""");  

inp=input(Fore.BLUE+"Enter The Folder You Want To Corrupt: ");
if(os.path.isdir(inp)):
	try:
		os.chdir(inp);
		rex=re.compile('.*\.(txt|php)');
		reg=re.compile('.*?(\.\w+)$');
		ar=[];
		ro=[]
		res=os.walk(inp);
		for root, dirs, files in res:
			if not files:
				continue;
			else:
				for x in files:
					ar.append(os.path.join(root,x));
					ro.append(root);

		for x in range(len(ar)):
			if not ar[x]:
				continue;
			else:
				rand=str(random.randint(0,10000));
				if(reg.match(ar[x])):
					sp=ar[x].split('.');
					sp2=sp[len(sp)-1];
					with open(ar[x],'w') as fx:
						fx.write('oopss!! this file is no longer avilable');
					os.rename(ar[x],ro[x]+'/'+'7h15 15 4 C0rRu97 f1L3'+rand+'.'+sp2);
				else:
					os.rename(ar[x],ro[x]+'/'+'7h15 15 4 C0rRu97 f1L3'+rand+'.txt')
					with open(ro[x]+'/'+'7h15 15 4 C0rRu97 f1L3'+rand+'.txt','w') as fx:
						fx.write('oopss!! this file is no longer avilable');
		print(Fore.GREEN+"\nAll Gone!!\n")
	except Exception as e:
			print(e);
else:
	print(Fore.RED+"\n\"{0}\" is not a dir".format(inp));
