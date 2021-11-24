#|
 Ivan Chen <ichen42@stuy.edu>
 homework26
 worked with no one
 advised by no one
|#

; task03

(display           ; means "make dots of light on the screen
                   ; that can represent value of the argument"
 (                 ; means "invoke the instructions in a procedure"
  lambda (r) (     ; ...that relies on 1 parameter
              (*
               3.1415926535
               (expt r 2)     ; ...and that produces a value the product of pi and r squared.
              )
             )
 )                 ; end of "Package instructions into a procedure"
)                  ; end of Display

(display "\n")

;############################################

; task04

(display           ; means "make dots of light on the screen
                   ; that can represent value of the argument"
 (                 ; means "invoke the instructions in a procedure"

  ; Package instructions into a procedure...
  (lambda (r)      ; ...that relies on 1 parameter
             (*
              3.1415926535
              (expt r 2)     ; ...and that produces a value the product of pi and r squared.
             )

  )                          ; end of "Package instructions into a procedure"
  10               ; Supply an argument to the invocation
 )
)                  ; end of Display

(display "\n")

;############################################

; task05

(display           ; means "make dots of light on the screen
                   ; that can represent value of the argument"
 (                 ; means "invoke the instructions in a procedure"

  ; Package instructions into a procedure...
  (lambda (r)      ; ...that relies on 1 parameter
             (*
              3.1415926535
              (expt r 2)     ; ...and that produces a value the product of pi and r squared.
             )

  )                          ; end of "Package instructions into a procedure"
  737473456.235635641        ; Supply an argument to the invocation
 )
)                  ; end of Display

(display "\n")

(display           ; means "make dots of light on the screen
                   ; that can represent value of the argument"
 (                 ; means "invoke the instructions in a procedure"

  ; Package instructions into a procedure...
  (lambda (r)      ; ...that relies on 1 parameter
             (*
              3.1415926535
              (expt r 2)     ; ...and that produces a value the product of pi and r squared.
             )

  )                          ; end of "Package instructions into a procedure"
  0.134928967465893425436    ; Supply an argument to the invocation
 )
)                  ; end of Display