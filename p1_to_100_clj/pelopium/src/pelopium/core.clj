(ns pelopium.core)
(require 'clojure.set)

(defn p1-trigo []
  (->> (set (range 3 1000 3))
       (clojure.set/union (set (range 5 1000 5)))
       (into [])
       (reduce +)))

(defn fibo [n]
  (if (or (zero? n) (= 1 n))
    1
    (+ (fibo (- n 1)) (fibo (- n 2)))))