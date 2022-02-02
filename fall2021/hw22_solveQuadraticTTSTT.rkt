; Ivan Chen <ichen42@stuy.edu>
; hw22
; worked with no one
; advised by no one

;----------------------------------------------------------

; symbols
(define a -0.618)
(define b 1.618)
(define c 1.732)
(define negativeB (- b))
(define discriminant_sqrt (sqrt (- (expt b 2) (* 4 a c)) ))
(define divisor (* 2 a))

; task01

; the quadratic equation of interest:
;   -0.618x^2 + 1.618x + 1.732 = 0

(display "One solution is approximately ")
(display (/ (+ negativeB discriminant_sqrt) divisor))
(display "\n\n")

(display "The other solution is approximately ")
(display (/ (- negativeB discriminant_sqrt) divisor))
(display "\n\n")

;----------------------------------------------------------

; task02

; the quadratic equation of interest:
;    2.71828x^2 + 7.64x + 1.616 = 0

(define a 2.71828)
(define b 7.64)
(define c 1.616)
(define negativeB (- b))
(define discriminant_sqrt (sqrt (- (expt b 2) (* 4 a c)) ))
(define divisor (* 2 a))

(display "One solution is approximately ")
(display (/ (+ negativeB discriminant_sqrt) divisor))
(display "\n\n")

(display "The other solution is approximately ")
(display (/ (- negativeB discriminant_sqrt) divisor))