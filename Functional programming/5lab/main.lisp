(defclass line ()
 ((start :initarg :start :accessor line-start)
  (end   :initarg :end   :accessor line-end)))

(defmethod print-object ((lin line) stream)
  (format stream "[LINE ~s ~s]"
          (line-start lin) (line-end lin)))

(defclass cart ()
 ((x :initarg :x :reader cart-x)
  (y :initarg :y :reader cart-y)))

(defmethod print-object ((c cart) stream)
  (format stream "[CART x ~d y ~d]"
          (cart-x c) (cart-y c)))

(defclass polar ()
 ((radius :initarg :radius :accessor radius)
  (angle  :initarg :angle  :accessor angle)))

(defmethod cart-x ((p polar))
  (* (radius p) (cos (angle p))))

(defmethod cart-y ((p polar))
  (* (radius p) (sin (angle p))))

(setq lin (make-instance 'line
           :start (make-instance 'cart :x 2 :y 1)
           :end (make-instance 'cart :x 2 :y 5)))

(defgeneric containing-rect (shape)
    )

(defmethod containing-rect ((l line))
    (let ((x1 (cart-x (line-start l)))
          (y1 (cart-y (line-start l)))
          (x2 (cart-x (line-end l)))
          (y2 (cart-y (line-end l))))
        (cond ((= x1 x2)
                (list (make-instance 'cart :x (1- x1) :y y1)
                      (make-instance 'cart :x (1+ x1) :y y1)
                      (make-instance 'cart :x (1- x2) :y y2)
                      (make-instance 'cart :x (1+ x2) :y y2))
                    )
              ((= y1 y2)
                (list (make-instance 'cart :x x1 :y (1- y1))
                      (make-instance 'cart :x x1 :y (1+ y1))
                      (make-instance 'cart :x x2 :y (1- y2))
                      (make-instance 'cart :x x2 :y (1+ y2))))
              (t
                (list (make-instance 'cart :x x1 :y y1)
                      (make-instance 'cart :x x1 :y y2)
                      (make-instance 'cart :x x2 :y y2)
                      (make-instance 'cart :x x2 :y y1))))))

(print (containing-rect (make-instance 'line
           :start (make-instance 'cart :x 0 :y 1)
           :end (make-instance 'polar :radius 5 :angle (/ pi 4)))))
