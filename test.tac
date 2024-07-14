TAC:
   list = [1.3, 7.5, 3.1, 9.5, 1.0] 'float'
   t1 = list.length 'int'
   t2 = 2 'int'
   t3 = t1 - 1 'float'
L1:
  if t3 < t2 goto L2
   t4 = list[t3] 'float'
   list[t3 + 1] = t4 'float'
  goto L1
L2:
   list[t2] = 500 'int'
   t5 = list.length 'int'
   t6 = t5 + 1 'float'
   list.length = t6 'int'
