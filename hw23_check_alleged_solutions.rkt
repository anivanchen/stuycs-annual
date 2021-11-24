;  Ivan Chen <ichen42@stuy.edu>
;  hw23
;  worked with no one
;  advised by no one

; constants
(define solutionTextOne "\nWhen plugged back into the equation: ")
(define solutionTextTwo "\nOne solution of x is approximately ")
(define solutionTextThree "\nThe other solution of x is approximately ")
(define aboutZero " ≈ 0")
(define correct "\n\nThe returned values of x are accepted. ")

; equation 1:
;   -0.618x^2 + 1.618x + 1.732 = 0

(define a -0.618)
(define b 1.618)
(define c 1.732)

(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

; define solutions
(display "Equation 1\n")

(define x (/(+ (- b) discriminant_sqrt) 2 a))             ; define x as a solution of the quadratic
(define check (+ (* a (expt x 2)) (* b x) c))             ; define check as the quadratic equation solved
(display solutionTextTwo) (display x)
(display solutionTextOne) (display check) (display aboutZero)

(display "\n")

(define x (/(- (- b) discriminant_sqrt) 2 a))             ; define x as a solution of the quadratic
(define check (+ (* a (expt x 2)) (* b x) c))             ; define check as the quadratic equation solved
(display solutionTextThree) (display x)
(display solutionTextOne) (display check) (display aboutZero) (display correct)

;############################################################################################################
(display "\n\n########################################################################")

; equation 2:
;   2.71828x^2 + 7.64x + 1.616 = 0

(define a 2.71828)
(define b 7.64)
(define c 1.616)

(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

; define solutions
(display "\n\nEquation 2\n")

(define x (/(+ (- b) discriminant_sqrt) 2 a))             ; define x as a solution of the quadratic
(define check (+ (* a (expt x 2)) (* b x) c))             ; define check as the quadratic equation solved
(display solutionTextTwo) (display x)
(display solutionTextOne) (display check) (display aboutZero)

(display "\n")

(define x (/(- (- b) discriminant_sqrt) 2 a))             ; define x as a solution of the quadratic
(define check (+ (* a (expt x 2)) (* b x) c))             ; define check as the quadratic equation solved
(display solutionTextThree) (display x)
(display solutionTextOne) (display check) (display aboutZero) (display correct)