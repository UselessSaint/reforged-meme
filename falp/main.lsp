
(defun gen_dstate (size am) 
    (pgen_dstate size am nil)
)

(defun pgen_dstate (size am acc)
    (if (> size 1)
        (pgen_dstate (- size 1) am (append acc `(,am)))
        (append acc `(0))
    )
)

(defun change_val (state ind val)
    (reduce     (lambda (prev cur) 
                    (if (equal (length prev) ind)
                        (append prev `(,val))
                        (append prev `(,cur))
                    )
                ) state :initial-value Nil
    )
)

(defun move_seeds (state ind)
    (let ((am (nth ind state)))
        (if (> am 0)
            (pmove_seeds (change_val state ind 0) (+ ind 1) am)
            Nil
        )
    )
)

(defun pmove_seeds (state ind am)
    (cond 
        (   
            (and 
                (< ind (- (length state) 1)) 
                (> am 1)
            ) 
            ;(and (print "1cond") (print (append state `( "|" ,am ,ind))) (pmove_seeds (change_val state ind (+ (nth ind state) 1)) (+ ind 1) (- am 1)))
            (pmove_seeds (change_val state ind (+ (nth ind state) 1)) (+ ind 1) (- am 1))
        )

        (   
            (and 
                (>= ind (- (length state) 1)) 
                (> am 1)
            ) 
            ;(and (print "2cond") (print (append state `( "|" ,am ,ind))) (pmove_seeds (change_val state ind (+ (nth ind state) 1)) 0 (- am 1)))
            (pmove_seeds (change_val state ind (+ (nth ind state) 1)) 0 (- am 1))
        )
        
        (
            (and 
                (equal ind (- (length state) 1)) 
                (equal am 1)
            )
            ;(and (print "3cond") (print (append state `( "|" ,am ,ind))) (change_val state ind (+ (nth ind state) 1)))
            (change_val state ind (+ (nth ind state) 1))
        )

        (
            (> (nth ind state) 0)
            ;(and (print "4cond") (print (append state `( "|" ,am ,ind))) (move_seeds (change_val state ind (+ (nth ind state) 1)) ind))
            (move_seeds (change_val state ind (+ (nth ind state) 1)) ind)
        )

        (
            (equal (nth ind state) 0)
            ;(and (print "5cond") (print (append state `( "|" ,am ,ind))) Nil)
            Nil
        )
    )
)

(defun is_res (state)
    (let ((lstate (- (length state) 1)))
        (reduce (lambda (prev cur)
                    (cond   
                        (
                            (and 
                                (= cur 0) 
                                (< (length prev) lstate)
                            )
                            (append prev `(,cur))
                        )

                        (
                            (and 
                                (/= cur 0)
                                (< (length prev) lstate)
                            )
                            Nil
                        )

                        (
                            (and
                                (/= cur 0) 
                                (= (length prev) lstate)
                            )
                            (append prev `(,cur))
                        )
                    )
                ) state :initial-value Nil
        )
    )
)

(defun find_strat (size am)
    (pfind_strat (gen_dstate size am) 0 nil)
)

(defun pfind_strat (state ind acc)
    (if (< ind (- (length state) 1))
        (let ( ( rstate (move_seeds state ind) ) )
            (cond
                (
                    rstate
                    (if (is_res rstate)
                        (append acc `(,ind))
                        (let ((res (pfind_strat rstate 0 (append acc `(,ind)))))
                            (if res
                                res
                                (and (print `("1" ,state ,rstate ,ind ,acc)) (pfind_strat state (+ ind 1) acc))
                            )
                        )
                    )
                )

                (
                    (null rstate)
                    (and (print `("2" ,state ,rstate ,ind ,acc)) (pfind_strat state (+ ind 1) acc))
                    ;(pfind_strat state (+ ind 1) acc)
                )
            )
        )

        Nil
    )
)

(find_strat 5 2)