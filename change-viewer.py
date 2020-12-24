import os
import shutil

base_path = os.getcwd()

opening_dir = base_path + '/opening'
changed_dir = base_path + '/changed_opening'
reading_dir = base_path + '/reading'

opening_list = os.listdir(opening_dir)
changed_list = os.listdir(changed_dir)
reading_list = os.listdir(reading_dir)

rm_dir_path = changed_dir 
rm_dir_list = os.listdir(changed_dir)


def removeDirs(index_path, list_path):
    for dir in range(4):

      if dir == 2:
         os.remove(index_path + '/' + list_path[dir])
      else: 
         shutil.rmtree(index_path + '/' + list_path[dir])


def removeReadingDirs(index_path, list_path):
    for dir in range(6):

      if dir == 1:
          continue
      elif dir == 3:
         os.remove(index_path + '/' + list_path[dir])
      elif dir == 4:
          continue
      else:  
         shutil.rmtree(index_path + '/' + list_path[dir])


def copyDirs(index_path, list_path):
    for dir in range(4):

      if dir == 2:
         shutil.copy(opening_dir + '/' + opening_list[dir], index_path + '/' + list_path[dir])
      else: 
         shutil.copytree(opening_dir + '/' + opening_list[dir], index_path +'/'+ opening_list[dir])


def copyReadingDirs(index_path, list_path):
    for dir in range(6):
      if dir == 1:
          continue
      elif dir == 3:
         shutil.copy(reading_dir + '/' + reading_list[dir], index_path + '/' + list_path[dir])
      elif dir == 4:
          continue
      else: 
         shutil.copytree(reading_dir + '/' + reading_list[dir], index_path +'/'+ reading_list[dir])


def checkDirLastName(list):
   if len(list) == 0:
       print('작업 폴더 안에 교체가 필요한 폴더를 넣어주세요')
   else:
        for idx, val in enumerate(changed_list):
            # print(val)
            if '_01' in val:
                rm_dir_path = changed_dir + '/' + changed_list[idx]
                rm_dir_list = os.listdir(changed_dir + '/' + changed_list[idx])
                removeDirs(rm_dir_path, rm_dir_list)
                copyDirs(rm_dir_path, rm_dir_list)
                print( val + ' 책 열기 교체 완료')
            else:
                rm_dir_path = changed_dir + '/' + changed_list[idx]
                rm_dir_list = os.listdir(changed_dir + '/' + changed_list[idx])
                removeReadingDirs(rm_dir_path, rm_dir_list)
                copyReadingDirs(rm_dir_path, rm_dir_list)
                print( val + ' 책 읽기 교체 완료')


checkDirLastName(changed_list)
print('모두 완료')







