(defun sub-f (h m acc)
    (cond
        ((= h 12) (sub-f 0 m acc))
        ((= m 60) (sub-f (+ h (/ 1 60)) 0 acc))
        ((and (> h (/ m 5)) (< (+ h (/ 1 60)) (/ (+ m 1) 5))) acc)
        (t (sub-f (+ h (/ 1 60)) (+ m 1) (+ acc 1)))))

(defun parallel-hands-minutes (h m) 
    (if (= (rem (+ m 1) 60) 0) 
        (sub-f (+ h 1) (+ m 1) 1) 
        (sub-f (+ h (/ 1 60)) (+ m 1) 1)))

(print (parallel-hands-minutes 0 0))
(print (parallel-hands-minutes 0 15))
(print (parallel-hands-minutes 10 0))
