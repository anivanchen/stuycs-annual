#|
  Ivan Chen <ichen42@stuy.edu>
  homework50
  worked with no one
  advised by no one
|#

; if multiplier if positive

(define positiveMultiplier
  (lambda (x y)
    (+ x (multiply x (- y 1)))
    )
  )

; if multiplier is negative

(define negativeMultiplier
  (lambda (x y)
    (- (positiveMultiplier x (abs y)))
    )
  )

; Calculate the product of two numbers using repeated addition.

(define multiply
  (lambda (multiplicand multiplier)
    (if (or (= multiplier 0) (= multiplicand 0))
        0
        (if (>= multiplier 0)
            (positiveMultiplier multiplicand multiplier)
            (negativeMultiplier multiplicand multiplier)
            )
        )
    )
  )

; ========= TEST ==========
(define tests
  (lambda (x y)
    ; x corresponds to the multiplicand, y corresponds to the multiplier
    ; tests x*y, -x*y, x(-y), and (-x)(-y)
    (display (multiply x y))
    (display "\n")
    (display (multiply (- x) y))
    (display "\n")
    (display (multiply x (- y)))
    (display "\n")
    (display (multiply (- x) (- y)))
    (display "\n\n")
    )
  )

(tests 2 0) ; 0
(tests 2 1) ; 2, -2
(tests 2 2) ; 4, -4
(tests 2 3) ; 6, -6