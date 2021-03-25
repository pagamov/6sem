#!/usr/local/bin/sbcl --script
(defun sub-f (x y z)
    (cond
        ((> x 11) (sub-f 0 y z))
        ((> y 59) (sub-f (+ x 1) 0 z))
        ((and (= x (/ y 5)) (= 0 (rem y 5))) z)
        (t (sub-f x (+ y 1) (+ z 1)))))

(defun parallel-hands-minutes (x y) 
    (if (= (rem (+ y 1) 60) 0) 
        (sub-f (+ x 1) (+ y 1) 1) 
        (sub-f x (+ y 1) 1)))

(print (parallel-hands-minutes 0 0))
(print (parallel-hands-minutes 0 15))
