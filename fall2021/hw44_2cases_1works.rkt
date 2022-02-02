#|
  homework44
  Ivan Chen <ichen42@stuy.edu>
  worked with no one
  advised by no one
|#

; Calculate the instructions for Michael The Bot to
; move "nDisks" from "source" to "target" using "spare".
; Corresponds to the Manual for a Monastery.
(define instructionsForBot
  (lambda (nDisks source target spare)
    (announce nDisks source target spare)
    
    (if (= nDisks 1)
        (string-append "Pick up top disk from " source
                   " and carry them to " target " directly.\n"
                   "Without using " spare "."
                   )
        ; stub to produce the end-of-universe instructions
        (string-append "Pick up all the disks from " source
                   " and carry them to " target ".\n"
                   "Don't worry about " spare "! MWAHAHA!"
                   )
        )
    
  ))

; Announce what will happen,
; corresponding to the Manual's instruction to
; "Tell us what was requested of you"
(define announce
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

(define separator "\n-----------------\n\n")

; test 0: an easy one
(define steps (instructionsForBot 1 "Hanoi"  "HCMC"  "Da Nang"))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "\n...expecting\n"
                "Move the top disk from Hanoi to HCMC.\n"
                separator
                )
 )


; test 1: next step up
(define steps (instructionsForBot 5 "Kingman"  "Barstow"  "San Bernardino"))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "\n...expecting\n"
                "stub for RECURSIVE caseS\n"
                separator
                )
 )