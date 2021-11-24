#|
  Ivan Chen <ichen42@stuy.edu>
  homework35
  worked with no one
  advised by no one
|#

; helpers

(define areaOfCircle
  (lambda (radius)
    (* 3.1415
       (expt radius 2)
     )
   )
 )

(define forAnnulusPair
  (lambda (ring innerRadius)
    (annulusArea
      (* ring innerRadius)
      (* (+ ring 1) innerRadius)
     )
   )
 )

; ######################################################

; task 1

(define annulusArea
  (lambda (innerRadius outerRadius)
    (- (areaOfCircle outerRadius)
       (areaOfCircle innerRadius))
   )
 )

; tests

(display "Annulus Area Tests\n")
(display (annulusArea 10 20))
(display "\n")
(display (annulusArea 192 937))
(display "\n")
(display (annulusArea 0.23942 0.93462))
(display "\n")
(display (annulusArea 13e-134 8e-05))
(display "\n")
(display (annulusArea (expt 15 20) (expt 32 23)))
(display "\n\n")

; ######################################################

; task 2

(define targetArea
  (lambda (innerRadius)
    (+
      (forAnnulusPair 1 innerRadius)
      (forAnnulusPair 3 innerRadius)
      (forAnnulusPair 5 innerRadius)
     )
   )
 )

(display "Target Area Tests\n")
(display (targetArea 10))
(display "\n")
(display (targetArea 99232))
(display "\n")
(display (targetArea 21e-38))
(display "\n")
(display (targetArea 0.23849273))
(display "\n")
(display (targetArea (expt 109 20)))