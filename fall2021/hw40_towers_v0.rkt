#|
  Ivan Chen <ichen42@stuy.edu>
  homework40
  worked with no one
  advised by no one
|#

#|

  Returns instructions to solve the Towers of Hanoi puzzle such:
    Move the top disk from [source] to [target].

  source - disk's source city
  target - disk's target city
  spare - disk's temporary storage city

|#

(define towersOfHanoi
  (lambda (source target spare)
    ; todo: add non-stub expressions
    "Move the top disk from source to target."
  )
)

(display (towersOfHanoi "Hanoi" "HCMC" "Da Nang"))
(display "\n")
(display (towersOfHanoi "Hanoi" "Da Nang" "HCMC"))
(display "\n")
(display (towersOfHanoi "Da Nang" "HCMC" "Hanoi"))
(display "\n")
