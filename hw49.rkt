#|
  Ivan Chen <ichen42@stuy.edu>
  homework49
  worked with no one
  assisted by no one
|#

; ########## Fib ##########

; calculates the nth element of the Fibonacci sequence Fn
(define Fib
  (lambda (n)
    (if (= n 0)                ; base case 0
        0
        (if (< n 3)            ; base case 1, 2
            1
            (+                 ; recursive cases
             (Fib (- n 1))
             (Fib (- n 2))
             )
            )
        )
    ))

; ########## TEST ##########

(define test
  (lambda (n expected)
    (display (string-append
              "Calculated Value: "
              (number->string n)
              "\nExpecting: "
              (number->string expected)
              ))
    (if (= n expected)
        (display "\nCorrect\n")
        (display "\nWrong\n")
        )
    ))

(test (Fib 0) 0)
(test (Fib 1) 1)
(test (Fib 2) 1)
(test (Fib 3) 2)
(test (Fib 4) 3)
(test (Fib 5) 5)
(test (Fib 6) 8)
(test (Fib 7) 13)
