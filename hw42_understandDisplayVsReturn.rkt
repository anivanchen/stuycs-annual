#|  homework42
    Ivan Chen <ichen42@stuy.edu>
    worked with no one
    help from no one
|#

; Announce what will happen,
    ; corresponding to the Manual's instruction to
    ; "Tell us what was requested of you"
(define announcement
  (lambda (nDisks source target spare)
    (display "I will move the top ")
    (display nDisks)
    (display " disks \nfrom ")
    (display source)
    (display "\nto ")
    (display target)
    (display "\nusing ")
    (display spare)
    (display " if the Manual says to.\n\n")
  ))

; Calculate the instructions for Michael The Bot to
; move "nDisks" from "source" to "target" using "spare".
; Corresponds to the Manual for a Monastery.
(define instructionsForBot
  (lambda (nDisks source target spare)
    (announcement nDisks source target spare)
    
    "stub, to be replaced by code that produces the instructions, eventually"
  ))


(define separator "\n-----------------\n\n")

; corresponds to Abbot:
; test 0: an easy one
(display (instructionsForBot 1 "Hanoi"  "HCMC"  "Da Nang"))
(display separator)


; corresponds to Abbot:
; test 1: next step up
(display (instructionsForBot 2 "Kingman"  "Barstow"  "Berdoo"))
(display separator)