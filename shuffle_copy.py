import sys
import shutil
import glob
import random

def main(argv):
    print(argv[1], argv[2])
    file_list = []
    count = 0
    for filename in glob.iglob(argv[1] + '/**/*.mp3', recursive=True):
        file_list.append(filename)
        count += 1
    for i in range(int(argv[3])):
        filename = file_list[random.randrange(0,len(file_list))]
        #print(filename)
        #shutil.copy2(filename, argv[2] + 'trak\03d.mp3'.format(i))
        #print('track{:03d}.mp3'.format(i))
        shutil.copy2(filename, argv[2] + '/track{:03d}.mp3'.format(i))

    return 0

if __name__ == '__main__':
    main(sys.argv)
