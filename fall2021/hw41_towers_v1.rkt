#|
  Ivan Chen <ichen42@stuy.edu>
  homework40
  worked with no one
  advised by no one
|#

#|

  Returns string literals containing the instructions
  to solve the Towers of Hanoi puzzle such:
    Move the top disk from [source] to [target].

  numberOfDisks - number of disks
  source - disk's source city
  target - disk's target city
  spare - disk's temporary storage city

|#

(define monkInstructions
  (lambda (numberOfDisks source target spare)

    ; announcement
    (display "I will move the top ") (display numberOfDisks)
    (display " disks from ") (display source) (display " to ")
    (display target) (display " using ") (display spare)
    (display " if the Manual says to.")
    
    ; todo: add non-stub expressions
    "stub"
  )
)

#|  TESTING  |#

(display (monkInstructions 1 "LA" "NYC" "Beijing"))
#|
  expecting: Move the top disk from LA to NYC.
|#

(display "\n")
(display (monkInstructions 2 "Hanoi" "Da Nang" "HCMC"))
#|
  expecting: Move the top disk from Hanoi to HCMC.
             Move the top disk from Hanoi to Da Nang.
             Move the top disk from HCMC to Da Nang.
|#