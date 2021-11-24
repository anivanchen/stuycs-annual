; task00

(define averageOf2    ; start of procedure, tells DrRacket to set a symbol to identify as the following procedure
  (lambda (a b)   ; definition of the procedure
    (/ (+ a b) 2  ; expressions in the procedure
       )
    )             ; end of procedure
  )               ; end parentheses for the define command, telling DrRacket that the section of the code is complete

; task01

(define trapezoidArea ; start of procedure, tells DrRacket to set a symbol to identify as the following procedure
  (lambda (a b h)     ; definition of the procedure
    (*                ; expressions in the procedure
     (/ (+ a b)
        2
        )
     h
     )
    )                 ; end of procedure
  )                   ; end parentheses for the define command, telling DrRacket that the section of the code is complete

(display         ; get DrRacket to display dots of light in the shape of the returned value of the following procedure
 (trapezoidArea  ; get procedure from symbol trapezoidArea
  10             ; first argument
  6              ; second argument
  5              ; third argument
  )              ; end of procedure
 )               ; end parentheses for the display command, telling DrRacket that the section of the code is complete

(display "\n")

(display         ; get DrRacket to display dots of light in the shape of the returned value of the following procedure
 (trapezoidArea  ; get procedure from symbol trapezoidArea
  119.1342123    ; first argument
  0.12392352512  ; second argument
  3.9134e-6      ; third argument
  )              ; end of procedure
 )               ; end parentheses for the display command, telling DrRacket that the section of the code is complete
