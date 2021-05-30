(defclass circle ()
 ((center :initarg :center :reader center)
  (radius :initarg :radius :reader radius)))

(defgeneric containing-rect (shape))
(defmethod containing-rect ((c circle))
    (let ((x (cart-x (center c)))
          (y (cart-y (center c)))
          (r (radius c)))
        (list (make-instance 'cart :x (- x r) :y (+ y r))
              (make-instance 'cart :x (+ x r) :y (+ y r))
              (make-instance 'cart :x (+ x r) :y (- y r))
              (make-instance 'cart :x (- x r) :y (- y r)))))

(defclass polar ()
 ((radius :initarg :radius :accessor radius)
  (angle  :initarg :angle  :accessor angle)))

(defclass cart ()
 ((x :initarg :x :reader cart-x)
  (y :initarg :y :reader cart-y)))

(defmethod cart-x ((p polar))
  (* (radius p) (cos (angle p))))

(defmethod cart-y ((p polar))
  (* (radius p) (sin (angle p))))

(defmethod print-object ((c cart) stream)
  (format stream "[CART x ~d y ~d]"
          (cart-x c) (cart-y c)))




(print (containing-rect (make-instance 'circle
           :center (make-instance 'cart :x 4 :y 3)
           :radius 5)))

(print (containing-rect (make-instance 'circle
           :center (make-instance 'polar :radius 5 :angle (/ pi 4))
           :radius 5)))
