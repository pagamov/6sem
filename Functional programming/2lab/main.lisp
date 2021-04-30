(defun count-real (num l)
    (if (equal l '())
      0
      (if (listp (car l))
        (+ (count-real num (car l)) (count-real num (cdr l)))
        (if (equalp (car l) num)
          (+ 1 (count-real num (cdr l)))
          (count-real num (cdr l))))))

(print (count-real 3.0 '(1 2 3.0))) ; => 1
(print (count-real 3.0 '())) ; => 0
(print (count-real 3.0 '((1) 2 9/3))) ; => 1
(print (count-real 3.0 '(1 2 (3)))) ; => 1
(print (count-real 3.0 '((1 2.2) 3.0 (4 5/6 (3 6)) 7))) ; => 2
