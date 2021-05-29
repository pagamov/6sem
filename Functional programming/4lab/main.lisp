(defun whitespace-char-p2 (char)
  (member char '(#\Space #\Tab #\Newline)))

(defun word-list (string)
  (loop with len = (length string)
        for left = 0 then (1+ right)
        for right = (or (position-if #'whitespace-char-p2 string
                                     :start left)
                        len)
        unless (= right left)
          collect (subseq string left right)
        while (< right len)))

(defun count-words(txt)
  (let ((found 0))
    (dolist (sentence txt)
      (dolist (word (word-list sentence))
        (setf found (+ found 1))
        )
      )
    found)
  )

(count-words '("Встаёт рассвет во мгле холодной." "На нивах шум работ умолк."))
