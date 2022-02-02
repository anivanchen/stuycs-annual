#|
  Ivan Chen <ichen42@stuy.edu>
  homework48
  worked with no one
  advised by no one
|#

; ########## SOLUTION ##########

; calculates the number of ways to arrange n students in a linear line
(define nowtasial
  (lambda (nStudents)
    (if (= nStudents 1)
        1
        (* nStudents                     ; number of positions the nth student can be in for each arrangement
           (nowtasial (- nStudents 1))   ; the number of ways to arrance n-1 students in a linear line
           )
        )
    )
  )

; ########## TESTS ##########

(define test
  (lambda (nStudents expectedOutcome)
    (display (string-append "For "
                            (number->string nStudents)
                            " students, there are "
                            (number->string (nowtasial nStudents))
                            " way(s) to arrange them in a linear line.\n"
                            )
             )
    (display (string-append "Expecting: "
                            (number->String expectedOutcome)
                            " way(s)\n\n"
                            )
             )
    )
  )

(test 1 1)
(test 2 2)
(test 3 6)
(test 4 24)
(test 5 120)