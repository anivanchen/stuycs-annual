#|  hw#43: universe-ending instructions
    Ivan Chen  <ichen42@stuy.edu>
    worked with no one
    advised by no one
|#

; Calculate the instructions for Michael The Bot to
; move "nDisks" from "source" to "target" using "spare".
; Corresponds to the Manual for a Monastery.
(define instructionsForBot
  (lambda (nDisks source target spare)
    (announce nDisks source target spare)
    (string-append "Move the top disk from "
                   source
                   " to "
                   target
                   " using "
                   spare
                   " if needed as the Manual says.")
  ))

; Announce what will happen,
; corresponding to the Manual's instruction to
; "Tell us what was requested of you"
(define announce
  (lambda (nDisks source target spare)

    (display (string-append
              "I will move the top "
              (number->string nDisks)
              " disks \n from "
              source
              "\nto"
              target
              "\nusing"
              spare
              " if the Manual says to.\n\n"
              ))
  ))

(define separator "\n-----------------\n\n")

; test 0: an easy one
(define steps (instructionsForBot 1 "Hanoi"  "HCMC"  "Da Nang"))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "\n...expecting\n"
                "Pick up all the disks from Hanoi and carry them to HCMC.\n"
                "Don't worry about Da Nang! MWAHAHA!"
                separator
                )
 )


; test 1: next step up
(define steps (instructionsForBot 2 "Kingman"  "Barstow"  "San Bernardino"))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "\n...expecting\n"
                "Pick up all the disks from Kingman and carry them to Barstow.\n"
                "Don't worry about San Bernardino! MWAHAHA!"
                separator
                )
 )
