;gnu clisp  2.49.60
(defun whitespace-char-p (char)
  (member char '(#\Space #\Tab #\Newline)))

(defun word-list (string)
  (loop with len = (length string)
        for left = 0 then (1+ right)
        for right = (or (position-if #'whitespace-char-p string
                                     :start left)
                        len)
        unless (= right left)	; исключить пустые слова
          collect (subseq string left right)
        while (< right len)))

(defun is-ordinar (char)
    (or (member char (coerce "ABCDEFGHIGKLMNOPQRSTUVWXYZ" 'list))
        (member char (coerce "abcdefghigklmnopqrstuvwxyz" 'list))
        (member char (coerce "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" 'list))
        (member char (coerce "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" 'list))))

(defun if-text-is-ordinary(txt)
    (let ((found 0))
        (dolist (sentence txt)
            (dolist (word (word-list sentence))
                (loop for c across word do
                    (if (not (is-ordinar c))
                        (setf found (+ found 1))))))
        (> found 0)))

(print (if-text-is-ordinary '("русский текст, где есть знаки препинания" "тут тоже есть, ведь так?")))
(print (if-text-is-ordinary '("русский текст без знаков препинания" "тут тоже их нет")))

(print (if-text-is-ordinary '("eng text with punctuation marks." "here another one!")))
(print (if-text-is-ordinary '("eng text without punctuation marks." "тут тоже их нет")))
