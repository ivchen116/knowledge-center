# -*- coding: UTF-8 –*-

import os
import subprocess

def image_to_string(img, cleanup=False, plus=''):
	'''install 'tesseract' first, see https://github.com/UB-Mannheim/tesseract/wiki ''' 
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' --psm 7 ' + plus, shell=True)
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text
	
if __name__ == "__main__":
	print 'image_to_string'