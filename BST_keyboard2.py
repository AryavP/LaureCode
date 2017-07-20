#Aryav Pal

import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np
import autocomplete
autocomplete.load()

class Node:
 def __init__(self, val):
  self.left= None
  self.right= None
  self.data= val

class BST:
 def __init__(self, val): self.root = Node(val)

 def insert(self, val): self.insert2(val, self.root)

 def insert2(self, val, n):
  if val == n.data: return
  elif val<n.data:
   if n.left==None: n.left = Node(val)
   else: self.insert2(val, n.left)
  else:
   if n.right==None: n.right = Node(val)
   else: self.insert2(val, n.right)

 def traverse(self, val):
  list = []
  list = self.traverse2(self.root, list)
  return list

 def traverse2(self, n, l=[]):
  if n.left is not None: self.traverse2(n.left, l)
  l.append(n.data)
  if n.right is not None: self.traverse2(n.right, l)
  return l

def traverse(n, focus):
 if n.left is not None: traverse(n.left, focus)
 specialPrint(n.data, focus)
 sys.stdout.flush()
 if n.right is not None: traverse(n.right, focus)
 
def specialPrint(char, focus):
 if char is " ": sys.stdout.write("[space]")
 elif char is "~": sys.stdout.write("[delete]")
 elif char is focus: sys.stdout.write(color.RED + char + color.END + " ")
 else: sys.stdout.write(char + " ")

class color:
 PURPLE = '\033[95m'
 CYAN = '\033[96m'
 DARKCYAN = '\033[36m'
 BLUE = '\033[94m'
 GREEN = '\033[92m'
 YELLOW = '\033[93m'
 RED = '\033[91m'
 BOLD = '\033[1m'
 UNDERLINE = '\033[4m'
 END = '\033[0m'

def eye_tracker(n, bst, expression=[], right_x=[], left_x=[]):
 cap = cv2.VideoCapture(0)

 eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

 while(True):
  ret, img = cap.read()
  width = np.size(img,1)
  height = np.size(img,0)
  img = cv2.flip(img,1)
                    
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
  cv2.line(img,(0,height/2),(width,height/2),(0,0,255),1,8,0)
  cv2.line(img,(width/2,0),(width/2,height),(0,0,255),1,8,0)
                                            
  for(x,y,w,h) in eyes:
   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
   roi_gray=gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]
                                                            
   eyes_x = x+w/2
   eyes_y = y+h/2
   
   if eyes_x > width/2:
    right_x.append(eyes_x)
   else:
    left_x.append(eyes_x)

   comparitor = compare(eyes_y, right_x, left_x)

   if comparitor is not None: print comparitor
   
   if comparitor is "right":
    if n.right!=None: n=n.right
    traverse(n, n.data)
    print "\n"
   elif comparitor is "left":
    if n.left!=None: n=n.left
    traverse(n, n.data)
    print "\n"
   elif comparitor is "selection":
    if n.data is "~": del expression[-1]
    elif n.data is ".": del expression[:]
    else: expression.append(n.data)
    n=bst
    string = n.data
    print ''.join(expression)
   elif comparitor is "middle":
    traverse(n, n.data)
    print "\n"

  cv2.imshow('frame',img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

 cap.release()
 cv2.destroyAllWindows()

def reset(right_x=[], left_x=[]): #code to reset the lists
 del right_x[:]
 del left_x[:]

def compare(height, right_x=[], left_x=[]):
 max_length = 30
 height_cap = 295
 if (len(right_x) >= max_length - 15 & len(left_x) >= max_length-15):
  reset(right_x, left_x)
  if(height<height_cap):
   return "selection"
  else:
   return "middle"
 elif len(right_x) > max_length:
  reset(right_x, left_x)
  return "right"
 elif len(left_x) > max_length:
  reset(right_x, left_x)
  return "left"

if __name__ == "__main__":
 bst = BST('m')
 bst.insert('e');
 bst.insert('u');
 bst.insert('a');
 bst.insert('i');
 bst.insert('q');
 bst.insert('y');
 bst.insert('.');
 bst.insert('c');
 bst.insert('g');
 bst.insert('k');
 bst.insert('o');
 bst.insert('s');
 bst.insert('w');
 bst.insert('|');
 bst.insert(' ');
 bst.insert('?');
 bst.insert('b');
 bst.insert('d');
 bst.insert('f');
 bst.insert('h');
 bst.insert('j');
 bst.insert('l');
 bst.insert('n');
 bst.insert('p');
 bst.insert('r');
 bst.insert('t');
 bst.insert('v');
 bst.insert('x');
 bst.insert('z');
 bst.insert('~');

 right_x=[]
 left_x=[]
 string = []
 print "m"
 eye_tracker(bst.root, bst.root, string, right_x, left_x)
