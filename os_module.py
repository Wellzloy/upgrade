import  os

print('Текущаяя директория: ', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущаяя директория: ', os.getcwd())
# os.makedirs(r'third\fourth')
print(os.listdir())
# for i in os.walk('.'):
#     print(i)
os.chdir(r'D:\Доки\Програмирование\Python\lessons\upgrade\pythonProject')
print('Текущаяя директория: ', os.getcwd())
# print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)
# os.startfile(file[1])
print(os.stat(file[1]).st_size)