(defun whitespace-char-p2 (char)
  (member char '(#\Space #\Tab #\Newline)))

; (defun word-list (string)
;   (loop with len = (length string)
;         for left = 0 then (1+ right)
;         for right = (or (position-if #'whitespace-char-p2 string
;                                      :start left)
;                         len)
;         unless (= right left)
;           collect (subseq string left right)
;         while (< right len)))

(defun find-non-trivial (string)
  ; (loop for c across string do (princ c))
  ; '(> 1 0)

  (loop with len = (length string)
        for left = 0 then (1+ right)
        for right = (or (position-if #'whitespace-char-p2 string
                                     :start left)
                        len)
        unless (= right left)
          collect (subseq string left right)
        while (< right len))
)

(defun count-words(txt)
  (let ((found 0))
    (dolist (sentence txt)
      (dolist (word (find-non-trivial sentence))
        ; (print word)
        (setf found (+ found 1))
      )
    )
    (> found 0)
  )
)

(defun rus (char)
  ; (print char)
  (>= (position char "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя") 0)
)

; (print (rus "a"))
(rus "a")


; (print (count-words '("Встаёт рассвет во мгле холодной." "На нивах шум работ умолк.")))
