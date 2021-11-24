#|  Ivan Chen <ichen42@stuy.edu>
    hw34
    worked with no one
    advised by no one
|#

; symbols for coefficients of the first equation,
;   -0.618x^2 + 1.618x + 1.732 = 0
(define a -0.618)
(define b 1.618 )
(define c 1.732 )

(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

(define aSolution
  (lambda (a b sign)
    (/
          (sign (- b)
             discriminant_sqrt
             )
          2 a  ; n-ary division! numerator/ (2*a) = numerator/2/a
          )
   )
 )

; display solutions
(display "One solution is approximately ")
(display (aSolution a b +))
(display "\n")  

(display "The other solution is approximately ")
(display (aSolution a b -))
(display "\n\n")

(display "For the second equation\n")
;   2.71828x^2 + 7.64x + 1.616 = 0

; task 2a: bind new values to the symbols
(define a 2.71828)
(define b 7.64   )
(define c 1.616  )
(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

; copy the solution-displaying code
(display "One solution is approximately ")
(display (aSolution a b +))
(display "\n")  

(display "The other solution is approximately ")
(display (aSolution a b -))
