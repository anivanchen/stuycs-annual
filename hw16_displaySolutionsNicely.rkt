; Ivan Chen <ichen42@stuy.edu>
; hw16
; worked with no one
; advised by no one

; task 0

(display "hw14#3a. length of other leg: ")

(
  display
    (sqrt
      (abs
        (- (expt 12 2) (expt 13 2))
      )
    )
)

(display " units\n\n")

(display "hw14#3b. quotient: ")

(
  display
    (/
      (/ 11 22)
      (- (expt 5 2.5) 123)
    )
)

(display "\n\nThat's all, folks!\n\n")

; task 2

(display "One solution is approximately ")

(
  display
    (/
      (+ -1.618
        (sqrt
          (+
            (expt 1.618 2)
            (* -4 -0.618 1.732)
          )
        )
      )
      (* 2 0.618)
    )
)

(display "\n\nThe other solution is approximately ")

(
  display
    (/
      (- -1.618
        (sqrt
          (+
            (expt 1.618 2)
            (* -4 -0.618 1.732)
          )
        )
      )
      (* 2 0.618)
    )
)
