;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname familiar) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
(define encrypted-flag (list 115 116 117 121 99 116 102 123 114 97 98 99 107 108 101 102 116 95 105 36 95 112 114 51 116 116 121 95 107 108 101 102 119 108 125))

(define (setup-check-number-is-prime n)
  (if (> n 2)
      (append (setup-check-number-is-prime (- n 1)) (list (- n 1)))
      (list)))

(define (check-number-is-prime n setup-num-list)
  (if (= (length setup-num-list) 0)
      #t
      (if (= (remainder n (car setup-num-list)) 0)
          #f
          (check-number-is-prime n (cdr setup-num-list)))))

(define (check-numbers-are-prime num-list-to-check)
  (if (= (length num-list-to-check) 0)
      (list)
      (cons (check-number-is-prime (car num-list-to-check) (setup-check-number-is-prime (car num-list-to-check))) (check-numbers-are-prime (cdr num-list-to-check)))))

(define (convert-string-to-numbers string-to-convert)
  (if (= (string-length string-to-convert) 0)
      (list)
      (cons (char->integer (car (string->list string-to-convert))) (convert-string-to-numbers (list->string (cdr (string->list string-to-convert)))))))

(define (encrypt-flag flag)
  (if (= (string-length flag) 0)
      (list)
      (if (equal? (car (check-numbers-are-prime(convert-string-to-numbers flag))) #t)
          (append (cons (car (convert-string-to-numbers flag)) (list (+ (car (convert-string-to-numbers flag)) 1))) (encrypt-flag (substring flag 1)))
          (append (list (car (convert-string-to-numbers flag))) (encrypt-flag (substring flag 1))))))

(define (decrypt-flag cipher)
  (if (= (length cipher) 0)
      (list)
      (if (equal? (car (check-numbers-are-prime cipher)) #t)
          (append (list (integer->char (car cipher))) (decrypt-flag (cdr (cdr cipher))))
          (append (list (integer->char (car cipher))) (decrypt-flag (cdr cipher))))))

(list->string (decrypt-flag encrypted-flag)) ;This decryption algorithm SHOULD work... but it doesn't :(