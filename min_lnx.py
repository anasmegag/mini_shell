#this project is created by Anas Megag
#it consists at creating a simple linux shell using python
#the shell will be able to execute basic commands like ls, cd, pwd, cdt ....
import os

def check_command(command):
    res = command.split(' ')
    if res[0] not in ['ls', 'cd', 'pwd' , 'mkdir', 'cat','head','tail','rm','echo','mv','rmdir']:
        return False
    return True
def excute_commande(command):
    if not check_command(command):
        return 'command not found'
    res = command.split(' ')
    fl = False
    s=''
    if '>' in res:
       fl= True
    if res[0]=='echo':
        for i in range(1,len(res)):
            if res[i]=='>':
                break
            s+=res[i]+' '  
    if res[0]=='pwd':
        s=os.getcwd()
    if res[0]=='mkdir':
        os.mkdir(res[1])
        s= res[1]+' created successfully'
    if res[0]=='ls':
        s= '\n'.join(os.listdir())  
    if res[0]=='rm':
        if res[1] not in  os.listdir():
            return 'file not found'
        os.remove(res[1])
        s= res[1]+' removed successfully'
    if res[0]=='cd':
        os.chdir(res[1])
        s= 'directory changed to '+res[1]
    if res[0]=='mv':
        os.rename(res[1],res[2])
        s= res[1]+' renamed to '+res[2]
    if res[0]=='rmdir':
        if res[1] not in os.listdir():
            return 'directory not found'
        os.rmdir(res[1])
        s= res[1]+' removed successfully'
    if res[0]=='cat':
        if res[1] not in os.listdir():
            return 'file not found'
        with open(res[1],'r') as f:
            l=f.readlines()
            s=''.join(l)
    if res[0]=='head':
        if res [1] not in os.listdir():
            return 'file not found'
        with open(res[1],'r') as f:
            l = f.readlines()
            if res[2]=='-n':
                s=''.join(l[:int(res[3])])
            else:
                s=''.join(l[:10])
    if res[0]=='tail':
        if res [1] not in os.listdir():
            return 'file not found'
        with open(res[1],'r') as f:
            l = f.readlines()
            if res[2]=='-n':
                s=''.join(l[-int(res[3]):])
            else:
                s=''.join(l[-10:])
    if fl:
        idx = res.index('>')
        with open(res[idx+1],'w') as f:
            f.write(s)
        return 'output redirected to '+res[idx+1]
    return s
def main():
    while True:
        command = input("min_lnx> ")
        if command.strip() == "exit":
            print('exiting...')
            break
        try:
            print(excute_commande(command))
        except Exception:
            print("An error occurred while executing the command.")
main()